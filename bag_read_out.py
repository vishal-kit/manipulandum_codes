#!/usr/bin/env python
import rosbag

fp= open('data.txt',w)
if (!fp):
    print "coudnot open file to write."

bag = rosbag.Bag('subset.bag')
for topic, msg, t in bag.read_messages(topics=['/tf']):
#    print msg
     
bag.close()
