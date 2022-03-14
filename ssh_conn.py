import paramiko

import sys

# declaration des variables
adresse_ip = "192.168.1.21"
utlisateur = "master"
motdepasse = "M0zart"

results = []

def ssh_conn():

  client = paramiko.SSHClient()
  client.load_system_host_keys() # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(adresse_ip, username='utlisateur', password='M0zart')
  print("Successfully connected to",adresse_ip )


  ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('ls -al')

  for line in ssh_stdout:
    results.append(line.strip('\n'))

ssh_conn()

for i in results:
  print(i.strip())


sys.exit()
