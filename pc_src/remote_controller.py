#!/usr/bin/env python
import tkinter
import tkinter.messagebox as Message
from tkinter.constants import *
from socket import *
import sys

#from objc._objc import NULL
from tkinter import Frame, LabelFrame

#define callback function for car control
def keyDown(event):
    #if event == "ud":
     #   tcpClientSock.send("ud")
    print(str(event.char))
    print("============")
    print(carButtonUp)
    if event == carButtonUp:
        print("press" + str(event) + "down")

def upPressDown(event):
    tcpClientSock.send(b"ud\n")
    print("go forward key press")

def upPressUp(event):
    tcpClientSock.send(b"uu")
    print("go forward key relase")

def leftPressDown(event):
    tcpClientSock.send(b"ld\n")
    print("turn left key press")

def leftPressUp(event):
    tcpClientSock.send(b"lu")
    print("turn left key relase")

def rightPressDown(event):
    tcpClientSock.send(b"rd\n")
    print("turn right key press")

def rightPressUp(event):
    tcpClientSock.send(b"ru")
    print("turn right key relase")

def downPressDown(event):
    tcpClientSock.send(b"dd\n")
    print("back key press")

def downPressUp(event):
    tcpClientSock.send(b"du")
    print("back key release")

#define call back function for camera control
def upPressDownCam(event):
    tcpClientSock.send(b"udc\n")
    print("up key press")

def upPressUpCam(event):
    tcpClientSock.send(b"uuc")
    print("up key release")

def leftPressDownCam(event):
    tcpClientSock.send(b"ldc\n")
    print("left key press")

def leftPressUpCam(event):
    tcpClientSock.send(b"luc")
    print("left key release")

def rightPressDownCam(event):
    tcpClientSock.send(b"rdc\n")
    print("right key press")

def rightPressUpCam(event):
    tcpClientSock.send(b"ruc")
    print("right key release")

def downPressDownCam(event):
    tcpClientSock.send(b"ddc\n")
    print("down key press")

def downPressUpCam(event):
    tcpClientSock.send(b"duc")
    print("down key release")

#define call back function for not connected raspi
def popUpMessageBox(event):
    Message.showerror('Contro raspi', 'Has not connected to raspi!!')

def connectToServer():
    global tcpClientSock
    tcpClientSock = socket(AF_INET, SOCK_STREAM)
    tcpClientSock.settimeout(2)
    try:
        print("IP:"+ipEntry.get())
        print("port:"+portEntry.get())
        if (ipEntry.get() is None or ipEntry.get()==""):
            Message.showerror('Contro raspi', 'Please input raspi IP Address!!')
        else:
            ADDR = (ipEntry.get(), int(portEntry.get()))
            tcpClientSock.connect(ADDR)
    except timeout:
        print("time out exception")
        tcpClientSock.close()
        Message.showerror('Contro raspi', 'Can not connected to raspi, please retry later!')
    else:
        carButtonLeft.bind("<ButtonPress-1>", leftPressDown, "")
        carButtonLeft.bind('<ButtonRelease-1>', leftPressUp, "")
        carButtonUp.bind("<ButtonPress-1>", upPressDown, "")
        carButtonUp.bind('<ButtonRelease-1>', upPressUp, "")
        carButtonRight.bind("<ButtonPress-1>", rightPressDown, "")
        carButtonRight.bind('<ButtonRelease-1>', rightPressUp, "")
        carButtonDown.bind("<ButtonPress-1>", downPressDown, "")
        carButtonDown.bind('<ButtonRelease-1>', downPressUp, "")

        '''
            bind key for motion control
        '''
        top.bind("<KeyPress-a>", leftPressDown, "")
        top.bind("<KeyPress-w>", upPressDown, "")
        top.bind("<KeyPress-d>", rightPressDown, "")
        top.bind("<KeyPress-s>", downPressDown, "")

        camButtonLeft.bind("<ButtonPress-1>", leftPressDownCam, "")
        camButtonLeft.bind('<ButtonRelease-1>', leftPressUpCam, "")
        camButtonUp.bind("<ButtonPress-1>", upPressDownCam, "")
        camButtonUp.bind('<ButtonRelease-1>', upPressUpCam, "")
        camButtonRight.bind("<ButtonPress-1>", rightPressDownCam, "")
        camButtonRight.bind('<ButtonRelease-1>', rightPressUpCam, "")
        camButtonDown.bind("<ButtonPress-1>", downPressDownCam, "")
        camButtonDown.bind('<ButtonRelease-1>', downPressUpCam, "")

        '''
            bind key for camera control
            j: left
            i: up
            k: down
            l: right
        '''
        top.bind("<KeyPress-j>", leftPressDownCam, "")
        top.bind("<KeyPress-i>", upPressDownCam, "")
        top.bind("<KeyPress-k>", downPressDownCam, "")
        top.bind("<KeyPress-l>", rightPressDownCam, "")

        connState['bg']='green'
        top.focus_set()

