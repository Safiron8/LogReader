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

print("Otevírám log")

with gzip.open(file, 'rb') as f_in:
    with open(logFile, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Log otevřen, čekám na zavření notepadu")

proces = subprocess.Popen(["notepad.exe", logFile])
proces.wait()

shutil.rmtree(dirpath)