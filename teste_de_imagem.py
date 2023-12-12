import pyautogui
# Localize a imagem do botão
def teste_de_imagem():
    try:
        #pyautogui.hotkey('alt','tab')
        button_image = 'botaofim.PNG'
        matches = pyautogui.locateAllOnScreen(button_image, confidence= 0.7)
        # Encontre o centro de cada correspondência e escolha o que estiver mais próximo do centro da tela
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width / 2, screen_height / 2
        closest_match = None
        closest_distance = float('inf')
        for match in matches:
            match_center_x, match_center_y = pyautogui.center(match)
            distance = ((center_x - match_center_x) ** 2 + (center_y - match_center_y) ** 2) ** 0.5
            if distance < closest_distance:
                closest_match = match
                closest_distance = distance
        # Clique no botão
        if closest_match is not None:
            button_x, button_y = pyautogui.center(closest_match)
            pyautogui.click(button_x, button_y)
    except:
        pass

