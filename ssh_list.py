from paramiko import SSHClient, AutoAddPolicy
""" script ssh connect de brad de devopslifecycle.com"""

hosts = ['192.168.1.21', '192.168.1.22', '192.168.1.23']

for host in hosts:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host, username='master', password='M0zart')
try:
    pass
except:
    Print('erreur connexion ssh  usename or login ')

       #client.exec_command('hostname')
    stdin, stdout, stderr = client.exec_command('hostname')

    if stdout.channel.recv_exit_status() == 0:
        print(f'STDOUT: {stdout.read().decode("utf8")}')
    else:
        print(f'STDERR: {stderr.read().decode("utf8")}')


    stdin.close()
    stdout.close()
    stderr.close()
    client.close()
    