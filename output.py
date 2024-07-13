import time
import cv2 # type: ignore
import matplotlib.pyplot as plt # type: ignore
#matplotlibパッケージの中のモジュールの一つ
import numpy as np # type: ignore
#Pythonで数値計算をより高速に行うことができる

img1 = cv2.imread('images/アビス1.jpeg')
img2 = cv2.imread('アビス1_trim.jpg')
#imreadは画像をファイルから読み込むやつ
#img2 =cv2.resize(img2,(600,600))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#cvtColorは色の変更につかう

large_img = img1
small_img = img2
#座標
x_offset=524
y_offset=156

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
cv2.imshow('test', large_img)
#imshowは画像を画面に表示するやつ
cv2.waitKey(0)
#waitKey() はキーボード入力を処理する関数
cv2.destroyAllWindows()
#destroyAllWindowsで画面を閉じる

#  cv2.rectangle(img_tmp,(x,y),(x+wh,y+wh),(255,255,255), thickness=1)
# cv2.putText(img_tmp, text=f'(x,y):({x},{y})',org=(x, y-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#             fontScale=0.5, color=(255,255,255),thickness=1,lineType=cv2.LINE_4)
# print(f'start x:{x}, y:{y} --wh:{wh}-- end x:{x+wh}, y:{y+wh}')