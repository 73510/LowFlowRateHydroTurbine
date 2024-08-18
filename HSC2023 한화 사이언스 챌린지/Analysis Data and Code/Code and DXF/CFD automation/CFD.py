import pyautogui
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(pyautogui.locateCenterOnScreen('fusion360icon.png', confidence=0.9))

pyautogui.click(pyautogui.locateCenterOnScreen('fusion360icon.png', confidence=0.9))

time.sleep(2)

pyautogui.moveTo(pyautogui.locateCenterOnScreen('designbutton.png', confidence=0.9), duration=1)
pyautogui.click()
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('simulationbutton.png', confidence=0.9))
time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen('dansunhwa.png', confidence=0.9))
time.sleep(1.5)
pyautogui.click(pyautogui.locateCenterOnScreen('dogubutton.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('cfdbutton.png', confidence=0.9))
time.sleep(2.5)
pyautogui.click(pyautogui.locateCenterOnScreen('sulgay update.png', confidence=0.9))
time.sleep(2)
pyautogui.doubleClick(pyautogui.locateCenterOnScreen('stf10.png', confidence=0.9))
time.sleep(0.1)
pyautogui.click(pyautogui.locateCenterOnScreen('sulgay1.png', confidence=0.9))
time.sleep(0.1)
pyautogui.click(pyautogui.locateCenterOnScreen('sulgayupdate_.png', confidence=0.9))
time.sleep(12)
pyautogui.rightClick(pyautogui.locateCenterOnScreen('hyungsang.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('danyubyungyung.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('mm.png', confidence=0.9))

time.sleep(0.2)
pyautogui.rightClick(pyautogui.locateCenterOnScreen('jijungx.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('pyunjip.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('youchae.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('solid.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('jukyong.png', confidence=0.9))

time.sleep(0.2)
pyautogui.rightClick(pyautogui.locateCenterOnScreen('ABS.png', confidence=0.9))
time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('del.png', confidence=0.9))

time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('solveit.png', confidence=0.9))

time.sleep(0.2)
coord = pyautogui.locateCenterOnScreen('gyesokyuchi.png', confidence=0.9)
pyautogui.click(x = coord.x + 200, y = coord.y)

time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('zero.png', confidence=0.9))
coord = pyautogui.click(pyautogui.locateCenterOnScreen('haysuk.png', confidence=0.9))
pyautogui.moveTo(coord, duration=0.2)
pyautogui.click(coord)

time.sleep(0.2)
pyautogui.click(pyautogui.locateCenterOnScreen('yes.png', confidence=0.9))