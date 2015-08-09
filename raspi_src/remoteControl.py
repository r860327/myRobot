#!/usr/bin/env python
from socket import *
from time import ctime
from raspirobotboard import *
import sys
import RPi.GPIO as GPIO

rr = RaspiRobot()

HOST = ''
PORT = 20000
BUFSIZE = 1024    #1KB
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

CAMERA_VERTICAL_CHANNEL = 23
CAMERA_HORIZONTAL_CHANNEL = 18
DEFAULT_VERTICAL_POS = 40
DEFAULT_HORIZONTAL_POS = 82

class Camera:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(CAMERA_VERTICAL_CHANNEL, GPIO.OUT)
		GPIO.setup(CAMERA_HORIZONTAL_CHANNEL, GPIO.OUT)
		self.vertical_p = GPIO.PWM(CAMERA_VERTICAL_CHANNEL, 50)
		self.horizontal_p = GPIO.PWM(CAMERA_HORIZONTAL_CHANNEL, 50)

		vertical_h_edge = 0.5 + DEFAULT_VERTICAL_POS * 2.0 / 180
		horizontal_h_edge = 0.5 + DEFAULT_HORIZONTAL_POS * 2.0 / 180
		self.current = cameraPosition(DEFAULT_VERTICAL_POS, DEFAULT_HORIZONTAL_POS)
		self.vertical_p.start(100 * vertical_h_edge/(20.0 - vertical_h_edge))
		self.horizontal_p.start(100 * horizontal_h_edge/(20.0 - horizontal_h_edge))
		time.sleep(0.2)
		self.vertical_p.ChangeDutyCycle(0)
		self.horizontal_p.ChangeDutyCycle(0)

	def pwmOut(self, channel, duty_cycle, frequence):
		#GPIO.setmode(GPIO.BCM)
		channel.ChangeDutyCycle(int(duty_cycle))
#   	p.start(int(a))
		print('channel: ' + str(channel))
		print('duty_cycle: ' + str(duty_cycle))
		print('frequence: ' + str(frequence))

		time.sleep(0.1)
		channel.ChangeDutyCycle(0)
#		GPIO.cleanup()

	def setCameraPostion(self, command):
		if command == 'udc' and self.current.vertical > 0:
			self.current.vertical = max(0, self.current.vertical - 15)
			high_level = 0.5 + self.current.vertical * 2.0 / 180
			self.pwmOut(self.vertical_p, 100 * high_level/(20.0 - high_level), 50)
		elif command == 'ddc' and self.current.vertical < 120:
			self.current.vertical = min(120, self.current.vertical + 15)
			high_level = 0.5 + self.current.vertical * 2.0 / 180
			self.pwmOut(self.vertical_p, 100 * high_level/(20.0 - high_level), 50)
		elif command == 'rdc' and self.current.horizontal > 20:
			self.current.horizontal = max(10, self.current.horizontal - 15)
			high_level = 0.5 + self.current.horizontal * 2.0 / 180
			self.pwmOut(self.horizontal_p, 100 * high_level/(20.0 - high_level), 50)
		elif command == 'ldc' and self.current.horizontal < 160:
			self.current.horizontal = min(160, self.current.horizontal + 15)
			high_level = 0.5 + self.current.horizontal * 2.0 / 180
			self.pwmOut(self.horizontal_p, 100 * high_level/(20.0 - high_level), 50)
		else:
			print("unknow command : " + str(command) + " or need no nothing!\n")

class cameraPosition:
	def __init__(self, vertical, horizontal):
		self.vertical = vertical
		self.horizontal = horizontal

cam = Camera()

while True:
	print 'waiting for connection...'
	tcpClientSock,clientAddr = tcpSerSock.accept()
	print '...connected from :', clientAddr
	while True:
		data = tcpClientSock.recv(BUFSIZE)
		if not data:
			break
		print '[%s] %s' % (ctime(), data)

		if data == 'ud':
			rr.forward(0.075)
		elif data == 'ld':
			rr.left(0.075)
		elif data == 'dd':
			rr.reverse(0.075)
		elif data == 'rd':
			rr.right(0.075)
		elif data == 'udc' or data == 'ddc' or data == 'ldc' or data == 'rdc':
			cam.setCameraPostion(data)
		else:
			print 'unknow command'
	tcpClientSock.close()
tcpSerSock.close()
