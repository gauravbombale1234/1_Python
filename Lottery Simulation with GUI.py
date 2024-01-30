#!/usr/bin/env python
# coding: utf-8

# In[20]:


from tkinter import *
from tkinter import messagebox
top=Tk()
top.title("Lottery Simulation")
top.geometry("300x300") 

res=StringVar()
bet2=StringVar()
lott=StringVar()
lbl=Label(top,text='Lottery Simulation', fg="Red", bg='pink')
lbl.place(x=10,y=10)

lbl=Label(top,text=' Enter Your Bet number between 1 to 10', fg="Red", bg='pink')
lbl.place(x=10,y=60)
bet=Text(top,width=15,height=1)
bet.place(x=10,y=100)

lbl=Label(top,textvariable=bet2, fg="Red", bg='pink')
lbl.place(x=10,y=130)

lbl=Label(top,textvariable=lott, fg="Red", bg='pink')
lbl.place(x=10,y=160)

lbl=Label(top,textvariable=res, fg="Red", bg='pink')
lbl.place(x=10,y=190)

btn=Button(text="Play", fg="Blue", command=lambda:lot())
btn.place(x=10, y=220)
top.mainloop()


# In[19]:


'''Lottery Simulation

bet 1,10

lottery 1,10

if bet== lottery  won 900 added account but pay 100 rs for game 
bet != Lottery    pay 100 rs '''

import random as r
def lot():
    amt=0
    bet1=bet.get(1.0,"end-1c")
 
    bet2.set("Yoy enterd number is "+bet1)
    lottery=r.randint(1,10)
  
    lott.set("Yoy enterd number is "+str(lottery))
    if lottery==int(bet1):
        amt=amt+900-100
        res.set('You Won'+str(amt))
    else:
        amt=amt-100
        res.set('You Loss '+str(amt))


# In[ ]:





# In[ ]:




