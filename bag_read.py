#!/usr/bin/env python
import rosbag
bag = rosbag.Bag('subset.bag')
for topic, msg, t in bag.read_messages(topics=['/tf']):
    print msg
bag.close()
