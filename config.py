# -*- coding: utf-8 -*- 
#__author__='fanweiming'
#__time__ ='2018/4/19 16:29'

import os
# basedir = os.path.abspath(os.path.dirname(__file__))
# print basedir


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    BIG_DATA_PREFIX="node"
    REDIS_NODE="6"
    SPARK_NODE="1"
    KAFKA_NODE="1"
    HADOOP_NODE="1"
    LOGSTASH_NODE="4"
    TASK_LOG_DIR = r"C:\Users\fanweiming\Desktop\gansu\RTSP_URL\RTSP_List.txt"
    TASK_FAIL_LOG = r"C:\Users\fanweiming\Desktop\gansu\sensetime_scripts\fail.log"
    DATA_BASE_NAME="task"
    DATA_BASE_TABLE_NAME="statistics"
    HOST="127.0.0.1"
    SENSETIME_IP="62.0.50.116"






