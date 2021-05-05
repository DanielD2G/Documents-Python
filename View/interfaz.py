from tkinter import *


root = Tk()

mFrame = Frame(root)
mFrame.pack()

operation = ""
numberInScreen= 0
ScreenReset=False

#Main Screen----------------------------------------------------
ScreenNumber=StringVar()

screen =Entry(mFrame, textvariable=ScreenNumber)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")
#Functions-------------------------------------------------------
def setNumberOnScreen(num):
    global operation
    if operation != "":
        ScreenNumber.set(num)
        operation = ""
    else:
        ScreenNumber.set(ScreenNumber.get() + num)
# Sum-------------------------------------------------------------
def SumFunction(num):
    global operation
    global numberInScreen
    operation= "sum"
    numberInScreen += float(num)
    ScreenNumber.set(numberInScreen)
#RestFunction---------------------------------------------
num1 = 0
RestCount = 0
def RestFunction(num):
    global operation
    global numberInScreen
    global num1
    global RestCount
    global ScreenReset

    if RestCount == 0:
        num1 = float(num)
        numberInScreen = num1
    else:
        if RestCount == 1:
            numberInScreen = num1 - float(num)
        else:
            numberInScreen = float(numberInScreen) - float(num)
        ScreenNumber.set(numberInScreen)
        numberInScreen = ScreenNumber.get()

    RestCount = RestCount + 1
    operation = "rest"
    ScreenReset = True


# Mult-------------------------------------------------------------
MultCount = 0
def MultFunction(num):
    global operation
    global numberInScreen
    global num1
    global MultCount
    global ScreenReset
    if MultCount == 0:
        num1 = int(num)
        numberInScreen = num1
    else:
        if MultCount == 1:
            numberInScreen = num1 * int(num)
        else:
            numberInScreen = int(numberInScreen) * int(num)
        ScreenNumber.set(numberInScreen)
        numberInScreen = ScreenNumber.get()

    MultCount = MultCount + 1
    operation = "mult"
    ScreenReset = True
# Div-------------------------------------------------------------
DivCount = 0
def DivFunction(num):
    global operation
    global numberInScreen
    global num1
    global DivCount
    global ScreenReset
    if DivCount == 0:
        num1 = float(num)
        numberInScreen = num1
    else:
        if DivCount == 1:
            numberInScreen = num1 / float(num)
        else:
            numberInScreen = float(numberInScreen) / float(num)
        ScreenNumber.set(numberInScreen)
        numberInScreen = ScreenNumber.get()

    DivCount = DivCount + 1
    operation = "div"
    ScreenReset = True
# Result----------------------------------------------------------------
def Result():
    global numberInScreen

    global operation

    global RestCount

    global MultCount

    global DivCount

    if operation == "sum":

        ScreenNumber.set(numberInScreen + float(ScreenNumber.get()))

        numberInScreen = 0

    elif operation == "rest":

        ScreenNumber.set(float(numberInScreen) - float(ScreenNumber.get()))

        operation = 0

        RestCount = 0

    elif operation == "mult":

        ScreenNumber.set(float(numberInScreen) * float(ScreenNumber.get()))

        numberInScreen = 0

        MultCount = 0

    elif operation == "div":

        ScreenNumber.set(float(numberInScreen) / float(ScreenNumber.get()))

        numberInScreen = 0

        DivCount = 0


#Buttons1-------------------------------------------------------
button7 = Button(mFrame, text='7', width=3,command=lambda:setNumberOnScreen("7"))
button7.grid(row=2,column=1)
button8 = Button(mFrame, text='8', width=3,command=lambda:setNumberOnScreen("8"))
button8.grid(row=2,column=2)
button9 = Button(mFrame, text='9', width=3,command=lambda:setNumberOnScreen("9"))
button9.grid(row=2,column=3)
buttonDiv = Button(mFrame, text='/', width=3,command=lambda:DivFunction(ScreenNumber.get()))
buttonDiv.grid(row=2,column=4)
#Buttons2-------------------------------------------------------
button4 = Button(mFrame, text='4', width=3, command=lambda:setNumberOnScreen("4"))
button4.grid(row=3,column=1)
button5 = Button(mFrame, text='5', width=3,command=lambda:setNumberOnScreen("5"))
button5.grid(row=3,column=2)
button6 = Button(mFrame, text='6', width=3,command=lambda:setNumberOnScreen("6"))
button6.grid(row=3,column=3)
buttonMult = Button(mFrame, text='*', width=3,command=lambda:MultFunction(ScreenNumber.get()))
buttonMult.grid(row=3,column=4)
#Button3--------------------------------------------------------
button1 = Button(mFrame, text='1', width=3,command=lambda:setNumberOnScreen("1"))
button1.grid(row=4,column=1)
button2 = Button(mFrame, text='2', width=3,command=lambda:setNumberOnScreen("2"))
button2.grid(row=4,column=2)
button3 = Button(mFrame, text='3', width=3,command=lambda:setNumberOnScreen("3"))
button3.grid(row=4,column=3)
buttonSum = Button(mFrame, text='+', width=3,command=lambda:SumFunction(ScreenNumber.get()))
buttonSum.grid(row=4,column=4)
#Button3--------------------------------------------------------
buttonDel = Button(mFrame, text='=', width=3,command=lambda:setNumberOnScreen("="))
buttonDel.grid(row=5,column=1)
button0 = Button(mFrame, text='0', width=3,command=lambda:setNumberOnScreen("0"))
button0.grid(row=5,column=2)
buttonFloat = Button(mFrame, text=',', width=3,command=lambda:setNumberOnScreen("."))
buttonFloat.grid(row=5,column=3)
buttonRest = Button(mFrame, text='-', width=3,command=lambda:RestFunction(ScreenNumber.get()))
buttonRest.grid(row=5,column=4)

buttonCalculate= Button(mFrame, text='=', width=3,command=Result())
buttonCalculate.grid(row=2,column=5, rowspan=4)


root.mainloop()