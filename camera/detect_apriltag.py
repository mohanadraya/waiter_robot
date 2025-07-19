import cv2
import apriltag

# ���� ��������
cap = cv2.VideoCapture(0)  # ���� ����� ��� �������� �� USB

# ����� ������
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)

while True:
    ret, frame = cap.read()
    if not ret:
        print("��� �� ����� ������ �� ��������")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ����� �� �������
    results = detector.detect(gray)

    for r in results:
        corners = r.corners
        ptA, ptB, ptC, ptD = [tuple(map(int, pt)) for pt in corners]

        # ��� ���� �����
        cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
        cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
        cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
        cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

        # ����� ��� ID
        tagID = r.tag_id
        cv2.putText(frame, f"ID: {tagID}", ptA, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("AprilTag Detection", frame)

    # ������ ��� ����� ��� q
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
