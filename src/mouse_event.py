from pynput.mouse import Controller

def capture():
    mouse = Controller()
    print(f'Mouse position - {mouse.position}')

if __name__ == '__main__':
    capture()
