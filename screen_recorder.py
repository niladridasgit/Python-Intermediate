import pyautogui
import cv2
import numpy as np
 
# Specify resolution
resolution = (1920, 1080)
 
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
 
# Specify name of Output file
filename = input("Enter the name of the recorded file - ")+'.avi'
 
# Specify frames rate
fps = 60.0
 
# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)
 
# Creating an Empty window
cv2.namedWindow(filename, cv2.WINDOW_NORMAL)
 
# Resize the display window
cv2.resizeWindow(filename, 480, 270)
 
while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
 
    # Convert the screenshot to a numpy array
    frame = np.array(img)
 
    # Convert it from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # Write it to the output file
    out.write(frame)
     
    # Optional: Display the recording screen
    cv2.imshow(filename, frame)
     
    # Stop recording when we press 'quit'
    if cv2.waitKey(1) == ord('~'):
        break
 
# Release the Video writer
out.release()
 
# Destroy all windows
cv2.destroyAllWindows()