#!/usr/bin/env python
########################################################################
#This program is used to output the Rosbag file tf data for particular 
#joints to a csv file
#Author: Vishal Gaurav
#Date: 10/08/2015
########################################################################## 
import roslib
import rospy
import math
import tf
import rosbag
#import geometry_msgs.msg

i=1
if __name__ == '__main__':
	f=open("subset.csv",'w')
	if (f.closed):
		print "coudnot open file to read\n"
		#return -1
	rospy.init_node('openni_link',anonymous=True)
   # bag = rosbag.Bag('subset.bag')
	print "hi this is 1st value of i=%d" % (i)
	i=i+1
	header=['neck_2.x', 'neck_2.y', 'neck_2.z', 'right_shoulder_2.x', 'right_shoulder_2.y', 'right_shoulder_2.z', 'right_elbow_2.x',\
		'right_elbow_2.y', 'right_elbow_2.z', 'right_hand_2.x', 'right_hand_2.y', 'right_hand_2.z', 'right_hip_2.x',\
		'right_hip_2.y', 'right_hip_2.z', 'time']
	for j in range(len(header)):	
		if (j==len(header)):
			f.write(header[j]+'\n')
		else:
			f.write(header[j]+',')
	

	listener = tf.TransformListener()
	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():	
		try:
    			(trans,rot) = listener.lookupTransform('openni_depth_frame', 'neck_2',\
				      rospy.Time())
    			print "2 value of i=%d" % (i)
			i=i+1
			t=rospy.Time()
    		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			trans = [0, 0, 0]
    			continue
		try:
    			(trans1,rot1) = listener.lookupTransform('openni_depth_frame', 'right_shoulder_2',\
				      rospy.Time())
    			print "2 value of i=%d" % (i)
    			i=i+1
    		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			trans1 = [0, 0, 0]
    			continue
		try:
    			(trans2,rot2) = listener.lookupTransform('openni_depth_frame', 'right_elbow_2',\
				      rospy.Time())
    			print "2 value of i=%d" % (i)
    			i=i+1
    		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			trans2 = [0, 0, 0]
    			continue

		try:
    			(trans3,rot3) = listener.lookupTransform('openni_depth_frame', 'right_hand_2',\
				      rospy.Time())
    			print "2 value of i=%d" % (i)
    			i=i+1
    		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			trans3 = [0, 0, 0]
    			continue
		try:
    			(trans4,rot4) = listener.lookupTransform('openni_depth_frame', 'right_hip_2',\
				      rospy.Time())
    			print "2 value of i=%d" % (i)
    			i=i+1
    		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			trans4 = [0, 0, 0]
    			continue
        	#print "4 value of i=%d" % (i)
        	f.write("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%d\n"%(trans[0],trans[1],trans[2],trans1[0],trans1[1],trans1[2],trans2[0],trans2[1],\
			   trans2[2],trans3[0],trans3[1],trans3[2],trans4[0],trans4[1],trans4[2],t.secs))
		#print "trans= %f" %(trans[2])
        #print "10 value of i=%d" % (i)
		rate.sleep()
	   # openni_vel.publish(cmd)
  
            #rate.sleep()
	f.close()
