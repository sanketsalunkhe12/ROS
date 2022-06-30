#!/usr/bin/env python3

from ast import AnnAssign
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    print('I got data')

def teleop_listener():
    rospy.init_node('teleop_listener', anonymous=True)
    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    teleop_listener()