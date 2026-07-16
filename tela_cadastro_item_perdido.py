import customtkinter as ctk

from codigo import Categoria

class TelaCadastroItemPerdido(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        ctk.CTkLabel(
            self,
            text="Cadastro de Item Perdido",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        self.entry_nome = ctk.CTkEntry(
            self,
            placeholder_text="Nome do item",
            width=350
        )
        self.entry_nome.pack(pady=10)

        self.entry_descricao = ctk.CTkEntry(
            self,
            placeholder_text="Descrição",
            width=350
        )
        self.entry_descricao.pack(pady=10)

        self.entry_categoria = ctk.CTkEntry(
            self,
            placeholder_text="Categoria (Ex.: Eletrônicos)",
            width=350
        )
        self.entry_categoria.pack(pady=10)

        self.entry_cor = ctk.CTkEntry(
            self,
            placeholder_text="Cor",
            width=350
        )
        self.entry_cor.pack(pady=10)

        self.entry_local = ctk.CTkEntry(
            self,
            placeholder_text="Último local onde foi visto",
            width=350
        )
        self.entry_local.pack(pady=10)

        self.entry_data = ctk.CTkEntry(
            self,
            placeholder_text="Data da perda (dd/mm/aaaa)",
            width=350
        )
        self.entry_data.pack(pady=10)

        ctk.CTkLabel(
            self,
            text="Usuário"
        ).pack(pady=(10,0))

        usuarios = [
            f"{usuario.get_id()} - {usuario.get_nome()}"
            for usuario in self.sistema.listar_usuarios()
        ]

        self.combo_usuario = ctk.CTkComboBox(
            self,
            values=usuarios if usuarios else ["Nenhum usuário cadastrado"],
            width=350
        )

        self.combo_usuario.pack(pady=10)

        self.label_resultado = ctk.CTkLabel(
            self,
            text=""
        )
        self.label_resultado.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Cadastrar",
            command=self.cadastrar_item
        ).pack(pady=15)

        
    def cadastrar_item(self):

        nome = self.entry_nome.get().strip()
        descricao = self.entry_descricao.get().strip()
        categoria = Categoria(
            self.entry_categoria.get().strip()
        )
        cor = self.entry_cor.get().strip()
        local = self.entry_local.get().strip()
        data = self.entry_data.get().strip()

        usuario_selecionado = self.combo_usuario.get()

        id_usuario = int(
            usuario_selecionado.split(" - ")[0]
        )

        usuario = self.sistema.buscar_usuario_por_id(
            id_usuario
        )

        if (
            not nome or
            not descricao or
            not categoria.get_nome() or
            not cor or
            not local or
            not data
        ):

            self.label_resultado.configure(
                text="Preencha todos os campos.",
                text_color="red"
            )
            return

        self.sistema.cadastrar_item_perdido(nome, descricao, categoria, cor, local, data, usuario)

        self.label_resultado.configure(
            text="Item perdido cadastrado com sucesso!",
            text_color="green"
        )

        self.entry_nome.delete(0, "end")
        self.entry_descricao.delete(0, "end")
        self.entry_categoria.delete(0, "end")
        self.entry_cor.delete(0, "end")
        self.entry_local.delete(0, "end")
        self.entry_data.delete(0, "end")