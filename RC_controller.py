import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyautogui import *
from time import *

ip="192.168.1.168"
class Talker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CONTROLLER")
        self.setGeometry(1000,100,500,100)
        layout=QGridLayout()
        self.setLayout(layout)
        
        self.q_btn=QPushButton("HEADLIGHT")
        self.q_btn.pressed.connect(self.q_pressed)
        self.q_btn.released.connect(self.q_released)
        layout.addWidget(self.q_btn,0,0)
        
        self.w_btn=QPushButton("W")
        self.w_btn.pressed.connect(self.w_pressed)
        self.w_btn.released.connect(self.w_released)
        layout.addWidget(self.w_btn,0,1)
        
        self.a_btn=QPushButton("A")
        self.a_btn.pressed.connect(self.a_pressed)
        self.a_btn.released.connect(self.a_released)
        layout.addWidget(self.a_btn,1,0)
        
        self.s_btn=QPushButton("S")
        self.s_btn.pressed.connect(self.s_pressed)
        self.s_btn.released.connect(self.s_released)
        layout.addWidget(self.s_btn,1,1)
        
        self.d_btn=QPushButton("D")
        self.d_btn.pressed.connect(self.d_pressed)
        self.d_btn.released.connect(self.d_released)
        layout.addWidget(self.d_btn,1,2)
        
        self.cam_btn=QPushButton("CAM")
        self.cam_btn.pressed.connect(self.cam_pressed)
        layout.addWidget(self.cam_btn,2,0,1,3)
    
    def q_pressed(self):
        keyDown("q")
    def q_released(self):
        keyUp("q")
    
    def w_pressed(self):
        keyDown("w")
    def w_released(self):
        keyUp("w")
    
    def a_pressed(self):
        keyDown("a")
    def a_released(self):
        keyUp("a")
    
    def s_pressed(self):
        keyDown("s")
    def s_released(self):
        keyUp("s")
    
    def d_pressed(self):
        keyDown("d")
    def d_released(self):
        keyUp("d")
    
    def cam_pressed(self):
        os.system("gnome-terminal -x rqt_image_view")

if __name__=='__main__':
    hotkey("ctrl","alt","t")
    sleep(1)
    write("roscore")
    press("enter")
    
    hotkey("ctrl","shift","t")
    sleep(1)
    write("rosrun pub_sub_dialog talker")
    press("enter")
    
    hotkey("ctrl","shift","t")
    sleep(1)
    write("ssh ubuntu@"+ip)
    press("enter")
    sleep(1)
    write("turtlebot")
    press("enter")
    sleep(3)
    write("rosrun pub_sub_dialog listener")
    press("enter")
    
    hotkey("ctrl","shift","t")
    sleep(1)
    write("ssh ubuntu@"+ip)
    press("enter")
    sleep(1)
    write("turtlebot")
    press("enter")
    sleep(3)
    write("roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch")
    press("enter")
    
    window=QApplication(sys.argv)
    talker=Talker()
    talker.show()
    window.exec_()