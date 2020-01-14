#!/usr/bin/env bash

hdfs dfs -mkdir /data
hdfs dfs -put /home/cloudera/code/WUST-BDA/Big_data/resources/maelstrom.txt /data
hdfs dfs -put /home/cloudera/code/WUST-BDA/Big_data/resources/stopwords.txt /data
hdfs dfs -put /home/cloudera/code/WUST-BDA/Big_data/resources/digits.txt /data
