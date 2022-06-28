import os
import cv2
import time

from beepy import beep

Image_Path= 'Tensorflow/workspace/images/collection/'
labels = ['peace','done','no','thankyou','hello']
number_img=15
for label in labels:
    a = Image_Path + '/' + label
    os.mkdir(a)
    cap = cv2.VideoCapture(0)
    print('Collecting Image {}'.format(label))
    time.sleep(1)
    beep(sound="ping")
    for img_num in range(number_img):
        ret, frame = cap.read()
        imgname = os.path.join(Image_Path, label, label + '_' + '{}.jpg'.format(str(img_num)))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0b11111111 == ord('q'):
            break
    cap.release()



