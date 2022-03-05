from timezonefinder import TimezoneFinder  # na vyhľadanie zodpovedajúceho časového pásma pre dané súradnice na Zemi úplne offline
import pytz            # umožňuje presné výpočty časových pásiem
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests
from geopy.geocoders import Nominatim
#geopy: -uľahčuje nájsť súradnice adries, miest, krajín a orientačných bodov na celom svete pomocou geokóderov tretích strán a iných zdrojov údajov
# Nominatim: (by name-podľa mena) - vyhľadávanie údajov OpenStreetMap podľa adresy alebo polohy


api_key = '10c21feec6deeba3134aab0972c7d355'

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def get_weather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + "&appid=" + api_key
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-282.81)
        feels_like = int(json_data['main']['feels_like']-281.52)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", feels_like, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry.")


#search box
search_image = PhotoImage(file=r"C:\Users\Alica\Desktop\api_weather_tkinter_foto\search.png")
img_srch = Label(image=search_image)
img_srch.place(x=20, y=20)

#textfield search box
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "normal"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

#button - search icon
icon_image = PhotoImage(file=r"C:\Users\Alica\Desktop\api_weather_tkinter_foto\search_icon.png")
button_icon = Button(image=icon_image, borderwidth=0, cursor="hand2", bg="#404040", command=get_weather)
button_icon.place(x=390, y=32)

#logo
logo_image = PhotoImage(file=r"C:\Users\Alica\Desktop\api_weather_tkinter_foto\logo.png")
img_logo = Label(image=logo_image)
img_logo.place(x=150, y=100)

#time and text
name = Label(root, font=("poppins", 12, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

#bottom box
box_image = PhotoImage(file=r"C:\Users\Alica\Desktop\api_weather_tkinter_foto\box.png")
box = Label(image=box_image)
box.pack(padx=5, pady=5, side=BOTTOM)


#labels - bottom box
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

#temperature, condition labels
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)


w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)


root.mainloop()

