#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from rospy_message_converter import message_converter
import socket,json,ast,collections
import threading,os

def convert(data):
    if isinstance(data,basestring):
        return str(data)
    elif isinstance(data,collections.Mapping):
        return dict(map(convert,data.iteritems()))
    elif isinstance(data,collections.Iterable):
        return type(data)(map(convert,data))
    else:
        return data

def listener():
    sock1 = socket.socket(socket.AF_INET,sockett .SOCK_DGRAM)
    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock1.bind((os.environ['ros_serialize_receive_ip'],8080))
    sock2.bind((os.environ['ros_serialize_receive_ip'],8081))
    rospy.init_node('listener', anonymous=True)
    pub1 = rospy.Publisher('realsense_pose_data',PoseStamped,queue_size=100)
    pub2 = rospy.Publisher('pixhawk_pose_data',PoseStamped,queue_size=100)
    # pub1 = rospy.Publisher('realsense_pose_data',Odometry,queue_size=100)
    # pub2 = rospy.Publisher('pixhawk_pose_data',Odometry,queue_size=100)
    def callback(sock,pub):
        while(True):
            data,_ = sock.recvfrom(1000)
            dic = json.loads(data.decode())
            a = message_converter.convert_dictionary_to_ros_message("geometry_msgs/PoseStamped",convert(dic))
            # a = message_converter.convert_dictionary_to_ros_message("nav_msgs/Odometry",convert(dic))
            pub.publish(a)
    t1 = threading.Thread(target=callback,args=(sock1,pub1))
    t2 = threading.Thread(target=callback,args=(sock2,pub2))
    t1.start()
    t2.start()

def script():
    try:
        listener()
    except rospy.ROSInternalException:
        rospy.logerr("ROSInternalException")
        pass

