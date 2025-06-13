import webbrowser
import time
import pyautogui

def main():
    # Open the target downloads page
    url = "https://www.cursor.com/downloads"
    webbrowser.open(url)
    # Wait for the webpage to load; adjust the delay as needed
    time.sleep(10)

    # Attempt to find the "Windows" download button using a reference image.
    # Ensure you have captured a screenshot of the "Windows" button and saved it as 'windows.png' in the repo.
    try:
        button_location = pyautogui.locateOnScreen('windows.png', confidence=0.8)
        if button_location:
            click_point = pyautogui.center(button_location)
            pyautogui.click(click_point)
            print("Clicked on the Windows download button.")
        else:
            print("Could not locate the Windows download button on the screen.")
    except Exception as e:
        print("Error during GUI automation:", e)

    # Give some time for the download to start
    time.sleep(5)

if __name__ == "__main__":
    main()
