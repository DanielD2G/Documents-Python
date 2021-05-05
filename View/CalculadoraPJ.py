from tkinter import *


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


# suma-------------------------------------------------------
def suma(num):
    global operation
    global ResultInScreen
    global ScreenReset
    ResultInScreen += float(num)
    operation = "suma"
    ScreenReset = True
    ScreenNumber.set(ResultInScreen)


# resta-------------------------------------------------------
num1 = 0
RestCount = 0
def Sustraction(num):
    global operation
    global ResultInScreen
    global num1
    global RestCount
    global ScreenReset
    if RestCount == 0:
        num1 = float(num)
        ResultInScreen = num1
    else:
        if RestCount == 1:
            ResultInScreen = num1 - float(num)
        else:
            ResultInScreen = float(ResultInScreen) - float(num)
        ScreenNumber.set(ResultInScreen)
        ResultInScreen = ScreenNumber.get()
    RestCount = RestCount + 1
    operation = "resta"
    ScreenReset = True


#  multiplicacion-------------------------------------------------------
MultCount = 0
def Mult(num):
    global operation
    global ResultInScreen
    global num1
    global MultCount
    global ScreenReset
    if MultCount == 0:
        num1 = int(num)
        ResultInScreen = num1
    else:
        if MultCount == 1:
            ResultInScreen = num1 * int(num)
        else:
            ResultInScreen = int(ResultInScreen) * int(num)
        ScreenNumber.set(ResultInScreen)
        ResultInScreen = ScreenNumber.get()
    MultCount = MultCount + 1
    operation = "multiplicacion"
    ScreenReset = True


#  división-------------------------------------------------------
DivCount = 0
def divide(num):
    global operation
    global ResultInScreen
    global num1
    global DivCount
    global ScreenReset
    if DivCount == 0:
        num1 = float(num)
        ResultInScreen = num1
    else:
        if DivCount == 1:
            ResultInScreen = num1 / float(num)
        else:
            ResultInScreen = float(ResultInScreen) / float(num)
        ScreenNumber.set(ResultInScreen)
        ResultInScreen = ScreenNumber.get()
    DivCount = DivCount + 1
    operation = "division"
    ScreenReset = True


#  Result-------------------------------------------------------
def Result():
    global ResultInScreen
    global operation
    global RestCount
    global MultCount
    global DivCount
    if operation == "suma":
        ScreenNumber.set(ResultInScreen + int(ScreenNumber.get()))
        ResultInScreen = 0
    elif operation == "resta":
        ScreenNumber.set(int(ResultInScreen) - int(ScreenNumber.get()))
        ResultInScreen = 0
        RestCount = 0
    elif operation == "multiplicacion":
        ScreenNumber.set(int(ResultInScreen) * int(ScreenNumber.get()))
        ResultInScreen = 0
        MultCount = 0
    elif operation == "division":
        ScreenNumber.set(int(ResultInScreen) / int(ScreenNumber.get()))
        ResultInScreen = 0
        DivCount = 0


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