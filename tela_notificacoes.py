import customtkinter as ctk
from tkinter import ttk


class TelaNotificacoes(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        ctk.CTkLabel(
            self,
            text="Notificações",
            font=("Arial",22,"bold")
        ).pack(pady=20)


        colunas = (
            "ID",
            "Destinatário",
            "Mensagem",
            "Data",
            "Lida"
        )


        # Frame para conter tabela + scrollbars
        frame_tabela = ctk.CTkFrame(self)
        frame_tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )


        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=colunas,
            show="headings",
            height=15
        )


        larguras = {
            "ID":50,
            "Destinatário":180,
            "Mensagem":350,
            "Data":100,
            "Lida":80
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


        # Scroll vertical
        scrollbar_y = ttk.Scrollbar(
            frame_tabela,
            orient="vertical",
            command=self.tabela.yview
        )


        # Scroll horizontal
        scrollbar_x = ttk.Scrollbar(
            frame_tabela,
            orient="horizontal",
            command=self.tabela.xview
        )


        self.tabela.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )


        # Posicionamento da tabela
        self.tabela.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


        # Scroll vertical
        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )


        # Scroll horizontal
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
            command=self.carregar_notificacoes
        ).pack(pady=15)


        self.carregar_notificacoes()


    def carregar_notificacoes(self):

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)


        for notificacao in self.sistema.listar_notificacoes():

            self.tabela.insert(
                "",
                "end",
                values=(
                    notificacao.get_id(),
                    notificacao.get_destinatario().get_nome(),
                    notificacao.get_mensagem(),
                    notificacao.get_data_envio(),
                    "Sim" if notificacao.foi_lida() else "Não"
                )
            )