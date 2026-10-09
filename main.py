import tkinter as tk
from tkinter import ttk, messagebox
from processamento import Restaurante

r = Restaurante()
atual = []

def erro(m):
    messagebox.showerror('Erro', m)

def texto_pedido(p):
    return f"{p['cliente']}: " + ', '.join(i['nome'] for i in p['itens'])

def preencher(lb, linhas):
    lb.delete(0, 'end')
    for l in linhas:
        lb.insert('end', l)

def atualizar():
    tv.delete(*tv.get_children())
    for i in r.cardapio:
        tv.insert('', 'end', values=(i['id'], i['nome'], f"R$ {i['preco']:.2f}"))
    preencher(lb_cardapio, [f"{i['id']} - {i['nome']}" for i in r.cardapio])
    preencher(lb_atual, [i['nome'] for i in atual])
    preencher(lb_fila, [texto_pedido(p) for p in r.itens_fila()])
    preencher(lb_hist, r.historico_acoes())

def cadastrar():
    try:
        id = int(e_id.get())
        preco = float(e_preco.get().replace(',', '.'))
        r.cadastrar_item(id, e_nome.get().strip(), preco)
    except ValueError as ex:
        return erro('Dados inválidos.' if 'literal' in str(ex) or 'convert' in str(ex) else str(ex))
    for e in (e_id, e_nome, e_preco):
        e.delete(0, 'end')
    atualizar()

def remover():
    sel = tv.selection()
    if not sel:
        return erro('Selecione um item.')
    try:
        r.remover_item(int(tv.item(sel[0])['values'][0]))
    except ValueError as ex:
        return erro(str(ex))
    atualizar()

def adicionar_pedido():
    sel = lb_cardapio.curselection()
    if not sel:
        return erro('Selecione um item do cardápio.')
    atual.append(r.cardapio[sel[0]])
    atualizar()

def limpar_pedido():
    atual.clear()
    atualizar()

def lancar():
    try:
        r.lancar_pedido(e_cliente.get().strip(), [i['id'] for i in atual])
    except ValueError as ex:
        return erro(str(ex))
    atual.clear()
    e_cliente.delete(0, 'end')
    atualizar()

def atender():
    try:
        p = r.atender_pedido()
    except ValueError as ex:
        return erro(str(ex))
    messagebox.showinfo('Pedido atendido', texto_pedido(p))
    atualizar()

def desfazer():
    try:
        a = r.desfazer()
    except ValueError as ex:
        return erro(str(ex))
    messagebox.showinfo('Desfeito', a)
    atualizar()

root = tk.Tk()
root.title('Restaurante FastBite')
root.geometry('650x520')

abas = ttk.Notebook(root)
abas.pack(fill='both', expand=True, padx=5, pady=5)
a1, a2, a3 = ttk.Frame(abas), ttk.Frame(abas), ttk.Frame(abas)
abas.add(a1, text='Cardápio')
abas.add(a2, text='Cozinha e Pedidos')
abas.add(a3, text='Sistema')

tv = ttk.Treeview(a1, columns=('id', 'nome', 'preco'), show='headings', height=10)
for c, t in (('id', 'ID'), ('nome', 'Nome'), ('preco', 'Preço')):
    tv.heading(c, text=t)
tv.pack(fill='x', padx=10, pady=10)

f = ttk.Frame(a1)
f.pack(pady=5)
e_id, e_nome, e_preco = ttk.Entry(f, width=8), ttk.Entry(f, width=25), ttk.Entry(f, width=10)
for n, (t, e) in enumerate((('ID', e_id), ('Nome', e_nome), ('Preço', e_preco))):
    ttk.Label(f, text=t).grid(row=0, column=n)
    e.grid(row=1, column=n, padx=3)
ttk.Button(a1, text='Cadastrar item', command=cadastrar).pack(pady=3)
ttk.Button(a1, text='Remover item selecionado', command=remover).pack(pady=3)

esq, dir = ttk.Frame(a2), ttk.Frame(a2)
esq.pack(side='left', fill='both', expand=True, padx=10, pady=10)
dir.pack(side='left', fill='both', expand=True, padx=10, pady=10)

ttk.Label(esq, text='CARDÁPIO').pack()
lb_cardapio = tk.Listbox(esq, height=7, exportselection=False)
lb_cardapio.pack(fill='x')
ttk.Button(esq, text='Adicionar ao pedido', command=adicionar_pedido).pack(pady=3)
ttk.Label(esq, text='PEDIDO ATUAL').pack()
lb_atual = tk.Listbox(esq, height=7)
lb_atual.pack(fill='x')
ttk.Label(esq, text='Cliente').pack()
e_cliente = ttk.Entry(esq)
e_cliente.pack(fill='x')
ttk.Button(esq, text='Lançar pedido', command=lancar).pack(pady=3)
ttk.Button(esq, text='Limpar pedido', command=limpar_pedido).pack()

ttk.Label(dir, text='FILA DA COZINHA').pack()
lb_fila = tk.Listbox(dir, height=18)
lb_fila.pack(fill='both', expand=True)
ttk.Button(dir, text='Atender próximo pedido', command=atender).pack(pady=3)

ttk.Button(a3, text='Desfazer última ação', command=desfazer).pack(pady=10)
ttk.Label(a3, text='HISTÓRICO DE AÇÕES').pack()
lb_hist = tk.Listbox(a3, height=18)
lb_hist.pack(fill='both', expand=True, padx=10, pady=10)

atualizar()
root.mainloop()
