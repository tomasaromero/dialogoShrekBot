import pyautogui,time
#clickear en el chat a enviar
time.sleep(5)
print(pyautogui.position())
f=open("dialogoShrek", 'r')

for word in f:
    time.sleep(3)
    pyautogui.typewrite(word)
    pyautogui.press("Enter")




