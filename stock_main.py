import customtkinter

class App(customtkinter.CTk):
    customtkinter.set_appearance_mode("dark")
    def __init__(self):
        super().__init__()

        self.title("Gerenciador de Estoque py")
        self.geometry("400x400")
        self.grid_columnconfigure((0, 1), weight=1)
        self.resizable(False, False)

        #Campo de nome do produto
        # self.stateName = customtkinter.StringVar()
        self.labelNameProduct = customtkinter.CTkLabel(self, text="Nome do produto: ", fg_color="transparent", anchor="w")
        self.labelNameProduct.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.entryNameProduct = customtkinter.CTkEntry(self, placeholder_text="nome", textvariable=self.stateName)
        self.entryNameProduct.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Campo de quantidade do produto
        self.labelNumberProducts = customtkinter.CTkLabel(self, text="Quantidade do produto: ", fg_color="transparent", anchor="w")
        self.labelNumberProducts.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.entryNumberProducts = customtkinter.CTkEntry(self, placeholder_text="quantidade")
        self.entryNumberProducts.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Campo do setor do produto
        self.labelSectorProducts = customtkinter.CTkLabel(self, text="Código do produto: ", fg_color="transparent", anchor="w")
        self.labelSectorProducts.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.checkboxSectorProduct = customtkinter.CTkComboBox(self, values=["Setor 1", "Setor 2", "Setor 3"], command=self.combobox_callback)
        self.checkboxSectorProduct.grid(row=2, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Campo de código do produto
        self.labelCodeProducts = customtkinter.CTkLabel(self, text="Código do produto: ", fg_color="transparent", anchor="w")
        self.labelCodeProducts.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.entryCodeProducts = customtkinter.CTkEntry(self, placeholder_text="número")
        self.entryCodeProducts.grid(row=3, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Botão de cadastro do produto
        self.button = customtkinter.CTkButton(self, text="Cadastrar", command=self.button_registrate)
        self.button.grid(row=10, column=0, padx=150, pady=150, sticky="nsew", columnspan=2)

    def button_registrate(self, stateName):
        self.name = stateName.get()
        print(self.name)

    def combobox_callback(self, choice):
        print("Selecionado: ", choice)


app = App()
app.mainloop()