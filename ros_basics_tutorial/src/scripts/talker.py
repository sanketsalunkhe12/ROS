#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker_py', anonymous=True)
    rate = rospy.Rate(5)

    count = 0
    while not rospy.is_shutdown():
        hello_str = "Hello world {}".format(count)
        count+=1
        #rospy.loginfo(hello_str)
        print(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass