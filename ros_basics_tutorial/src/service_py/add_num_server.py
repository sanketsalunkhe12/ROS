#!/usr/bin/env python3

from ros_basics_tutorial.srv import AddNum
from ros_basics_tutorial.srv import AddNumRequest
from ros_basics_tutorial.srv import AddNumResponse

import rospy
import time

# create a service

def handle_add_num(data):
    print('Returning {} + {} = {}'.format(data.a, data.b, (data.a + data.b)))
    return AddNumResponse(data.a + data.b)

def add_two_num():
    rospy.init_node('AddTwoNum')
    s = rospy.Service('AddTwoNum', AddNum, handle_add_num)
    #(Service name, Service type, callback function to handle operation)

    print('Ready to add two ints')
    rospy.spin()

if __name__=="__main__":
    add_two_num()