'''
CREATOR: KAPIL SHARMA

Mail - djkaps1707@gmail.com
Twitter - QapilS
Instagram - @qapil.sh04
Github - kuzuri-03
Telegram - kuzuri_17
'''

import sys, os, pyowm, pyttsx3, time, datetime, smtplib, wolframalpha, random, geocoder, webbrowser
from playsound import playsound
from data_store import *

#========================== Calculator Function ========================================
class Calc:
	def add(self, num1,num2):
		return num1 + num2

	def sub(self, num1,num2):
		return num1 - num2

	def multi(self, num1,num2):
		return num1 * num2
				
	def div(self, num1,num2):
		return num1 / num2

	def sqr(self, num1,num2):
		return num1 ** num2

	def d_div(self, num1,num2):
		return num1 // num2


#=========================  Print Function  ===============================================
def pr(sent):
    print('\n' + 'JARVIS : ' + sent + '\n')
def pr_f(sent):
    print('\n' + 'JARVIS : ' + sent)
def pr_l(sent):
    print('JARVIS : ' + sent + '\n')

#=========================  Speak Function  ===============================================
client = wolframalpha.Client('[client ID]')
owm = pyowm.OWM('[API]')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.runAndWait()


def speak(audio):
    os.system('color c')
    engine.say(audio)
    engine.runAndWait()
    os.system('color a')

#========================== Play Music Function ===========================================
def playMusic():
    music_dir = format(profile[4].replace('\n', ''))
    songs = os.listdir(music_dir)
    for music_list in songs:
        pr(music_list)
    os.startfile(os.path.join(music_dir, songs[0]))

#========================== Create Folder Function ========================================

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        print('Error in creating new folder - ' + directory)
        
#============================= Alarm Function =============================================

def alarm():
    hour = int(input('Enter hour: '))
    min = int(input('Enter minute: '))
    sec = int(input('Enter seconds: '))

    print(f'Alarm is set for {hour}:{min}:{sec}')

    while True:
        if time.localtime().tm_hour==hour and time.localtime().tm_min == min and time.localtime().tm_sec == sec:
            print('Wake UP')
            speak('Wake UP')
            break
    playMusic()

#========================== Send Email Function ========================================

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('[your email]', '[your password]')
    server.sendmail('[your email]', to, content)
    server.close()

#========================== J.A.R.V.I.S. Version ============================================
def show_version():
    print ('''                  ################################################
                  #                J.A.R.V.I.S.                  #
                  #                                              #
                  #  Project        : JARVIS AI                  #
                  #  Model no.      : JV_001928                  #
                  #  Version        : V-1.0.5                    #
                  #  Developer      : Kapil Sharma               #
                  #                                              #
                  ################################################''')
    speak('Hi, I\'m JARVIS, version one point zero point five')

def show_creator_info():
    print('''
CREATOR: KAPIL SHARMA

Mail - djkaps1707@gmail.com
Twitter - QapilS
Instagram - @qapil.sh04
Github - kuzuri-03
Telegram - kuzuri_17
''')
    speak('here is some information about my creator Kapil Sharma')

#=====================  Clear Terminal  ===========================================
def clear_terminal():
    os.system('cls')
    speak('Terminal cleared')

#=====================  Chat History  ============================================
def show_history():
    history_file = open('includes\\history_file.jv', 'r')
    r_history_file = history_file.readlines()
    y = 1

    if r_history_file:
        pr('Here is the history of what you said me at what time -')
        for x in r_history_file:
            print(f'{y}.) {x}')
            y += 1
        speak('Here is the history of what you said at what time -')
    else:
        pr('There is no saved History in there.')
        speak('There is no saved History in there.')
    history_file.close()

def clear_history():
    pr('Do you really want me to clear all history. [Y/N]')
    speak('Do you really want me to clear all history.')
    choice = str(input())

    if choice in choice_y:
        with open('includes\\history_file.jv', 'w') as history_file:
            history_file.write('')
        print(' All history cleared.')
        speak('All history cleared.')
    elif choice in choice_n:
        print(' Ok sir !')
        speak('Ok sir')
    else:
        print('You were suppose to answer in yes or no.')
        speak('You were suppose to answer in yes or no.')

