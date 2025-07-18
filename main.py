'''
CREATOR: KAPIL SHARMA

Mail - djkaps1707@gmail.com
Twitter - QapilS
Instagram - @qapil.sh04
Github - kuzuri-03
Telegram - kuzuri_17
'''


import sys, os, pyowm, pyttsx3, time, datetime, webbrowser, smtplib, wikipedia, wolframalpha, random, geocoder
from playsound import playsound
from data_store import *
from func import *
#import speech_recognition as sr #pip install speechRecognition


ai = 'JARVIS :'

def main():
    while True:
        os.system('color a')
        doing_rnd = random.choice(doing)
        done_rnd = random.choice(done)

        #=====================  Query/History  ============================================
        history_file = open('includes\\history_file.jv', 'a')
        
        query = input('YOU : ')
        query = query.lower()
        
        DateTime = datetime.datetime.now().strftime('%H:%M %p') + ' ' + datetime.datetime.now().strftime('%D')
        str(DateTime)
        
        history_details = query + ' - ' + DateTime
        history_file.write(history_details)
        history_file.write('\n')
        history_file.close()
        
        #=====================  J.A.R.V.I.S. Version  ============================================
        if 'jarvis --v' in query or 'jv --v' in query:
            show_version()

        if 'kapil' in query or 'qapil' in query:
            show_creator_info()

        #=====================  Clear Terminal  ===========================================
        elif query == 'cls':
            clear_terminal()

        #=====================  Chat History  ============================================
        elif 'show' in query and 'history' in query or 'chat' in query and 'history' in query or 'history' in query:
            show_history()
            
        elif 'delete' in query and 'history' in query or 'clear' in query and 'history' in query:
            clear_history()

        elif query == 'cln':
            clear_history_fast()

        #=========================      Greet      ============================================
        elif 'hi' in query or 'hey' in query:
            greet_user()

        elif 'hello' in query:
            greet_user_in_different_language()
        
        elif 'good' in query or 'like' in query or 'great' in query or 'love' in query or 'bravo' in query or 'wow' in query or 'friend' in query or 'buddy' in query or 'pal' in query or 'thank' in query or 'thnx' in query:
            if 'bye' not in query:
                show_appreciation()

        elif "whats up" in query or "what\'s up" in query or 'how are you' in query:
            ask_about_user()

        #=========================      Flip a coin      ============================================
        elif 'flip a coin' in query:
            flip_coin()

        #=========================      Remember      ============================================
        elif 'told' in query and 'remember' in query or 'reminder' in query:
            show_reminders()
            
        elif 'remember' in query:
            add_reminder(query)

        elif 'forget' and '#' in query:
            forget_reminder_by_number(query)

        elif 'forget' in query:
            forget_all_reminders()

        #==========================  YourName  ==================================================
        elif 'your' in query and 'name' in query:
            if 'my' in query:
                clarify_name_request()
            else:
                tell_jarvis_name()

        #==========================  MyName  ==================================================
        elif 'change my name' in query:
            change_user_name()
        
        elif 'my' in query and 'name' in query:
            if 'your' in query:
                clarify_name_request()
            else:
                tell_user_name()

        #==========================  Sites Surf  ==================================================
        elif 'open google' in query:
            open_google()
        elif 'open youtube' in query:
            open_youtube()
        elif 'open facebook' in query or 'open fb' in query:
            open_facebook()
        elif 'open instagram' in query or 'open insta' in query:
            open_instagram()

        #==========================  Site Searches  ==================================================
        elif 'search google' in query:
            search_google(query)
        elif 'search youtube' in query:
            search_youtube(query)

        #==========================  Wikipedia  ==================================================
        elif 'wikipedia' in query:
            search_wikipedia(query)

        #==========================  Weather  ==================================================
        elif 'weather' in query:
            get_weather()

        elif 'my location' in query or 'current location' in query or 'where am i' in query or 'where i am' in query:
            get_my_location()

        #==========================  Open Files and Exe(s) ==================================================
        elif 'chrome' in query:
            open_chrome()

        #=========================   Timer ==================================================
        elif 'timer' in query:
            set_timer()

        #==========================  Folders/Directories ==================================================
        elif 'create folder ' in query:
            create_folder_with_name(query)

        elif 'create folder' in query:
            create_default_folder()
            
        #=========================   Email ==================================================
        elif 'email' in query:
            send_email()

        #=========================   PlayMusic  ==================================================
        elif 'music dir' in query:
            open_music_directory()
        elif 'play music' in query:
            play_music()

        #=========================   Directories  ==================================================
        elif 'jv project' in query:
            open_jarvis_project()
        elif 'test area' in query:
            open_test_directory()
        elif 'movie' in query:
            open_movie_directory()
        elif 'dir' in query:
            open_directory(query)

        #=========================   DateTime  ==================================================
        elif 'time' in query:
            tell_time()
        elif 'date' in query:
            tell_date()

        #=========================   Calculator  ==================================================
        elif 'calc help' in query:
            show_calculator_help()

        elif 'calc'in query:
            use_calculator()

        elif '+' in query or '-' in query or '*' in query or '/' in query:
            suggest_calculator()

        #=========================   Launch Explorer  ==================================================
        elif 'goto' in query:
            goto_directory(query)

        #=========================   Trick   ==================================================
        elif 'show' in query and 'trick' in query:
            show_trick()

        #=========================   Siri/Alexa/Bixbi/Friday   ==================================================
        elif 'siri' in query:
            talk_about_siri()
        elif 'alexa' in query:
            talk_about_alexa()
        elif 'bixbi' in query:
            talk_about_bixbi()
        elif 'friday' in query:
            talk_about_friday()

        #=========================   Exit  ==================================================
        elif 'exit' in query or 'bye' in query or 'close' in query:
            exit_jarvis()

        #=========================   Wifi Connect and Disconnect  ==================================================
        elif 'wifi' in query or 'wlan' in query:
            if 'disconnect' in query:
                disconnect_wifi()
            elif 'connect' in query:
                connect_wifi(query)

        #=========================   Shutdown/Restart/Sleep/Logoff/Signout  ==================================================
        elif 'shutdown f' in query:
            force_shutdown()
        elif 'restart f' in query:
            force_restart()
        elif 'logoff f' in query:
            force_logoff()
        elif 'restart' in query:
            restart_pc()
        elif 'shutdown' in query:
            shutdown_pc()
        elif 'logoff' in query:
            logoff_pc()
        elif 'sleep' in query:
            sleep_pc()
        elif 'abort' in query:
            abort_shutdown()

        #=========================  Chatting  =========================================================
        elif query is '':
            handle_empty_query()
        elif 'fact' in query:
            tell_fact()
        elif 'google fact' in query:
            tell_google_fact()
        elif 'what' in query and 'can' in query and 'do' in query:
            list_abilities()
        elif 'owner' in query:
            talk_about_owner()
        elif 'marry' in query or 'married' in query:
            talk_about_marriage()
        elif 'hurt' in query or 'hell' in query or 'angry' in query or 'bad' in query or 'damn' in query or 'poor' in query or 'shit' in query:
            show_remorse()
        elif 'me' in query:
            talk_about_user()
        elif 'oh' in query or 'ok' in query or 'fine' in query or 'hmm' in query:
            show_understanding()

        #=========================   Not Understand  ==================================================
        else:
            search_web_and_wikipedia(query)

if __name__ == '__main__':
    main()
