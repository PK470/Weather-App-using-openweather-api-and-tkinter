import tkinter as tk
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
class Weather:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+0+0")
        self.root.title("Weather Report")
        ##root.configure(bg='blue')

        self.city = tk.StringVar()
        self.degree_sign = u"\N{DEGREE SIGN}"
        self.apikey ='57c2a70365bcbef047c5633178925c1b'
        tk.Label(root, text="Weather Report", bd=10, relief=tk.RIDGE, bg="#e1ff59", pady=2,
                 font=("Helvetica", 30, "bold")).pack(fill=tk.X)
        tk.Entry(root, font=("Helvetica", 15, "bold"), relief=tk.SUNKEN, bd=8,
                 width=10, textvariable=self.city).place(x=20, y=80, width=400, height=50)
        tk.Button(text='Search', font=("Georgia", 16, "bold"), bg='orange', fg='black',bd=5, width=7, relief=tk.SUNKEN,
               activebackground="blue", activeforeground='white',command=self.weather).place(x=450, y=80)

    def weather(self):
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city.get()}&units=impherial&APPID={self.apikey}")

        if weather_data.json()['cod'] == '404' and weather_data.json()['message'] == 'city not found':
            tk.messagebox.showinfo("WARNING", "Please Enter Valid City")
            self.city.set("")
        else:


            weather = weather_data.json()['weather'][0]['main']
            temp = weather_data.json()['main']['temp'] - 273.15
            wind = weather_data.json() ['wind']['speed']
            name = weather_data.json()['name']

            x = round(temp, 2)
            if weather == "Clear":
                img = Image.open("clear.png")

            elif weather == "Clouds":
                img = Image.open("clouds.png")


            elif weather == "Rain":
                img = Image.open("rain.png")

            elif weather == 'Haze':
                img = Image.open("haze.png")

            else:
                img = Image.open("main.png")


            self.resizeimg3 = img.resize((200, 190))
            self.finalimg3 = ImageTk.PhotoImage(self.resizeimg3)
            self.icons = tk.Label(image=self.finalimg3)
            self.icons.place(x=70, y=200)
            Q2 = tk.LabelFrame(root, font=("Helvetica", 15, "bold"),
                                        )
            Q2.place(x=290, y=140, width=700, height=450)
            tk.Label(Q2, text=name, bd=10, pady=2,
                     font=("Helvetica", 30, "bold")).place(x= 200, y=30)
            tk.Label(Q2, text= weather, bd=10, pady=2,
                     font=("Helvetica", 30, "bold")).place(x=10, y=150)
            tk.Label(Q2, text='Temperature: ' + str(x) + self.degree_sign +'C' , bd=10, pady=2,
                     font=("Helvetica", 30, "bold")).place(x = 10, y=100)
            tk.Label(Q2, text='Wind Speed: ' + str(wind)+'Km/Hr', bd=10, pady=2,
                     font=("Helvetica", 30, "bold")).place(x=10, y=200)




root = tk.Tk()
obj = Weather(root)
root.mainloop()