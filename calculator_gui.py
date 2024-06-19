import tkinter as tk
def clearfunction():#clear function
    label.config(text='')
def decimalpoint():
    currentdisplay=label['text']
    if '.' not in currentdisplay:
        label.config(text=currentdisplay+'.')
def operations(operator):
    global firstnum,operatorsym
    firstnum=float(label['text'])
    operatorsym=operator
    label.config(text='')
def digitdisplay(digit):
    currentdisplay=label['text']
    newdisplay=currentdisplay+str(digit)
    label.config(text=newdisplay)
def result():
    global firstnum,secondnum,operatorsym
    secondnum=float(label['text'])
    if operatorsym=='+':
        answer=firstnum+secondnum
    elif operatorsym=='-':
        answer=firstnum-secondnum
    elif operatorsym=='x':
        answer=firstnum*secondnum
    elif operatorsym=='/':
        #checks if division is possible
        if secondnum==0:
            label.config(text="Error!Division not possible")
        else:
            answer=firstnum/secondnum
    #checks if answer is an integer or not and if it is then converts into integer and prints it in the label
    if answer.is_integer():
        answer= int(answer)
    label.config(text=str(answer))
    
window = tk.Tk()#window is name of parent variable
window.title("Calculator")
window.geometry('280x380')
window.configure(background="light pink")
label= tk.Label(window, text=" ",font=("Arial",20))
label.grid(row=0,column=0,columnspan=5,padx=20,pady=20,sticky='w')

#first row
bt7=tk.Button(window,width=15,height=3,text="7",font=("Arial",20,"bold"),command=lambda:digitdisplay(7))
bt7.grid(row=1,column=0)
bt8=tk.Button(window,width=15,height=3,text="8",font=("Arial",20,"bold"),command=lambda:digitdisplay(8))
bt8.grid(row=1,column=1)
bt9=tk.Button(window,width=15,height=3,text="9",font=("Arial",20,"bold"),command=lambda:digitdisplay(9))
bt9.grid(row=1,column=2)
bt_addition=tk.Button(window,width=15,height=3,text="+",font=("Arial",20,"bold"),command=lambda:operations('+'))
bt_addition.grid(row=1,column=3)
#second row
bt4=tk.Button(window,width=15,height=3,text="4",font=("Arial",20,"bold"),command=lambda:digitdisplay(4))
bt4.grid(row=2,column=0)
bt5=tk.Button(window,width=15,height=3,text="5",font=("Arial",20,"bold"),command=lambda:digitdisplay(5))
bt5.grid(row=2,column=1)
bt6=tk.Button(window,width=15,height=3,text="6",font=("Arial",20,"bold"),command=lambda:digitdisplay(6))
bt6.grid(row=2,column=2)
bt_subtraction=tk.Button(window,width=15,height=3,text="-",font=("Arial",20,"bold"),command=lambda:operations('-'))
bt_subtraction.grid(row=2,column=3)
#third row
bt1=tk.Button(window,width=15,height=3,text="1",font=("Arial",20,"bold"),command=lambda:digitdisplay(1))
bt1.grid(row=3,column=0)
bt2=tk.Button(window,width=15,height=3,text="2",font=("Arial",20,"bold"),command=lambda:digitdisplay(2))
bt2.grid(row=3,column=1)
bt3=tk.Button(window,width=15,height=3,text="3",font=("Arial",20,"bold"),command=lambda:digitdisplay(3))
bt3.grid(row=3,column=2)
bt_multiplication=tk.Button(window,width=15,height=3,text="x",font=("Arial",20,"bold"),command=lambda:operations('x'))
bt_multiplication.grid(row=3,column=3)
#fourth row
bt0=tk.Button(window,width=15,height=3,text="0",font=("Arial",20,"bold"),command=lambda:digitdisplay(0))
bt0.grid(row=4,column=0)
b_clear=tk.Button(window,width=15,height=3,text="C",font=("Arial",20,"bold"),command=lambda:clearfunction())
b_clear.grid(row=4,column=1)
b_equal=tk.Button(window,width=15,height=3,text="=",font=("Arial",20,"bold"),command=lambda:result())
b_equal.grid(row=4,column=2)
bt_division=tk.Button(window,width=15,height=3,text="/",font=("Arial",20,"bold"),command=lambda:operations('/'))
bt_division.grid(row=4,column=3)
bt_decimal = tk.Button(window, width=15, height=3, text=".", font=("Arial", 20, "bold"), command=decimalpoint)
bt_decimal.grid(row=5,column=0)
window.mainloop()
