import pyautogui

while True:
    try:
        pyautogui.scroll()
    except KeyboardInterrupt:
        print('Programa encerrado')