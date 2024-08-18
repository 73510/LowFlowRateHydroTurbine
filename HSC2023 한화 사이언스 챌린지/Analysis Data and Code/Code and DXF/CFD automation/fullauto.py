import pyautogui
import time

startangle =330

currentangle = 0

step = 10

maxangle = 360

flapname = 'halfcapsuleflap'

def click(name):
    pyautogui.click(pyautogui.locateCenterOnScreen(name, confidence=0.95))


def runCFD():
    
    #pyautogui.click(pyautogui.locateCenterOnScreen('fusion360icon.png', confidence=0.9))

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
    pyautogui.rightClick(pyautogui.locateCenterOnScreen('fucknigga.png', confidence=0.9))
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
    pyautogui.click(pyautogui.locateCenterOnScreen('bitch i said yes.png', confidence=0.9))
def waituntilcfdfinish():
    # wait till cfd ends
    while(1) : 
        if (None == pyautogui.locateCenterOnScreen('endmsg.png', confidence = 0.95)):
            time.sleep(5)
        else : 
            break
def saveresult():
    print("saveresult start")
    #time.sleep(1)
    #pyautogui.click(pyautogui.locateCenterOnScreen('cfdicon.png', confidence=0.95))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('wall calc.png', confidence=0.9))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('chaejuk.png', confidence=0.9))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('forec.png', confidence=0.95))
    time.sleep(0.5)
    coord = pyautogui.locateCenterOnScreen('micronewton.png', confidence=0.95)
    pyautogui.moveTo(coord, duration = 0.3)
    pyautogui.click()
    time.sleep(0.5)
    coord = pyautogui.locateCenterOnScreen('newton.png', confidence=0.95)
    pyautogui.moveTo(coord, duration = 0.3)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('torque.png', confidence=0.9))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('microNmm.png', confidence=0.95))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('Nm.png', confidence=0.95))


    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('chuksangjum.png', confidence=0.95))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('Xcoord.png', confidence=0.95))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("backspace")
    pyautogui.write('90')
    pyautogui.click(pyautogui.locateCenterOnScreen('Ycoord.png', confidence=0.95))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("backspace")
    pyautogui.write('110')
    pyautogui.click(pyautogui.locateCenterOnScreen('Zcoord.png', confidence=0.95))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("backspace")
    pyautogui.write('150')

    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('ok.png', confidence=0.95))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('dir.png', confidence=0.95))
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('Xdir0.png', confidence=0.95))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("backspace")
    pyautogui.write('1')
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('Zdir1.png', confidence=0.95))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("backspace")
    pyautogui.write('0')
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('ok.png', confidence=0.95))

    #체적 선택하기
    bigblockcoord = (1494, 627)
    pyautogui.moveTo(bigblockcoord, duration = 0.1)
    pyautogui.rightClick()
    
    click('hide.png')

    bodycoord = (1496, 615)

    pyautogui.moveTo(bodycoord, duration = 0.1)
    pyautogui.click()



    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('gyesan.png', confidence=0.95))

    click('writefile.png')
    pyautogui.write(flapname + str (currentangle))
    pyautogui.press('enter')

    print("saveresult finish")
def offCFD():
    coord1 = (2533, 24)
    coord2 = (1099, 741)
    pyautogui.click(coord1)
    time.sleep(0.1)
    pyautogui.click(coord2)
    time.sleep(5)
def readjustmodel():
    click('simulationbuttonbig.png')
    time.sleep(2)
    click('designbuttonsmall.png')
    time.sleep(2)
    pyautogui.doubleClick(pyautogui.locateCenterOnScreen('movetimeline.png'))
    time.sleep(2)
    click('anglebox.png')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("backspace")
    pyautogui.write(str(currentangle))
    pyautogui.press("enter")
    time.sleep(0.2)



click('fusion360icon.png')
time.sleep(1)
for currentangle in range(startangle, maxangle, step):
    readjustmodel()
    runCFD()
    waituntilcfdfinish()
    saveresult()
    offCFD()