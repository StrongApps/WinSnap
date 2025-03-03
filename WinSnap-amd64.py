import tkinter as tk
from tkinter import messagebox
import requests
import os
print("app: started, 0 errors")

class AppStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Win-Snap 0.3a")

        self.label = tk.Label(root, text="Добро пожаловать! Выберите приложение:")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.app_list = {
            "unknown_1": "http://example.com/app1.exe",
            "unknown_2": "http://example.com/app2.exe",
            "unknown_3": "http://example.com/app3.exe",
            "unknown_4": "http://example.com/app4.exe",
            "unknown_5": "http://example.com/app5.exe",
            "unknown_6": "http://example.com/app6.exe",
            "unknown_7": "http://example.com/app7.exe",
            "unknown_8": "http://example.com/app8.exe",
            "unknown_9": "http://example.com/app9.exe",
            "Проверить обновления WinSnap": "https://StrongApps.github.io/WinSnap/WinSnap-amd64.py",
        }

        # Создаем кнопки для каждого приложения и размещаем их в сетке
        row = 1
        col = 0
        for app_name, url in self.app_list.items():
            button = tk.Button(root, text=app_name, command=lambda url=url, app_name=app_name: self.download_app(url, app_name))
            button.grid(row=row, column=col, padx=10, pady=5, sticky='ew')

            col += 1
            if col > 2:  # Переход на следующую строку после 3 кнопок
                col = 0
                row += 1

    def download_app(self, url, app_name):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка на ошибки HTTP

            file_path = os.path.join(os.getcwd(), f"{app_name}.exe")
            with open(file_path, 'wb') as file:
                file.write(response.content)

            messagebox.showinfo("Успех", f"{app_name} успешно загружено!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("unsuccessful", f"WinSnap не удалось загрузить {app_name}, Ошибка:n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app_store = AppStore(root)
    root.mainloop()
