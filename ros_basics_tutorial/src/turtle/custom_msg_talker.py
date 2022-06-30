#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from ros_basics_tutorial.msg import Info

def custom_talker():
    custom_msg_pub = rospy.Publisher('custom_msg', Info, queue_size=10)
    rospy.init_node('custom_msg_tallker', anonymous=True)
    rate = rospy.Rate(5)

    id = 1001
    name = 'Sanket'
    number = 3.14
    

    while not rospy.is_shutdown():
        info_msg = Info()
        info_msg.id = id
        info_msg.name = name
        info_msg.number = number
        custom_msg_pub.publish(info_msg)
        print(info_msg)
        id +=1
        number +=3.14
        rate.sleep()



if __name__ == '__main__':
    try:
        custom_talker()
    except rospy.ROSInterruptException:
        pass