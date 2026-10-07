## Vagrant File tooling compatabile with Bhyve and Virtualbox, potentially ESXI/Vmware,KVM
##
## Self-bootstrapping driver: when driver/ is missing, the pinned
## core_provisioner release named in driver.version is downloaded, verified
## against its .sha256 sidecar, and extracted before Hosts.rb is required.
## The pin file is the single authority for this bootstrap AND the consumer's
## build CI — always an exact tag, never a floating branch.
require 'yaml'
require 'digest'
require 'fileutils'
require 'net/http'
require 'uri'
require 'tmpdir'

def download(url, dest, limit = 5)
  raise "Too many redirects fetching #{url}" if limit.zero?

  uri = URI(url)
  Net::HTTP.start(uri.host, uri.port, use_ssl: true) do |http|
    http.request(Net::HTTP::Get.new(uri)) do |response|
      case response
      when Net::HTTPRedirection
        return download(response['location'], dest, limit - 1)
      when Net::HTTPSuccess
        File.open(dest, 'wb') { |file| response.read_body { |chunk| file.write(chunk) } }
      else
        raise "Download failed (HTTP #{response.code}) for #{url}"
      end
    end
  end
end

root = File.dirname(__FILE__)
driver_dir = File.join(root, 'driver')

unless File.file?(File.join(driver_dir, 'Hosts.rb'))
  pin_file = File.join(root, 'driver.version')
  unless File.file?(pin_file)
    raise "driver/ is missing and no driver.version pin file exists — create driver.version containing the pinned core_provisioner release tag (for example: v0.3.0)"
  end

  tag = File.read(pin_file).strip
  version = tag.sub(/\Av/, '')
  archive_name = "core_provisioner-#{version}.tar.gz"
  base_url = "https://github.com/STARTcloud/core_provisioner/releases/download/#{tag}"

  Dir.mktmpdir('core_provisioner') do |tmp|
    archive = File.join(tmp, archive_name)
    sidecar = "#{archive}.sha256"
    puts "==> driver/ is missing — fetching core_provisioner #{tag}"
    download("#{base_url}/#{archive_name}", archive)
    download("#{base_url}/#{archive_name}.sha256", sidecar)

    expected = File.read(sidecar).split.first
    actual = Digest::SHA256.file(archive).hexdigest
    raise "Checksum mismatch for #{archive_name}: expected #{expected}, got #{actual}" unless expected == actual

    system('tar', '-xzf', archive, '-C', root) || raise("Extraction of #{archive_name} failed")
  end
end

require File.expand_path(File.join(root, 'driver', 'Hosts.rb'))

settings = YAML::load(File.read(File.join(root, 'Hosts.yml')))

Vagrant.configure("2") do |config|
  Hosts.configure(config, settings)
end
