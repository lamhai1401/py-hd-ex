#!/usr/bin/env python

import sys

# Read each line from STDIN
for line in sys.stdin:

    # Get the words in each line
    words = line.split()

    # Generate the count for each word
    for word in words:

        # Write the key-value pair to STDOUT to be processed by the reducer.
        # The key is anything before the first tab character and the value is
        # anything after the first tab character.
        print ('{0}\t{1}'.format(word, 1))

# hadoop jar $HADOOP_HOME/libexec/share/hadoop/tools/lib/hadoop-streaming*.jar     -files mapper.py,reducer.py     -mapper mapper.py     -reducer reducer.py     -input /input  -output ./output

# export HADOOP_HDFS_HOME=$HADOOP_HOME
