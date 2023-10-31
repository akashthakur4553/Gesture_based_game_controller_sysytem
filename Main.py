import cv2 
import numpy as np 
import time
import pyautogui
import mediapipe as mp
pose = mp.solutions.pose
pose_o = pose.Pose()
drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
#d - move forward
#j - jump
#s - shoot
d_down=False
s_down=False
j_down=False
def inFrame(lst):
	if lst[24].visibility > 0.7 and lst[23].visibility > 0.7 and lst[15].visibility>0.7:
		return True 
	return False

def isJump(p):
	if p<80:
		return True
	return False

def isShoot(finalres):
	if abs(finalres[15].x*640 - finalres[16].x*640) < 100:
		return True 
	return False
while True:
	print('hello world')
	_, frm = cap.read()
	res = pose_o.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
	if res.pose_landmarks:
		finalres = res.pose_landmarks.landmark

		drawing.draw_landmarks(frm, res.pose_landmarks, pose.POSE_CONNECTIONS)

	#main logic
	if res.pose_landmarks and inFrame(finalres):
        	 
         if isJump(finalres[0].y*480):
             #press j down only if j is not already down
            cv2.putText(frm, "JUMP DONE", (50,140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            if not(j_down):
                pyautogui.keyDown("z")
                j_down=True
            
        else: # relese j key
            cv2.putText(frm, "Not jump", (50,140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            if j_down:
                j_down=False 
                pyautogui.keyUp("z")

        if isShoot(finalres): # press s key for shooting
            cv2.putText(frm, "Shooting", (50,180), cv2.FONT_HERSHEY_SIMPLEX, 1, (85,0,85), 2)

            if not(s_down):
                s_down = True
                pyautogui.keyDown("d")

            
        else: # release s key up
            cv2.putText(frm, "Not Shooting", (50,180), cv2.FONT_HERSHEY_SIMPLEX, 1, (85,0,85), 2)

            if s_down:
                s_down = False
                pyautogui.keyUp("d")
    cv2.imshow("window", frm)
    # else: # here chek if any key down the make it up
	# 	cv2.putText(frm, "Make Sure full body in frame", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

	# 	if d_down:
	# 		pyautogui.keyUp("d")
	# 		d_down=False
	# 	if s_down:
	# 		pyautogui.keyUp("s")
	# 		s_down=False
	# cv2.line(frm, (0,80), (640,80), (255,0,0), 1)
	
