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
        self.stateName = customtkinter.StringVar()
        self.labelNameProduct = customtkinter.CTkLabel(self, text="Nome do produto: ", fg_color="transparent", anchor="w")
        self.labelNameProduct.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.entryNameProduct = customtkinter.CTkEntry(self, textvariable=self.stateName, placeholder_text="nome")
        self.entryNameProduct.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Campo de quantidade do produto
        self.stateQuantity = customtkinter.StringVar()
        self.labelNumberProducts = customtkinter.CTkLabel(self, text="Quantidade do produto: ", fg_color="transparent", anchor="w")
        self.labelNumberProducts.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.entryNumberProducts = customtkinter.CTkEntry(self, textvariable=self.stateQuantity, placeholder_text="quantidade")
        self.entryNumberProducts.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Campo do setor do produto
        self.labelSectorProducts = customtkinter.CTkLabel(self, text="Código do produto: ", fg_color="transparent", anchor="w")
        self.labelSectorProducts.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.checkboxSectorProduct = customtkinter.CTkComboBox(self, values=["Setor 1", "Setor 2", "Setor 3"])
        self.checkboxSectorProduct.grid(row=2, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)
        # command=self.combobox_callback

        #Campo de código do produto
        self.stateCode = customtkinter.StringVar()
        self.labelCodeProducts = customtkinter.CTkLabel(self, text="Código do produto: ", fg_color="transparent", anchor="w")
        self.labelCodeProducts.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.entryCodeProducts = customtkinter.CTkEntry(self, textvariable=self.stateCode, placeholder_text="número")
        self.entryCodeProducts.grid(row=3, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        #Botão de cadastro do produto
        self.button = customtkinter.CTkButton(self, text="Cadastrar", command=self.button_registrate)
        self.button.grid(row=4, column=0, padx=15, pady=120)

        self.button2 = customtkinter.CTkButton(self, text="Pesquisar", command=self.search_window)
        self.button2.grid(row=4, column=1, padx=15, pady=120)

    def button_registrate(self):
        name = self.stateName.get()
        quantity = self.stateQuantity.get()
        sector = self.checkboxSectorProduct.get()
        codeProduct = self.stateCode.get()
        print(name, quantity, sector, codeProduct)
        return self.write_database(name, quantity, sector, codeProduct)
    
    def write_database(self, name, quantity, sector, codeProduct):
        with open('db.txt', 'r+') as file:
            content = file.read()
        with open('db.txt', 'w') as file:
            file.write(content + f"\n{name}, {quantity}, {sector}, {codeProduct}")
        return
    
    def search_window(self):
        global secondWindow
        secondWindow = None
        if secondWindow is None or not secondWindow.winfo_exists():
            secondWindow = customtkinter.CTkToplevel()
            secondWindow.title("Pesquisa de material")
            secondWindow.geometry("400x400")
            secondWindow.grid_columnconfigure((0, 1), weight=1)
            # secondWindow.resizable(False, False)
            secondWindow.labelWarning = customtkinter.CTkLabel(secondWindow, text="Você deve preencher todos os valores.", fg_color="transparent")
            secondWindow.labelWarning.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        secondWindow.lift()

app = App()
app.mainloop()