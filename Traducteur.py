import pyttsx3
from tkinter import *
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
import os


language_map = {
    'Français': 'fr',
    'English': 'en',
    'Allemand': 'de',
    'Español': 'es',
    'Italien': 'it',
    'Japonnais': 'ja',
    'Arabe': 'ar',
    'Chinois': 'zh-tw'
}


def translate():
    t = T1.get("1.0", END)
    translator = Translator()
    translation = translator.translate(t, dest=language_map[combo2.get()])
    T2.delete('1.0', END)
    T2.insert(END, translation.text)

def listen_text(text_widget):
    data = text_widget.get("1.0", END)
    selected_language = language_map[combo1.get()] if text_widget == T1 else language_map[combo2.get()]
    myobj = gTTS(text=data, lang=selected_language, slow=False)
    myobj.save("welcome.mp3")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1.0)  
    engine.say(data)
    engine.runAndWait()
    os.remove("welcome.mp3")  

def on_enter(event):
    event.widget.config(bg="white", fg="black")

def on_leave(event):
    event.widget.config(bg="#6F2CF4", fg="white")

root = Tk()
root.title("Translator")
root.geometry("800x330")
root.iconbitmap("./icon/logo.ico")
root.config(bg="#212529")

labelChooseLang = Label(root, text="Choose language source", font=("Halvetica", 13), bg="#212529", fg="white")
labelChooseLang.place(x=20, y=50)

labelLangTraduct = Label(root, text="Destination language", font=("Halvetica", 13), bg="#212529", fg="white")
labelLangTraduct.place(x=430, y=50)


languages = list(language_map.keys())
combo1 = ttk.Combobox(root, values=languages)
combo1.place(x=230, y=50)
combo1.current(0)

combo2 = ttk.Combobox(root, values=languages)
combo2.place(x=620, y=50)
combo2.current(1)


T1 = Text(root)
T1.place(x=20, y=100, width=400, height=150)
T1.insert("1.0", "Enter your text ")

T2 = Text(root)
T2.place(x=430, y=100, width=350, height=150)

btn0 = Button(root, text="Translate", bg="#6F2CF4", fg="white", command=translate, width=10)
btn0.place(x=130, y=280)
btn0.bind("<Enter>", on_enter)
btn0.bind("<Leave>", on_leave)

btn1 = Button(root, text="Listen", bg="#6F2CF4", fg="white", command=lambda: listen_text(T1), width=10)
btn1.place(x=230, y=280)
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)

btn2 = Button(root, text="Listen", bg="#6F2CF4", fg="white", command=lambda: listen_text(T2), width=10)
btn2.place(x=560, y=280)
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)

root.mainloop()