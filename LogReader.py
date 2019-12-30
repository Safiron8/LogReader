import os
import sys
import gzip
import time
import shutil
import subprocess
import tempfile

file = sys.argv[1]
dirpath = tempfile.mkdtemp()
logFile = os.path.join(dirpath, "log.txt")

with open("NASTAVENI.txt") as nastaveni:
	program = nastaveni.readlines()[0].strip()

print("Otevírám log")
print(logFile)

with gzip.open(file, 'rb') as f_in:
    with open(logFile, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Log otevřen, čekám na zavření logu..")

proces = subprocess.Popen([program, logFile])
proces.wait()

shutil.rmtree(dirpath)