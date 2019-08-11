import PyCapture2
import cv2
import requests
import numpy as np
import threading
from datetime import datetime
import os
import glob



cap = cv2.VideoCapture(0)
filename=str((datetime.now().strftime('%H_%M_%S')))+'.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename,fourcc, 30, (640,480))
starttime =datetime.now()
Num_Of_avi=0

files_in_folder=len(os.listdir())


while(cap.isOpened()):
    
    num_images=30*5
    filename=str((datetime.now().strftime('%H_%M_%S')))+'.avi'
    out = cv2.VideoWriter(filename,fourcc, 30, (640,480))
    for i in range(num_images):
        ret, frame = cap.read()
        text='Elapsed time:'+str((datetime.now() - starttime))[0:7] +'\n'+'press "q" to halt the prog'+'\n'+str(Num_Of_avi)+' files were generated'
        y0, dy = 50, 30
        for i, line in enumerate(text.split('\n')):
            y = y0 + i*dy
            cv2.putText(frame, line, (50, y ), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0), 2)
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break
        files_in_folder=len(os.listdir())
        if files_in_folder>10:
            Target_current_folder=str(os.getcwd())+"\\"+str(os.listdir()[0])
            targetPattern = str(os.getcwd())+'\\*.avi'        
            os.remove(glob.glob(targetPattern)[0])
        
        
    Num_Of_avi=Num_Of_avi+1
    out.release()


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows()



    



       
