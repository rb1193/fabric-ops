from fabric import *
from provisioning.check import do_check
from provisioning.init import *
from provisioning.ssh import *
from provisioning.fail2ban import do_install_fail2ban, do_unban
from provisioning.docker import do_install_docker, do_install_docker_compose
 
@task()
def check(c):
    do_check(c)

@task()
def add_ssh_user(c, username, sshkeyfile):
    do_add_ssh_user(c, username, sshkeyfile)

@task()
def set_password(c, username, password):
    do_set_password(c, username, password)

@task()
def remove_user(c, username):
    c.run(f'deluser --remove-home {username}')

@task()
def disable_password_auth(c):
    do_disable_password_auth(c)

@task()
def disable_root_login(c):
    do_disable_root_login(c)

@task()
def fail2ban(c):
    do_install_fail2ban(c)

@task()
def unban_ip(c, ip):
    do_unban(c, ip)

@task()
def install_docker(c, user=None):
    do_install_docker(c, user)

@task()
def install_docker_compose(c, version):
    do_install_docker_compose(c, version)