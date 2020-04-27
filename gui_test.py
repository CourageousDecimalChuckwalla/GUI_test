import tkinter as tk
from PIL import ImageTk, Image
import requests

#variables
HEIGHT = 800
WIDTH = 700

def test_function(entry):
    print("butt clicked")

def get_weather(): # API Interaction
    weather_key = "7f390c320af43826fae50fc0748c3c57"
    city = 'omaha'
    state = 'ne'
    url = "https://api.openweathermap.org/data/2.5/forecast"  # ?q={city name},{state}&appid={your api key}
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params) # grab from server
    weather = response.json()# invoke response request
    print(weather['city']['name'])

# root
root = tk.Tk()
# root.attributes("-alpha", 0.5) # transparency

# first button
button = tk.Button(root, text='Almost about as many as 150 double niggers', bg='red', command=lambda: get_weather())
button.pack(fill='both', side='left', expand=True)

# canvas
canvas = tk.Canvas(root, height=HEIGHT , width=WIDTH, bg='purple')
canvas.pack()

# background image N:\temp\1584976768576.jpg
background_image = ImageTk.PhotoImage(Image.open("N:\\temp\\1584976768576.jpg"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)

# transparent image mamako example, mamako.png
photoimage = ImageTk.PhotoImage(file="mamako.png") #confirmed working
canvas.create_image(500,500,image=photoimage)

# frame
frame = tk.Frame(root, bg='#8cf') # accepts hex, normal color names ex. blue, red, green
frame.place(relx=0.1, rely=0.1, relwidth=.8, relheight=.8) # 1 = 100%
    # relx, rely: where frame is placed relative to the window
    #relwidth, relheight: dimensions of frame relative to the window

# label
label = tk.Label(frame, text='this is a label')
label.pack(side='left')

# entry
entry = tk.Entry(frame, bg='purple')
entry.pack()




root.mainloop()


