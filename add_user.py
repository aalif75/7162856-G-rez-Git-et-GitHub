""" # script creation mulitiple users à partir de fichier user.txt
# avec  mot de passe generique  "Pass@2022"  pour tous les utlisateurs
#

# import modules  necessaires pour l'execution des scripts
import sys
import os
import getpass
import subprocess
# Positinnement; Changer de répertoire courant
os.chdir("/P/P6/project")
os.getcwd() # Verif positionnement rep courant

# Ajout user
def  add_user(username,password):
    try:
        subprocess.run(['useradd','-p',password,username])
    except:
        print(f"Failed to add user.")
        sys.exit(1)

if os.path.exists("user.txt"):
    with open ("user.txt") as file:
        for line in file:

             #os.system("echo -e 'Pass@2022'\n'Pass@2022'|passwd{}").format line())
            add_user(line,'Pass2022')

else:
    print("Erreur: le ichier user.txt est manquanqant!")
    """


import os
import subprocess
import sys
import getpass


# add user function
def add_user():
    # Ask for the input
    username = input("Enter Username ")

    # Asking for users password
    password = getpass.getpass()

    try:
        # executing useradd command using subprocess module
        subprocess.run(['useradd', '-p', password, username])
        print(f"utilisateur créé")
    except:
        print(f"Failed to add user.")
        sys.exit(1)


add_user()