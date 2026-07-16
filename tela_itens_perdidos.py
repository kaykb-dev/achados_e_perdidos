import customtkinter as ctk
from tkinter import ttk


class TelaItensPerdidos(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        ctk.CTkLabel(
            self,
            text="Itens Perdidos",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        frame_tabela = ctk.CTkFrame(self)
        frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

        colunas = (
            "ID",
            "Nome",
            "Descrição",
            "Categoria",
            "Cor",
            "Status",
            "Local",
            "Data",
            "Usuário"
        )

        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=colunas,
            show="headings",
            height=15
        )

        larguras = {
            "ID": 50,
            "Nome": 140,
            "Descrição": 220,
            "Categoria": 120,
            "Cor": 100,
            "Status": 120,
            "Local": 120,
            "Data": 100,
            "Usuário": 150
        }

        for coluna in colunas:

            self.tabela.heading(
                coluna,
                text=coluna
            )

            self.tabela.column(
                coluna,
                width=larguras[coluna],
                anchor="center"
            )

        scrollbar_y = ttk.Scrollbar(
            frame_tabela,
            orient="vertical",
            command=self.tabela.yview
        )

        scrollbar_x = ttk.Scrollbar(
            frame_tabela,
            orient="horizontal",
            command=self.tabela.xview
        )

        self.tabela.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.tabela.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        frame_tabela.grid_rowconfigure(
            0,
            weight=1
        )

        frame_tabela.grid_columnconfigure(
            0,
            weight=1
        )

        ctk.CTkButton(
            self,
            text="Atualizar",
            command=self.carregar_itens
        ).pack(pady=15)

        self.carregar_itens()

    def get_local(self):
        return self._local

    def get_data(self):
        return self._data

    def get_usuario(self):
        return self._usuario
    
    def carregar_itens(self):

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for item in self.sistema.listar_itens_perdidos():

            self.tabela.insert(
                "",
                "end",
                values=(
                    item.get_id(),
                    item.get_nome(),
                    item.get_descricao(),
                    item.get_categoria().get_nome(),
                    item.get_cor(),
                    item.get_status().get_nome(),
                    item.get_local(),
                    item.get_data(),
                    item.get_usuario().get_nome()
                )
            )
