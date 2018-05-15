# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 17:43:40 2018

@author: fanweiming
"""

import json
import time

# %%
import requests
from config import Config

headers = {"ContentType": "application/x-www-form-urlencoded"}
# r=requests.post(url,headers=headers)
# response = json.loads(r.content.decode("utf-8"))
# print response

SENSETIME_IP = Config.SENSETIME_IP
#
log_dir = Config.TASK_LOG_DIR
fail_log = Config.TASK_FAIL_LOG
# log_dir="RTSP_List.txt"
# fail_log="fail.log"


def gen_single_url(camera_id, rtsp):
    return "http://" + SENSETIME_IP + "/stiva_vpa_vs_shuguang/cameraInfo/accept?cameraId=" \
           + camera_id + "&rtspUrl=" + rtsp


def get_camera_id(rtsp):
    camera_id = rtsp.split("/")[3]
    if len(camera_id) == 20:
        return camera_id
    else:
        print "wrong camera id!"



def gen_url_list(log1):
    url_list = []
    with open(log1, "r") as f:
        rtsp_list = f.readlines()
    length = len(rtsp_list)
    print "rtsp_list length is %d" % length
    for rtsp in rtsp_list:
        camera_id = get_camera_id(rtsp.rstrip("\n"))
        url_list.append(gen_single_url(camera_id, rtsp.rstrip("\n")))
    return url_list


def start_rtsp(b, log1):
    url_list = gen_url_list(log1)
    i = 0
    r_fail = []
    r_success=[]
    if b > len(url_list):
        b = len(url_list)
        print "total videos available is %d"%b
    for url in url_list[:b]:
        r = requests.post(url, headers=headers, timeout=None)
        print("== r.content %s ==" % r.content)
        response = json.loads(r.content.decode("utf-8"))
        print(response)
        if "0" != response["returnCode"]:
            r_fail.append(str(url))
            i += 1
        else:
            r_success.append(str(url))
    
    print "we have %d video failed !"%i
    print "we have %d video sucess !"%(b-i)
    f = open("fail.log", "w")
    f.write("\n".join(r_fail))
    f.close()
    f2=open("sucess.log","w")
    f2.write("\n".join(r_success))
    f2.close()
    return (len(url_list),len(r_success),len(r_fail))
    


def get_tasks():
    url = "http://" + SENSETIME_IP + "/stiva_vpa_vs_shuguang/taskList/query?type=2"
    r = requests.post(url, headers=headers, timeout=None)
    print(r.content.decode("utf-8"))
    response = json.loads(r.content.decode("utf-8"))
    return len(response["okList"]),len(response["failList"])


def delete_all():
    response = get_tasks()
    if "okList" in response:
        if response["okList"] is not None:
            for ok in response["okList"]:
                id1 = ok["taskId"]
                print("Deleting " + id1 + " ...")
                delete_task(id1)


def delete_task(id1):
    url = "http://" + SENSETIME_IP + "/stiva_vpa_vs_shuguang/task/delete"
    params = {
        "taskId": id1
    }
    r = requests.post(url, headers=headers, params=params, timeout=None)
    print("############")
    print(r.content.decode("utf-8"))
    print("############")
    response = json.loads(r.content.decode("utf-8"))
    print("############")
    print(response)


def start_one(rtsp):
    camera_id = rtsp.split("/")[3]
    print(camera_id)
    url = "http://" + SENSETIME_IP + "/stiva_vpa_vs_shuguang/cameraInfo/accept?cameraId=" \
          + camera_id + "&rtspUrl=" + rtsp
    r = requests.post(url, headers=headers, timeout=None)
    response = json.loads(r.content.decode("utf-8"))
    print(response)
    if "0" == response["returnCode"]:
        print("sucessful")


# startOne("rtsp://62.0.50.4:8556/62010260001320000511/1/main")
# startOne("rtsp://62.0.50.4:8556/62010260001320000781/1/main")
#fail_log = r"C:\Users\fanweiming\Desktop\gansu\sensetime_scripts\fail.log"


def try_again(log):
    f = open(log, "r")
    rtsp_list = [i.rstrip("\n") for i in f.readlines()]
    r_fail = []
    f.close()
    for i in rtsp_list:
        print i
        r = requests.post(i, headers=headers)
        print("== r.content %s ==" % r.content)
        response = json.loads(r.content.decode("utf-8"))
        print(response)
        if "0" == response["returnCode"]:
            print "sucessful !"
        else:
            r_fail.append(str(i))
    content="\n".join(r_fail)
    f1=open(log,"w")
    f1.write(content)
    f1.close()

"""
inside 60 minutes the script will continue to re start
"""


def main():
    start_rtsp(100,log_dir)
    start_time=time.time()
    while True:
        if time.time()-start_time < 600:
            with open(fail_log,"r") as f:
                content=f.readlines()
                if content:
                    try_again(fail_log)
        else:
            break

                