def clear_history_fast():
    with open('includes\\history_file.jv', 'w') as history_file:
        history_file.write('')
    pr(random.choice(done))
    speak(random.choice(done))

#=========================      Greet      ============================================
def greet_user():
    hi_ans = random.choice(hi)
    pr(hi_ans)
    speak(hi_ans)

def greet_user_in_different_language():
    greet = random.choice(list(rd_greet.keys()))
    greet_lang = rd_greet.get(greet)
    pr(f'{greet} that\'s Hello in {greet_lang}, how can i help you ?')
    speak(f'{greet}, that\'s Hello in {greet_lang}, how can i help you ?')

def show_appreciation():
    glad_rnd = random.choice(glad)
    pr(glad_rnd)
    speak(glad_rnd)

def ask_about_user():
    rand_fine = random.choice(fine)
    pr(rand_fine)
    speak(rand_fine)

#=========================      Flip a coin      ============================================
def flip_coin():
    pr('Flipping...')
    speak('Flipping')
    playsound('coinflip.mp3')

    toss = random.randint(0, 1)

    if toss == 0:
        pr_l('Its Head')
        speak('Its Head')
    elif toss == 1:
        pr_l('Its Tail')
        speak('Its Tail')

#=========================      Remember      ============================================
def show_reminders():
    with open('includes\\remem_file.jv', 'r') as remem_file:
        r_remem_file = remem_file.readlines()
    y = 1

    if r_remem_file:
        pr('You told me to remember following things -')
        for x in r_remem_file:
            print(f'{y}.) {x}')
            y += 1
        speak('You told me to remember following things -')
    else:
        pr('You haven\'t told me anything to remember.')
        speak('You haven\'t told me anything to remember.')

def add_reminder(query):
    remem = query.replace('remember', '')
    with open('includes\\remem_file.jv', 'a') as remem_file:
        if remem.strip():
            remem_file.write(remem + '\n')
            pr('Ok I\'ll remember that !')
            speak('Ok I\'ll remember that')
        else:
            pr('Maybe you forget to tell what to remember.')
            speak('Maybe you forget to tell what to remember.')

def forget_reminder_by_number(query):
    chars = 'forget# '
    for c in chars:
        query = query.replace(c, '')
    try:
        query = int(query)
        query -= 1
        with open('includes\\remem_file.jv','r') as infile:
            lines = infile.readlines()
        with open('includes\\remem_file.jv','w') as outfile:
            for index,line in enumerate(lines):
                if index != query:
                    outfile.write(line)
        pr(f'Forgotten #{query+1}')
        speak(f'Forgotten number {query+1}')
    except ValueError:
        pr('Invalid number format.')
        speak('Invalid number format.')

def forget_all_reminders():
    with open('includes\\remem_file.jv', 'r') as remem_file:
        r_remem_file = remem_file.readlines()

    if r_remem_file:
        pr('Do you really want me to forget everything that I remember. [Y/N]')
        speak('Do you really want me to forget everything that I remember.')
        choice = str(input())

        if choice in choice_y:
            with open('includes\\remem_file.jv', 'w') as remem_file:
                remem_file.write('')
            pr('As per your choice, I erased everything from my memory.')
            speak('As per your choice, I erased everything from my memory.')
        elif choice in choice_n:
            pr('Ok sir !')
            speak('Ok sir')
        else:
            pr('You were suppose to answer in yes or no.')
            speak('You were suppose to answer in yes or no.')
    else:
        pr('You haven\'t told me anything to remember.')
        speak('You haven\'t told me anything to remember.')

#==========================  YourName  ==================================================
def clarify_name_request():
    pr('Please be clear with the words, I mean your name or my name')
    speak('Please be clear with the words, I mean your name or my name')

def tell_jarvis_name():
    pr('My name is Jarvis and I\'m your assistant AI.')
    speak('My name is Jarvis and I\'m your assistant AI.')

