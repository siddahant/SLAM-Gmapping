#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    #define Targets
    Target_goles=[ 1 , -2  , -0.001,
              4.12923 , 3.4300 , -0.001,
              2.2576 , -4.3578 , -0.001,
              -4.2600 , 0.2623 ,-0.001,
              0.0029 , 0.0040 , -0.001] 
              
    for i in range(0,5):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = Target_goles[0+i*3]
        goal.target_pose.pose.position.y = Target_goles[1+i*3]
        goal.target_pose.pose.position.z = Target_goles[2+i*3]
        goal.target_pose.pose.orientation.w = 0.09012465928 
        goal.target_pose.pose.orientation.z = 0.098917586 

        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server DOWN ;/ ")
        else:
            print("{} Goal is Executed".format(i)) 
    return 1
if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("All Goals executed ")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation DONE ")