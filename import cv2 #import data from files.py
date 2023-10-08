import cv2  #import data from files
import time #import time from present
import numpy as np #
fitToEllipse = False #init to false
cap = cv2.VideoCapture('queda.mp4')  #import video from files and work on it!!
time.sleep(2) #after time=2s 
fgbg = cv2.createBackgroundSubtractorMOG2()  #use algo and subtract background from videos like noise
j = 0 #init to 0
while(1): #while true
    ret, frame = cap.read() #its going to read thje data from files
    #Convert each frame to gray scale and subtract the background
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #
        fgmask = fgbg.apply(gray) #apply gray 
        
        #Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #here finmd contors and make a change

        if contours:
        
            # List to hold all areas
            areas = []

            for contour in contours:
                ar = cv2.contourArea(contour)
                areas.append(ar) #run a loop and append in arrays
            
            max_area = max(areas, default = 0)  #its goin find max areas 

            max_area_index = areas.index(max_area) 

            cnt = contours[max_area_index] #max area ka index niklega

            M = cv2.moments(cnt) 

        def mean_squared_loss(x1, x2):
            difference = x1-x2  #frame 1-frame 2
            a, b, c, d = difference.shape
            n_samples = a*b*c*d
            sq_difference = difference**2
            Sum = sq_difference.sum()
            distance = np.sqrt(Sum)
            mean_distance = distance/n_samples
            return mean_distance
            x1=x, y, w, h 
            x1= cv2.boundingRect(cnt) #4 variables and based on that frame goin to make
            x2=f,g,i,m
            x2 =cv2.boundingRect(cnt)
            cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0) #here carryb all colors (r,g,b)
            
            if h < w: #if height is greater than width
                j += 1 #increment of j
            if m < i: 
                 j += 1  
            if j > 10:
                print("FALL") #if j value increases then fall
                cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2) #the whole text is placed in 
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) #here rect frame gona make and based on that result will come

            if h > w: #if height is greater than width
                j = 0  #j remains Same
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #changes in frame and happen 


            cv2.imshow('video', frame) #a video gona show
        if cv2.waitKey(33) == 27:
            break
    except Exception as e:
            break
cv2.destroyAllWindows() #here destroy all videos whenever we stop it!!!
''' if cv2.waitKey(33) == 27:
             break'''