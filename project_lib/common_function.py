#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

import project_lib.project_global as G
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommonFunction:

    def __init__(self):
        pass

    def get_element(self, el_dict, *args, **kwargs):
        """
        打包一些 driver 常用的 find_element 方法
        """
        el_type, el_value = [i for i in el_dict.items()][0]
        time_out = kwargs.get('time_out', 0)

        # 動態塞入指定字串到 xpath 中
        insert_string = kwargs.get('insert')
        if insert_string:
            el_value = el_value.format(insert_string)

        if el_type == "id":
            if time_out:
                el_obj = WebDriverWait(G.DRIVER, time_out).until(EC.visibility_of_element_located((By.ID, el_value)))
            elif 'list' in args:
                el_obj = G.DRIVER.find_elements_by_id(el_value)
            else:
                el_obj = G.DRIVER.find_element_by_id(el_value)
        elif el_type == "xpath":
            if time_out:
                el_obj = WebDriverWait(G.DRIVER, time_out).until(EC.visibility_of_element_located((By.XPATH, el_value)))
            elif 'list' in args:
                el_obj = G.DRIVER.find_elements_by_xpath(el_value)
            else:
                el_obj = G.DRIVER.find_element_by_xpath(el_value)
        else:
            return False

        return el_obj

    def swipe_screen(self, el_dict, direction, duration=200, **kwargs):
        """
        根據 direction 來滑動指定的 element
        """
        frame_rect = self.get_element(el_dict, **kwargs).rect
        if direction == 'up':
            G.DRIVER.swipe(frame_rect['x'] + frame_rect['width'] / 2, frame_rect['y'] + frame_rect['height'] * 0.9,
                           frame_rect['x'] + frame_rect['width'] / 2, frame_rect['y'] + frame_rect['height'] * 0.1, duration)
        elif direction == 'left':
            G.DRIVER.swipe(frame_rect['x'] + frame_rect['width'] * 0.9, frame_rect['y'] + frame_rect['height'] / 2,
                           frame_rect['x'] + frame_rect['width'] * 0.1, frame_rect['y'] + frame_rect['height'] / 2, duration)
        time.sleep(0.3)

    def print_screen(self, png_path):
        """
        全螢幕截圖, 並印出截圖路徑
        """
        G.DRIVER.get_screenshot_as_file(png_path)
        print(f'Screenshot: {png_path}')
