#클래스 불러오기
import motor,led
#GPIO제어/시간 모듈 불러오기
import rospy
import RPi.GPIO as GPIO
from time import sleep
#인스턴스 생성(괄호안은 핀번호)
FM=motor.Motor(11,22,27)
RM=motor.Motor(17,9,10)
FL=led.Led(4)
RL=led.Led(6)
##########실행##########
#출력100으로 전진
RM.motor(100)
#백색 led 켬
FL.on()
#적색 led 끔
RL.off()
#1초 대기
sleep(1)

#출력100으로 후진s
RM.motor(-100)
#백색 led 끔
FL.off()
#적색 led 켬
RL.on()
#1초 대기
sleep(1)
##########종료##########
FM.end()
RM.end()
FL.end()
RL.end()

GPIO.cleanup()
