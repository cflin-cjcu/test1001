from FaceDetectionModule import FaceDetector
import cv2
import pafy

url = "https://www.youtube.com/watch?v=skgh3juWdFU"

videoPafy = pafy.new(url)
best = videoPafy.getbest()
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(best.url)

detector = FaceDetector(model_selection=0)

while True:
    # success, img = cap.read()
    img = cv2.imread('./image/test1.jpg', cv2.IMREAD_UNCHANGED)
    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
