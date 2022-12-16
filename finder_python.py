#!/usr/bin/python3

import sys
import subprocess
from subprocess import Popen, PIPE
from sys import argv
#from nmap_modules import filter_ftp_output

class NmapArguments():

    # basic scan
    PORTS = argv[2]
    HOSTS = argv[3]
    BLACKLIST = ' --excludefile=/home/betaperson/scripts/scans/blacklist.txt'
    BASIC_INFORMATIONS = f'nmap -Pn -n --open -p {PORTS} -iR {HOSTS} -oA nmap'
    DEBUG = ' -dd -v '
    SPOOF = ' --spoof-mac -D RND,RND,RND,ME,RND '
    TIME_PERFORMANCE = ' -T5 --host-timeout=30 --max-retries=1 '

    # version detection scan
    VERSION_DETECTION = ' -sV --version-light '

    # NSE scans
    NSE_SCAN = ' -sC --script=ftp-anon'
    FTP_ANON = 'ftp-anon'


    def __run(self, nmap_string):
        return subprocess.Popen(nmap_string, shell=True,  universal_newlines=True).wait()

    # define basic scan
    def basic_scan(self):
        return self.__run(self.BASIC_INFORMATIONS + self.SPOOF + self.TIME_PERFORMANCE + self.DEBUG + self.VERSION_DETECTION + self.BLACKLIST)

    # define basic scan for output filter
    def basic_scan_to_pipe(self):
        return self.__run(self.BASIC_INFORMATIONS + self.SPOOF + self.TIME_PERFORMANCE + self.BLACKLIST + self.NSE_SCAN)

    # define version detection scan
    def version_detection_scan(self):
        return self.__run(self.BASIC_INFORMATIONS + self.SPOOF + self.VERSION_DETECTION + self.TIME_PERFORMANCE + self.BLACKLIST + self.NSE_SCAN)




# define service filters   
def filter_ftp_output(pushed):   
    # filter output
    lines = []
    for line in pushed.stdout:
        lines.append(line.strip('\n'))
        if 'report' in line:
            #out = sys.stdout.write(line[20:])
            
            with open('file.txt', 'w') as file:
                file.write(str(lines))

        #elif 'open' in line:
            #sys.stdout.write(line)
        elif 'allowed' in line:
            #sys.stdout.write(lines[2])
            #sys.stdout.write(line)
            print('\033[1;93m' + line + '\033[0m')
            #sys.stdout.write(line)
        elif 'Info' in line:
            print('\033[1;93m' + line + '\033[0m')
            #sys.stdout.write(line)                
        elif '|' in line:
            print('\033[1;92m' + line + '\033[0m')
            #sys.stdout.write(line)                
        else: 
            pass

# main
m_obj = NmapArguments()
if len(argv) == 4:
    if argv[1] == '1':
        #NmapArguments.NSE_SCAN+NmapArguments.FTP_ANON
        #print(NmapArguments.NSE_SCAN)
        a = m_obj.basic_scan_to_pipe()
        filter_ftp_output(a)
    elif argv[1] == '2':
        if argv[2] == '21':
            NmapArguments.NSE_SCAN + 'ftp-anon'
            b = m_obj.basic_scan_to_pipe()
            filter_ftp_output(b)
        else:
            m_obj.service_detection_scan()
    else:
        usage()
else:
    usage()

def usage():
    print('''
learn_classes.py SCAN_TYPE PORTS HOSTS 

SCAN_TYPES = (1) Basic port scan (2) Service version detection scan
PORTS = ex.: 80,8080
HOSTS = 500 ( How many hosts to scan )''')


