#!/usr/bin/env python3

from ros_basics_tutorial.srv import AddNum
from ros_basics_tutorial.srv import AddNumRequest
from ros_basics_tutorial.srv import AddNumResponse

import rospy

import sys

def add_two_nums(x, y):
    rospy.wait_for_service('AddTwoNum')
    # it will wait client untill service is alive

    try:
        AddTwoNum = rospy.ServiceProxy('AddTwoNum', AddNum)
        # ServiceProxy is an alternative name for client
        # AddTwoNum is the service name which should match with name on Server side
        # AddNum is the server type

        resp = AddTwoNum(x,y)
        return resp.sum
    except rospy.ServiceException as e:
        print('Service Call Failed %s'%e)


if __name__=="__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print('Requesting {}+{}'.format(x, y))
    s = add_two_nums(x, y)
    print("{} + {} = {}".format(x, y, s))   