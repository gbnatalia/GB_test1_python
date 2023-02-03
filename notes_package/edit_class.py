import tkinter as tk



class Editor(tk.Tk):

    def __init__(self, title, text):
        '''
        конструктор класса
        '''
        super().__init__()
        self.title(f'Редактор заметки "{title}"')
        self.geometry('500x270')
        self.res = text
        text_logo = ""
        for el in list(title):
            text_logo += f" {el}"

        # -------------------------------------------------------
        # Строка логотипа
        f_logo = tk.Frame(self, width=20)
        f_logo.pack(side=tk.TOP, expand=0, fill='x')
        l_logo1 = tk.Label(f_logo, text=text_logo, bg='blue', fg="red",
                           font=("Times New Roman", 20))
        l_logo1.pack(side=tk.LEFT, expand=True, fill='x')
        # -------------------------------------------------------
        text_frame = tk.Frame(self, pady=10, padx = 10)
        text_frame.pack()
        self.text_edit = tk.Text(text_frame, height=10)
        self.text_edit.pack()
        self.text_edit.insert(tk.END, text)
        # -------------------------------------------------------
        # Область кнопки "Установить"
        btn_frame = tk.Frame(self, pady=10, padx=10)
        btn_frame.pack(side=tk.TOP, expand=0, fill='x')

        ok_btn = tk.Button(btn_frame, text="Принять", width=10,
                        command=lambda: self.on_submit())
        ok_btn.pack(side=tk.RIGHT, padx=10)

        cansel_btn = tk.Button(btn_frame, text="Отмена", width=10,
                        command=lambda: self.destroy())
        cansel_btn.pack(side=tk.RIGHT, padx=10)
        # -------------------------------------------------------
    def on_submit(self):
        self.res = self.text_edit.get(0.3, tk.END)
        self.destroy()

if __name__ == "__main__":
    app = Editor("Заметка 1", "2222222")
    app.mainloop()
    print(app.res)