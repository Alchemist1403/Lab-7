import json
import requests
import tkinter as tk
from PIL import ImageTk, Image


def click():
    '''Функция выводит новое изображение лисы на экране псоле нажатия кнопки'''

    data = requests.post('https://randomfox.ca/floof/')
    fox_dict = json.loads(data.text)
    response = requests.get(fox_dict["image"], stream=True)
    file_path = 'fox.png'

    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    
    new_img = ImageTk.PhotoImage(Image.open(file_path))
    global label_bg
    label_bg.configure(image=new_img)
    label_bg.image = new_img


root = tk.Tk()
root.title('Cute foxes')
root.geometry('750x750')

label_bg = tk.Label(root)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

btn_key = tk.Button(
    root,
    text = "New fox",
    borderwidth = 7,
    height=5,
    width = 15,
    command=click
    )
btn_key.place(x=600,y=600)

root.mainloop()
