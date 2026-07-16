import customtkinter as ctk
from tkinter import ttk


class TelaUsuario(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        ctk.CTkLabel(
            self,
            text="Cadastro de Usuário",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        # ================= Formulário =================

        self.entry_nome = ctk.CTkEntry(
            self,
            placeholder_text="Nome",
            width=300
        )
        self.entry_nome.pack(pady=5)

        self.entry_telefone = ctk.CTkEntry(
            self,
            placeholder_text="Telefone",
            width=300
        )
        self.entry_telefone.pack(pady=5)

        self.entry_email = ctk.CTkEntry(
            self,
            placeholder_text="E-mail",
            width=300
        )
        self.entry_email.pack(pady=5)

        ctk.CTkButton(
            self,
            text="Cadastrar",
            command=self.cadastrar_usuario
        ).pack(pady=15)

        # ================= Tabela =================

        frame_tabela = ctk.CTkFrame(self)
        frame_tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        colunas = (
            "ID",
            "Nome",
            "Telefone",
            "E-mail",
            "Data Cadastro"
        )

        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=colunas,
            show="headings",
            height=8
        )

        larguras = {
            "ID": 50,
            "Nome": 180,
            "Telefone": 140,
            "E-mail": 220,
            "Data Cadastro": 120
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

        self.tabela.configure(
            yscrollcommand=scrollbar_y.set
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
            command=self.carregar_usuarios
        ).pack(pady=10)

        self.carregar_usuarios()

    def cadastrar_usuario(self):

        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()

        if not nome or not telefone or not email:
            return

        self.sistema.cadastrar_usuario(
            nome,
            telefone,
            email
        )

        self.entry_nome.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_email.delete(0, "end")

        self.carregar_usuarios()

    def carregar_usuarios(self):

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for usuario in self.sistema.listar_usuarios():

            self.tabela.insert(
                "",
                "end",
                values=(
                    usuario.get_id(),
                    usuario.get_nome(),
                    usuario.get_telefone(),
                    usuario.get_email(),
                    usuario.get_data_cadastro()
                )
            )