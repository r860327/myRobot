#!/usr/bin/env python
import Tkinter
import tkMessageBox as Message
from Tkconstants import *
from socket import *
import sys

from objc._objc import NULL
from Tkinter import Frame, LabelFrame

#define callback function for car control
def upPressDown(event):
    tcpClientSock.send("ud")
    print "press down"
    
def upPressUp(event):
    tcpClientSock.send("uu")
    print "press up"

def leftPressDown(event):
    tcpClientSock.send("ld")
    print "press down"
     
def leftPressUp(event):
    tcpClientSock.send("lu")
    print "press up"
    
def rightPressDown(event):
    tcpClientSock.send("rd")
    print "press down"
     
def rightPressUp(event):
    tcpClientSock.send("ru")
    print "press up"
    
def downPressDown(event):
    tcpClientSock.send("dd")
    print "press down"
     
def downPressUp(event):
    tcpClientSock.send("du")
    print "press up"

#define call back function for camera control
def upPressDownCam(event):
    tcpClientSock.send("udc")
    print "press down"
    
def upPressUpCam(event):
    tcpClientSock.send("uuc")
    print "press up"

def leftPressDownCam(event):
    tcpClientSock.send("ldc")
    print "press down"
     
def leftPressUpCam(event):
    tcpClientSock.send("luc")
    print "press up"
    
def rightPressDownCam(event):
    tcpClientSock.send("rdc")
    print "press down"
     
def rightPressUpCam(event):
    tcpClientSock.send("ruc")
    print "press up"
    
def downPressDownCam(event):
    tcpClientSock.send("ddc")
    print "press down"
     
def downPressUpCam(event):
    tcpClientSock.send("duc")
    print "press up"

#define call back function for not connected raspi
def popUpMessageBox(event):
    Message.showerror('Contro raspi', 'Has not connected to raspi!!')
    
def connectToServer():
    global tcpClientSock
    tcpClientSock = socket(AF_INET, SOCK_STREAM)
    tcpClientSock.settimeout(2)
    try:
        print "IP:"+ipEntry.get()
        print "port:"+portEntry.get()
        if (ipEntry.get()==NULL or ipEntry.get()==""):
            Message.showerror('Contro raspi', 'Please input raspi IP Address!!')
        else:
            ADDR = (ipEntry.get(), int(portEntry.get()))
            tcpClientSock.connect(ADDR)
    except timeout:
        print "time out exception"
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
    if(tcpClientSock != NULL):
        tcpClientSock.close()
    top.quit()


HOST = '192.168.1.116'
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)
# tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock = NULL
print "set tcpClientSock NULL"

connected = FALSE

top=Tkinter.Tk()
top.title('Raspi Controler')
top.geometry("500x300")
top.resizable(FALSE, FALSE)

hello = Tkinter.Label(top, text='please control your raspi!',bg='white',fg='blue')
hello.pack()

frmControl = Frame()
frmControl.pack(side=TOP)

frmgap = Frame(height=50)
frmgap.pack(side=TOP)
connState = Tkinter.Label(frmgap,bg='red', width=2)
connState.pack()

frmOther = Frame()
frmOther.pack(side=TOP)

#define car controller panel
frmCar = LabelFrame(frmControl, text='Car controller')
frmCar.pack(side=LEFT)


carButtonUp = Tkinter.Button(frmCar,text="up",bg='blue')
carButtonUp.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonUp.pack(side=TOP)

carButtonLeft = Tkinter.Button(frmCar,text="left",bg='green')
carButtonLeft.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonLeft.pack(side=LEFT)

carButtonRight = Tkinter.Button(frmCar,text="right",bg='blue')
carButtonRight.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonRight.pack(side=RIGHT)

carButtonDown = Tkinter.Button(frmCar,text="down",bg='blue')
carButtonDown.bind('<ButtonRelease-1>', popUpMessageBox, "")
carButtonDown.pack(side=BOTTOM)

#define gap between car and camera control panel
frmControlGap = Frame(frmControl, width=20)
frmControlGap.pack(side=LEFT)

#define camera controller panel
frmCamera = LabelFrame(frmControl, text='Camera controller')
frmCamera.pack(side=RIGHT)

camButtonUp = Tkinter.Button(frmCamera,text="up",bg='blue')
camButtonUp.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonUp.pack(side=TOP)

camButtonLeft = Tkinter.Button(frmCamera,text="left",bg='green')
camButtonLeft.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonLeft.pack(side=LEFT)

camButtonRight = Tkinter.Button(frmCamera,text="right",bg='blue')
camButtonRight.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonRight.pack(side=RIGHT)

camButtonDown = Tkinter.Button(frmCamera,text="down",bg='blue')
camButtonDown.bind('<ButtonRelease-1>', popUpMessageBox, "")
camButtonDown.pack(side=BOTTOM)


#define connected button
frmConnect = LabelFrame(frmOther, text='Status')
frmConnect.pack(side=TOP)
buttonConnect = Tkinter.Button(frmConnect, text='Connect to server',command=connectToServer, activeforeground='white',activebackground='red')
buttonConnect.pack(side=LEFT)

varIp = Tkinter.StringVar()
ipEntry = Tkinter.Entry(frmConnect, textvariable=varIp)
varIp.set("192.168.1.116")
ipEntry.pack(side=LEFT)

varPort = Tkinter.StringVar()
portEntry = Tkinter.Entry(frmConnect, textvariable=varPort, width=5)
varPort.set("20000")
portEntry.pack(side=RIGHT)

buttonQuit=Tkinter.Button(top, text='QUIT',command=closeControl, activeforeground='white',activebackground='red')
buttonQuit.pack(side=BOTTOM)

Tkinter.mainloop()
