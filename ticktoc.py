from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("tic tok game")
root.geometry("600x500")
root.resizable(True,True)
bcl=True

#framing 
f1=Frame(root,height=100,width=300)
f1.pack(side="top")

f2=Frame(root,height=100,width=300)
f2.pack(side="top")

f3=Frame(root,height=100,width=300)
f3.pack(side="top")

#defining function {g}
def g(vb):
    global bcl
    if vb['text']=="" and bcl == True:
        vb['text']='X'
        bcl=False
#-HORIZANTAL LINE CONDITIONS FOR X
        if b1['text']== 'X' and b2['text']== 'X' and b3['text']== 'X':
            b1['fg']='yellow'
            b2['fg']='yellow'
            b3['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b4['text']== 'X' and b5['text']== 'X' and b6['text']== 'X':
            b4['fg']='yellow'
            b5['fg']='yellow'
            b6['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b7['text']== 'X' and b8['text']== 'X' and b9['text']== 'X':
            b7['fg']='yellow'
            b8['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
#-HORIZANTAL LINE CONDITIONS FOR O           
        elif b1['text']== 'O' and b2['text']== 'O' and b3['text']== 'O':
            b1['fg']='yellow'
            b2['fg']='yellow'
            b3['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b4['text']== 'O' and b5['text']== 'O' and b6['text']== 'O':
            b4['fg']='yellow'
            b5['fg']='yellow'
            b6['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b7['text']== 'O' and b8['text']== 'O' and b9['text']== 'O':
            b7['fg']='yellow'
            b8['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
#-VERTICAL LINE CONDITIONS FOR X            
        elif b1['text']== 'X' and b4['text']== 'X' and b7['text']== 'X':
            b1['fg']='yellow'
            b4['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b2['text']== 'X' and b5['text']== 'X' and b8['text']== 'X':
            b2['fg']='yellow'
            b5['fg']='yellow'
            b8['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b3['text']== 'X' and b6['text']== 'X' and b9['text']== 'X':
            b3['fg']='yellow'
            b6['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
#-VERTICAL LINE CONDITIONS FOR O
        elif b1['text']== 'O' and b4['text']== 'O' and b7['text']== 'O':
            b1['fg']='yellow'
            b4['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b2['text']== 'O' and b5['text']== 'O' and b8['text']== 'O':
            b2['fg']='yellow'
            b5['fg']='yellow'
            b8['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b3['text']== 'O' and b6['text']== 'O' and b9['text']== 'O':
            b3['fg']='yellow'
            b6['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
#-DIAGOAL COMBINATION FOR X
        elif b3['text']== 'X' and b5['text']== 'X' and b7['text']== 'X':
            b3['fg']='yellow'
            b5['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b1['text']== 'X' and b5['text']== 'X' and b9['text']== 'X':
            b1['fg']='yellow'
            b5['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
#-DIAGOAL COMBINATION FOR O
        elif b3['text']== 'O' and b5['text']== 'O' and b7['text']== 'O':
            b3['fg']='yellow'
            b5['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player O wins')

        elif b1['text']== 'O' and b5['text']== 'O' and b9['text']== 'O':
            b1['fg']='yellow'
            b5['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
            
#SIMILAR CONDITION FOR O           
    elif vb['text']=="" and bcl == False:
        vb['text']='O'
        bcl=True
        #HORIZANTAL LINE CONDITIONS FOR X
        if b1['text']== 'X' and b2['text']== 'X' and b3['text']== 'X':
            b1['fg']='yellow'
            b2['fg']='yellow'
            b3['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b4['text']== 'X' and b5['text']== 'X' and b6['text']== 'X':
            b4['fg']='yellow'
            b5['fg']='yellow'
            b6['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b7['text']== 'X' and b8['text']== 'X' and b9['text']== 'X':
            b7['fg']='yellow'
            b8['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
#-HORIZANTAL LINE CONDITIONS FOR O           
        elif b1['text']== 'O' and b2['text']== 'O' and b3['text']== 'O':
            b1['fg']='yellow'
            b2['fg']='yellow'
            b3['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b4['text']== 'O' and b5['text']== 'O' and b6['text']== 'O':
            b4['fg']='yellow'
            b5['fg']='yellow'
            b6['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b7['text']== 'O' and b8['text']== 'O' and b9['text']== 'O':
            b7['fg']='yellow'
            b8['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
#-VERTICAL LINE CONDITIONS FOR X            
        elif b1['text']== 'X' and b4['text']== 'X' and b7['text']== 'X':
            b1['fg']='yellow'
            b4['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b2['text']== 'X' and b5['text']== 'X' and b8['text']== 'X':
            b2['fg']='yellow'
            b5['fg']='yellow'
            b8['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b3['text']== 'X' and b6['text']== 'X' and b9['text']== 'X':
            b3['fg']='yellow'
            b6['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
#-VERTICAL LINE CONDITIONS FOR O
        elif b1['text']== 'O' and b4['text']== 'O' and b7['text']== 'O':
            b1['fg']='yellow'
            b4['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b2['text']== 'O' and b5['text']== 'O' and b8['text']== 'O':
            b2['fg']='yellow'
            b5['fg']='yellow'
            b8['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b3['text']== 'O' and b6['text']== 'O' and b9['text']== 'O':
            b3['fg']='yellow'
            b6['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
#-DIAGOAL COMBINATION FOR X
        elif b3['text']== 'X' and b5['text']== 'X' and b7['text']== 'X':
            b3['fg']='yellow'
            b5['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
        elif b1['text']== 'X' and b5['text']== 'X' and b9['text']== 'X':
            b1['fg']='yellow'
            b5['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player X wins')
#-DIAGOAL COMBINATION FOR O
        elif b3['text']== 'O' and b5['text']== 'O' and b7['text']== 'O':
            b3['fg']='yellow'
            b5['fg']='yellow'
            b7['fg']='yellow'
            messagebox.showinfo('Results','player O wins')
        elif b1['text']== 'O' and b5['text']== 'O' and b9['text']== 'O':
            b1['fg']='yellow'
            b5['fg']='yellow'
            b9['fg']='yellow'
            messagebox.showinfo('Results','player O wins')        
    else:
        messagebox.showinfo('Results','match is drawed')
def c(vb_1):
    if vb_1['text']=='END GAME':
        root.destory()
    elif vb_1['text']=='RESET':
        b1['text']=""
        b2['text']=""
        b3['text']=""
        b4['text']=""
        b5['text']=""
        b6['text']=""
        b7['text']=""
        b8['text']=""
        b9['text']=""
        b1['fg']='black'
        b2['fg']='black'
        b3['fg']='black'
        b4['fg']='black'
        b5['fg']='black'
        b6['fg']='black'
        b7['fg']='black'
        b8['fg']='black'
        b9['fg']='black'
               
#BUTTONS ON FRAME 1
b1=Button(f1,text='',bg='white',font="Times 10 bold",height=12,width=24,command=lambda:g(b1))
b1.pack(side='left')

b2=Button(f1,text='',font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b2))
b2.pack(side='left')

b3=Button(f1,text='',font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b3))
b3.pack(side='left')
#BUTTONS ON FRAME 2
b4=Button(f2,font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b4))
b4.pack(side='left')

b5=Button(f2,font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b5))
b5.pack(side='left')

b6=Button(f2,font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b6))
b6.pack(side='left')

#BUTTONS ON FRAME 3
b7=Button(f3,font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b7))
b7.pack(side='left')

b8=Button(f3,font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b8))
b8.pack(side='left')

b9=Button(f3,font="Times 10 bold",bg="white",height=12,width=24,command=lambda:g(b9))
b9.pack(side='left')
#BUTTON FOR RESET AND END GAME
b10=Button(root,text="RESET",font="Times 10 bold",bg="black",height=5,width=12,
           command=lambda:c(b10))
b10.pack(side='left')

b11=Button(root,text="END GAME",font="Times 10 bold",bg="black",height=5,width=12,
           command=lambda:c(b11))
b11.pack(side='right')
root.mainloop()

