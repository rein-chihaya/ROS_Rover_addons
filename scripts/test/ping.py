#!/usr/bin/env python
#  send a ping message to /chatter topic in ROS
import rospy
from std_msgs.msg import String

def ping():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        ping()
    except rospy.ROSInterruptException:
        pass
