#!/usr/lib/python
import os.path
import datetime
from subprocess import call

def runInterProscan(seqdir):
    f0 = open('run_commands.sh', 'w')
    proteins = [os.path.abspath('%s/'%seqdir+j) for j in os.listdir(seqdir)]
    print proteins
    for i in proteins:
        opfile = 'myresults/'+os.path.basename(i).split('.')[0]
        cmd = './interproscan.sh -i %s -b %s -goterms -pa\n'%(i, opfile)
        f0.write(cmd)
    f0.close()
    call('chmod 777 run_commands.sh', shell=True)

if __name__ == "__main__":
    import sys
    runInterProscan(sys.argv[1])
