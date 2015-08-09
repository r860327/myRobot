/**************************************************************
机器人基地 RobotBase www.robotbase.cn       	
		                                                            
目    的:   Arduino控制器通过双H桥直流电机驱动板控制直流电机
		
目标系统:   基于Arduino Duemilanove AVR Mega168、Arduino Duemilanove AVR Mega328、Arduino UNO控制器

应用软件:   Arduino 1.0.1

功能描述：  直流电机1s正转，1s反转                                             
		                                                                                                                        
发布时间:   2013-9-4

说    明:   若用于商业用途，请保留此段文字或注明代码来源
		
	        哈尔滨奥松机器人科技有限公司保留所有版权   
**************************************************************/
int pin1=8;               // I1或I3
int pin2=9;               // I2或I4
int speedpin=10;         // EA或EB
int pin3=7;               // I3或I1
int pin4=6;               // I4或I2
int speedpin1=5;         // EB或EA
void setup()
{                      //将各个引脚置于输出模式
pinMode(pin1,OUTPUT);
pinMode(pin2,OUTPUT);
pinMode(speedpin,OUTPUT);
pinMode(pin3,OUTPUT);
pinMode(pin4,OUTPUT);
pinMode(speedpin1,OUTPUT);
}
void loop()
{
analogWrite(speedpin,180);    //
delay(1000);
digitalWrite(pin1,LOW);        //
digitalWrite(pin2,HIGH);
digitalWrite(pin3,LOW);        //
digitalWrite(pin4,HIGH);

analogWrite(speedpin1,180);
delay(1000);
digitalWrite(pin1,HIGH);        //
digitalWrite(pin2,LOW);
digitalWrite(pin3,HIGH);        //
digitalWrite(pin4,LOW);
}
