import cv2

# ��� ��������
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera not def")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("fream read f")
        break

    cv2.imshow('rpi camera', frame)

    # ������ ������ ��� �� q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

