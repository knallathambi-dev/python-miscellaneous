import cv2
import os
import glob
import time

TMP_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'tmp'
)

def create_video(img_path, out_path, fps=60):
    img_arr = sorted([ x for x in glob.glob(img_path) ])
    img = cv2.imread(img_arr[0])
    height, width, channels = img.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')     
    out = cv2.VideoWriter(
        os.path.join(out_path, 'output_video.avi'),
        fourcc,
        fps, (width, height)
    )
    for filename in img_arr:        
        img = cv2.imread(filename)
        print(f'Read img - {filename}')
        out.write(img)

    cv2.destroyAllWindows()
    out.release()

def show_image(img_path):
    frame = cv2.imread(img_path)
    cv2.imshow('video',frame)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img_path = os.path.join(TMP_DIR, 'screenshots', '*.png')
    out_path = os.path.join(TMP_DIR, 'videos')
    create_video(img_path, out_path, fps=5)

    # img_path = os.path.join(TMP_DIR, 'screenshots', 'sceen_001.png')
    # show_image(img_path)

