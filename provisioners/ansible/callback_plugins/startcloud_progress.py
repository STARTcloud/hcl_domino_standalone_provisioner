# Role-granularity progress bar for STARTcloud provisioning.
#
# A notification callback that reports progress by OBSERVING execution, so it
# needs no changes to any role: no count_progress vars, no per-role progress
# block, no filter to pre-compute totals. The denominator is the play's own
# role list, resolved at runtime, so roles can be added, removed, or reordered
# with zero bookkeeping.
#
# It runs ALONGSIDE the normal stdout callback (CALLBACK_TYPE = notification),
# so it only adds lines. It advances on role COMPLETION (a new role starting
# means, under the linear strategy, the previous one finished), so the bar
# never reads 100% until work is actually done — the last role runs at
# (total-1)/total and 100% is emitted only at the end of the play.
#
# Two lines per step: a human banner (star-padded, like the TASK [...] ****
# banners) and a machine-readable PROGRESS:: JSON marker the provisioning
# agent can lift into a GUI progress bar.
from __future__ import annotations

from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = "notification"
    CALLBACK_NAME = "startcloud_progress"
    CALLBACK_NEEDS_ENABLED = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._total = 0
        self._completed = 0
        self._current = None
        self._index = 0

    def _role_ident(self, task):
        # Returns (ident, name). Transitions are detected by the role
        # invocation's UUID, not its name: a role listed twice in a row with
        # different vars (e.g. package_repository_server public + private) is
        # two compiled role objects, and name-based detection would collapse
        # them into one counted step (the observed 94/95). Every invocation
        # emits at least one task (arg-spec validation is unconditional), so
        # uuid transitions always equal the play's compiled role count.
        role = getattr(task, "_role", None)
        if role is None:
            return None, None
        try:
            name = role.get_name()
        except Exception:
            return None, None
        ident = getattr(role, "_uuid", None) or name
        return ident, name

    def _emit(self, label, running_name):
        total = self._total if self._total >= self._completed else self._completed
        percent = int(self._completed / total * 100) if total else 0
        self._display.banner(
            "PROGRESS [%d/%d] (%d%%) - %s" % (self._completed, total, percent, label)
        )
        running = ('"%s"' % running_name) if running_name else "null"
        done = "true" if running_name is None else "false"
        self._display.display(
            'PROGRESS::{"completed": %d, "total": %d, "percent": %d, '
            '"running": %s, "index": %d, "done": %s, "label": "%s"}'
            % (self._completed, total, percent, running, self._index, done, label)
        )

    def v2_playbook_on_play_start(self, play):
        self._completed = 0
        self._current = None
        self._index = 0
        try:
            names = [r.get_name() for r in play.get_roles()]
        except Exception:
            names = []
        self._total = len(names)

    def v2_playbook_on_task_start(self, task, is_conditional):
        ident, name = self._role_ident(task)
        if not ident or not name or ident == self._current:
            return
        # A new role invocation has begun. Under the linear strategy the
        # previous one has finished, so credit it complete now; the invocation
        # just starting is the current activity and is not counted done until
        # the NEXT one begins (or the play ends).
        if self._current is not None:
            self._completed += 1
        self._current = ident
        self._index += 1
        label = name.split(".")[-1].replace("_", " ").title()
        self._emit(label, name)

    def v2_playbook_on_stats(self, stats):
        # Nothing ran (e.g. the generate-playbook helper play) — stay silent.
        if self._index == 0:
            return
        # The final role completes only when the play ends.
        if self._current is not None:
            self._completed += 1
            self._current = None
        self._emit("Complete", None)
