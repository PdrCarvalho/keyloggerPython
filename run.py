import subprocess
import os 

p = subprocess.Popen(['pgrep', '-f', 'cliente.py'], stdout=subprocess.PIPE)
out, err = p.communicate()

if len(out.strip()) == 0:
    os.system("nohup python3 " + os.path.dirname(os.path.realpath(__file__)) + "/cliente.py </dev/null >/dev/null 2>&1 &")