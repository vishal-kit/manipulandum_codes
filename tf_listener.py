#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import rosbag
import geometry_msgs.msg

i=1
if __name__ == '__main__':
    rospy.init_node('tf_link')
    bag = rosbag.Bag('subset.bag')
    print "hi this is 1st value of i=%d" % (i)
    i=i+1
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():	
    	try:
    	   (trans,rot) = listener.lookupTransform('head_2', 'openni_depth_frame', rospy.Time())
    	   print "7 value of i=%d" % (i)
    	   i=i+1
    	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
	   print "8 value of i=%d" % (i)
    	   continue
        print "9 value of i=%d" % (i)
        #i=i+1
        #angular = 4 * math.atan2(trans[1], trans[0])
        #linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        #print "9 value of i=%d" % (i)
        #i=i+1
	    #cmd = tf.msg.Transform()
           # cmd.linear.x = linear
           # cmd.angular.z = angular
	print "trans= %f" %(trans[2])
        #print "10 value of i=%d" % (i)
        
	rate.sleep()
	   # openni_vel.publish(cmd)
  
            #rate.sleep()
    bag.close()
