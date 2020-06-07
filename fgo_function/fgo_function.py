from base import BlueToothMouse
import time


def friend_summon(port):
    mouse = BlueToothMouse.BlueToothMouse(port=port)
    mouse.open()
    mouse.set_zero()
    # 606,606 is the center.
    mouse.touch(606, 606)
    time.sleep(1)
    flag = True
    while flag:
        # touch 1st button position
        mouse.touch(606 + 200, 606 + 327, 2)
        time.sleep(1)
        # touch 2nd button position
        mouse.touch(606 + 160, 606 + 500, 6)


if __name__ == '__main__':
    friend_summon("com3")