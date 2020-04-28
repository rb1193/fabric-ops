from provisioning.init import sudo_add_user_to_group

def do_install_docker(c, user=None):
    c.sudo('apt-get update')
    c.sudo('apt-get install -y apt-transport-https ca-certificates curl software-properties-common')
    c.sudo('apt-key adv --fetch-keys https://download.docker.com/linux/ubuntu/gpg')
    c.sudo('add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"')
    c.sudo('apt-get update')
    c.sudo('apt-get install -y containerd docker-ce-cli')
    c.sudo('apt-get install -y docker-ce')
    if (user is not None):
        sudo_add_user_to_group(c, user, 'docker')

def do_install_docker_compose(c, version):
    c.sudo(f'curl -L "https://github.com/docker/compose/releases/download/{version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    c.sudo('chmod +x /usr/local/bin/docker-compose')