#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver import Chrome

GAME_URL = 'https://tbot.xyz/math/#eyJ1IjoyNTU5ODMwOTAsIm4iOiJTbWwgSnpuIiwiZyI6Ik1hdGhCYXR0bGUiLCJjaSI6IjI3ODM4Mjc0MzI5MTU1MzY2NTAiLCJpIjoiQVFBQUFDMEpBQUFKeTM0Si0xM1J5ZDlYX1I0In03YzE3ZDBmYmYwODNjN2ZlNjgwMmY3Y2U4ZmIxMmU0YQ==&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3Dckn64YT1Rhfr_naISt_bIeVgBCQAMGKvcotrfYBxDtE'
WEBDRIVER_PATH = '/home/test/Downloads/chromedriver'
NUMBER_OF_WINS = 246

browser = Chrome(WEBDRIVER_PATH)
browser.get(GAME_URL)

#Start game
button = browser.find_element_by_id("button_correct")
button.click()

#Play 
i =0
while i<NUMBER_OF_WINS:
    task_x = int(browser.find_element_by_id("task_x").text.encode('utf8', 'ignore').strip())
    task_op = browser.find_element_by_id("task_op").text.encode('utf8', 'ignore')
    task_y = int(browser.find_element_by_id("task_y").text.encode('utf8', 'ignore'))
    task_res = int(browser.find_element_by_id("task_res").text.encode('utf8', 'ignore').strip())
    print 'X:%d OP:%s Y:%d RES: %d'% (task_x, task_op,task_y,task_res)

    result = -1
    if task_op=="/":
        result = task_x / task_y
    if task_op=="+":
        result = task_x + task_y
    if task_op=="–":
        result = task_x - task_y
    if task_op=="×":
        result = task_x * task_y
    
    print result
    button_wrong = button = browser.find_element_by_id("button_wrong")
    button_correct = button = browser.find_element_by_id("button_correct")
    if result==task_res:
        button_correct.click()
    else:
        button_wrong.click()
    browser.implicitly_wait(1)
    i=i+1
