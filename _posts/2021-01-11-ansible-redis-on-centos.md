---
layout: post
title: Redis Installation on CentOS Using Ansible
menutitle: CentOS Redis Install Using Ansible
kategori:
  - ansible
  - server
label:
  - server
---


## Ansible Introduction

Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.
Ansible use SSH for transport to run the tasks.

Documentation: [Ansible User Guide Intro](https://docs.ansible.com/ansible/latest/user_guide/intro.html).

<!--more-->


## Install Redis to Our Centos Server


#### Create Ansible Inventory

```bash
# Create ansible directory
$ mkdir centos_ansible
$ cd centos_ansible
$ mkdir playbooks

# Prepare required files
$ touch ansible.cfg
$ touch hosts
$ touch playbooks/redis_setup.yml
```

#### Clone Redis Ansible Role

Clone ansible role to `roles` directory (on current directory)

```
$ ansible-galaxy install davidwittman.redis -p ./roles
```


#### File Contents

`ansible.cfg`

```
inventory           = hosts
roles_path          = ./roles
```

> Note: `MY_HOSTNAME` is listed on `~/.ssh/config` with use ssh key authentication

`hosts`

```
[servers]
MY_HOSTNAME
```

> For our redis we use version `5.0.10`

`playbooks/redis_setup.yml`

```yaml
- hosts: MY_HOSTNAME
  become: yes
  tasks:
    - name: Install single node Redis
      vars:
        redis_version: 5.0.10
        redis_port: 6379
        redis_bind: 127.0.0.1
        redis_socket: /var/run/redis/redis.sock
        redis_password: YOUR_REDIS_PASSWORD
      include_role: 
        name: davidwittman.redis
```

#### Run 

```
$ ansible-playbook playbooks/redis_setup.yml \
  --extra-vars "ansible_become_pass=YOUR_SERVER_SUDO_USER_PASSWORD"
```


## Log


```
PLAY [MY_HOSTNAME] ***********************************************************************************************

TASK [Gathering Facts] ******************************************************************************************
Enter passphrase for key '/home/user/.ssh/id_rsa': 
ok: [MY_HOSTNAME]

TASK [Install single node Redis] ********************************************************************************

TASK [davidwittman.redis : check for ansible 1.x] ***************************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : check for checksum] ******************************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : set redis checksum] ******************************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : download redis] **********************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : upload redis] ************************************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : extract redis tarball] ***************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : install debian dependencies] *********************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : install redhat dependencies] *********************************************************
ok: [MY_HOSTNAME]

TASK [davidwittman.redis : update libgcc on rhel for 32-bit dependencies] ***************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : install redhat 32-bit dependencies] **************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : install suse dependencies] ***********************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : enable overcommit in sysctl] *********************************************************
ok: [MY_HOSTNAME]

TASK [davidwittman.redis : compile redis] ***********************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : create redis install directory] ******************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : create /etc/redis] *******************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : check if redis user exists (ignore errors)] ******************************************
fatal: [MY_HOSTNAME]: FAILED! => {"changed": false, "cmd": ["id", "redis"], "delta": "0:00:00.005127", "end": "2021-01-14 19:05:19.348880", "msg": "non-zero return code", "rc": 1, "start": "2021-01-14 19:05:19.343753", "stderr": "id: redis: no such user", "stderr_lines": ["id: redis: no such user"], "stdout": "", "stdout_lines": []}      
...ignoring

TASK [davidwittman.redis : add redis group] *********************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : add redis user] **********************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : create /var/run/redis] ***************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : install redis] ***********************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : list redis binaries to add to alternatives] ******************************************
ok: [MY_HOSTNAME]

TASK [davidwittman.redis : add redis binaries to alternatives] **************************************************
changed: [MY_HOSTNAME] => (item=redis-benchmark)
changed: [MY_HOSTNAME] => (item=redis-check-aof)
changed: [MY_HOSTNAME] => (item=redis-check-rdb)
changed: [MY_HOSTNAME] => (item=redis-cli)
changed: [MY_HOSTNAME] => (item=redis-sentinel)
changed: [MY_HOSTNAME] => (item=redis-server)

TASK [davidwittman.redis : create redis working directory] ******************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : create redis init script] ************************************************************
skipping: [MY_HOSTNAME] => (item=/home/user/Kode/ansible/ANSIBLE_DIR/roles/davidwittman.redis/templates/../templates/RedHat/redis.init.j2)                                                                                        

TASK [davidwittman.redis : create redis systemd service] ********************************************************
changed: [MY_HOSTNAME] => (item=/home/user/Kode/ansible/ANSIBLE_DIR/roles/davidwittman.redis/templates/../templates/default/redis.service.j2)                                                                                     

TASK [davidwittman.redis : create systemd tmpfiles configuration] ***********************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : reload systemd daemon] ***************************************************************
ok: [MY_HOSTNAME]

TASK [davidwittman.redis : set redis to start at boot] **********************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : check if log directory exists] *******************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create log directory if it does not exist] *******************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create log file if it does not exist] ************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : update permissions of log file if needed] ********************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : check if pid directory exists] *******************************************************
ok: [MY_HOSTNAME]

TASK [davidwittman.redis : create pid directory if it does not exist] *******************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create redis config file] ************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : add redis init config file] **********************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : add redis init config file] **********************************************************
skipping: [MY_HOSTNAME]
[WARNING]: flush_handlers task does not support when conditional

RUNNING HANDLER [davidwittman.redis : restart redis] ************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : ensure redis is running] *************************************************************
ok: [MY_HOSTNAME]

TASK [davidwittman.redis : create sentinel working directory] ***************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create sentinel init script] *********************************************************
skipping: [MY_HOSTNAME] => (item=/home/user/Kode/ansible/ANSIBLE_DIR/roles/davidwittman.redis/templates/../templates/RedHat/redis_sentinel.init.j2)                                                                               

TASK [davidwittman.redis : create sentinel systemd service] *****************************************************
skipping: [MY_HOSTNAME] => (item=/home/user/Kode/ansible/ANSIBLE_DIR/roles/davidwittman.redis/templates/../templates/default/redis_sentinel.service.j2)                                                                           

TASK [davidwittman.redis : create systemd tmpfiles configuration] ***********************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : reload systemd daemon] ***************************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : set sentinel to start at boot] *******************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : check if sentinel log directory exists] **********************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create sentinel log directory if it does not exist] **********************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : touch the sentinel log file] *********************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : check if sentinel pid directory exists] **********************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create sentinel pid directory if it does not exist] **********************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create sentinel config file] *********************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : add sentinel init config file] *******************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : add sentinel init config file] *******************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : ensure sentinel is running] **********************************************************
skipping: [MY_HOSTNAME]

TASK [davidwittman.redis : create facts directory] **************************************************************
changed: [MY_HOSTNAME]

TASK [davidwittman.redis : create redis facts] ******************************************************************
changed: [MY_HOSTNAME]

PLAY RECAP ******************************************************************************************************
MY_HOSTNAME                 : ok=27   changed=19   unreachable=0    failed=0    skipped=30   rescued=0    ignored=1
```