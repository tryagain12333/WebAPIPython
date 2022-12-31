import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1854263fe6fd9617942ca63017dd2586"
    #Đăng ký tài khoản trang web để lấy api
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))

    final_info = condition+"\n" + str(temp) + "°C"
    final_data = "\n" +"Nhiệt độ cao nhất: " + str(max_temp) + "°C" + "\n" + "Nhiệt độ thấp nhất:" + str(min_temp) + "°C"+ "\n" + "Áp suất: " + str(pressure) + "\n" + "Độ ẩm: " + str(humidity) + "\n" + "Tốc độ gió: " + str(wind) + "\n" +"Mặt trời mọc: " + sunrise + "\n" +"Mặt trời lặn: " + sunset
    label1.config(text= final_info)
    label2.config(text=final_data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather app")

f = ("Poppins",15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(canvas,justify='center',font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas,font=t)
label1.pack()
label2 = tk.Label(canvas,font=f)
label2.pack()
canvas.mainloop()
