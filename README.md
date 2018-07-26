# load-config

## Example Playbook
-------------------

```

tasks:
- name: load configuration file to network device
  import_role:
    name: load-config
    tasks_from: load_config
  vars:
    ansible_network_os: nxos
    config_file: eth_desc.cfg

```
