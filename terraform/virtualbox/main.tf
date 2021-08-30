terraform {
  required_providers {
    virtualbox = {
      source  = "terra-farm/virtualbox"
      version = "0.2.1-alpha.1"
    }
  }
}


resource "virtualbox_vm" "python_app" {
  name  = "python_app"
  image = "https://app.vagrantup.com/ubuntu/boxes/bionic64/versions/20180903.0.0/providers/virtualbox.box"

  network_adapter {
    type           = "hostonly"
    host_interface = "vboxnet1"
  }
}

output "IPAddr" {
  value = element(virtualbox_vm.python_app.*.network_adapter.0.ipv4_address, 1)
}