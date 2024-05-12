import cv2
import winsound
# for opening the web cam of the system 
cam = cv2.VideoCapture(0)
while cam.isOpened():
    try:
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        difference = cv2.absdiff(frame1, frame2)
        gray_color = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray_color, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Granny Cam', frame1)
    except:
        print("some problem occured")