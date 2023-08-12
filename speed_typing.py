import tkinter as tk
from tkinter import *
import sys
import time
import random
window=tk.Tk()
window.title('SPEEDY')
window.geometry("920x600")
window.configure(bg='#69fa90')
window.resizable(False,False)

Top_Image = PhotoImage(file=r"E:\codeclause\Speed_Typing\speedy.png")
Label(window, image=Top_Image, bg="#0f1a2b").pack()

window.iconphoto(False,Top_Image)

def stopTest():
    try:
        global writeAble
        writeAble = False

        amountWords=labelLeft.cget('text').count(" ")

        timeLeftLabel.destroy()
        currentLetterLabel.destroy()
        labelLeft.destroy()
        labelRight.destroy()

        global ResultLabel
        ResultLabel=Label(window,text=f'Words per Minute: {amountWords}', fg='black', bg='yellow', font=('Arial',16),borderwidth=2, relief='groove')
        ResultLabel.place(relx=0.5,rely=0.4,anchor=CENTER)

        global ResultButton
        ResultButton = Button(window, text=f'Retry', command=restart, bg='red',font=('Arial',13 ))
        ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    except:
        pass

def restart():
    ResultLabel.destroy()
    ResultButton.destroy()
    resetWritingLabels()

def addSecond():
    if writeAble:
        global passedSeconds
        passedSeconds -= 1
        timeLeftLabel.configure(text=f'{passedSeconds} seconds')
        if passedSeconds<10:
            timeLeftLabel.configure(text=f'{passedSeconds} seconds',bg='red',borderwidth=2,relief='raised',font=('Arial',15))
        window.after(1000,addSecond)
def keyPress(event=None):
    try:
        if event.char==labelRight.cget('text')[0]:
            labelRight.configure(text=labelRight.cget('text')[1:])
            labelLeft.configure(text=labelLeft.cget('text')+event.char)
            currentLetterLabel.configure(text=labelRight.cget('text')[0])


        elif ord(event.char)==8 and len(labelLeft.cget('text'))>0:
            labelRight.configure(text=labelLeft.cget('text')[-1]+labelRight.cget('text'))
            labelLeft.configure(text=labelLeft.cget('text')[:-1])
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except:
        pass


def resetWritingLabels():
    texts=['''In the modern world of technological advancement, computer is the amazing gift given by the science to us. It has changed the living style and standard of the people. No one can imagine the life without computer as it has made lots of works so easy within less time. Computer is playing great role in the development of the developing countries. It is not only a storage or processing device but it is like an angel which can make anything possible. By many people it used as the source of entertainment and communication. We can get connected to our friends, relatives, parents or others in no time through the use of video chat or email. Using internet in the computer we can search and retrieve vast information on any subject useful for our education or project work. However it is very safe and easy for the business transactions purposes through banks to any accounts. By providing the facility of data storage it has lessen the paper works in the governmental and non-governmental offices or colleges. One can save lots of time and effort by online shopping, paying bill, etc by being at home through the computer. Computer education has made compulsory by the government of India in all the schools, colleges and other educational institutions for enhancing the skill level as well as the easiness of the students in their professional life. Learning computer has become very essential in all the modern-day jobs. In the higher education there are subjects like network administration, hardware maintenance, software installation, etc., for the enhancement of skill.''',
           '''Often the terms Data Science and Business Analytics are considered synonymous. After all, both the Business Analytics and Data Science activities deal with the data, their acquisition, and the development of models and information processing. What then is the difference between Data Science and Business Analytics? As the name suggests, Business Analytics is focused on the processing of data, business or sectorial, to extract information useful to the company, focused on its market and on that of its competitors. Data Science instead responds to questions about the influence of customer behavior on the company's business results. Data Science combines the potential of data with the creation of algorithms and the use of technology to answer a series of questions. Recently the functions of machine learning and artificial intelligence have evolved and will bring data science to levels that are still difficult to imagine. Business Analytics, on the other hand, continues to be a form of business data analysis with statistical concepts to obtain solutions and in-depth analysis by relating past data to those relating to the present.''',
           '''Music is a pleasant sound which is a combination of melodies and harmony and which soothes you. Music may also refer to the art of composing such pleasant sounds with the help of the various musical instruments. A person who knows music is a Musician. The music consists of Sargam, Ragas, Taals, etc. Music is not only what is composed of men but also which exists in nature. Have you ever heard the sound of a waterfall or a flowing river? Could you hear music there? Thus, everything in harmony has music. Here, I would like to quote a line by Wolfgang Amadeus Mozart, one of the greatest musicians, “The music is not in the notes, but in the silence between.''',
           '''Pollution is a term which even kids are aware of these days. It has become so common that almost everyone acknowledges the fact that pollution is rising continuously. The term ‘pollution’ means the manifestation of any unsolicited foreign substance in something. When we talk about pollution on earth, we refer to the contamination that is happening of the natural resources by various pollutants. All this is mainly caused by human activities which harm the environment in ways more than one. Therefore, an urgent need has arisen to tackle this issue straightaway. That is to say, pollution is damaging our earth severely and we need to realize its effects and prevent this damage. In this essay on pollution, we will see what are the effects of pollution and how to reduce it.''',
           '''Both school life and college life is the most memorable time of a person's life, but both of them are quite different from each other. While in School life, we learn everything in a protected environment, College Life exposes us to a new environment where we have to learn new things and face new challenges by ourselves. We spend half of our young lives in school, and thus we get comfortable living in that environment. But College Life is for three years only, where every year introduces new challenges and lessons to us. While in school, our teachers and friends always protect and guard us, in college life we form a relationship with our mentors, and they don't protect us all the time as our school teachers did. Unlike school life, we don't have many limitations in college life, and it is up to us how we want to spend our college life. In college life, we see new faces and experience a unique environment in which we have to mingle ourselves. We make new friends there who stay with us for the rest of our lives. Also, we get a chance to shape our careers asking the right decisions and studying hard. College life is not only about the study but also about the overall development of an individual through various activities and challenges.''',
           ]
    text= random.choice(texts)

    splitPoint=0
    global labelLeft
    labelLeft=Label(window,text=text[:splitPoint],bg='#69fa90',font=('Arial',16))
    labelLeft.place(relx=0.5,rely=0.53,anchor=E)

    global labelRight
    labelRight=Label(window,text=text[splitPoint:],bg='yellow',font=('Arial',16))
    labelRight.place(relx=0.5,rely=0.53,anchor=W)

    global currentLetterLabel
    currentLetterLabel=Label(window,text=text[splitPoint],fg='grey', bg='yellow',font=('Arial',17))
    currentLetterLabel.place(relx=0.5,rely=0.6)

    global timeLeftLabel
    timeLeftLabel=Label(window,text=f'60 seconds',fg='black',bg='#07e6fa',borderwidth=2,relief='sunken',font=('Arial',15))
    timeLeftLabel.place(relx=0.45,rely=0.4)

    global writeAble
    writeAble=True
    window.bind('<Key>',keyPress)

    global passedSeconds
    passedSeconds = 60

    window.after(60000,stopTest)
    window.after(1000,addSecond)

def start():
    startButton.destroy()
    resetWritingLabels()


startButton = Button(window, text=f'Start', command=start, bg='yellow',fg='blue',font=('Arial',15))
startButton.place(relx=0.5, rely=0.6, anchor=CENTER)



window.mainloop()