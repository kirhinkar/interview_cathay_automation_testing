#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

global APPIUM_SERVER_IP  # Appium connection setting
global APPIUM_SERVER_PORT
global DEVICE_INFO
global DRIVER
global DIR_REPORT_PATH


def global_initialize():

    global APPIUM_SERVER_IP
    global APPIUM_SERVER_PORT
    global DEVICE_INFO
    global DIR_REPORT_PATH

    APPIUM_SERVER_IP = ''
    APPIUM_SERVER_PORT = '4723'

    DEVICE_INFO = {
        "DefName": "",
        "udid": "",
        "deviceName": "",
        "platformName": "Android",
        "platformVersion": "",
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main",
        "noReset": True,
        "dontStopAppOnReset": True,
        "newCommandTimeout": 1000,
    }

    # 檢查設定
    if not APPIUM_SERVER_IP:
        raise Exception(f'"APPIUM_SERVER_IP" is not set. Please check the README.md. ')
    for i in ('DefName', 'udid', 'deviceName', 'platformName', 'platformVersion'):
        if not DEVICE_INFO.get(i):
            raise Exception(f'desired_capabilities["{i}"] is not set. Please check the README.md. ')

    # Define the report directory path
    DIR_REPORT_PATH = os.path.join('report', f'[{time.strftime("%Y%m%d_%H%M%S")}]')
    if not os.path.isdir(DIR_REPORT_PATH):
        os.mkdir(DIR_REPORT_PATH)
