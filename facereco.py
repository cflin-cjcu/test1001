import cv2
from face_lib import face_lib
FL = face_lib()
cflin_img = cv2.imread('./image/cflin.jpg')
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
while(cap.isOpened()):
    ret, frame = cap.read()
    cflin_exist, no_of_faces = FL.recognition_pipeline(frame, cflin_img)
    if no_of_faces != 0:
        _, faces_locations = FL.faces_locations(frame)
        x, y, w, h = faces_locations[0]
        if cflin_exist == True:
            cv2.putText(frame, 'This is cflin', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (30, 200, 40), 2)
        else:
            cv2.putText(frame, 'This is not cflin', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (30, 200, 40), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('cflin', frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
