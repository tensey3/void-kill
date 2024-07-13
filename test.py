import time
import cv2 # type: ignore

class ImageCropper:
    def __init__(self, file_name, time_out=120):
        self.file_name = file_name
        self.time_out = time_out
        self.cropping = False
        self.start_x, self.start_y = None, None
        self.end_x, self.end_y = None, None

        self.img = cv2.imread(file_name)
        h, w, _ = self.img.shape
        cv2.namedWindow('images/アビス1.jpeg', cv2.WINDOW_NORMAL)
        cv2.imshow('images/アビス1.jpeg', self.img)
        cv2.setMouseCallback('images/アビス1.jpeg', self.crop)
        self.print_instructions()

        while True:
            start = time.time()

            elapsed_time = time.time() - start

            if cv2.waitKey(20) & 0xFF == 27:
                break

            if elapsed_time > self.time_out:
                print('Time out')
                break

        cv2.destroyAllWindows()

    def crop(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.cropping = True
            self.start_x, self.start_y = x, y
            self.end_x, self.end_y = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.cropping:
                self.end_x, self.end_y = x, y

        elif event == cv2.EVENT_LBUTTONUP:
            self.cropping = False
            self.end_x, self.end_y = x, y

            # Ensure that start and end points are in the right order
            if self.start_x > self.end_x:
                self.start_x, self.end_x = self.end_x, self.start_x
            if self.start_y > self.end_y:
                self.start_y, self.end_y = self.end_y, self.start_y

            cropped_img = self.img[self.start_y:self.end_y, self.start_x:self.end_x]
            cv2.imshow('cropped', cropped_img)
            cv2.waitKey(0)
            cv2.destroyWindow('cropped')

            idx = self.file_name.rindex('.')
            trim_name = f'{self.file_name[:idx]}_trim.jpg'
            cv2.imwrite(trim_name, cropped_img)

    def print_instructions(self):
        print('Click and drag to select a region to crop. Press ESC to exit.')
