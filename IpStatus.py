import requests
import json
import sys,argparse
import bcolors
import os

def banner():
    print("""
               ██╗██████╗░░░░░░░░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗
               ██║██╔══██╗░░░░░░██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
               ██║██████╔╝█████╗╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░
               ██║██╔═══╝░╚════╝░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
               ██║██║░░░░░░░░░░░██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝
               ╚═╝╚═╝░░░░░░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░                                                                                                                             
                                                                      Code By: NG
              """
          )

if (len(sys.argv) > 1):
    banner()
    if((sys.argv[1] != 'a')|(sys.argv[1] != 'i')):
        try:
            input_api = sys.argv[2]
            input_ip = sys.argv[4]

            print(bcolors.BITALIC + "Testing for Ip address status from the mentioned location")
            if(os.path.exists(input_ip) == False):
               parser = argparse.ArgumentParser()
               parser.add_argument("-a", required=True)
               parser.add_argument("-i", required=True)
               args = parser.parse_args()
               try:
                input_url = 'https://api.hetrixtools.com/v2/' + input_api + '/blacklist-check/ipv4/' + input_ip  + '/'
                print(bcolors.BOLD + 'Full URL',input_url)
                input_url_status = requests.get(input_url).status_code

                input_url_text = requests.get(input_url).text
                input_url_json = input_url_text.encode("utf-8")
                input_url_decode = json.loads(input_url_json)
                print(bcolors.BITALIC + "Status", input_url_decode['status'])
                input_array = []

                for j in range(len(input_url_decode['blacklisted_on'])):
                    input_array.append(input_url_decode['blacklisted_on'][j]['delist'])

                input_set = set()
                unique_array = []
                str = " "
                print(bcolors.BOLD + 'Unique URL for checking blacklisting Ips')
                for j in input_array:
                    if j not in input_set:
                        unique_array.append(j)
                        input_set.add(j)
                print(str.join(unique_array))
               except:
                print(bcolors.ERRMSG + 'Ip status can not be find for this ip address')

            elif(os.path.exists(input_ip) == True):
                parser = argparse.ArgumentParser()
                parser.add_argument("-a", required=True)
                parser.add_argument("-i", required=True)
                args = parser.parse_args()

                input_file = open(input_ip, "r")
                input_file_line = input_file.readlines()
                for file_ip in input_file_line:
                    try:
                        input_file_ip = file_ip.strip()

                        input_url = 'https://api.hetrixtools.com/v2/' + input_api + '/blacklist-check/ipv4/' + input_file_ip + '/'
                        print('*************************************************')
                        print(bcolors.BOLD + 'Full URL', input_url)

                        input_url_status = requests.get(input_url).status_code
                        input_url_text = requests.get(input_url).text
                        input_url_json = input_url_text.encode("utf-8")
                        input_url_decode = json.loads(input_url_json)
                        print(bcolors.BITALIC + "Status", input_url_decode['status'])
                        input_array = []
                        for j in range(len(input_url_decode['blacklisted_on'])):
                            input_array.append(input_url_decode['blacklisted_on'][j]['delist'])

                        input_set = set()
                        unique_array = []
                        str = " "
                        print(bcolors.BOLD + 'Unique URL for checking blacklisting Ips')
                        for j in input_array:
                            if j not in input_set:
                                unique_array.append(j)
                                input_set.add(j)
                        print(str.join(unique_array))
                    except:
                           print(bcolors.ERRMSG + 'Ip status can not be find for this ip address')
        except:
            print(bcolors.OKMSG + 'Please enter python IpStatus.py -a < Valid api key from your account > -i < Mentioned the valid Ipaddress > ')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
            print(bcolors.BOLD + 'usage: IpStatus.py [-h] -a API' '\n' 'OPTIONS:' '\n' '-h,--help    '
                                 'show this help message and exit' '\n''-a API,   --api API' '\n' '-i IpAddress    Ip address which status you want to search')

    elif ((sys.argv[1] != '-a')|(sys.argv[1] != '-i')):
            print(bcolors.OKMSG + 'Please enter -a < Valid api key from your account > -i < Mentioned the valid Ipaddress >')
    else:
            banner()
            print(bcolors.ERR + 'Please select valid options(-a,-i) or -h from IpStatus.py')
