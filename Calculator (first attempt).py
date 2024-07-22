#This is a calculator

from tkinter import * #Using the tkinter GUI python library

#displaying inputs on label screen
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

#calculating input
def equals_to():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    #checking for syntax errors
    except SyntaxError:
        equation_label.set('syntax error!')
        equation_text = ""
    #checking for division by zero
    except ZeroDivisionError:
        equation_label.set('math error!')
        equation_text = ""

#clear command to clear the screen
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

#calculator window
window = Tk()
window.title("Fiyin's Calculator")
window.geometry("500x600")
window.configure(bg='#CFE1C9')#pale green

#calculation display
equation_text = ""
equation_label = StringVar()
label = Label(window,textvariable=equation_label,font=("helvetica",20),bg="white",width=25,height=3)
label.pack()

#button displays [frame]
frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, width=10, height=4, font = 35, command=lambda:button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, width=10, height=4, font = 35, command=lambda:button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, width=10, height=4, font = 35, command=lambda:button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame, text=4, width=10, height=4, font = 35, command=lambda:button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, width=10, height=4, font = 35, command=lambda:button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, width=10, height=4, font = 35, command=lambda:button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, width=10, height=4, font = 35, command=lambda:button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, width=10, height=4, font = 35, command=lambda:button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, width=10, height=4, font = 35, command=lambda:button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, width=10, height=4, font = 35, command=lambda:button_press(0))
button0.grid(row=3,column=1)

button_plus = Button(frame, text='+', width=10, height=4, font = 35, command=lambda:button_press('+'))
button_plus.grid(row=0,column=3)

button_minus = Button(frame, text='-', width=10, height=4, font = 35, command=lambda:button_press('-'))
button_minus.grid(row=1,column=3)

button_multiply = Button(frame, text='*', width=10, height=4, font = 35, command=lambda:button_press('*'))
button_multiply.grid(row=2,column=3)

button_divide = Button(frame, text='/', width=10, height=4, font = 35, command=lambda:button_press('/'))
button_divide.grid(row=3,column=3)

button_equal = Button(frame, text='=', width=10, height=4, font = 35,bg='#9CAF88', command=equals_to)#sage green
button_equal.grid(row=4,column=2)

button_decimal = Button(frame, text='.', width=10, height=4, font = 35, command=lambda:button_press('.'))
button_decimal.grid(row=3,column=0)

button_open_bracket = Button(frame, text='(', width=10, height=4, font = 35, command=lambda:button_press('('))
button_open_bracket.grid(row=4,column=0)

button_close_bracket = Button(frame, text=')', width=10, height=4, font = 35, command=lambda:button_press(')'))
button_close_bracket.grid(row=4,column=1)

button_power = Button(frame, text='^', width=10, height=4, font = 35, command=lambda:button_press('^'))
button_power.grid(row=3,column=2)

button_clear = Button(frame, text='CLEAR', width=10, height=4, font = 35, command=clear)
button_clear.grid(row = 4, column = 3)
window.mainloop()