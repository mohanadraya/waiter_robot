import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("no camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("no reading")
        break

    cv2.imshow("live", frame)

    # ��� ������ ������ ��� q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
