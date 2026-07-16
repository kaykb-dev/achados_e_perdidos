import customtkinter as ctk
from tkinter import ttk


class TelaCorrespondencias(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        ctk.CTkLabel(
            self,
            text="Correspondências Encontradas",
            font=("Arial",22,"bold")
        ).pack(pady=20)

        colunas = (
            "ID",
            "Item Perdido",
            "Item Encontrado",
            "Compatibilidade",
            "Status"
        )

        self.tabela = ttk.Treeview(
            self,
            columns=colunas,
            show="headings",
            height=15
        )

        larguras = {
            "ID":50,
            "Item Perdido":180,
            "Item Encontrado":180,
            "Compatibilidade":120,
            "Status":120
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

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tabela.yview
        )

        self.tabela.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabela.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(20,0),
            pady=20
        )

        scrollbar.pack(
            side="right",
            fill="y",
            pady=20
        )

        ctk.CTkButton(
            self,
            text="Atualizar",
            command=self.carregar_correspondencias
        ).pack(pady=15)

        self.carregar_correspondencias()

    def carregar_correspondencias(self):

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for correspondencia in self.sistema.listar_correspondencias():

            self.tabela.insert(
                "",
                "end",
                values=(
                    correspondencia.get_id(),
                    correspondencia.get_item_perdido().get_nome(),
                    correspondencia.get_item_encontrado().get_nome(),
                    f"{correspondencia.get_porcentagem():.1f}%",
                    correspondencia.get_status().get_nome()
                )
            )
    