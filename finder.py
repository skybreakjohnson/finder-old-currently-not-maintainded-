
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("finder").setMaster("local")
sc = SparkContext(conf=conf)
sc.stop()
sc = SparkContext(conf=conf)
import os
import nmap

def banner():
    os.system("clear")
    print("""
 /'___\ __            /\ \                 
/\ \__//\_\    ___    \_\ \     __   _ __  
\ \ ,__\/\ \ /' _ `\  /'_` \  /'__`\/\`'__\
 \ \ \_/\ \ \/\ \/\ \/\ \L\ \/\  __/\ \ \/ 
  \ \_\  \ \_\ \_\ \_\ \___,_\ \____\\ \_\ 
   \/_/   \/_/\/_/\/_/\/__,_ /\/____/ \/_/ 

Ver: 0.0.2-build
""")

# Start
banner()
jo = input("""
1. Top 10 (Test) 6. Microsoft (work)
2. Myssql        7. Webcam    (work)   
3. Mssql         8.
4. Http          9.
5. Ftp           10. All 

> """)
how_many = input("Hosts: ")

# initialisiere Nmap Scan
def nmap_scan():
    nm = nmap.PortScanner()
    nm.scan(
       arguments=
       "-Pn -T5 -p80 -sV --version-light --max-retries=1 -iR " + how_many + " -n"
    )

# erstelle csv file
    csv = nm.csv()
    with open("nmap.csv", "w") as file:
        file.write(csv)

# lade csv file in Spark
    x = sc.textFile("nmap.csv")

# ausgewählter service (Vorübergehend...!)
    if jo == "1":
        #top_10()
        microsoft_ips()
        #webcam_ips()
    else:
        print("Fuck you im a Pre-Alpha! Bye.")
        exit(1)

# Wie viele offene Ports
    count = x.map(lambda x: x.split(";"))\
        .filter(lambda x: x[6] == "open").count()
    print("Devices with open port found: ", count)

# Liste der vulnerable versions
iis = ["microsoft", "6.0", "5.0", "4.0"]
mysql = ["5.0.51a-24+lenny2", "5.0.45-Debian_1ubuntu3.1-log", "5.5.9", "5.5",
         "5.4", "5.3", "0.9.2", "2.4.6", "5.0.45-community-nt",
         "5.1.22-rc-community"] 
mssql = ["MSSQL 2000", "MSDE", "8.00.194", "8.00.384", "8.00.534", "8.00.760",
         "8.00.2039", "9.00.1399.06", "9.00.2047.00", "9.00.3042.00"]
http = ["WRT160n" ]
ftp = ["1.3.2rc3", "1.3.3b", "1.2", "1.3.0", "1.3.2rc3", "1.3", "1.3.3b",
       "3.2.0.0.258", "3.4.0.0.348", "3.4.0.0.348", "3.4.0". "3.3.0", "3.2", 
       "wu-2.4", "wu-2.6.0", "23c8", "WebSTAR", "1.3.3c", "1.3.5", "v2.3.4"]

def top_10():
    rdd = sc\
    .textFile("nmap.csv")\
    .map(lambda x: x.split(";"))\
    .cache()
    x = rdd\
    .filter(lambda x:\
    x[6] == "open")\
    .filter(lambda x:\
    "microsoft" in x[12] or\
    "nginx" in x[12] or\
    "cam" in x[12])\
    .collect()
    print("*"*10)
    print("[+] Services ", x)

def microsoft_ips():
    rdd = sc\
    .textFile("nmap.csv")\
    .map(lambda x: x.split(";"))\
    .cache()
    x = rdd\
    .filter(lambda x:\
    iis[0] in x[12]\
    and iis[1] in x[10]\
    or iis[0] in x[12]\
    and iis[2] in x[10]\
    or iis[0] in x[12]\
    and iis[3] in x[10])\
    .map(lambda x: x[0])\
    .collect()
    print("*"*10)
    print("[+] Vulnerable Microsoft IIS Server found: ", x)

def webcam_ips():
    rdd = sc\
    .textFile("nmap.csv")\
    .map(lambda x: x.split(";"))\
    .cache()
    x = rdd\
    .filter(lambda x:\
    "cam" in x[12])\
    .map(lambda x:\
    x[0] and x[4] and x[7])\
    .collect()
    print("*"*10)
    print("[+] Webcam found: ", x)

# alle IP's in einer Liste    
# ips = x.map(lambda x: x.split(";")).map(lambda x: x[0]).collect()

nmap_scan()

# major_release.minor_release.build
# Ver: 0.0.1-build
# - nothing useful
# Ver: 0.0.2-build
# - filter is working
# - add menu
# - make list for vulnerable versions
# To fix:
