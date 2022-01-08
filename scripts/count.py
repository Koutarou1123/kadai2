#!/usr/bin/env python3
"""
BSD 2-Clause License
Copyright(c)2022 Ryuichi Ueda.All right reserved.
"""

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up',Int32,queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
