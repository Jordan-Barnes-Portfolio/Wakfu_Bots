# -*- coding: utf-8 -*-
"""
@author: Jordan
"""

import cv2 as cv
from windowcapture import WindowCapture
from vision import Vision
import pyautogui as pg
import time
from threading import Thread
import numpy as np
import win32gui, win32ui, win32con

# initialize the WindowCapture class
wincap = WindowCapture('WAKFU')
# initialize the Vision class
vision_mineral = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/Mineral.JPG')
vision_side_mineral = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/SideMinCheck.JPG')

#initialize mine icon
vision_mine_icon = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/mineIcon.JPG')
#global to define thread actions
vision_wait_icon = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/ProgressBarCheck.JPG')
#initialize the copper_icon
vision_mineral_icon = Vision("C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/SyanideOreCheck.JPG")




global click_history
click_history = []
global bot_in_action
bot_in_action = False
global search_vectors
search_vectors = ['right', 'down', 'left', 'up']

def bot_actions(rectangles):
       
    
    global bot_in_action
    global click_history
# =============================================================================
#     
#     wait_icon = vision_wait_icon.find(screenshot, 0.70)
# =============================================================================
    
    def get_window_size_here(window_name):
        
        hwnd = win32gui.FindWindow(None, "WAKFU")
        window_rect = win32gui.GetWindowRect(hwnd)
        
        w = window_rect[2] - window_rect[0]
        h = window_rect[3] - window_rect[1]
        
        win_x =window_rect[0]
        win_y = window_rect[1]
        
        return(w, h, win_x, win_y)
        
    def check_if_c_target():
        
        check_icon = vision_mineral_icon.find(screenshot, 0.65)
        time.sleep(0.1)
        c_targets = Vision.get_click_points(screenshot, check_icon)
        
        return True if c_targets else False
    
    def search(search_vector):
        global bot_in_action
        
        # get the window size
        h = get_window_size_here("WAKFU")[1] / 2
        w = get_window_size_here("WAKFU")[0] / 2
                
        #get the window pos
        win_x = get_window_size_here("WAKFU")[2]
        win_y = get_window_size_here("WAKFU")[3]
    
                
        my_pos = (win_x + w, win_y + h)
        
        if search_vector == 'right':
            pg.moveTo(my_pos[0]+300, my_pos[1] + 375)
            pg.click()
            time.sleep(1.5)
        
        elif search_vector == 'down':
           pg.moveTo(my_pos[0]-300, my_pos[1] - 375)
           pg.click()
           time.sleep(1.5)
            
        elif search_vector == 'left':
            pg.moveTo(my_pos[0] - 250, my_pos[1])
            pg.click()
        
        elif search_vector == 'up':
            pg.moveTo(my_pos[0] + 250, my_pos[1])
            pg.click()
            
        time.sleep(4)
            
        screenshot = wincap.get_screenshot()
        rectangles = vision_mineral.find(screenshot, 0.61)
        targets = Vision.get_click_points(screenshot, rectangles)
        
        time.sleep(2)

        if(targets):
            print("target found")
            bot_in_action = False
            
        
        print(my_pos)
        
    
    def click_backtrack(click_history):
        
        global bot_in_action
        
        # get the window size
        h = get_window_size_here("WAKFU")[1] / 2
        w = get_window_size_here("WAKFU")[0] / 2
                
        #get the window pos
        win_x = get_window_size_here("WAKFU")[2]
        win_y = get_window_size_here("WAKFU")[3]
    
                
        my_pos = (win_x + w, win_y + h)
        
        
        if(click_history):
            
            for click in range(len(click_history)):
                last_click = click_history.pop()
                
                m_x = my_pos[0] - (last_click[0] - my_pos[0])
                m_y = my_pos[1] - (last_click[1] - my_pos[1])
                
                pg.moveTo(x=m_x, y=m_y)
                pg.click()
                
                time.sleep(4)
                
                screenshot = wincap.get_screenshot()
                rectangles = vision_mineral.find(screenshot, 0.61)
                targets = Vision.get_click_points(screenshot, rectangles)
                
                time.sleep(2)

                if(targets):
                    print("target found")
                    bot_in_action = False
                    break
                    

        elif(not click_history):
            print("no click history")
            print("looking for ore..")
            time.sleep(4)
    
    
    bot_in_action = True
    #bot actions in a seperate thread  
    
    if len(rectangles) > 0:
        
        print("start")

        time.sleep(0.5)
        
        targets = Vision.get_click_points(screenshot, rectangles)
        target = wincap.get_screen_position(targets[0])
    
        #move cursor to mineral location
        pg.moveTo(x=target[0], y=target[1])
        
        time.sleep(0.2)
        
        
        
        if(check_if_c_target()):
            
            time.sleep(0.2)
            print("confirmed target")
            pg.click(button="right")
            
            click_position = (target[0], target[1])
            click_history.append(click_position)
       
            time.sleep(0.2)
                        
            mine_icon = vision_mine_icon.find(screenshot, 0.58)
            
            m_targets = Vision.get_click_points(screenshot, mine_icon)
            time.sleep(0.1)
            m_target = wincap.get_screen_position(m_targets[0])   
                
            pg.moveTo(x=m_target[0], y=m_target[1])
            pg.click()
            
            time.sleep(0.1)
            
            time.sleep(10)
            
            
        
