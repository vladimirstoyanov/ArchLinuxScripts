import cv2
import numpy as np
from matplotlib import pyplot as plt
import autopy
import time
import math
import random

def get_screenshot():
  autopy.bitmap.capture_screen().save('screenshot.png')

def mouse_click(x,y):
  width, height = autopy.screen.get_size()
  if (width<=x or x<0 or height<=y or y<0):
    print "Error: def mouse_move(x,y): if (width<=x or x<0 or height<=y or y<0):"
    return 
  autopy.mouse.smooth_move(x,y)
  time.sleep(random.randint(1,100)/100.0) ## 0,1 to 1 seconds
  autopy.mouse.click()
  
def calculate_right_coordinates(coordinates, right_coordinates):
  tol=5
  
  if (len(right_coordinates)== 0):
    right_coordinates.append([])
    right_coordinates[0].append(coordinates)
    #print "if:" + str(right_coordinates)
    return right_coordinates
  
  for i in range (len(right_coordinates)):
      if (math.fabs(right_coordinates[i][0][0][0]-coordinates[0][0]) <= tol or math.fabs(right_coordinates[i][0][0][1]-coordinates[0][1]) <= tol or math.fabs(right_coordinates[i][0][1][0]-coordinates[1][0]) <= tol or math.fabs(right_coordinates[i][0][1][1]-coordinates[1][1]) <= tol):
	right_coordinates[i].append(coordinates)
	return right_coordinates
  
  right_coordinates.append([])
  right_coordinates[len(right_coordinates)-1].append(coordinates)
  return right_coordinates
  
def contains_image(base_image, template_image):
  print "image:" + template_image
  right_coordinates=[]
  coordinates = []
  img = cv2.imread(base_image,0)
  img2 = img.copy()
  template = cv2.imread(template_image,0)
 
  w, h = template.shape[::-1]

  # All the 6 methods for comparison in a list
  methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
	      'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

  for meth in methods:
      img = img2.copy()
      method = eval(meth)

      # Apply template Matching
      res = cv2.matchTemplate(img,template,method)
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

      # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
      if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
	  top_left = min_loc
      else:
	  top_left = max_loc
      bottom_right = (top_left[0] + w, top_left[1] + h)      
      
      coordinates = []
      coordinates.append(top_left)
      coordinates.append(bottom_right)
      #print coordinates
      right_coordinates = calculate_right_coordinates(coordinates, right_coordinates)
   
  max_len=0
  index = -1
  
  for i in range(len(right_coordinates)):
    if (len(right_coordinates) == 0):
      continue
    if max_len < len(right_coordinates[i]):
      index = i
      max_len = len(right_coordinates[i])
  
  if index == -1:
    return [(-1,-1), (-1,-1)]
  
  top_left = right_coordinates[index][0][0]
  bottom_right =  right_coordinates[index][0][1]
  #print top_left
  #print bottom_right
  
  total_length = 6
  percentage = (max_len/(total_length*1.0)) * 100
  print template_image + ':' +  str(percentage) + '%'

  if (percentage > 50):
    return right_coordinates[index][0]
  
  return [(-1,-1), (-1,-1)]
  
def random_coordinates_from_bounding_box(top_left, bottom_right):
  x=random.randint(top_left[0], bottom_right[0])
  y=random.randint(top_left[1], bottom_right[1])
  return x,y

def random_time():
  time_to_next = random.randint(1,20)/10.0 ##0.1 to 2 seconds
  return time_to_next;
  pass

def check_for_image_and_return_coordinates(image_name):
  get_screenshot()
  coord = contains_image("./screenshot.png", image_name)
  if coord[0][0]!=-1 and coord[0][1]!=-1 and coord[1][0]!=-1 and coord[1][1]!=-1:
    x,y = random_coordinates_from_bounding_box(coord[0], coord[1])
    return x,y
  return -1,-1
  
def check_for_image(image_name):
  get_screenshot()
  coord = contains_image("./screenshot.png", image_name)
  print coord
  if coord[0][0]!=-1 and coord[0][1]!=-1 and coord[1][0]!=-1 and coord[1][1]!=-1:
    time_to_next = random_time()
    print "Found x on image: " + image_name +", sleeping time to click: " + str(time_to_next)
    time.sleep(time_to_next)
    x,y = random_coordinates_from_bounding_box(coord[0], coord[1])
    mouse_click(x,y)
    return 1
  return 0
  
def check_for_x ():
  res=1
  while (res):
   time.sleep(2)
   res=check_for_image("./images/x.png")
   if (res==1):
     continue
   res=check_for_image("./images/x1.png")
   if (res==1):
     continue
   res=check_for_image("./images/x2.png")
   if (res==1):
     continue
   res=check_for_image("./images/x3.png")
   if (res==1):
     continue
   res=check_for_image("./images/x4.png")
   
def collect_gold_ex():
    ##check for finish 
    if check_for_image("./images/hm0.png") == 0:
	check_for_x()
	if (check_for_image("./images/hm0.png") == 0):
	    return 0
    
    
    time.sleep(1)
    if check_for_image("./images/hm4_1.png") == 1:
      time.sleep(1)
      x,y = check_for_image_and_return_coordinates("./images/hm4_1.png")
      if (y==-1):
	check_for_x()
	time.sleep(1)
	x,y = check_for_image_and_return_coordinates("./images/hm4_1.png")
      x1,y1 = check_for_image_and_return_coordinates("./images/hm4_2.png")
      if (x1 == -1):
	check_for_x()
	time.sleep(1)
	x1,y1 = check_for_image_and_return_coordinates("./images/hm4_2.png")
      mouse_click(x1,y)
      time.sleep(1)	
      if check_for_image("./images/hm5.png") == 0:
	check_for_x()
	check_for_image("./images/hm5.png")
      return 1
    
    time.sleep(1)	  
    if check_for_image("./images/hm2.png") == 0:
	check_for_x()
	check_for_image("./images/hm2.png")
    time.sleep(1)	
    if check_for_image("./images/hm3.png") == 0:
	check_for_x()
	check_for_image("./images/hm3.png")
    time.sleep(1)
    check_for_image("./images/hm4_1.png")
    x,y = check_for_image_and_return_coordinates("./images/hm4_1.png")
    if (y==-1):
      check_for_x()
      time.sleep(1)
      x,y = check_for_image_and_return_coordinates("./images/hm4_1.png")
    
    x1,y1 = check_for_image_and_return_coordinates("./images/hm4_2.png")
    if (x1 == -1):
      check_for_x()
      time.sleep(1)
      x1,y1 = check_for_image_and_return_coordinates("./images/hm4_2.png")
    mouse_click(x1,y)
    """
    if check_for_image("./images/hm4_2.png") == 0:
	check_for_x()
	check_for_image("./images/hm4_2.png")
    """
    time.sleep(1)	
    if check_for_image("./images/hm5.png") == 0:
	check_for_x()
	check_for_image("./images/hm5.png")
 
    return 1

def collect_gold ():
  get_screenshot()
  ##check for 'x' button if has it, then click it
  check_for_x()
  ##check for finish and danyci
  res=collect_gold_ex()

while (1):
  collect_gold()
  width, height = autopy.screen.get_size()
  x=random.randint(0, width-1)
  y=random.randint(0, height-1)
  autopy.mouse.smooth_move(x,y)
  time.sleep(random.randint(500,3000)/100.0)