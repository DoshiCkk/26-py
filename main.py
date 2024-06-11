import tkinter as tk
import requests

class JsonDownloader:
    def __init__(self, window):
        self.window = window
        window.title('Выводит json файл и сохраняет')
        window.geometry('300x200')

        self.label = tk.Label(window, text='введите ID: ')
        self.entry = tk.Entry(window)
        self.button = tk.Button(window, text="сохранить", command=self.get_text)

        self.label.pack()
        self.entry.pack()
        self.button.pack()

    def get_text(self):
        integ = int(self.entry.get())
        url = f'https://jsonplaceholder.typicode.com/todos/{integ}'
        req = requests.get(url)
        with open(f'data{integ}.json', 'w') as file:
            file.write(req.text)



window = tk.Tk()
app = JsonDownloader(window)
window.mainloop()