#==========================  MyName  ==================================================
def change_user_name():
    speak(random.choice(doing))
    pr('Enter your new name :')
    speak('Enter your new name.')
    name = str(input())

    pr(f'So its {name} right ! [Y/N]')
    speak(f'So its {name} right !')
    choice = str(input())

    if choice in choice_y:
        profile[0] = name + '\n'
        with open('includes\\profile.jv', 'w') as profile_open:
            profile_open.writelines(profile)

        pr(f'Fine, i\'ll call you {name} from now.')
        speak(f'Fine, i\'ll call you {name} from now.')
    elif choice in choice_n:
        pr('Ok fine !')
        speak('ok fine')

def tell_user_name():
    if profile[0] == '\n':
        pr_f(' You haven\'t told me your name. Do you want me to remember your name ?[Y/N]')
        speak('You haven\'t told me your name. Do you want me to remember your name ?')
        choice = str(input())

        if choice in choice_y:
            pr_f('Enter your name please')
            speak('Enter your name please')
            name = str(input())

            pr_f(f'So its {name} right ! [Y/N]')
            speak(f'So its {name} right !')
            choice = str(input())

            if choice in choice_y:
                profile[0] = name + '\n'
                with open('includes\\profile.jv', 'w') as profile_open:
                    profile_open.writelines(profile)

                pr(f'Fine, i\'ll call you {name} from now.')
                speak(f'Fine, i\'ll call you {name} from now.')
            elif choice in choice_n:
                pr_f('So what should I call you ?')
                speak('So what should I call you ?')
                name = str(input())

                profile[0] = name + '\n'
                with open('includes\\profile.jv', 'w') as profile_open:
                    profile_open.writelines(profile)

                pr(f'Fine, i\'ll call you {name} from now.')
                speak(f'Fine, i\'ll call you {name} from now.')

            else:
                pr('You were supposed to answer in yes or no !')
                speak('You were supposed to answer in yes or no !')


        elif choice in choice_n:
            pr('Ok fine, no problem. Perhaps you would like to talk more with me !')
            speak('Ok fine, no problem. Perhaps you would like to talk more with me !')
        else:
            pr('You were supposed to answer in yes or no !')
            speak('You were supposed to answer in yes or no !')
    else:
        user_name = profile[0].strip()
        pr(f'That\'s {user_name} !')
        speak(f'That\'s {user_name}')

#==========================  Sites Surf  ==================================================
def open_google():
    pr('Opening Google...')
    speak('Opening Google')
    webbrowser.open('google.com')
    pr_l('Here you go !')
    speak('Here you go !')

def open_youtube():
    pr('Opening YouTube...')
    speak('Opening YouTube')
    webbrowser.open('youtube.com')
    pr_l('Here you go !')
    speak('Here you go !')

def open_facebook():
    pr('Opening Facebook...')
    speak('Opening Facebook')
    webbrowser.open('fb.com')
    pr_l('Here you go !')
    speak('Here you go !')

def open_instagram():
    pr('Opening Instagram...')
    speak('Opening Instagram')
    webbrowser.open('instagram.com')
    pr_l('Here you go !')
    speak('Here you go !')

#==========================  Site Searches  ==================================================
def search_google(query):
    pr('Searching on Google...')
    speak('Searching on Google...')
    g_results = query.replace('search google ', '')
    webbrowser.open(f'google.com/search?q={g_results}')
    pr_l('Here you go !')
    speak('Here you go !')

def search_youtube(query):
    pr('Searching on YouTube...')
    speak('Searching on YouTube...')
    yt_results = query.replace('search youtube ', '')
    webbrowser.open(f'youtube.com/results?search_results={yt_results}')
    pr_l('Here you go !')
    speak('Here you go !')

