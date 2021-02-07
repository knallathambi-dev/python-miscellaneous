import os
import time
from PIL import Image, ImageGrab
import win32gui

TMP_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'tmp'
)
RESOURCES_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'resources'
)

def capture_screenshots(num_of_shots=1, delay=0, dir_path=None):
    cursor_img_path = os.path.join(RESOURCES_DIR, 'img', 'cursor.png')
    img_cursor = Image.open(cursor_img_path)
    cur_x, cur_y = win32gui.GetCursorPos()
    # dir_path = os.path.join(TMP_DIR, 'screenshots')
    for n in range(num_of_shots):
        img = ImageGrab.grab()
        file_name = f'screen_{n + 1:03}.png'
        img.paste(img_cursor, box=(cur_x, cur_y), mask=img_cursor)
        img.save(os.path.join(dir_path, file_name))

        if delay:
            time.sleep(delay)


if __name__ == '__main__':
    dir_path = os.path.join(TMP_DIR, 'screenshots')
    capture_screenshots(num_of_shots=50, delay=1/2, dir_path=dir_path)





