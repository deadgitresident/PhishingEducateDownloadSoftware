import pyautogui
import time
import webbrowser
import os
import tkinter as tk
from tkinter import messagebox

# Set the link to download the software (replace with your own link)
download_link = "https://example.com/download_software"

# Set the software name (replace with your own software name)
software_name = "Example Software"

# Set the download directory (replace with your own directory)
download_dir = "C:\\Downloads"

# Create a phishing window
root = tk.Tk()
root.title("Phishing Simulation")
label = tk.Label(root, text="Click here to download the latest version of {}!".format(software_name))
label.pack()
button = tk.Button(root, text="Download Now", command=lambda: simulate_phishing())
button.pack()
root.mainloop()

def simulate_phishing():
    # Open the default web browser
    webbrowser.open(download_link)

    # Wait for the page to load
    time.sleep(5)

    # Move the mouse to the download link and click
    pyautogui.moveTo(500, 500)  # Replace with the coordinates of the download link
    pyautogui.click()

    # Wait for the download to complete
    time.sleep(10)

    # Move the mouse to the download directory and click
    pyautogui.moveTo(500, 500)  # Replace with the coordinates of the download directory
    pyautogui.click()

    # Open the downloaded software
    os.startfile(os.path.join(download_dir, software_name + ".exe"))

    # Display a warning message
    messagebox.showwarning("Phishing Simulation", "You have just fallen victim to a phishing attack! Be cautious when clicking on links and downloading software from unknown sources.")

print("Phishing simulation complete!")