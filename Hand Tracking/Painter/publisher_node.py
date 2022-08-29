#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from tutorials.msg import Position

def talk_to_me():
    pub = rospy.Publisher('talking_topic', Position, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messages...")
    while not rospy.is_shutdown():
        msg = Position()
        msg.message = "my Position is : "
        msg.x = 5.0
        msg.y = 10
        pub.publish(msg)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass