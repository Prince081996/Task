import cv2                  #Install open cv using pip3 install opencv-python


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #cascadefile to search face
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #("Converted RGB image to grayscale")
        faces = face_cascade.detectMultiScale(gray, 1.1, 4) #perform the detection
        for (a,b,c,d) in faces:
          cv2.rectangle(frame, (a,b),(a+c,b+d), (255, 0, 0), 3)  # syntax cv2.rectangle(image, start_point, end_point, color, thickness)
          cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):  #Press 's' to capture image                  
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Photo is successfully saved")
            break
        elif key == ord('q'):     #press 'q' to turnoff the camera
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break