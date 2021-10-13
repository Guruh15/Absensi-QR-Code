from tkinter import *
import random 

root=Tk()
root.title("Game Lempar Dadu")
root.geometry("400x300")
label=Label(root,font=('helvetica',250,'bold'),text='')

def lempar_dadu():     
	dadu=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	label.configure(text=f'{random.choice(dadu)}')	
	label.pack()

button=Button(root,font=('helvetica',25,'bold'),text='Lemparkan Dadu',command=lempar_dadu,bg="green")
button.pack()
root.mainloop()
