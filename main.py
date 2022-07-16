import requests, threading, datetime, sys, os, time
from time import sleep

os.system('clear')
print ('Subscribe yt ku ngab Brezxy ok!')
os.system('termux-open-url https://youtube.com/channel/UCQGgmljcA-bap-13YdL-sAQ')
sleep(3)
os.system('clear')
# Recore : Brezxy 
banner= """
╔════════════════════════════════════════════════╗
║  [•] Authour : Brezxy                                   ║
║  [•] Credits : https://github.com/Eskeyz                ║
║  [•] Yotube  : Brezxy                                   ║
╚════════════════════════════════════════════════╝
╔═══════════════════════════╗
║     JANGAN TERLALU BRUTAL      ║
╚═══════════════════════════╝"""
sleep(1)
print(banner)

def main():
	global auth, maxerr, api, pos, dely
	api = "kitkabackend.eastus.cloudapp.azure.com:5010"
	auth = str(input("Auth Key : "))
	pos = int(input("""
1 = Round 1 (Eliminated)
2 = Round 2 (Eliminated)
3 = Round 3 (Winner)
Input: """))
	dely = float(input("\nDelay ( Ex. 2.0 and etc ): "))
	thr = int(input("\nThreads ( Default '1' ): "))
	print("="*64)
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
                                negara = response.text.split('"Country":')[1].split(',')[0]
                                nama = response.text.split('"Username":')[1].split(',')[0]
                                trophy = response.text.split('"SkillRating":')[1].split(',')[0]
                                crown = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r[{dt.hour}:{dt.minute}:{dt.second}] {negara} | Username: {nama} | Trophy: {trophy} | Crowns: {crown}")
                                sys.stdout.flush()
                        elif response.status_code == 403 and response.text == "BANNED":
                                print (f"\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Account get Banned! \033[1;33m• \033[0m\033[1;30m]══════════════>")
                                break
                                sys.exit(0)
                        elif response.text == "SERVER_ERROR":
                                continue
                        else:
                                print(f"[{response.status_code}] Code Expired!")
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__main__":
	main()
