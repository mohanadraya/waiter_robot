import cv2
import numpy as np
import apriltag
import math

# --------------- Camera Calibration Parameters ---------------
fx = 600  # Focal length in x (in pixels)
fy = 600  # Focal length in y (in pixels)
cx = 320  # Optical center x (image center)
cy = 240  # Optical center y (image center)
tag_size = 0.05  # Real size of the tag (in meters)

# --------------- AprilTag Detector Initialization ---------------
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)

# --------------- Open Camera ---------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read from camera")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect AprilTags in the frame
    detections = detector.detect(gray)

    for detection in detections:
        # Estimate pose of the detected tag
        pose, e0, e1 = detector.detection_pose(detection, (fx, fy, cx, cy), tag_size)

        # Extract translation vector (position)
        t = pose[0:3, 3]
        x, y, z = round(t[0], 3), round(t[1], 3), round(t[2], 3)

        # Extract rotation matrix
        R = pose[0:3, 0:3]

        # Compute yaw and pitch from rotation matrix
        yaw = math.atan2(R[1, 0], R[0, 0])
        pitch = math.atan2(-R[2, 0], math.sqrt(R[2, 1]**2 + R[2, 2]**2))
        yaw_deg = round(math.degrees(yaw), 2)
        pitch_deg = round(math.degrees(pitch), 2)

        # Display results
        print(f"AprilTag ID: {detection.tag_id}")
        print(f"Position => X: {x} m, Y: {y} m, Z: {z} m")
        print(f"Rotation => Yaw: {yaw_deg}�, Pitch: {pitch_deg}�")
        print("-" * 40)

        break  # Process only the first detected tag

    # Show the camera feed with detection (optional)
    cv2.imshow("AprilTag Detection", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --------------- Cleanup ---------------
cap.release()
cv2.destroyAllWindows()
