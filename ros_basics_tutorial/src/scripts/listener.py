#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard {}".format(data.data))
    print('I also heard {}'.format(data.data))

    #rospy.loginfo() also prints but it includes login info with it.

def listener():
    rospy.init_node('listener_py', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()



    