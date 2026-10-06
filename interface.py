import tkinter as tk 
from tkinter import ttk

def submit():
    print(listbox.get(listbox.curselection()))

def adicionar():
    listbox.insert(listbox.size(), entrada.get())
    listbox.config(height=listbox.size())

def apagar():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


root = tk.Tk()

root.title("Lanchonete dos amigos")
root.configure(background="cyan")
root.minsize(500, 500)
root.maxsize(500, 500)
root.geometry("300x300+50+50")


label = tk.Label(root, text="Olá mundo", font=100)
label.pack()

tk.Label(root, text="Olá clientes!").pack()


combobox = ttk.Combobox(root, values=["Cardápio", "Cozinha e Pedidos", "Sistema"])
combobox.set("One")
combobox.bind("<<ComboboxSelected>>")
combobox.pack(padx=5, pady=5, fill="x")

listbox = tk.Listbox(root, bg="#f7ffde",font=20)
listbox.pack()
listbox.insert(1, "Pizza")
listbox.config(height=listbox.size())

entrada = tk.Entry(root, text='Insira um produto')
entrada.pack(padx=10, pady=10)

botao_adicionar = tk.Button(root, text="Adicionar à lista", command=adicionar)
botao_adicionar.pack(padx=5, pady=5)

botao_submit = tk.Button(root, text="Enviar Pedido", command=submit)
botao_submit.pack(padx=5, pady=5)

botao_apagar = tk.Button(root, text="Remover da lista", command=apagar)
botao_apagar.pack(padx=5, pady=5)

root.mainloop()
