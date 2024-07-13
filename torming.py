
import time

import cv2 # type: ignore

def cutpoint(file_name, wh=300, time_out=300):#ここで切り取るが範囲を指定できる

    start = time.time()

    img = cv2.imread('images/アビス1.jpeg')

    def printCoor(event,x,y,flags,param):
        #マウスのcallbackは引数。

        nonlocal img
        nonlocal img_mes
        nonlocal file_name

        if event == cv2.EVENT_LBUTTONDOWN:
            # 元の画像に直接書き込むと前の描画がそのまま残ってしまうため、コピーを作成。

            img_tmp = img_mes.copy()

            # 直線で書きたい場合
            # cv2.line(img_tmp,(x,y),(x+wh,y),(255,255,255),1)
            # cv2.line(img_tmp,(x,y),(x,y+wh),(255,255,255),1)
            # cv2.line(img_tmp,(x+wh,y),(x+wh,y+wh),(255,255,255),1)
            # cv2.line(img_tmp,(x,y+wh),(x+wh,y+wh),(255,255,255),1)

            cv2.rectangle(img_tmp,(x,y),(x+wh,y+wh),(255,255,255), thickness=1)

            # 座標は左上が原点　x座標:左から右　y座標：上から下　行列では,行(height):y、列(width):x
             # orgは文字オブジェクトの左下の座標
            cv2.putText(img_tmp, text=f'(x,y):({x},{y})',org=(x, y-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5, color=(255,255,255),thickness=1,lineType=cv2.LINE_4)
            

            print(f'start x:{x}, y:{y} --wh:{wh}-- end x:{x+wh}, y:{y+wh}')

            cv2.imshow('image',img_tmp)

        elif event == cv2.EVENT_RBUTTONDOWN:
            # cv2.imshow('image',img)
            idx = file_name.rindex('.')
            trim_name = f'{file_name[:idx]}_trim.jpg'
            trim_array = trim(array=img, x=x, y=y, width=wh, height=wh)
            cv2.imwrite(trim_name, trim_array)


    h,w,_ =  img.shape  
    img_mes = img.copy() 
    print(img.shape)
    print('Quit -> ESC Key ')

    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('image',printCoor)
    cv2.moveWindow('image',100,100) #100,100はwindows上に表示される位置を指定。
    cv2.putText(img_mes, text=f'Quit -> ESC Key',org=(5,10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.3, color=(255,255,255),thickness=1,lineType=cv2.LINE_4)

    # cv2.imshow('image',img)
    cv2.imshow('image',img_mes)
    # 第一引数の名前が同じだと同じウィンドウに上書き表示(名前が異なると別のウインドウが作成される)。

    while True:
        elasped_time = time.time() - start

        if cv2.waitKey(20) & 0xFF == 27:
            break

        if elasped_time > time_out:
            # Exit with a timeout 
            print('time out')
            break

    cv2.destroyAllWindows()


def trim(array, x, y, width, height):
    array_trim = array.copy()
    array_trim = array_trim[y:y + height, x:x+width]

    print(f'Original h(Y), w(X) : {array.shape}')
    print(f'Trimmed h(Y), w(X) :  {array_trim.shape}')

    return array_trim

if __name__ == '__main__':
# test sampleとしてlenaさんを利用しています。
    cutpoint(file_name='アビス1.jpeg', time_out=120)
