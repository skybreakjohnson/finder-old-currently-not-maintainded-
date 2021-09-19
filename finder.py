import os
import nmap
import pandas as pd

def banner():
    os.system("clear")
    print("""
 /'___\ __            /\ \                 
/\ \__//\_\    ___    \_\ \     __   _ __  
\ \ ,__\/\ \ /' _ `\  /'_` \  /'__`\/\`'__\
 \ \ \_/\ \ \/\ \/\ \/\ \L\ \/\  __/\ \ \/ 
  \ \_\  \ \_\ \_\ \_\ \___,_\ \____\\ \_\ 
   \/_/   \/_/\/_/\/_/\/__,_ /\/____/ \/_/ 

Ver: 0.0.3-build
""")

banner()
jo = input("""
1. Top 10 (Test) 6. Microsoft 
2. Mysql (work)  7. Webcam    
3. Mssql (work)  8.
4. Http          9.
5. Ftp (work)    10. All 

> """)
how_many = int(input("Hosts: "))
port = input("Port: ")

# initialisiere Nmap Scan
def nmap_scan():
    if how_many >= 100 and how_many < 1000:
        print("[!] This may take a while.")
    elif how_many >= 1000 and how_many < 10000:
        print("[!] Take a coffee..")
    elif how_many >= 10000 and how_many < 100000:
        print("[!] Take a coffee or two..")
    elif how_many >= 100000:
        print("[!] U should wait for the finder update which includes massscan support u crazy mf..")
    nm = nmap.PortScanner()
    nm.scan(
        arguments=
        "-Pn -T5 --open -p " + port + " -sV --version-light --max-retries=1 -iR " + str(how_many)
    )
   
# erstelle csv file
    csv = nm.csv()
    with open("nmap.csv", "w") as file:
        file.write(csv)

# ausgewählter service (Vorübergehend...!)
    if jo == "2":
        mysql_scan()
    elif jo == "3":
        mssql_scan()
    elif jo == "5":
        ftp_scan()
    else:
        print("Fuck you im a Pre-Alpha! Bye.")
        exit(1)

# Liste der vulnerable versions
iis = ["microsoft", "6.0", "5.0", "4.0", "8.5", "7.5"]
mysql = ["5.0.51a-24+lenny2", "5.0.45-Debian_1ubuntu3.1-log", "5.5.9", "5.5",
         "5.4", "5.3", "0.9.2", "2.4.6", "5.0.45-community-nt",
         "5.1.22-rc-community"] 
mssql = ["MSSQL 2000", "MSDE", "8.00.194", "8.00.384", "8.00.534", "8.00.760",
         "8.00.2039", "9.00.1399.06", "9.00.2047.00", "9.00.3042.00"]
http = ["WRT160n" ]
ftp = ["1.3.2rc3", "1.3.3b", "1.2", "1.3.0", "1.3.2rc3", "1.3", "1.3.3b",
       "3.2.0.0.258", "3.4.0.0.348", "3.4.0.0.348", "3.4.0", "3.3.0", "3.2", 
       "wu-2.4", "wu-2.6.0", "23c8", "WebSTAR", "1.3.3c", "1.3.5", "v2.3.4"]


def mssql_scan():
    
    df = pd.read_csv('nmap.csv', delimiter=';')

    for index, row in df.iterrows():
        for x in row:
            mssql_filter = row['host'], row['product'], row['version']            
            if x == '12.00.2000': # for testing
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter)) 
            elif x == '13.00.1708': # for testing
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == 'MSSQL 2000':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == 'MSDE':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '8.00.194':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '8.00.384':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '8.00.534':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '8.00.760':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter)) 
            elif x == '8.00.2039':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '9.00.1399.06':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '9.00.2047.00':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '9.00.3042.00':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            elif x == '12.00.2000':
                print('[+] Vulnerable MSSQL Server found: ' + str(mssql_filter))
            else:
                pass
    item_counts = df["product"].value_counts()
    print('*'*10)
    print(item_counts)
    print('*'*10)

def mysql_scan():
    
    df = pd.read_csv('nmap.csv', delimiter=';')

    for index, row in df.iterrows():
        for x in row:
            mysql_filter = row['host'], row['product'], row['version']
            if x == '5.7.32-35-log': # for testing
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter) + '[ just for testing ]') 
            elif x == '5.7.33-36': # for testing
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter) + '[ just for testing ]')  
            elif x == '5.0.51a-24+lenny2':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.0.45-Debian_1ubuntu3.1-log':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.5.9':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.5':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.4':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.3':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))   
            elif x == '0.9.2':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '2.4.6':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.0.45-community-nt':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            elif x == '5.1.22-rc-community':
                print('[+] Vulnerable MYSQL Server found: ' + str(mysql_filter))  
            else:
                pass
    item_counts = df["product"].value_counts()
    print('*'*10)
    print(item_counts)
    print('*'*10)  

def ftp_scan():

    df = pd.read_csv('nmap.csv', delimiter=';')

    for index, row in df.iterrows():
        for x in row:
            ftp_filter = row['host'], row['product'], row['version']
            if x == '12.00.2000': # for testing
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter)) 
            elif x == '13.00.1708': # for testing
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3.2rc3':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3.3b':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.2':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3.0':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3.2rc3':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter)) 
            elif x == '1.3.3b':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '3.2.0.0.258':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '3.4.0.0.348':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '3.3.0':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '3.4.0':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '3.2':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == 'wu-2.4':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == 'wu-2.6.0':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '23c8':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == 'WebSTAR':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3.3c':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == '1.3.5':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))
            elif x == 'v2.3.4':
                print('[+] Vulnerable FTP Server found: ' + str(ftp_filter))    
            else:
                pass
    item_counts = df["product"].value_counts()
    print('*'*10)
    print(item_counts)
    print('*'*10)

nmap_scan()
