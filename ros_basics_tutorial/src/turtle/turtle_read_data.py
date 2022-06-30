#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(data):
    print('The x data is {} \n'.format(data.x))
    print('The y data is {} \n'.format(data.y))
    print('The theta data is {} \n'.format(data.theta))
    print('The angular velocity data is {} \n'.format(data.angular_velocity))
    print('The linear velocity data is {} \n'.format(data.linear_velocity))


def turtle_data_listener():
    rospy.init_node('turtle_data_listener', anonymous=True)
    rospy.Subscriber('turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == "__main__":
    turtle_data_listener()
