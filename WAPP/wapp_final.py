from tkinter import *
import requests

# APP
root = Tk()
root.geometry('400x400')
root.title('Weather App')
root.resizable(0,0)

# IMAGES 
bg_image=PhotoImage(file='bg1.png')
bg_label=Label(root,image=bg_image)
bg_label.place(relwidth=1,relheight=1)
root.iconbitmap('kweather.ico')

# FUNCTIONS
def format_response(weather):
    try:
        name = weather['name']
        des = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = '''City: %s
Conditions: %s
Temperature(°C): %s''' % (name, des, temp)

    except:
        final_str = '''  There was a problem 
  retrieving that information'''

    return final_str

def get_weather(city):
    global info_label
    weather_key = '74c153bcefd81616aab804f6434acc5b'

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    info_label.destroy()
    info_label = Label(output_frame, font=('Consolas 10'), bg='light gray', text=format_response(weather),
                       justify='left',)
    info_label.place(relx=0.4, rely=0.45, anchor='center')

# FRAMES, ENTRY BOX & LABEL
output_frame = Frame(bg_label, height=180, width=340,bg='light gray').place(relx=0.5, rely=0.6, anchor='center')

city_entry = Entry(bg_label, width=15, bg='beige', font='Times 16')
city_entry.place(relx=0.4, rely=0.225, anchor='center')

get_button = Button(bg_label, text='Get', bg='beige', font=('Times 15', 13),
                    width=7,command=lambda: get_weather(city_entry.get()))
get_button.place(relx=0.725, rely=0.225, anchor='center')

info_label = Label(output_frame, bg='light gray')
info_label.place(relx=0.325, rely=0.45, anchor='center')

# RUN THE APP
root.mainloop()