def closeControl():
    if(tcpClientSock is not None):
        tcpClientSock.close()
    top.quit()


HOST = '192.168.50.126'
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)
# tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock = None
print("set tcpClientSock NULL")

connected = FALSE

top=tkinter.Tk()
#initial set title and and size of window
top.title('Raspi Controler')
top.geometry("500x300")
top.resizable(FALSE, FALSE)

hello = tkinter.Label(top, text='please control your raspi!',bg='white',fg='blue')
hello.pack()

#define connection status
frmControl = Frame()
frmControl.pack(side=TOP)

frmgap = Frame(height=50)
frmgap.pack(side=TOP)
connState = tkinter.Label(frmgap,bg='red', width=5)
connState.pack()

frmOther = Frame()
frmOther.pack(side=TOP)

#define car controller panel
frmCar = LabelFrame(frmControl, text='Car controller')
frmCar.pack(side=LEFT)


top.bind("<KeyPress-a>", keyDown, "")

carButtonUp = tkinter.Button(frmCar,text="w",bg='blue')
carButtonUp.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonUp.pack(side=TOP)

carButtonLeft = tkinter.Button(frmCar,text="a",bg='blue')
carButtonLeft.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonLeft.pack(side=LEFT)

carButtonRight = tkinter.Button(frmCar,text="d",bg='blue')
carButtonRight.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonRight.pack(side=RIGHT)

carButtonDown = tkinter.Button(frmCar,text="s",bg='blue')
carButtonDown.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonDown.pack(side=BOTTOM)

#define gap between car and camera control panel
frmControlGap = Frame(frmControl, width=50)
frmControlGap.pack(side=LEFT)

#define camera controller panel
frmCamera = LabelFrame(frmControl, text='Camera controller')
frmCamera.pack(side=RIGHT)

camButtonUp = tkinter.Button(frmCamera,text="i",bg='green')
camButtonUp.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonUp.pack(side=TOP)

camButtonLeft = tkinter.Button(frmCamera,text="j",bg='green')
camButtonLeft.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonLeft.pack(side=LEFT)

camButtonRight = tkinter.Button(frmCamera,text="l",bg='green')
camButtonRight.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonRight.pack(side=RIGHT)

camButtonDown = tkinter.Button(frmCamera,text="k",bg='green')
camButtonDown.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonDown.pack(side=BOTTOM)


#define connected button
frmConnect = LabelFrame(frmOther, text='Status')
frmConnect.pack(side=TOP)
buttonConnect = tkinter.Button(frmConnect, text='Connect to server',command=connectToServer, activeforeground='white',activebackground='red')
buttonConnect.pack(side=LEFT)

varIp = tkinter.StringVar()
ipEntry = tkinter.Entry(frmConnect, textvariable=varIp)
varIp.set(HOST)
ipEntry.pack(side=LEFT)

varPort = tkinter.StringVar()
portEntry = tkinter.Entry(frmConnect, textvariable=varPort, width=5)
varPort.set(PORT)
portEntry.pack(side=RIGHT)

buttonQuit=tkinter.Button(top, text='QUIT',command=closeControl, activeforeground='white',activebackground='red')
buttonQuit.pack(side=BOTTOM)

tkinter.mainloop()
