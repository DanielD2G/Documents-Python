from tkinter import *
#from CalculadoraFunciones import NumberInButton
from CalculadoraFunciones import divide
from CalculadoraFunciones import Mult
from CalculadoraFunciones import Sustraction
from CalculadoraFunciones import Result
from CalculadoraFunciones import suma

root = Tk()
mFrame = Frame(root)
mFrame.pack()
operation = ""
ScreenReset = False
ResultInScreen = 0


#  screen-------------------------------------------------------
ScreenNumber = StringVar()
Screen = Entry(mFrame, textvariable=ScreenNumber)
Screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
Screen.config(background="black", fg="#03f943", justify="right")

#  botones-------------------------------------------------------
def NumberInButton(num):
    global operation
    global ScreenReset
    if ScreenReset != False:
        ScreenNumber.set(num)
        ScreenReset = False
    else:
        ScreenNumber.set(ScreenNumber.get() + num)


#  Button7-9/Div-------------------------------------------------------
button7 = Button(mFrame, text="7", width=3, command=lambda: NumberInButton("7"))
button7.grid(row=2, column=1)
button8 = Button(mFrame, text="8", width=3, command=lambda: NumberInButton("8"))
button8.grid(row=2, column=2)
button9 = Button(mFrame, text="9", width=3, command=lambda: NumberInButton("9"))
button9.grid(row=2, column=3)
buttonDiv = Button(mFrame, text="/", width=3, command=lambda: divide(ScreenNumber.get()))
buttonDiv.grid(row=2, column=4)


#  Button4-6/Mult-------------------------------------------------------
button4 = Button(mFrame, text="4", width=3, command=lambda: NumberInButton("4"))
button4.grid(row=3, column=1)
button5 = Button(mFrame, text="5", width=3, command=lambda: NumberInButton("5"))
button5.grid(row=3, column=2)
button6 = Button(mFrame, text="6", width=3, command=lambda: NumberInButton("6"))
button6.grid(row=3, column=3)
buttonMult = Button(mFrame, text="x", width=3, command=lambda: Mult(ScreenNumber.get()))
buttonMult.grid(row=3, column=4)


#  Button1-3/Rest-------------------------------------------------------
button1 = Button(mFrame, text="1", width=3, command=lambda: NumberInButton("1"))
button1.grid(row=4, column=1)
button2 = Button(mFrame, text="2", width=3, command=lambda: NumberInButton("2"))
button2.grid(row=4, column=2)
button3 = Button(mFrame, text="3", width=3, command=lambda: NumberInButton("3"))
button3.grid(row=4, column=3)
buttonRest = Button(mFrame, text="-", width=3, command=lambda: Sustraction(ScreenNumber.get()))
buttonRest.grid(row=4, column=4)


#  ButtonPoint/0/Resultado/Suma-------------------------------------------------------
buttonP = Button(mFrame, text=",", width=3, command=lambda: NumberInButton("."))
buttonP.grid(row=5, column=1)
button0 = Button(mFrame, text="0", width=3, command=lambda: NumberInButton("0"))
button0.grid(row=5, column=2)
buttonResult = Button(mFrame, text="=", width=3, command=lambda: Result())
buttonResult.grid(row=5, column=3)
buttonSum = Button(mFrame, text="+", width=3, command=lambda: suma(ScreenNumber.get()))
buttonSum.grid(row=5, column=4)


root.mainloop()