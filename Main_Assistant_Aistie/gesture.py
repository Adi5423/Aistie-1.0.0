import cv2
import mediapipe as mp
import pyautogui
import time
import os
import webbrowser
import pyttsx3

engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()



cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width , screen_height = pyautogui.size()
index_y = 0
prev_time = time.time()

def code_preset(great_printed):
    if great_printed == True:
        # start the default browser
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\msedge.exe")
        webbrowser.open("https://github.com/Adi5423")
        webbrowser.open("https://www.blackbox.ai/")
        webbrowser.open("https://www.youtube.com/watch?v=mm_I1M8njD4&list=RDMMmm_I1M8njD4&start_radio=1")
        os.startfile("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
        

def gesture(code):
    while code:
        _, frame = cap.read()
        frame = cv2.flip(frame , 1)
        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        frame_height, frame_width, _ = frame.shape
        # print(hands)
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame,hand)
                landmarks = hand.landmark
                palm = [17,13,9,5]
                finger_tip = [20,16,12,8]
                palm_x_sum = 0
                palm_y_sum = 0
                for id in palm + finger_tip:
                    landmark = landmarks[id]
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    cv2.circle(img=frame , center = (x,y) , radius=10 , color=(0 , 255 ,255 ))   
                    # print(f"Palm landmark {id}: ({x}, {y})")
                    
                    # avg_palm_x = int(palm_x_sum / len(palm))
                    # avg_palm_y = int(palm_y_sum / len(palm))
                    # print(f"Average palm coordinate: ({avg_palm_x}, {avg_palm_y})")
                
                for id in finger_tip:
                    landmark = landmarks[id]
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    cv2.circle(img=frame , center = (x,y) , radius=10 , color=(0 , 255 ,255 ))
                    palm_x_sum = 0
                    palm_y_sum = 0
                    for palm_id in palm:
                        palm_landmark = landmarks[palm_id]
                        palm_x = int(palm_landmark.x * frame_width)
                        palm_y = int(palm_landmark.y * frame_height)
                        cv2.circle(img=frame , center = (palm_x,palm_y) , radius=5 , color=(255 , 0 , 0 ))
                        palm_x_sum += palm_x
                        palm_y_sum += palm_y
                    avg_palm_x = int(palm_x_sum / len(palm))
                    avg_palm_y = int(palm_y_sum / len(palm))
                    print("before great - " , abs(avg_palm_x - x) , "\nFor y - " , abs(avg_palm_y - y))
                    if abs(avg_palm_x - x) < 25 and abs(avg_palm_y - y) < 25:
                        if not great_printed:
                            code_preset(great_printed)
                            
                    else:
                        great_printed = False
    
                    
                    
                    # print("outside" , abs(index_y - thumb_y ))
                        # current_time = time.time()
                        # if abs(index_y - thumb_y ) < 25:
                        #     pyautogui.click()
                        #     pyautogui.sleep(1)
    
    
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            code=False
            exit
            break
# code = True        
# gesture(code)
# code = False