from utils.set_file import sudo_set_file
from patchwork import files
import os

def do_install_fail2ban(c):
    c.sudo('apt-get update')
    c.sudo('apt-get install -y fail2ban')
    jailConfigPath = os.path.dirname(__file__) + '/stubs/fail2ban.jail'
    with open(jailConfigPath, 'r') as f:
        jailConfig = f.read()
        location = '/etc/fail2ban/jail.local'
        sudo_set_file(c, location, mode=640)
        if (not c.sudo(f'egrep sshd {location}').ok):
            c.sudo(f'{jailConfig} >> {location}')
    c.sudo('systemctl start fail2ban')
    c.sudo('systemctl enable fail2ban')

def do_unban(c, ip):
    c.sudo(f'fail2ban-client set sshd unbanip {ip}')