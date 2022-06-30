#!/usr/bin/env python3

from random import triangular
import rospy
from geometry_msgs.msg import Twist


def pose_description(data):
    print('The pose of turtle bot is {}'.format(data.data))

def turtle_control():
    velocity_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_move_py', anonymous=True)
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        turtle_twist = Twist()
        turtle_twist.linear.x = 2.0
        velocity_pub.publish(turtle_twist)
        rate.sleep()
        turtle_twist.linear.x = -2.0
        velocity_pub.publish(turtle_twist)
        rate.sleep()



if __name__ == '__main__':
    try:
        turtle_control()
    except rospy.ROSInterruptException:
        pass


