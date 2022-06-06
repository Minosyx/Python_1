import os
from subprocess import Popen, check_output

# print(os.getcwd())
# os.chdir("G:/Studia")
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("a")
# print(os.listdir())
# os.rmdir("a")
# print(os.listdir())
# print(os.environ)
# print(os.uname())

# Popen("firefox", shell=True)
# print(check_output('dir', shell=True))
print(check_output('ls', shell=True, encoding='utf8'))
