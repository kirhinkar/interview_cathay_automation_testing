#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import time

from appium import webdriver
import project_lib.project_global as G
from project_lib.map_element import EL
from project_lib import common_function


def main():

    print('Step 0: Driver remoting...')
    # 建立 driver & start remote
    G.global_initialize()
    appium_server_url = f"http://{G.APPIUM_SERVER_IP}:{G.APPIUM_SERVER_PORT}/wd/hub"
    G.DRIVER = webdriver.Remote(appium_server_url, desired_capabilities=G.DEVICE_INFO)
    cm = common_function.CommonFunction()

    print('Step 1: 進入官網並截圖')
    # 輸入網址並 enter (換行)
    cm.get_element(EL.CHROME_SEARCH_EDITTEXT, time_out=10).click()
    cm.get_element(EL.CHROME_SEARCH_EDITTEXT, time_out=3).send_keys('https://www.cathaybk.com.tw/cathaybk/' + r'\n')
    # 等待 Menu 選單出現後, 截圖
    menu_btn = cm.get_element(EL.MENU_BTN, time_out=10)
    cm.print_screen(os.path.join(G.DIR_REPORT_PATH, 'step_1_screenshot.png'))

    print('Step 2: 進入信用卡列表, 計算項目並截圖')
    # 依序點擊 個人金融 > 產品介紹 > 信用卡列表
    menu_btn.click()
    cm.get_element(EL.CATEGORY_PRODUCT_INTRODUCTION, time_out=3).click()
    cm.get_element(EL.CREDICT_CARD_TITLE, time_out=3).click()
    time.sleep(1)

    # 計算目前信用卡項目, 並向上滑動螢幕. 如沒有新增的項目則跳出 loop
    credit_card_item_list = []
    card_introduction_el = None
    for _ in range(10):
        count_added_item = 0
        item_el_list = cm.get_element(EL.CREDICT_CARD_ITEMS, 'list')
        for item_el in item_el_list:
            item_text = item_el.get_attribute('text')
            if item_text == '卡片介紹':
                card_introduction_el = item_el  # pre-store the element '卡片介紹' for step 3

            if item_text not in credit_card_item_list:
                credit_card_item_list.append(item_text)
                count_added_item += 1
        else:
            if count_added_item:
                cm.swipe_screen(EL.CREDICT_CARD_ITEM_FRAME, 'up')
            else:
                break

    print(f'Count of credict card item = {len(credit_card_item_list)}: {credit_card_item_list}')
    cm.print_screen(os.path.join(G.DIR_REPORT_PATH, 'step_2_screenshot.png'))

    print('Step 3: 計算頁面上所有(停發)信用卡數量並截圖')
    # 等待進入信用卡介紹 page
    card_introduction_el.click()
    cm.get_element(EL.CREDICT_CARD_INTRO_PAGE_TITLE, time_out=10)

    # 持續滑動卡片介紹頁面的 menu bar, 直到 "停發卡" 選項出現為止
    target_text = '停發卡'
    for _ in range(10):
        cm.swipe_screen(EL.CREDICT_CARD_INTRO_MENU_FRAME, 'left')
        card_intro_menu_titles = cm.get_element(EL.CREDICT_CARD_INTRO_MENU_TITLES, 'list')
        card_intro_menu_title_texts = [(i, i.get_attribute('text')) for i in card_intro_menu_titles if i.get_attribute('text') == target_text]
        if card_intro_menu_title_texts:
            card_intro_menu_title_texts[0][0].click()
            break

    # 撈取目前顯示的停發卡名稱並截圖. 持續左划螢幕, 直到沒有新的停發卡出現才跳出 loop
    stored_card_list = []
    G.DRIVER.switch_to.context('WEBVIEW_chrome')
    for _ in range(50):
        disabled_cards = cm.get_element(EL.WEB_DISABLED_CARDS, 'list', insert=target_text)
        current_card = [el for el in disabled_cards if el.is_displayed()][0]
        if current_card.text not in stored_card_list:
            stored_card_list.append(current_card.text)
            cm.print_screen(os.path.join(G.DIR_REPORT_PATH, f'step_3_{current_card.text}.png'))

            G.DRIVER.switch_to.context('NATIVE_APP')
            cm.swipe_screen(EL.CREDICT_CARD_INTRO_PAGE_FRAME, 'left', insert=target_text)
            G.DRIVER.switch_to.context('WEBVIEW_chrome')
        else:
            break

    print(f'Count of disabled card = {len(stored_card_list)}: {stored_card_list}')

    # 計算停發卡的截圖數量
    card_screenshot_path_list = [os.path.join(G.DIR_REPORT_PATH, i) for i in os.listdir(G.DIR_REPORT_PATH) if i.startswith('step_3')]
    print(f'Count of disabled card screenshot = {len(card_screenshot_path_list)}: ')
    for i in card_screenshot_path_list:
        print(i)

    # 檢查儲存的卡片數量與截圖的數量一致
    assert len(stored_card_list) == len(card_screenshot_path_list)

    # Quite driver
    G.DRIVER.quit()


if __name__ == '__main__':

    main()
