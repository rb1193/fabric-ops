def set_file(c, path, user=None, group=None, mode=None):
    c.run("touch {}".format(path))
    if user is not None:
        group = group or user
        cmd = "chown {}:{} {}".format(user, group, path)
        c.run(cmd)
    if mode is not None:
        c.run("chmod {} {}".format(mode, path))

def sudo_set_file(c, path, user=None, group=None, mode=None):
    c.sudo("touch {}".format(path))
    if user is not None:
        group = group or user
        cmd = "chown {}:{} {}".format(user, group, path)
        c.sudo(cmd)
    if mode is not None:
        c.sudo("chmod {} {}".format(mode, path))