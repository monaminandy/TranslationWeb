from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from PIL import ImageTk, Image

root=Tk()
root.title("Translation Web")
root.geometry("1000x400")
root.resizable(False,False)
root.configure(background="#DCDCDC")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)


arrow = Image.open('arrow-removebg-preview.png')
arrow = arrow.resize((300, 135))
arrow = ImageTk.PhotoImage(arrow)
Label(root, image=arrow, bg="#DCDCDC").place(x=340, y=50)


language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Arial 14", state="r")
combo1.place(x=80,y=20)
combo1.set("english")

label1=Label(root,text="english", font="Roboto 25 ",bg="white",width=18,bd=3,relief=GROOVE)
label1.place(x=20,y=50)


combo2=ttk.Combobox(root,values=languageV,font="Arial 14", state="r")
combo2.place(x=670,y=20)
combo2.set("Select language")

label2=Label(root,text="english", font="Roboto 25 ",bg="white",width=18,bd=3,relief=GROOVE)
label2.place(x=610,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=370,height=210)

text1=Text(f,font="Arial 15",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=360,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

f1=Frame(root,bg="Black",bd=5)
f1.place(x=600,y=118,width=370,height=210)

text2=Text(f1,font="Arial 15",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=360,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text2.yview)
text1.configure(yscrollcommand=scrollbar2.set)


translate=Button(root,text="Translate",font=("Arial", 14),activebackground="white",cursor="hand2",width=10,height=2
                 ,bg="red",fg="white",command=translate_now)
translate.place(x=430,y=250)

label_change()
root.mainloop()
