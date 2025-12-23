import tkinter as tk
#Button click function
def button_click(value):
    current=entry_box.get()
    entry_box.delete(0,tk.END)
    entry_box.insert(0,current+value)
#clear function
def clear():
    entry_box.delete(0,tk.END)
#Evaluate Function(=)
def evaluate():
    try:
        expression=entry_box.get()
        result=str(eval(expression))
        entry_box.delete(0,tk.END)
        entry_box.insert(0,result)
    except:
        entry_box.delete(0,tk.END)
        entry_box.insert(0,"Error")
#Keyboard support
def key_support(event):
    char=event.char
    #Allow digits 0-9
    if char.isdigit():
        button_click(char)
    #Allow + * / -
    elif char in "+*/-":
        button_click(char)
    #Enter key=>evaluate 
    elif event.keysym=="Return":
        evaluate()
    #BackSpace Key
    elif event.keysym=="BackSpace":
        entry_box.delete(len(entry_box.get())-1,tk.END)
    #Escape Key=>Clear
    elif event.keysym=="Escape":
        clear()
    return "break"
#Main Window
root=tk.Tk()
root.title("Python Calculator")
#root.geometry("800x600")
#Entry box
entry_box=tk.Entry(root,width=25,font=("Arial",18),borderwidth=3,relief="sunken")
entry_box.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#Bind keyboard events
entry_box.bind("<Key>",key_support)
#Buttons(Digit+Operator)
#('text',row,column)
buttons=[
    ('1',1,0),('2',1,1),('3',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('7',3,0),('8',3,1),('9',3,2),('-',3,3),
    ('0',4,0),('C',4,1),('=',4,2),('+',4,3),
]
colors={
    'C':"#ff4d4d",
    '+':"#ffa500",
    '-':"#ffa500",
    '/':"#ffa500",
    '*':"#ffa500"
}
for (text,row,col) in buttons:
    bg_colors=colors.get(text,"#ffffff")
    if text=="=":
        btn=tk.Button(root,text=text,width=5,height=2,command=evaluate,bg="#00cc66",fg="black")
    elif text=="C":
        btn=tk.Button(root,text=text,width=5,height=5,command=clear,bg=bg_colors,fg="black")
    else:
        btn=tk.Button(root,text=text,width=5,height=2,bg=bg_colors,fg="black",command=lambda t=text:button_click(t))
    btn.grid(row=row,column=col,padx=5,pady=5)
root.mainloop()

