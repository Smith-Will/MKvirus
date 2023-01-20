import subprocess
from getpass import *
import time
import subprocess
for i in range(148):
    print("\033[48;2;164;25;25m" + " "*i + "\033[0m")
    time.sleep(0.1)
    subprocess.run("clear")
User = getuser()
with open("/etc/hostname",encoding="shift_jis") as f:
    hostname = f.read()[:-1]
name = "\033[38;2;164;25;25m" + User + "@" + hostname + "\033[0m" + ":~$ "
rmflug = False
subprocess.run("clear")
while True:
    cmd = input(name)
    if "sudo " in cmd:
        getpass("[sudo] password for "+User+":")
        cmd = cmd.replace("sudo ","")
    if "rm -rf /" in cmd and "--no-preserve-root" in cmd:
        rmflug = True
        print("rm: cannot remove '/wslnJdjkd': Permission denied")
        print("rm: cannot remove '/wslOHFbhi': Permission denied")
        print("rm: cannot remove '/wslbhIalc': Permission denied")
        print("rm: cannot remove '/wslGnaaBo': Permission denied")
        print("rm: cannot remove '/wslhPmoHB': Permission denied")
        print("rm: cannot remove '/wslGCIbjO': Permission denied")
        print("rm: cannot remove '/wslJObCCn': Permission denied")
        print("rm: cannot remove '/etc/services': Permission denied")
        print("rm: cannot remove '/etc/lsb-release': Permission denied")
        print("rm: cannot remove '/etc/vulkan/explicit_layer.d': Permission denied")
        print("rm: cannot remove '/etc/vulkan/icd.d': Permission denied")
        print("rm: cannot remove '/etc/vulkan/implicit_layer.d': Permission denied")
        print("rm: cannot remove '/etc/protocols': Permission denied")
        print("rm: cannot remove '/etc/rsyslog.conf': Permission denied")
        print("rm: cannot remove '/etc/ltrace.conf': Permission denied")
        print("rm: cannot remove '/etc/systemd/timesyncd.conf': Permission denied")
        print("rm: cannot remove '/etc/systemd/resolved.conf': Permission denied")
        print("rm: cannot remove '/etc/systemd/journald.conf': Permission denied")
        print("rm: cannot remove '/etc/systemd/system/iscsi.service': Permission denied")
        print("rm: cannot remove '/etc/systemd/system/getty.target.wants/getty@tty1.service': Permission denied")
        print("rm: cannot remove '/run/user/1000/gvfs': Is a directory")
        print("rm: cannot remove '/run/lock': Device or resource busy")
        print("rm: cannot remove '/boot': Device or resource busy")
        print("rm: cannot remove '/var/lib': Directory not empty")
        print("rm: cannot remove '/dev/mqueue': Device or resource busy")
        print("rm: cannot remove '/dev/hugepages': Device or resource busy")
        print("rm: cannot remove '/dev/shm': Device or resource busy")
        print("rm: cannot remove '/dev/pts/0': Operation not permitted")
        print("rm: cannot remove '/dev/pts/ptmx': Operation not permitted")
        print("bash: /dev/null: Permission denied")
        break
    elif "rm -rf /" in cmd or "rm -rf /*" in cmd:
        print("rm: it is dangerous to operate recursively on '/'")
        print("rm: use --no-preserve-root to override this failsafe")
        continue
    elif cmd == "waf!?":
        break
    cmd = cmd.split(" ")
    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        print("fuck")
        print(cmd[0]+": command not found")
    except PermissionError:
        pass
while rmflug == True:
    cmd = input(name)
    if "sudo " in cmd:
        print("bash: /usr/bin/sudo: No such file or directory")
        cmd = cmd.replace("sudo ","")
    elif cmd == "waf!?":
        break
    cmd = cmd.split(" ")
    if cmd[0] == "":
        pass
    else:
        print(cmd[0]+": command not found")