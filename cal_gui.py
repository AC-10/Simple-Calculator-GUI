from tkinter import *
root=Tk()
root.title("Calculator")
#setting a label name
#packing everything into application
#*main_label.pack()*#
#a more sophisticated approach is a grid system

#defining a function which when called will be the result of clicking the button
#creating a input box


e=Entry(root,width=40,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#####e.insert(0,"Enter:")
def click(number):
    curr_digit=e.get()   #current digit
    e.delete(0,END)      #deletes whole thing starting from 0 till END   #we want to forget the old number so that it doesnt get printed again
    whole_num=str(curr_digit)+str(number)
    e.insert(0,whole_num)  #inserts the number at position 0   adds the new digit to the current digit and forms a number(5&3=53)
    #very imp step becoz without this step number would be printed in wrong order

def clear():
    e.delete(0,END)


def add():
    first_num=e.get()
    global f_num
    global op    #operation type
    op="addition"
    f_num=int(first_num)
    e.delete(0,END)

def sub():
    first_num=e.get()
    global f_num
    global op    #operation type
    op="subtraction"
    f_num=int(first_num)
    e.delete(0,END)

def div():
    first_num=e.get()
    global f_num
    global op    #operation type
    op="division"
    f_num=int(first_num)
    e.delete(0,END)

def mul():
    first_num=e.get()
    global f_num
    global op    #operation type
    op="multiplication"
    f_num=int(first_num)
    e.delete(0,END)

def equals():
    second_num=e.get()
    e.delete(0,END)
    if op=="addition":
        e.insert(0,f_num+int(second_num))
    if op=="subtraction":
        e.insert(0,f_num-int(second_num))
    if op=="multiplication":
        e.insert(0,f_num*int(second_num))
    if op=="division":
        e.insert(0,f_num/int(second_num))






#using buttons and defining each button
button1=Button(root, text="1",padx=40,pady=20,command=lambda:click(1))     #a button can be disabled using state=DISABLED
button2=Button(root, text="2",padx=40,pady=20,command=lambda:click(2))
button3=Button(root, text="3",padx=40,pady=20,command=lambda:click(3))
button4=Button(root, text="4",padx=40,pady=20,command=lambda:click(4))
button5=Button(root, text="5",padx=40,pady=20,command=lambda:click(5))
button6=Button(root, text="6",padx=40,pady=20,command=lambda:click(6))
button7=Button(root, text="7",padx=40,pady=20,command=lambda:click(7))
button8=Button(root, text="8",padx=40,pady=20,command=lambda:click(8))
button9=Button(root, text="9",padx=40,pady=20,command=lambda:click(9))
button0=Button(root, text="0",padx=40,pady=20,command=lambda:click(0))
button_mul=Button(root, text="X",padx=40,pady=20,command=mul)
button_div=Button(root, text="/",padx=40,pady=20,command=div)
button_add=Button(root, text="+",padx=40,pady=20,command=add)
button_sub=Button(root, text="-",padx=40,pady=20,command=sub)
button_equals=Button(root, text="=",padx=40,pady=20,command=equals)
button_clear=Button(root, text="C",padx=40,pady=20,command=clear)



#placing buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_clear.grid(row=4, column=0)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)



#used to display your gui
root.mainloop()
