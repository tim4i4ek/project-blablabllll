import random as r
from asyncio import all_tasks

from customtkinter import *

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(child1)



app = CTk()
app.geometry("400x500")
app.title('Календарь')
app.configure(fg_color='#2a1212')
app.resizable(width=False, height=False)

# Ввод текста
entry = CTkEntry(app, placeholder_text="Текст вроде", bg_color='#5f0909',fg_color='#5f0909', border_color='#5f0909',placeholder_text_color='#d26464',font=("Arial", 32),text_color='#d26464',width=400,height=40,justify="center")
entry.grid(column = 0, row = 0,columnspan = 2,sticky="ew")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(1, weight=1)


btn = CTkButton(app,width=300,height=15,fg_color='#950101',text='+',font=("Arial",32),hover_color='#590000',command=plus)
btn.grid(row=7, column=0, padx=20, sticky="w")


frame1 = CTkFrame(app,width=300,height=400,fg_color='#950101')
frame1.grid(row=1, column=0, padx=20, sticky="w",pady=(15,0),rowspan = 6)


bbtn = CTkButton(app,text='завдання 1',width=70,height=50,fg_color='#8A3834',corner_radius=5)
bbtn.grid(row=1,column=1,padx=(0,15))

app.mainloop()