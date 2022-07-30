# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:17:03 2022
@author: Jordan
"""

import cv2 as cv
# =============================================================================
# from windowcapture import WindowCapture
# from vision import Vision
# import numpy as np
# 
# =============================================================================


# =============================================================================
# class MiniGame_Logic:
#     
#     wincap = WindowCapture("WAKFU")
#     
#     vone = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/1.JPG')
#     vtwo = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/2.JPG')
#     vthree = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/3.JPG')
#     vfour = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/4.JPG')
#     vfive = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/5.JPG')
#     vsix = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/6.JPG')
#     vseven = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/7.JPG')
#     veight = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/8.JPG')
#     
#     screenshot = wincap.get_screenshot()
#     
#     one = vone.find(screenshot, 0.8)
#     two = vtwo.find(screenshot, 0.8)
#     three = vthree.find(screenshot, 0.70)
#     four = vfour.find(screenshot, 0.70)
#     five = vfive.find(screenshot, 0.70)
#     six = vsix.find(screenshot, 0.70)
#     seven = vseven.find(screenshot, 0.70)
#     eight = veight.find(screenshot, 0.70)
#     
#     
#     def actions_to_take():
#         
#         vglyph = Vision('C:/Users/Jordan/Desktop/Wakfu_Bot/Mining_bot/Resources/GlyphOfDestruction.JPG')
# 
#             
#             
#     
#     
#     while(True):
#         
#         screenshot = wincap.get_screenshot()
#         
#         rectangles = np.concatenate((one, two, three, four, five, six, seven, eight))
#         
#         output_image = vone.draw_rectangles(screenshot, rectangles)
#         
#         
#         
#         if cv.waitKey(1) == ord('q'):
#             cv.destroyAllWindows()
#             break
#         
#         cv.imshow('Matches', output_image)
# =============================================================================
