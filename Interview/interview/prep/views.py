from django.shortcuts import render
import speech_recognition as sr
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
import tkinter as tk
import tkinter.messagebox
import pyaudio
import wave
import speech_recognition as sr 
from user import views

def text_to_words_andcomparefromdatabase(path,database):
    r = sr.Recognizer()
    audio = sr.AudioFile(path)
    with audio as source:
        audio_file = r.record(source)
    text = r.recognize_google(audio_file)
    text=' '.join(set(text.split()))
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    words = [w for w in word_tokens if not w.lower() in stop_words]
    words = []
    for w in word_tokens:
        if w not in stop_words:
            words.append(w)

    nlp = spacy.load('en_core_web_sm')
    
    score=0
    for comp in database:
        for word in words:
            sent= word+" "+comp
            tokens = nlp(sent)
            token1, token2 = tokens[0], tokens[1]
            if (token1.similarity(token2))>0.6:
                score=score+1
    return score

class RecAUD:

    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):

        self.main = tkinter.Tk()
        self.collections = []
        self.main.geometry('500x300')
        self.main.title('Record')
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        self.buttons = tkinter.Frame(self.main, padx=120, pady=20)
        self.buttons.pack(fill=tk.BOTH)
        self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Start Recording', command=lambda: self.start_record())
        self.strt_rec.grid(row=0, column=0, padx=50, pady=5)
        self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Stop Recording', command=lambda: self.stop())
        self.stop_rec.grid(row=1, column=0, columnspan=1, padx=50, pady=5)

        tkinter.mainloop()

    def start_record(self):
        
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            self.main.update()

        stream.close()

        wf = wave.open('voice.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        

    def stop(self):
        self.st = 0

def record_result(request):
    guiAUD = RecAUD()
    # sent="achievement job applicant interview bonus company contract customer job middle manager resume secretary student trial period ambition an ad an office background boss business busy environment certificate cover letter day off deadline dismissed employee employer employment end of the contract fired informal full time full-time job hands-on experience hired hobbies holiday pay holiday rest day holidays internship work placement job requirement motivated notice opportunity organised overtime hours part time pay rise pay slip personal qualities positive preference previous job professional experience prospective employer qualification recruiter salary salary after deductions and social charges salary before deductions and social charges seasonal employment sector skill strenghts teamwork temporary job under pressure unemployed person unemployment weakness work work ethic accomplished adapted administered advised allocated analyzed applied arranged assisted built carried out catalogued classified collaborated completed conceived conducted constructed consulted controlled cooperated coordinated counseled created decided decreased delegated derived designated developed devised directed discovered distributed documented encouraged engineered enlarged established estimated evaluated examined explored facilitated finalized formulated founded governed guided handled identified implemented improved increased initiated inspected installed interpreted introduced invented investigated led located made maintained managed merged moderated motivated negotiated obtained operated organized overcame performed planned prepared presented presided processed programmed promoted purchased raised recommended recorded recruited redesigned repaired replaced restored reviewed revised screened selected serviced set up solved sorted specified started stimulated strengthened summarized supervised supported tested trained transcribed transformed upgraded validated verified Skills accurate active adaptable adept broad-minded, open minded competent conscientious creative dependable determined diplomatic discreet efficient energetic engaged enterprising enthusiastic experienced expert fair firm genuine honest initiative innovative logical loyal mature methodical motivated multi-skilled / multitasking objective organizational skills outgoing personable pleasant positive practical productive punctual reliable resourceful responsibility self-disciplined sense of humor sensitive sincere successful tactful team player trustworthy apply for job be contracted/employed be experienced be fired be hired be interested in be keen  … be made redundant be unemployed call back carry out collaborate develop direct/  lead do ext hours earn money facilitate fire fired get up graduate from handle pressure stress have experience hire implement intend  introduce leave look forward  major in motivate obtain perform recruit resign respond start supervise wear work work full time work part time"
    # sent1=' '.join(set(sent.split()))
    # database=sent1.split()
    database=views.questionid()
    # record_result.sc
    score=text_to_words_andcomparefromdatabase("voice.wav",database)
    # fact=len(database)*3/100
    score=(score/len(database))*100
    # record_result.sco=score
    dict={'score':int(score)}

    return render(request,'prep.html',dict)

# def sc_save():
#     y=record_result.sco
#     return y
