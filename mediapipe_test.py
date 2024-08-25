import mediapipe as mp
import requests
import math
import cv2
URL = "http://192.168.224.52:8080/confusion/info"
rate = 1.25

mp_face = mp.solutions.face_detection
FD = mp_face.FaceDetection()

mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


def search_bounding_box(res, size):
    bounding_box = res.location_data.relative_bounding_box
    x1, y1 = bounding_box.xmin, bounding_box.ymin
    width, height = bounding_box.width, bounding_box.height
    x1_px = max(0, min(math.floor(x1 * size[0]), size[0] - 1))
    y1_px = max(0, min(math.floor(y1 * size[1]), size[1] - 1))
    x2_px = min(size[0], min(math.floor((x1 + width) * size[0]), size[0] - 1))
    y2_px = min(size[1], min(math.floor((y1 + height) * size[1]), size[1] - 1))
    return (x1_px, y1_px), (x2_px, y2_px)


def distance(pos_list, size):
    info_list = [((pos[2] - pos[0]) * (pos[3] - pos[1]), (pos[2] + pos[0]) // 2) for pos in pos_list]
    confu_list = [[0]*2 for _ in range(3)]
    for info in info_list:
        x, y = int(info[1] < size[0] // 2), 2 if info[0] >= 31000 else 1 if info[0] >= 12000 else 0
        confu_list[y][x] += 1
    confu_list = sum(confu_list, [])
    print(info_list[0])
    print(confu_list)
    # requests.post(URL, json={"list": confu_list})


def face_blur(img, pos):
    mosaic_img = img[pos[1]:pos[3], pos[0]:pos[2]]
    small_img = cv2.resize(mosaic_img, ((pos[3]-pos[1]) // 20, (pos[2]-pos[0]) // 20))
    big_img = cv2.resize(small_img, ((pos[2]-pos[0]), (pos[3]-pos[1])), interpolation=cv2.INTER_NEAREST)
    img[pos[1]:pos[3], pos[0]:pos[2]] = big_img
    return img


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('카메라 오류 발생')

    dsize = (int(frame.shape[1]*rate), int(frame.shape[0]*rate))
    frame = cv2.resize(frame, dsize)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    results = FD.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    if results.detections:
        positions = []
        for result in results.detections:
            start_point, end_point = search_bounding_box(result, dsize)
            frame = face_blur(frame, start_point + end_point)
            cv2.rectangle(frame, start_point, end_point, (255, 255, 255), 2, cv2.LINE_AA)
            positions.append(start_point+end_point)
        distance(positions, dsize)

    cv2.imshow('', frame)
    if cv2.waitKey(20) == ord('q'):
        print('카메라 종료')
        break

cap.release()
cv2.destroyAllWindows()
