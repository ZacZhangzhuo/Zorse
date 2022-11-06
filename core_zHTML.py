__author__ = ["Zac Zhuo Zhang"]
__copyright__ = "Copyright 2022"
__license__ = "MIT License"
__email__ = ["<Arch.Z@outlook.com>"]

import os
import datetime


def ModificationDate(filePath):
    """
    Get the modification date of the file
    """
    t = os.path.getmtime(filePath)
    return datetime.datetime.fromtimestamp(t).replace(microsecond=0)


def IsOnTime(startTime, endTime, Minutes=5):
    """
    Exam if the interval between the startTime ans endTime is less than the minutes
    """
    d_start = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    # print(d_start)
    d_end = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    # thresholdInHour = datetime.datetime.strptime(thresholdInHour, "%Y-%m-%d %H:%M:%S")
    result = d_start + datetime.timedelta(minutes=Minutes) > d_end
    # print(result)
    return result


def IsRecentFile(filePath, RecentMinutes=5):
    """
    Exam if the file is recently (RecentMinutes ago) changed
    """
    t = os.path.getmtime(filePath)
    t = datetime.datetime.fromtimestamp(t).replace(microsecond=0)
    return IsOnTime(str(t), str(datetime.datetime.now().replace(microsecond=0)), RecentMinutes)