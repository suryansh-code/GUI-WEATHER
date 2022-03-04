import tkinter as tk

from tkinter import font

import requests

HEIGHT = 500
WIDTH = 600


def test_function(entry):
    print('this is entry:', entry)


def format_response(weather):
    name = (weather['name_'])
    desc = (weather['weather'][0]['description'])
    temp = (weather['main']['temp'])

    label['text'] = str(name) + '/' + str(desc) + '/' + str(temp)


def get_weather(city):
    weather_key = '60f507cbe3b5e6a2b40e32f55bdf3226'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'uits': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    name = (weather['name_'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label1 = tk.Label(root, image=background_image)
background_label1.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='get weather', font=30, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Modern', 12))
label.place(relwidth=1, relheight=1)

root.mainloop()