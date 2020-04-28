def do_check(c):
    # check host type
    host(c)
 
    # Check diskspace
    diskspace(c)

def host(c):
    c.run('uname -s')
    c.run('whoami')
    c.run('hostname -I')
 
 
def diskspace(c):
    c.run('df') 
