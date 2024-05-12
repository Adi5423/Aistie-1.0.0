import cv2
import mediapipe as mp
import pyautogui
import numpy as np

def drawing(query):
    while query:    
        # Initialize the webcam capture
        cap = cv2.VideoCapture(0)

        # Create a hand detector using MediaPipe
        hand_detector = mp.solutions.hands.Hands()

        # Create a drawing utility for drawing hand landmarks
        drawing_utils = mp.solutions.drawing_utils

        # Get the screen width and height using pyautogui
        screen_width, screen_height = pyautogui.size()

        # Initialize the drawing window
        drawing_window = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

        # Initialize the previous index finger coordinates
        prev_index_x, prev_index_y = 0, 0

        # Create a window for displaying the camera feed
        cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)

        while True:
            # Read a frame from the webcam
            _, frame = cap.read()

            # Flip the frame horizontally (since the webcam is mirrored)
            frame = cv2.flip(frame, 1)

            # Convert the frame from BGR to RGB (required by MediaPipe)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame using the hand detector
            output = hand_detector.process(rgb_frame)

            # Get the detected hand landmarks
            hands = output.multi_hand_landmarks

            # If hands are detected
            if hands:
                # Iterate through each hand
                for hand in hands:
                    # Draw the hand landmarks on the camera feed
                    drawing_utils.draw_landmarks(frame, hand)

                    # Get the individual landmarks for the hand
                    landmarks = hand.landmark

                    # Iterate through each landmark
                    for id, landmark in enumerate(landmarks):
                        # Get the x and y coordinates of the landmark
                        x = int(landmark.x * screen_width)
                        y = int(landmark.y * screen_height)

                        # If the landmark is the index finger tip (id=8)
                        if id == 8:
                            # Draw a circle on the drawing window at the index finger tip
                            cv2.circle(drawing_window, (x, y), 5, (255, 255, 255), -1)

                            # If this is not the first frame, draw a line from the previous index finger coordinates to the current coordinates
                            if prev_index_x!= 0 and prev_index_y!= 0:
                                cv2.line(drawing_window, (prev_index_x, prev_index_y), (x, y), (255, 255, 255), 5)

                            # Update the previous index finger coordinates
                            prev_index_x, prev_index_y = x, y

            # Display the camera feed and the drawing window
            cv2.imshow('Camera Feed', frame)
            cv2.imshow('Drawing Window', drawing_window)

            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # Release the webcam capture and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()