#==========================  Wikipedia  ==================================================
def search_wikipedia(query):
    try:
        pr('Searching Wikipedia')
        speak('Searching Wikipedia')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=3)
        results_speak = wikipedia.summary(query, sentences=2)
        pr_l('According to wikipedia...')
        pr_l(results)
        speak('According to wikipedia...')
        speak(results_speak)
    except:
        pr('No result found, maybe due to incorrect keyword or bad internet connectivity.')
        speak('No result found, maybe due to incorrect keyword or bad internet connectivity.')

#==========================  Weather  ==================================================
def get_weather():
    speak(random.choice(doing))
    try:
        pr_f('Enter Location :')
        speak('Enter location')

        city = str(input())
        location = owm.weather_at_place(city)
        weather = location.get_weather()
        temp = weather.get_temperature('celsius')
        humidity = weather.get_humidity()


        current_temp = int(temp.get('temp'))
        max_temp = int(temp.get('temp_max'))
        min_temp = int(temp.get('temp_min'))

        pr_f(f'Here are the weather conditions of {city}')
        pr_f(f'Current Temperature: {current_temp} °C')
        pr_f(f'Maximum Temperature: {max_temp} °C')
        pr_f(f'Minimum Temperature: {min_temp} °C')
        pr_f(f'And Humidity: {humidity} %')

        speak(f'Current Temperature: {current_temp} °Celsius')
        speak(f'Maximum Temperature: {max_temp} °Celsius')
        speak(f'Minimum Temperature: {min_temp} °Celsius')
        speak(f'And Humidity: {humidity} %')
    except:
        pr('Sorry sir, nothing found. Please check for internet access.')
        speak('Sorry sir, nothing found. Please check for internet access.')

def get_my_location():
    g = geocoder.ip('me')
    loc = g.geojson
    pr(loc)
    speak(loc)

#==========================  Open Files and Exe(s) ==================================================
def open_chrome():
    pr_f('Opening Google Chrome...')
    chrome_dir = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    os.startfile(chrome_dir)
    speak('opening google chrome')
    pr(random.choice(done))

#=========================   Timer ==================================================
def set_timer():
    speak('Set Timer')
    try:
        sec = int(input('Enter time limit (in sec) : '))
        pr_f(f'So alarm will ring after {sec} seconds')
        for i in range(sec):
            time.sleep(1)

        playMusic()
    except ValueError:
        pr('Invalid input. Please enter a number.')
        speak('Invalid input. Please enter a number.')

#==========================  Folders/Directories ==================================================
def create_folder_with_name(query):
    folder_name = query.replace('create folder ', '')
    createFolder(folder_name)
    pr(f'New folder created {folder_name}')
    speak(f'New folder created {folder_name}')

def create_default_folder():
    createFolder('New Folder')
    pr('New folder created')
    speak('New folder created')

#=========================   Email ==================================================
def send_email():
    try:
        pr(random.choice(doing))
        speak('To whom ?')
        to = str(input('To :'))
        speak('What would be the content ?')
        content = str(input('Content :'))

        sendEmail(to, content)
        pr(f'Email sent to {to}')
        speak(f'Email sent to {to}')
    except:
        pr('Sorry, unable to sent email')
        speak('Sorry, unable to sent email')

#=========================   PlayMusic  ==================================================
def open_music_directory():
    pr('Opening Music Directory...')
    speak('got it')
    os.system(f'explorer {profile[4]}')

def play_music():
    pr('Playing Music...')
    speak('Playing Music')
    playMusic()

#=========================   Directories  ==================================================
def open_jarvis_project():
    os.system(f'explorer H:\\python\\jarvis\\jarvis')
    pr('Opening Jarvis Project...')
    speak('Opening Jarvis Project...')

def open_test_directory():
    os.system(f'explorer H:\\test')
    pr('Opening Test Directory...')
    speak('Opening Test Directory...')

def open_movie_directory():
    os.system(f'explorer {profile[5]}')
    pr('Opening Movie Directory...')
    speak('Opening Movie Directory...')

def open_directory(query):
    dir = query.replace('dir ', '')
    os.system(f'explorer {dir}')
    pr('Opening Directory...')
    speak('Opening Directory...')

