import tkinter as tk
import tkinter.ttk as ttk
import passagem_tk as ptk
import webscrapping as w
import webbrowser


class App:

    def __init__(self):
        self.queue = []
        self.window = tk.Tk()
        self.window.title("Encontrar Passagens")
        self.inputframe = tk.Frame(self.window)
        self.inputframe.grid(row=0, column=0, pady=4)
        self.queueframe = tk.Frame(self.window)
        self.queueframe.grid(row=1, column=0, pady=4)
        self.origem = ptk.EntryPlaceholder(
            self.inputframe, placeholder="Origem", width=10
        )
        self.origem.grid(row=0, column=0, padx=4)
        self.destino = ptk.EntryPlaceholder(
            self.inputframe, placeholder="Destino", width=10
        )
        self.destino.grid(row=0, column=1, padx=4)
        self.dia = ptk.EntryPlaceholder(
            self.inputframe, placeholder="DD", width=3, justify="right"
        )
        self.dia.grid(row=0, column=2, padx=1)
        self.mes = ptk.EntryPlaceholder(
            self.inputframe, placeholder="MM", width=4, justify="right"
        )
        self.mes.grid(row=0, column=3, padx=1)
        self.ano = ptk.EntryPlaceholder(
            self.inputframe, placeholder="AAAA", width=6, justify="right"
        )
        self.ano.grid(row=0, column=4, padx=1)
        self.label_adulto = tk.Label(self.inputframe, text="Adultos", justify="right")
        self.label_adulto.grid(row=0, column=5, padx=(2, 0))
        self.adulto = ttk.Combobox(
            self.inputframe, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], width=2
        )
        self.adulto.grid(row=0, column=6, padx=(0, 2))
        self.label_crianca = tk.Label(self.inputframe, text="Crianças", justify="right")
        self.label_crianca.grid(row=0, column=7, padx=(2, 0))
        self.crianca = ttk.Combobox(
            self.inputframe, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], width=2
        )
        self.crianca.grid(row=0, column=8, padx=(0, 2))
        self.label_bebe = tk.Label(self.inputframe, text="Bebês", justify="right")
        self.label_bebe.grid(row=0, column=9, padx=(2, 0))
        self.bebe = ttk.Combobox(
            self.inputframe, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], width=2
        )
        self.bebe.grid(row=0, column=10, padx=(0, 2))
        self.button_enviar = tk.Button(
            self.inputframe, text="Enviar", command=self.on_click
        )
        self.button_enviar.grid(row=0, column=11, padx=4)
        self.tree = ttk.Treeview(
            columns=("Site", "Saida", "Chegada", "Duracao", "Preco", "Link")
        )
        self.tree.heading("Site", text="Site")
        self.tree.heading("Saida", text="Saida")
        self.tree.heading("Chegada", text="Chegada")
        self.tree.heading("Duracao", text="Duracao")
        self.tree.heading("Preco", text="Preco")
        self.tree.heading("Link", text="Link")
        self.tree.column("#0", stretch=False, minwidth=0, width=0)
        self.tree.column("#1", stretch=False, minwidth=0, width=120)
        self.tree.column("#2", stretch=False, minwidth=0, width=120)
        self.tree.column("#3", stretch=False, minwidth=0, width=120)
        self.tree.column("#4", stretch=False, minwidth=0, width=120)
        self.tree.column("#5", stretch=False, minwidth=0, width=120)
        self.tree.column("#6", stretch=False, minwidth=0, width=120)
        self.tree.bind("<Double-1>", self.tree_double_click)
        self.tree.grid()
        self.window.mainloop()

    def on_click(self):
        origem = self.origem.get()
        destino = self.destino.get()
        ano = int(self.ano.get())
        mes = int(self.mes.get())
        dia = int(self.dia.get())
        adulto = int(self.adulto.get())
        crianca = int(self.crianca.get())
        bebe = int(self.bebe.get())
        self.web_scrap(origem, destino, ano, mes, dia, adulto, crianca, bebe)

    def web_scrap(
        self,
        origem: str,
        destino: str,
        ano: int,
        mes: int,
        dia: int,
        adulto: int,
        crianca: int,
        bebe: int,
    ):
        vaidepromo = w.passagens_vaidepromo(
            origem, destino, ano, mes, dia, adulto, crianca, bebe
        )
        vaidepromo = self.build_dict(vaidepromo)
        maxmilhas = w.passagens_maxmilhas(
            origem, destino, ano, mes, dia, adulto, crianca, bebe
        )
        maxmilhas = self.build_dict(maxmilhas)
        milhas123 = w.passagens_123milhas(
            origem, destino, ano, mes, dia, adulto, crianca, bebe
        )
        milhas123 = self.build_dict(milhas123)
        azul = w.passagens_azul(origem, destino, ano, mes, dia, adulto, crianca, bebe)
        azul = self.build_dict(azul)
        gol = w.passagens_gol(origem, destino, ano, mes, dia, adulto, crianca, bebe)
        gol = self.build_dict(gol)
        latam = w.passagens_latam(origem, destino, ano, mes, dia, adulto, crianca, bebe)
        latam = self.build_dict(latam)
        list = [vaidepromo, maxmilhas, milhas123, azul, gol, latam]
        self.add_queue(f"{origem} - {destino} - {dia:02d}/{mes:02d}/{ano%100}", list)
        self.update_tree(list)

    def build_dict(self, list: list):
        return {
            "site": list[0],
            "saida": list[1],
            "chegada": list[2],
            "duracao": list[3],
            "preco": list[4],
            "link": list[5],
        }

    def update_tree(self, list: list):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in range(len(list)):
            self.tree.insert(
                "",
                0,
                values=(
                    list[i]["site"],
                    list[i]["saida"],
                    list[i]["chegada"],
                    list[i]["duracao"],
                    list[i]["preco"],
                    list[i]["link"],
                ),
            )

    def add_queue(self, name: str, list: list):
        children = self.queueframe.winfo_children()
        if len(self.queue) != 5:
            self.queue.insert(0, list)
        else:
            children[0].destroy()
            self.queue.pop()
            self.queue.insert(0, list)
            children = self.queueframe.winfo_children()
        if children != False:
            for i in children:
                grid = i.grid_info()
                i.grid_forget()
                i.grid(row=grid["row"], column=grid["column"] + 1)
        b = tk.Button(
            self.queueframe,
            text=name,
            command=lambda: self.click_queue(b.grid_info()["column"]),
        )
        b.grid(row=0, column=0)

    def click_queue(self, i):
        self.update_tree(self.queue[i])

    def tree_double_click(self, *args):
        iid = self.tree.selection()
        tree_dict = self.tree.item(iid, option="values")
        return webbrowser.open(tree_dict[-1])


if __name__ == "__main__":
    gui = App()
