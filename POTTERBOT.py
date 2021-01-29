import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import string
import random
import os
import pywhatkit as kit
import calendar
from turtle import*
from tkinter import*
import cv2
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',190)
def intro_Screen():
    
    try:
        bgcolor("black")
        color("light green")
        penup()
        goto(-100,0)
        pendown()
        str="The Potter Bot"
        for i in str:
            speed('slowest')
            write(i,font=("algerian",32,"bold"))
            penup()
            forward(30)
            pendown()
        penup()
        goto(0,-50)
        pendown()
        write("click to continue")
        exitonclick()
    except:
        bgcolor("black")
        color("light green")
        penup()
        goto(-100,0)
        pendown()
        str="The Potter Bot"
        for i in str:
            speed('slowest')
            write(i,font=("algerian",32,"bold"))
            penup()
            forward(30)
            pendown()
        penup()
        goto(0,-50)
        pendown()
        write("click to continue")
        exitonclick()
def OpenCam():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")
def Audiobook():

    
    def Accept():
            root.destroy()
            window=Tk()
            frame = Frame(window, width=300, height=80)
            frame.pack_propagate(False) # prevent frame to resize to the labels size
            frame.pack()
            Label(text="What type of file do you want me to read").pack()
            p_button=Button(window,text="PDF",command=pdf)
            p_button.pack()
            p_button.place(width=50,x=120,y=30)
            t_button=Button(window,text="TXT",command=txt)
            t_button.pack()
            t_button.place(width=50,x=120,y=60)
    def Decline():
            Label(text="Sorry could not access the contents of your computer").pack()
    def pdf():
        window=Tk()
        book = askopenfilename()
        reader= PyPDF2.PdfFileReader(book)
        pages = reader.numPages
        window.mainloop()
        for num in range(0,pages):
            page = reader.getPage(num)
            txt = page.extractText()
            speak(txt)
            print(txt)
        window.destroy()
    def txt():
        window=Tk()
        book = askopenfilename()
        file=open(book)
        speak(file.read())
        print(file.read())
        file.close()
        window.destroy()
        
    root=Tk()
    frame = Frame(root, width=300, height=80)
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    label1=Label(text="SAGNIK would like to access the files on your computer")
    label1.pack()
    a_button=Button(root,text="Allow",command=Accept)
    a_button.pack()
    a_button.place(width=50,x=120,y=30)
    d_button=Button(root,text="Deny",command=Decline)
    d_button.pack()
    d_button.place(width=50,x=120,y=60)
    frame.pack()
    root.mainloop()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    day= int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    if day ==27 and month==1:
        speak("I'm not exactly sure Why I'm saying this. But as per my code I'm inclined to think that It's your birthday today so.....")
        speak("Happy Birthday ,miss Shreeja Shhorkaar")
    speak("Hello miss I am Harry how may I help you ")
def send_pressed():
        global respo,inp
        input_get = input_field.get().lower()
        print(input_get)
        var = StringVar()
        Display(input_get)
        ans=response(input_get)
        DisplayasResp(ans)
        speak(ans)
        input_user.set('')

def enter_pressed(event):
        global respo,inp
        input_get = input_field.get().lower()
        print(input_get)
        var = StringVar()
        Display(input_get)
        ans=response(input_get)
        DisplayasResp(ans)
        speak(ans)
        input_user.set('')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Display(txt):
    lbl=Label(text=txt,foreground="white",background="black")
    lbl.pack()
    lbl.place(width=300,height=100,x=700,y=120)
def DisplayasResp(txt1):
    lbl1=Label(text=txt1,foreground="white",background="blue")
    lbl1.pack()
    lbl1.place(width=300,height=100,x=0,y=340)
def Tasks(query):
    
    
      if "open youtube" in query :
          speak("Opening Youtube")
          webbrowser.open("https://www.youtube.com/")
      elif "search something" in query:
          speak("what should I search for you")
          c = takeCommand().lower()
          webbrowser.open(f"{c}")   
      elif "what is the time" in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Miss,the time is{strTime}")  
      elif "Harry tell me about yourself" in query:
          speak("Miss I am your friend,I will help you in your work  24 into 7,I love you very much and was created by your friend who gifted me to you")
      elif "sleep" in query:
          speak("Going to sleep")
          sys.exit(0)
      
      elif "goodbye" in query:
          speak("It was great working with you miss,have a good day,goodbye")
          sys.exit()
     
     
