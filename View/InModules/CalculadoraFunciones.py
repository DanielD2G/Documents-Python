from CalculadoraBotones import *
# suma-------------------------------------------------------
def suma(num):
    global operation
    global ResultInScreen
    global ScreenReset
    ResultInScreen += int(num)
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
        num1 = int(num)
        ResultInScreen = num1
    else:
        if RestCount == 1:
            ResultInScreen = num1 - int(num)
        else:
            ResultInScreen = int(ResultInScreen) - int(num)
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

