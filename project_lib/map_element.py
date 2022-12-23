#!/usr/bin/python
# -*- coding: UTF-8 -*-


class EL:
    CHROME_SEARCH_EDITTEXT = {
        "xpath": '//*[@resource-id="com.android.chrome:id/url_bar" or @resource-id="com.android.chrome:id/search_box_text"]',
    }
    MENU_BTN = {
        'xpath': '//*[@resource-id="lnk_MyBankLink"]/parent::android.view.View/preceding-sibling::android.view.View',
    }
    CATEGORY_PRODUCT_INTRODUCTION = {
        'xpath': '//android.view.View/android.view.View/android.widget.TextView[@text="產品介紹"]',
    }
    CREDICT_CARD_TITLE = {
        'xpath': '//android.view.View/android.view.View/android.widget.TextView[@text="信用卡"]',
    }
    CREDICT_CARD_ITEMS = {
        'xpath': '//android.widget.TextView[@text="信用卡"]/following-sibling::android.view.View[@resource-id="lnk_Link"]/android.widget.TextView',
    }
    CREDICT_CARD_ITEM_FRAME = {
        'xpath': '//android.widget.TextView[@text="信用卡"]/following-sibling::android.view.View[1]/parent::android.view.View',
    }
    CREDICT_CARD_INTRO_PAGE_FRAME = {
        'xpath': '//android.widget.FrameLayout/android.webkit.WebView',
    }
    CREDICT_CARD_INTRO_PAGE_TITLE = {
        'xpath': '//android.view.View[@resource-id="lnk_MajorButtonLink"]/parent::android.view.View/parent::android.view.View/'
                 'parent::android.view.View/preceding-sibling::android.view.View/android.widget.TextView[@text="信用卡介紹"]',
    }
    CREDICT_CARD_INTRO_MENU_FRAME = {
        'xpath': '//android.view.View[@resource-id="lnk_ButtonLink"]/parent::android.view.View/preceding-sibling::android.view.View',
    }
    CREDICT_CARD_INTRO_MENU_TITLES = {
        'xpath': '//android.view.View[@resource-id="lnk_ButtonLink"]/parent::android.view.View/preceding-sibling::android.view.View'
                 '/android.view.View/android.view.View/android.view.View/android.widget.TextView',
    }
    WEB_DISABLED_CARDS = {
        'xpath': '//div[@class="cubre-a-iconTitle__text" and text()="{}"]/ancestor::div[@class="cubre-o-block__wrap"]'
                 '/div[@class="cubre-o-block__component"]//div[@class="cubre-m-compareCard__title"]'
    }