#=========================   DateTime  ==================================================
def tell_time():
    strTime = datetime.datetime.now().strftime('%H:%M %p')
    pr(f'The time is {strTime}')
    speak(f'The time is {strTime}')

def tell_date():
    strDate = datetime.datetime.now().strftime('%D')
    pr(f'The date is {strDate}')
    speak(f'The date is {strDate}')

#=========================   Calculator  ==================================================
def show_calculator_help():
    print ('''                  ####################################################
                  #                Calculator Help                   #
                  #  Step 1.) Enter first number.                    #
                  #  Step 2.) Enter operator number.                 #
                  #           such as [+, -, *, /, ** or //]         #
                  #           + is for Addition                      #
                  #           - is for Subtraction                   #
                  #           * is for Multiplication                #
                  #           / is for Division                      #
                  #           ** is for Squaring                     #
                  #           // is for Remainder Division           #
                  #  Step 3.) Enter second number.                   #
                  #           (you have to enter the power of the    #
                  #           number if you are using **)            #
                  ####################################################''')
    speak ('Here are the instructions to use the Calculator.')

def use_calculator():
    calculator = Calc()
    try:
        speak(random.choice(doing))
        num1 = float(input('Enter 1st Number : '))
        operator = str(input('Enter Operator : '))
        num2 = float(input('Enter 2nd Number : '))

        if operator == '+':
            sum = calculator.add(num1, num2)
        elif operator == '-':
            sum = calculator.sub(num1, num2)
        elif operator == '*':
            sum = calculator.multi(num1, num2)
        elif operator == '/':
            sum = calculator.div(num1, num2)
        elif operator == '**':
            sum = calculator.sqr(num1, num2)
        elif operator == '//':
            sum = calculator.d_div(num1, num2)
        else:
            pr('Invalid Operator ! Use +, -, *, /, ** or // only. To see the list of features of Operators write \'calc help\'')
            speak('Invalid Operator !')
            return

        pr(f'Answer is {sum}')
        speak(f'Answer is {sum}')
    except ValueError:
        pr('Invalid input. Please enter numbers only.')
        speak('Invalid input. Please enter numbers only.')
    except:
        pr('An error occurred during calculation.')
        speak('An error occurred during calculation.')

def suggest_calculator():
    pr('Type \'calc\' keyword to use Calculator')
    speak('Type \'calc\' keyword to use Calculator')

#=========================   Launch Explorer  ==================================================
def goto_directory(query):
    speak(random.choice(doing))
    query = query.replace('goto ', '')
    os.system(f'explorer c:\\{query}')
    pr(random.choice(done))
    speak(random.choice(done))

#=========================   Trick   ==================================================
def show_trick():
    pr('Here is the best trick that I\'ve learned from Doctor Strange')
    speak('Here is the best trick that I\'ve learned from Doctor Strange')
    x=0

    def trick():
        nonlocal x
        print('Trick', x)
        os.system(f'explorer C:\\"{query.replace("open", "").replace("launch", "")}"')
        x+=1

    while True:
        try:
            trick()
        except KeyboardInterrupt:
            print('Really nigguh !!')
            speak('Really nigguh')
            break

#=========================   Siri/Alexa/Bixbi/Friday   ==================================================
def talk_about_siri():
    siri_ans = random.choice(siri)
    pr(siri_ans)
    speak(siri_ans)

def talk_about_alexa():
    alexa_ans = random.choice(alexa)
    pr(alexa_ans)
    speak(alexa_ans)

def talk_about_bixbi():
    bixbi_ans = random.choice(bixbi)
    pr(bixbi_ans)
    speak(bixbi_ans)

def talk_about_friday():
    friday_ans = random.choice(friday)
    pr(friday_ans)
    speak(friday_ans)

#=========================   Exit  ==================================================
def exit_jarvis():
    pr('Bye have a great time !!')
    speak('Bye have a great time !!')
    sys.exit()

#=========================   Wifi Connect and Disconnect  ==================================================
def disconnect_wifi():
    os.system('netsh wlan disconnect')
    pr_l('Disconnected !')
    speak('Disconnected !')

