import requests, threading, datetime, sys, os, time
from time import sleep

a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

os.system('clear')
print ('Subscribe yt ku ngab Brezxy ok!')
os.system('termux-open-url https://youtube.com/channel/UCQGgmljcA-bap-13YdL-sAQ')
sleep(3)
os.system('clear')
# sssst
banner= """            
\033[37m ███╗   ██╗ ██████╗
\033[37m ████╗  ██║██╔═══██╗
\033[37m ██╔██╗ ██║██║   ██║
\033[37m ██║╚██╗██║██║   ██║
\033[37m ██║ ╚████║╚██████╔╝
\033[37m ╚═╝  ╚═══╝ ╚═════╝                     
\033[35m ██╗     ██╗███╗   ███╗██╗████████╗   
\033[35m ██║     ██║████╗ ████║██║╚══██╔══╝    
\033[35m ██║     ██║██╔████╔██║██║   ██║       
\033[35m ██║     ██║██║╚██╔╝██║██║   ██║       
\033[35m ███████╗██║██║ ╚═╝ ██║██║   ██║       
\033[35m ╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝                                      
\033[35m[•]───────────────────────────────────────────[•]
\033[37m | [+]  Author  : Brezxy 		       |
\033[37m | [+]  Credits : Eskeyz		       |
\033[37m | [+]  TEAM    : DARK CYBER HUNTER            |
\033[37m | [+]  Chanel  : Brezxy		       |
\033[35m[•]───────────────────────────────────────────[•]"""
os.system('clear')
print(banner)

def main():
	global auth, maxerr, api, pos, dely
	api = "kitkabackend.eastus.cloudapp.azure.com:5010"
	auth = str(input("\033[37m Auth Key : "))
	pos = int(input("""
\033[37m 1 : Round 2 (Eliminated)
\033[37m 2 : Round 3 (Eliminated)
\033[37m 3 : Round 3 (Winner)
Input : """))
	dely = float(input("\n\033[37mDelay ( Ex. 2.0 ): "))
	thr = int(input("\n\033[37mThreads ( Default '1' ): "))
	print (f"\033[1;30m<════════════[\033[1;33;41m • \033[1;37m STARTING \033[1;33m• \033[0m\033[1;30m]══════════════>")
	for _ in range(thr):
	        threading.Thread(target=s).start()

def s():
        global maxerr
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': "keep-alive",
                            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36',
                        }
                        response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
                        if response.status_code == 200:
                                id = response.text.split('"Id":')[1].split(',')[0]
                                nama = response.text.split('"Username":')[1].split(',')[0]
                                trophy = response.text.split('"SkillRating":')[1].split(',')[0]
                                crown = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r\033[37m[{dt.minute}:{dt.second}] \033[31;1m{id} | \033[37m{nama} | \033[1;37m{crown} | \033[33;1m{trophy}")
                                sys.stdout.flush()
                        elif response.status_code == 403 and response.text == "BANNED":
                                print (f"\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Account get Banned! \033[1;33m• \033[0m\033[1;30m]══════════════>")
                                break;
                                sys.exit(0)
                        elif response.text == "SERVER_ERROR":
                                continue
                        else:
                                print(f"[{response.status_code}] Ini Bukan Expired Tunggu aja")
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__main__":
	main()
