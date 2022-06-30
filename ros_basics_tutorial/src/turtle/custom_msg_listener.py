#!/usr/bin/env python3

import rospy
from ros_basics_tutorial.msg import Info
from std_msgs.msg import _String

def callback(data):
    print('I got data, Id: {}, name: {}, number: {}'.format(data.id,
                data.name, data.number))

def custom_listener():
    rospy.init_node('custom_msg_listener', anonymous=True)
    rospy.Subscriber('custom_msg', Info, callback)
    rospy.spin()

if __name__ == '__main__':
    custom_listener()