def connect_wifi(query):
    query = query.replace('wifi ', '').replace('wlan ', '').replace('connect ', '')
    os.system(f'netsh wlan connect name="{query}"')
    pr(f'Connected to {query}!')
    speak(f'Connected to {query}!')

#=========================   Shutdown/Restart/Sleep/Logoff/Signout  ==================================================
def force_shutdown():
    speak('Ok , good bye Sir !!')
    os.system('shutdown /s /t 0')
    sys.exit()

def force_restart():
    speak('Ok, see you later Sir !!')
    os.system('shutdown /r /t 0')
    sys.exit()

def force_logoff():
    speak('Ok Sir !!')
    os.system('shutdown /l /t 0')
    sys.exit()

def restart_pc():
    speak('Ok Sir !!')
    speak('You have about 30 seconds to save your files or abort the process of restarting PC. ')
    os.system('shutdown /r')
    sys.exit()

def shutdown_pc():
    speak('Ok Sir !!')
    speak('You have about 30 seconds to save your files or abort the process of shutting down PC.')
    os.system('shutdown /s')
    sys.exit()

def logoff_pc():
    speak('Ok Sir !!')
    speak('You have about 30 seconds to save your or abort the process of logging off PC')
    os.system('shutdown /l')
    sys.exit()

def sleep_pc():
    speak('Ok Sir')
    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

def abort_shutdown():
    speak('Ok Sir')
    os.system('shutdown /a')
    speak('Command Executed')

#=========================  Chatting  =========================================================
def handle_empty_query():
    blank_rnd = random.choice(blank)
    pr(blank_rnd)
    speak(blank_rnd)

def tell_fact():
    fact_rnd = random.choice(facts)
    pr(fact_rnd)
    speak(f'Do you know, {fact_rnd}')

def tell_google_fact():
    google_fact_rnd = random.choice(google_facts)
    pr(google_fact_rnd)
    speak(google_fact_rnd)

def list_abilities():
    print ('''                  ####################################################
                  #       I can serve you following facilities :     #
                  #                                                  #
                  #  1.) I can play music, movies and games.         #
                  #  2.) I can remember things.                      #
                  #  3.) I can search anything on Google, Youtube    #
                  #      and Wikipedia.                              #
                  #  4.) I can tell you Facts about many things.     #
                  #  5.) I can control your PC and perform functions #
                  #      like shutdown, restart, logout, sleep etc.  #
                  #  6.) I can set timer and alarm.                  #
                  #  7.) I can act as a calculator.                  #
                  #  8.) I can send Email.                           #
                  #  9.) You can chat with me.                       #
                  #  10.) I'll connect you to wifi, whenever you     #
                  #       want.                                      #
                  ####################################################''')
    speak('Here are some top 10 services I can provide you.')

def talk_about_owner():
    owner_rnd = random.choice(owner)
    pr(owner_rnd)
    speak(owner_rnd)

def talk_about_marriage():
    married_rnd = random.choice(married)
    pr(married_rnd)
    speak(married_rnd)

def show_remorse():
    remorse_rnd = random.choice(remorse)
    pr(remorse_rnd)
    speak(remorse_rnd)

def talk_about_user():
    me_rnd = random.choice(me)
    pr(me_rnd)
    speak(me_rnd)

def show_understanding():
    expressions_rnd = random.choice(expressions)
    pr(expressions_rnd)
    speak(expressions_rnd)

#=========================   Not Understand  ==================================================
def search_web_and_wikipedia(query):
    speak('Searching on web')
    try:
        try:
            res = client.query(query)
            results = next(res.results).text
            pr(results)
            speak(results)

        except:
            results = wikipedia.summary(query, sentences=2)
            speak('Got it.')
            pr_f('According to Wikipedia')
            pr_l(results)
            speak('According to Wikipedia')
            speak(results)

    except:
        notunderstand = random.choice(exception)
        pr_f('Nothing found !')
        pr(notunderstand)
        speak(notunderstand)
