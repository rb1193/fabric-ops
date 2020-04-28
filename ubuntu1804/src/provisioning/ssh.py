from patchwork import files

def do_disable_password_auth(c):
    ssh_config = '/etc/ssh/sshd_config'
    if (files.contains(c, ssh_config, '#?PasswordAuthentication (yes|no)')):
        c.run(f'sudo sed -i "s/#?PasswordAuthentication (yes|no)/PasswordAuthentication no/g" {ssh_config}')
    else:
        files.append(c, ssh_config, 'PasswordAuthentication no')
    c.run('sudo systemctl restart ssh')

def do_disable_root_login(c):
    ssh_config = '/etc/ssh/sshd_config'
    if (files.contains(c, ssh_config, '#?PermitRootLogin (yes|no)', escape=False)):
        c.sudo(f'sed -i -E "s/#?PermitRootLogin (yes|no)/PermitRootLogin no/g" {ssh_config}')
    else:
        files.append(c, ssh_config, 'PermitRootLogin no')
    c.sudo('systemctl restart ssh')