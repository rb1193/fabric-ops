from patchwork import files
from utils.set_file import set_file

def do_add_ssh_user(c, username, sshkeyfile, password=None):
    c.run(f'adduser {username} --disabled-password --gecos ""')
    do_add_user_to_group(c, username, 'sudo')
    if (password is not None):
        do_set_password(c, username, password)
    with open(sshkeyfile) as f:
        sshkey = f.read()
        homedir = f'/home/{username}'
        files.directory(c, f'{homedir}/.ssh', username, username, '700')
        authorized_key_file = f'{homedir}/.ssh/authorized_keys'
        if (not files.exists(c, authorized_key_file)):
            set_file(c, authorized_key_file, username, username, 600)
        files.append(c, authorized_key_file, sshkey)

    print(f'Successfully created {username} user on {c.host}')

def do_set_password(c, username, password):
    c.run(f'echo {username}:{password} | chpasswd')

def do_add_user_to_group(c, username, group):
    c.run(f'usermod -aG {group} {username}')

def sudo_add_user_to_group(c, username, group):
    c.sudo(f'usermod -aG {group} {username}')