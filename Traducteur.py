from tkinter import *
from tkinter import ttk
from googletrans import Translator
import pyttsx3

# définir les variables globales à utiliser
source  = ""
destination = ""
t = ""
translation = ""


def comboAction(event):  
    global source
    global destination 
    destination = combo2.get()
    
    
def Traduct(event):
    global t
    t = T1.get("1.0" , END)
    translator = Translator()
    translation = translator.translate(t  , dest = destination)
    T2.delete('1.0', END)
    T2.insert(END , translation.text)
    
def ecoute ():
    s = pyttsx3.init() 
    data = T2.get("1.0" , END)
    s.say (data)
    s.runAndWait()


def ecoute1 ():
    s = pyttsx3.init() 
    data = T1.get("1.0" , END)
    s.say (data)
    s.runAndWait()

def entrer (event):
    btn.config (bg = "white" , fg = "black" )

def leave (event):
    btn.config ( bg = "#212F3D" , fg = "white")


def entrer1 (event):
    btn2.config (bg = "white" , fg = "black")
def leave1 (event):
    btn2.config ( bg = "#212F3D" , fg = "white")

    
root = Tk()
root.title ("Translator")
root.geometry("800x300")
root.iconbitmap("./img/logo.ico")


#-------------------------------
# Création de la liste combobox
#-------------------------------
labelChooseLang = Label(root, text = "Choose language source" , font = ("Courrier" , 13)) 
labelChooseLang.place(x = 20 , y = 50)

labelLangTraduct = Label(root, text = "Destination language" , font = ("Courrier" , 13)) 
labelLangTraduct.place(x = 430 , y = 50)


# Liste des valeurs d'option de la combobox
languages =['fr' , 'en' , 'es' , 'ar' , "zh-tw" ]

# Création des listes combobox
combo1 = ttk.Combobox(root, values = languages )
combo1.place(x = 230 , y = 50)

# Définir l'élément qui s'affiche par défaut
combo1.current(0)

# Associé une bind action à la liste combo
combo1.bind("<<ComboboxSelected>>", comboAction)

combo2 = ttk.Combobox(root, values = languages)
combo2.place(x = 620 , y = 50)

# Définir l'élément qui s'affiche par défaut
combo2.current(1)

# Associé une bind action à la liste combo
combo2.bind("<<ComboboxSelected>>", comboAction)

T1 = Text(root )
T1.place(x = 20 , y = 100 , width = 400 , height = 150)
T1.insert ("1.0" , "Enter your text ")
T1.bind("<Return>" , Traduct)




T2 = Text(root)
T2.place(x = 430 , y = 100 , width = 350 , height = 150)

btn = Button (root , text = "Listen", bg = "#212F3D" , fg = "white", command = ecoute1)
btn.place(x = 180 , y = 260)
btn.bind ("<Enter>" ,entrer )
btn.bind ("<Leave>" , leave)

btn2 = Button (root , text = "Listen Traduction", bg = "#212F3D" , fg = "white", command = ecoute)
btn2.place(x = 560 , y = 260)
btn2.bind ("<Enter>" ,entrer1 )
btn2.bind ("<Leave>" ,leave1 )

root.mainloop()