# =============================================================================
#         elif(not check_if_c_target()):
# 
#             for target2 in targets:
#                 
#                 time.sleep(0.1)
#                 #move cursor to mineral location
#                 target2 = wincap.get_screen_position(target2)
#                 pg.moveTo(x=target2[0], y=target2[1])
#                 
#                 time.sleep(0.1)
#                 
#                 if(check_if_c_target()):
#                     
#                     time.sleep(0.2)
#                     print("confirmed target")
#                     pg.click(button="right")
#                     
#                     click_position = (target2[0], target2[1])
#                     click_history.append(click_position)
#                
#                     time.sleep(0.2)
#                                 
#                     mine_icon = vision_mine_icon.find(screenshot, 0.57)
#                     
#                     m_targets = Vision.get_click_points(screenshot, mine_icon)
#                     time.sleep(0.1)
#                     
#                     m_target = wincap.get_screen_position(m_targets[0])   
#                         
#                     pg.moveTo(x=m_target[0], y=m_target[1])
#                     pg.click()
#     
#                     while(len(wait_icon) == 0):
#                         
#                         print("Checking (In Loop)")
#                         
#                         time.sleep(0.5)
#                         wait_icon = vision_wait_icon.find(screenshot, 0.87)
#                         
#                     
#                     time.sleep(5.2)
#                     print("end loop")
#                     wait_icon = wait_icon.tolist()
#                     wait_icon.clear()
#                     break
#                 
#                 else:
#                     print("not a target")
# =============================================================================
     
            
    if(len(rectangles) == 0):
        last_search_vector = search_vectors.pop(0)
        search_vectors.append(last_search_vector)
        search(last_search_vector)
# =============================================================================
#         print(click_history)
#         click_backtrack(click_history)
# =============================================================================
        
    
    bot_in_action = False
    
        
while(True):
    
    #@TODO
    #Implement pathing algorithm and path for character to run.
    # this could possibly be done with a backtracking algorithm.. look up how to mirror
    # clicks.. its in the opencv video we watched earlier with the guy that has a messed up eye.    
    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    
    # do mineral detection
    rectangles = vision_mineral.find(screenshot, 0.59)
    check_icon = vision_mineral_icon.find(screenshot, 0.65)
    side_min = vision_side_mineral.find(screenshot, 0.69)
    
# =============================================================================
#     copper_icon = vision_copper_icon.find(screenshot, 0.69)
#     
#     rectangles = np.concatenate((rectangles, copper_icon))
# =============================================================================

    wait_icon = vision_wait_icon.find(screenshot, 0.87)
    rectangles = np.concatenate((rectangles, wait_icon, check_icon, side_min))

    # draw the detection results onto the original image
    output_image = vision_mineral.draw_rectangles(screenshot, rectangles)

    
    if not bot_in_action:
        t = Thread(target=bot_actions, args=(rectangles,))
        t.start()

    cv.imshow('Matches', output_image)
    
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')



#previous detection protocol
# =============================================================================
# #Check if threshold is met, then define the image by a rectangone on your screen.
# if(max_val >= threshold):
#     
#     mineral_w = mineral_img.shape[1]
#     mineral_h = mineral_img.shape[0]
#     
#     top_left = max_loc
#     
#     bottom_right = (top_left[0] + mineral_w, top_left[1] + mineral_h)
#     
#     cv.rectangle(screen_img, top_left, bottom_right,
#                  color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
#     
#     
#     #to show image with rectangles uncomment this 
#     #cv.imshow('Result', screen_img)
#     #cv.waitKey()
#     
#     
# else:
#     print("Error: no mineral found")
#     #TODO add path here so that when no mineral is found, character continues looking for one
#     
# =============================================================================

#possibly how to grab new icons?
# =============================================================================
#         #wait 1 seconds
#         time.sleep(2)
#         
#         screenshot2 = wincap.get_screenshot()
#         
#         #detect option to mine icon
#         mine_targets = Vision.get_click_points(screenshot2, mine_icon)
#         mine_target = wincap.get_screen_position(mine_targets)
#         
#         time.sleep(2)
#         
#         pg.moveTo(x=mine_target[0], y=mine_target[1])
#         pg.click()
#         
#         #detect loading bar.
#         targets = Vision.get_click_points(screenshot, loading_icon)
#         target = wincap.get_screen_position(targets)
# =============================================================================