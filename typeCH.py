from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

root=Tk()
root.title("Typing Mania")
root.geometry("500x500")
root.configure(bg="Black")
img = PhotoImage(file="background.png")
label = Label(root,image=img,height=500,width=500)
label.place(x=0,y=0)

window=Tk()
window.title("Typing Mania")
window.geometry("550x500")
window.configure(bg="white")
window.withdraw()

hs_file=open('highscore.txt','r+')
x=0


def game():
    global x
    if x==0:
        root.withdraw()
        x=x+1
    window.deiconify()
    def chk_speed():
        j=error=0
        itext=entry.get("1.0","end-1c")
        end=timer()
        time_taken=end-start
        #len diff
        if len(words[word])>=len(itext):
            error=len(words[word])-len(itext)
            for i in itext: #take shorter sentence
                if i==words[word][j]:
                    pass
                else:
                    error+=1
                j+=1
        elif len(words[word])<=len(itext):
            error=len(itext)-len(words[word])
            for i in words[word]:
                if i==itext[j]:
                    pass
                else:
                    error+=1
                    j+=1
        wpm=len(itext)/5
        wpm=wpm-error
        wpm=int(wpm/(time_taken/60))
        hs_file.seek(0)
        line=int(hs_file.readline())
        if wpm>line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result="Amazing! New HighScore is: "+str(wpm)+"WPM "
            messagebox.showinfo("Score",result)
        else:
            result='Your score is: '+str(wpm)+'WPM\n Better luck next time!'
            messagebox.showinfo('Score',result)

    def finish():
        hs_file.close()
        window.destroy()
        root.destroy()

    words=["Humans are too weak and divided, they will fall.","Everyday is a miracle."," This is the 3rd line in the typing text."]
    #words=[]
    word=random.randint(0,(len(words)-1))

    x2=Label(window,text=words[word],bg='black',fg='white',height=7,width=47,font="times 15",wraplength=500)
    x2.place(x=15,y=10)

    x3=Button(window,text='Submit!',font='times 13',bg='#fc2828',command=chk_speed)
    x3.place(x=220,y=350)


    entry = Text(window,font="times 12")
    entry.place(x=100, y=180, height=150, width=350)
    entry.focus_set()

    b2=Button(window,text="Done",font="times 13",bg="#ffc003",width=12,command=finish)
    b2.place(x=155,y=420)

    b3=Button(window,text="Another Round", font="times 13",bg='#ffc003',width=12,command=game)
    b3.place(x=265,y=420)

    start=timer()

    window.mainloop()


x1=Label(root,text="Let's test your typing speed!",bg="white",fg="black",font="comic 15")
x1.place(x=118,y=50)

go=PhotoImage(file="type-speed-open.png")
logo=Button(root,image=go,border=0)
logo.place(x=120,y=105)

b1=Button(root,text="Let's Go!",width=12,bg="#fcba03",font="times 20",command=game)
b1.place(x=150,y=325)

hs_text=Label(root, text="Highscore",width=12,bg="#03fcf8",font="times 10",)
hs_text.place(x=200,y=448)

hs=hs_file.readline()
hs_val=Label(root,text=str(hs)+' WPM',fg='#03fcf8',bg='black',font="times 12")
hs_val.place(x=214,y=470)

root.mainloop()
