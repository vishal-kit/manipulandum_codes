#!/usr/bin/env python
import rosbag
bag = rosbag.Bag('subset.bag')
topics = bag.get_type_and_topic_info()[1].keys()
types = []
for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
     types.append(bag.get_type_and_topic_info()[1].values()[i][0])

print topics
print types