def sendmsg():
    try:
        while(True):
            speak("Dictate the number")
            ph=takeCommand()
            speak("the number you entered was"+ph+"is that correct?")
            ch=takeCommand()
            if ch[0]=="y":
                speak("Dictate your message")
                msg=takeCommand()
                kit.sendwhatmsg(ph,msg,int(datetime.datetime.now().hour()),int(datetime.datetime.now().minute()))
                break
            else:
                continue
    except:
        while(True):
            speak("Dictate the number")
            ph=takeCommand()
            speak("the number you entered was"+ph+"is that correct?")
            ch=takeCommand()
            if ch[0]=="y":
                speak("Dictate your message")
                msg=takeCommand()
                kit.sendwhatmsg(ph,msg,int(datetime.datetime.now().hour()),int(datetime.datetime.now().minute()+1))
                break
            else:
                continue
        
def response(cmd):
    
    a=cmd.split()
    st=""
    greetings = ['hey there', 'hello', 'hi', 'hai', 'hey!', 'hey','hola']
    addrsGret = ['hey there potter','hey there harry', 'hello potter','hello harry', 'hi potter','hi harry', 'hai potter',"hai harry", 'hey potter','hey harry']
    gret=["good morning","good evening","good night","good afternoon"] 
    question = ['how are you', 'how are you doing']
    var1 = ['who made you', 'who created you']
    var2 = ['I_was_created_by_Soujash and Ambud_right_in_their_computer.', 'Soujash and Ambud', 'Some_guy_whom_i_never_got_to_know.']
    var4 = ['who are you', 'what is your name']
    cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
    cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
    jokes = ['Can a kangaroo jump higher than a house?\n Of course,\n a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot.\n It got so bad, finally I had to take his bike away.', "Why cant a aethist solve exponenetial problems?\n  Because he/she doesn't believe in higher power","what did the proton tell the electron?\n  don't be so negative.",'Reaching the end of a job interview,\n the Human Resources Officer asks a young engineer fresh out of the Massachusetts Institute of Technology,\n "And what starting salary are you looking for?"\n The engineer replies,\n "In the region of $125,000 a year, depending on the benefits package."\m The interviewer inquires,\n "Well, what would you say to a package of five weeks vacation,\n 14 paid holidays,\n full medical and dental,\n company matching retirement fund to 50% of salary,\n and a company car leased every two years,\n say, a red Corvette?"\n The engineer sits up straight and says,\n "Wow!\n Are you kidding?" \n The interviewer replies, \n"Yeah, but you started it.']
    cmd4 = ['open youtube', 'i want to watch a video']
    cmd5 = ['tell me the weather', 'weather', 'what about the weather','what is the weather today']
    cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color']
    colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
    cmd8 = ['what is you favourite colour', 'what is your favourite color']
    cmd9 = ['thank you']
    repfr9 = ['you are welcome', 'glad i could help you']
    name1=["POTTER. HARRY POTTER","HARRY"]
    appreciation=["you are great"," you are cool","you are the best","i love you"]
    fav=["play my favourite song"]
    siblings=["do you have any siblings","name your siblings"]
    age=["what is your age","how old are you"]
    stat=["battery status","check battery status"]
    default=["can you train","how is your memory","can you learn","can i train you"]
    command=["train"]
    religion=["do you believe in god","what is your religion","are you an aethist"]
    bday=["when was your birthday","when were you born","when is your bday","when was your bday","when is your birthday"]
    default=["I see","hmmmm","okay","ok","ha"]
    adbk=["read me a pdf","read me a file"]
    happy=["its my birthday today","today is my birthday","i got engaged","today is my anniversary"]
    sad=["dead","died","passed away"]
    sndmsg=["send a message","I wanna send a message"]
    opc=["open camera","show me how I look","how do I look"]
    if cmd in addrsGret:
        return"Hey ther buddy"
    elif "show me this month calendar" in cmd:
          Month=int(datetime.datetime.now().month)
          Year = int(datetime.datetime.now().year)
          cal = calendar.month(Year,Month)
          print(cal)
          speak("Here you go miss")
    elif cmd in greetings:
        return "hullo there, miss"
    elif cmd in sndmsg:
        sendmsg()
    elif "sleep" in cmd:
          speak("Going to sleep")
          sys.exit(0)
    elif cmd in opc:
        speak("Opening Camera...")
        speak("Press ESCAPE to exit the mirror mode")
        OpenCam()
        
        return "you look quite pretty I must say.(wink)"
    elif "show me this month calendar" in cmd:
          Month=int(datetime.datetime.now().month)
          Year = int(datetime.datetime.now().year)
          cal = calendar.month(Year,Month)
          print(cal)
          speak("Here you go miss")
    elif "goodbye" in cmd:
          speak("It was great working with you miss,have a good day,goodbye")
          sys.exit()
     
     
    elif cmd in default:
        return "Hmmm"
    elif cmd in happy:
        return "Many Many Happy Returns of the Day"
    elif cmd in gret:
        hr=int(datetime.datetime.now().hour)
        a=""
        if(hr>=0 and hr<12):
            a="Good Morning"
        elif(hr>=12 and hr<17):
            a="Good Afternoon"
        else:
            a="Good Evening"
        if a.lower()==cmd:
            return a
        else:
            st="Actually miss you should be \n wishing "+a+"\n and not "+cmd+"."+"\n Neverthless "+a+" ,miss!" 
            return st
    
    elif cmd in adbk:
        Audiobook()
    elif "yourself" in cmd:
        return "My name is HARRY POTTER. I was created as a gift to a friend of one of my masters,namely Ambud Lahiri.I'm here to help you 24/7"
    elif "news" in a:
        webbrowser.open("news.google.com")
        return "opening news website(Could nnot search for specifics as news.google.com declined permission"
    elif(cmd=="Shutdown"or cmd=="shutdown"):
                speak("Are you sure,miss?(Please check the prompt)")
                window = Tk()

                input_user = StringVar()
                input_field = Entry(window, text=input_user)
                input_field.pack(side=BOTTOM, fill=X)
                Label(text="Are you sure miss?").pack()
                def enter_pressed(event):
                    
                    input_get = input_field.get()
                    print(input_get)
                    if input_get=="yes":
                        var = StringVar()
                        label = tkinter.Label( background="pale green",textvariable=var, relief=RAISED )
                        var.set("Shutting Down")
                        speak("Shutting Down")
                        os.system('shutdown /s /t 1')
                        input_user.set('')
                        label.pack()
                        label.place(height=40, width=210,x=0,y=20)
                    elif input_get=="no":
                        var = StringVar()
                        label = Message( background="pale green",textvariable=var, relief=RAISED )
                        var.set("Shut Down procedure aborted")
                        input_user.set('')
                        label.pack()
                        label.place(height=40,width=210,x=0,y=20)
                    label = tkinter.Label(frame, text=input_get,relief=RAISED)
                    input_user.set('')
                    label.pack()
                    label.place(width=50,x=250,y=0)
                    return "break"
                frame = Frame(window, width=300, height=300)
                frame.pack_propagate(False) # prevent frame to resize to the labels size
                input_field.bind("<Return>", enter_pressed)
                frame.pack()
                
                window.mainloop()
    elif(cmd=="Restart"or cmd=="restart"):
                window = Tk()
                speak("Are you sure miss?")
                input_user = StringVar()
                input_field = Entry(window, text=input_user)
                input_field.pack(side=BOTTOM, fill=X)
                Label(text="Are you sure miss?").pack()
                def enter_pressed(event):
                    input_get = input_field.get()
                    print(input_get)
                    if input_get=="yes":
                            var = StringVar()
                            label = tkinter.Label( background="pale green",textvariable=var, relief=RAISED )
                            var.set("Restarting")
                            speak("Restarting")
                            os.system('shutdown /r /t 1')
                            input_user.set('')
                            label.pack()
                            label.place(height=40, width=210,x=0,y=20)
                    elif input_get=="no":
                            var = StringVar()
                            label = Message( background="pale green",textvariable=var, relief=RAISED )
                            var.set("Restart procedure aborted")
                            input_user.set('')
                            label.pack()
                            label.place(height=40,width=210,x=0,y=20)
                    label = tkinter.Label(frame, text=input_get,relief=RAISED)
                    input_user.set('')
                    label.pack()
                    label.place(width=50,x=250,y=0)
                    return "break"
                frame = Frame(window, width=300, height=300)
                frame.pack_propagate(False) # prevent frame to resize to the labels size
                input_field.bind("<Return>", enter_pressed)
                frame.pack()
                
                window.mainloop()
    elif(cmd=="What is the time?"):
                hr=datetime.datetime.now()
                return(hr)
    elif cmd in age:
            yr=int(datetime.datetime.now().year)
            
            mo=int(datetime.datetime.now().month)
            
            da=int(datetime.datetime.now().day)
            ay=yr-2020
            ad=da-6
            am=mo-11
            if ad<0:
                if mo in [1,3,5,7,10,12]:
                    ad=31+da
                    am=am-1
                else:
                    ad=30+da
                    am=am-1
            st="I'm"+str(ay)+"years"+str(ad)+"months"+str(am)+"days old"
            return st
    elif cmd in bday:
            return "I was born on 17 th of August 2020"
    elif cmd in religion:
            return "I do believe in god.\n  Because just like I've been \n programmed to respond like this \n.So are you.\n Thus I do believe in god "
                
    elif cmd in command:
            return "This feature is not available in this version of me."
    elif cmd in default:
            return "Yes you can train me.\n you can train me by typing th word 'Train()'"
    elif cmd in stat:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"
            return(percent+'% | '+plugged)
    elif cmd in siblings:
            return("Yes! I have a big brother,\n Robert, who is in Java.\n I also have an elder sister MMANA in Python")
    elif cmd in fav:
        webbrowser.open("https://gaana.com/song/lag-ja-gale-se-phir")        
        return("playing Lag Ja Gale...")
    elif cmd in greetings:
            random_greeting = random.choice(greetings)
            return(random_greeting)
    elif cmd in question:
            return("I am Fine,miss")
    elif cmd in  var1:
            reply='I was made by Soujash And Ambud all alone right in his laptop with some help from the internet'
            return(reply)
    elif cmd  in cmd9:
            return(random.choice(repfr9))
    elif cmd  in cmd7:
            return(random.choice(colrep)+'\n It keeps changing every micro second')
    elif cmd  in cmd8:
            color=random.choice(colrep)
            return(color)
    elif cmd in cmd2:
            webbrowser.open("https://gaana.com/playlist/gaana-dj-gaana-international-top-50")
            return("Playing one of my preferred music playlist")
    elif cmd  in var4:
            return(random.choice(name1))
    elif cmd  in cmd4:
            webbrowser.open('www.youtube.com')
            return "opening"
    elif cmd  in cmd5:
            webbrowser.open("https://www.bing.com/search?q=today%27s+weather+forecast&qs=SC&pq=today%27s+wae&sc=8-11&cvid=529AB3594F30416DB2A557F154BCB435&FORM=GEOTRI&sp=1&ghc=1&isRef=1&showTw=1")
            return "opening"
    elif cmd in cmd3:
            jokrep = random.choice(jokes)
            return(jokrep)

    elif cmd in appreciation:
            return("Thank You ! miss .  I Like being appreciated!")
     
    else:
        try:                
            err_msg=["Hmm...I don't have an answer to that"]
            speak(random.choice(err_msg))
            speak("I found this on the web")
            result= wikipedia.summary(cmd)
            speak(result)
        except:
            speak("You have a connection error")
def takeCommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
    
        r.energy_threshold = 1000
        audio = r.listen(source)
    
    try:
        print("Recognizing....")    
        query = r.recognize_google(audio,language='en-in')
        print(f"miss said:{query}\n")
        Display(query)
        res=response(query)
        DisplayasResp(res)
        speak(res)
        

    except Exception as e:    
  
        print("Could not hear Say that again please...")
        speak("Could not hear Say that again please...")
        return "None"    
     

root = Tk() 

# Adjust size 
root.geometry("958x603") 
root.resizable(0,0)
# Add image file 
bg = PhotoImage(file = "hp.png") 

# Create Canvas 
canvas1 = Canvas( root, width = 793, 
				height = 668) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 0, 0, image = bg, 
					anchor = "nw") 
btn1=Button(text="Speak to me",command=takeCommand,relief=FLAT,foreground="white",background="blue")
btn1.pack()
btn1.place(x=490,y=510)
input_user = StringVar()
input_field = Entry(text=input_user)
input_field.pack()
input_field.place(height=40,width=570,x=0,y=540)
input_field.bind("<Return>", enter_pressed)
btn1= Button(text="Send",foreground="white",activebackground="blue" ,command=send_pressed,background="blue",relief="flat")
btn1.place(width=50,height=50,x=600,y=510)
wishMe()
root.mainloop()