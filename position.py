import pyautogui,time

time.sleep(3)
print(pyautogui.position())
time.sleep(2)
#pyautogui.moveTo(3093, 299,1)

#pyautogui.mouseDown(3093, 310,button="left")


pyautogui.click(2656, 428, 3, button="left")
time.sleep(1)
pyautogui.tripleClick(2557, 52, button="left")
pyautogui.click(button="right")
pyautogui.moveRel(50, 215, 1)
pyautogui.click(button="left")  # copioLinkPublicacion
pyautogui.click(2058, 10, 3, button="left")  # cambio pestaña a wpp
pyautogui.click(2264, 260, 3, button="left")  # buscoDondeMandarlo
pyautogui.typewrite("....")
pyautogui.press("Enter")
pyautogui.click(2855, 976, 3, button="left")  # pegoLink
pyautogui.click(button="right")
pyautogui.moveRel(50, -335, 1)
pyautogui.click(button="left")
pyautogui.press("Enter")  # envio
pyautogui.click(2665, 14, 3, button="left")  # cierroPestaña,sino modifica tamaño de labels

pyautogui.click(2365, 8, 3, button="left")  # cambio pestaña a ZonaProp
pyautogui.moveTo(2656, 428, 3)
pyautogui.scroll(-227)
time.sleep(5)
