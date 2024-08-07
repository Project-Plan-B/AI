# yolov5 모델을 이용해서 사람(얼굴)을 감지한다. : detection()
# 감지된 사람의 얼굴 영역을 모자이크 처리한다. : face_blur()

import torch
import cv2

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/model/best.pt')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (640, 480))

        results = model(frame)
        detections = results.pandas().xyxy[0]
        if not detections.empty:
            # 결과를 반복하며 객체 표시
            for _, detection in detections.iterrows():
                x1, y1, x2, y2 = detection[['xmin', 'ymin', 'xmax', 'ymax']].astype(int).values
                label = detection['name']
                conf = detection['confidence']

                # 박스와 라벨 표시
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 프레임 표시
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
