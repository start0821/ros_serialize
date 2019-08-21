#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from rospy_message_converter import message_converter
import socket
import json,os

def listener():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def callback1(data):
        dic = message_converter.convert_ros_message_to_dictionary(data)
        a = json.dumps(dic)
        sock.sendto(a.encode(),(os.environ['ros_serialize_receive_ip'],8080))
    def callback2(data):
        dic = message_converter.convert_ros_message_to_dictionary(data)
        a = json.dumps(dic)
        sock.sendto(a.encode(),(os.environ['ros_serialize_receive_ip'],8081))
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/mavros/vision_pose/pose',PoseStamped,callback1)
    rospy.Subscriber('/mavros/local_position/pose',PoseStamped,callback2)
    # rospy.Subscriber('/camera/odom/sample',Odometry,callback1)
    # rospy.Subscriber('/mavros/local_position/odometry',Odometry,callback2)
    rospy.spin()

def script():
    try:
        listener()
    except rospy.ROSInternalException:
        rospy.logerr("ROSInternalException")
        pass

