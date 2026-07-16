import customtkinter as ctk

from tela_inicio import TelaInicio
from tela_cadastro_item_perdido import TelaCadastroItemPerdido
from tela_itens_perdidos import TelaItensPerdidos
from tela_cadastro_item_encontrado import TelaCadastroItemEncontrado
from tela_itens_encontrados import TelaItensEncontrados
from tela_correspondencias import TelaCorrespondencias
from tela_solicitacoes import TelaSolicitacoes
from tela_notificacoes import TelaNotificacoes
from tela_usuario import TelaUsuario


class Interface:

    def __init__(self, sistema):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.janela = ctk.CTk()
        self.janela.title("Sistema de Achados e Perdidos")
        self.janela.geometry("900x650")
        self.janela.resizable(False, False)

        self.sistema = sistema
        self.criar_header()
        self.criar_body()
        self.criar_menu()

        self.frame_atual = None
        self.mostrar_inicio()

    def criar_header(self):

        header = ctk.CTkFrame(self.janela, height=60)
        header.pack(fill="x")

        titulo = ctk.CTkLabel(
            header,
            text="Sistema de Achados e Perdidos",
            font=("Arial",24,"bold")
        )

        titulo.pack(pady=15)

    def criar_body(self):

        self.body = ctk.CTkFrame(
            self.janela,
            fg_color="transparent"
        )

        self.body.pack(fill="both", expand=True)

    def criar_menu(self):

        menu = ctk.CTkFrame(self.body,width=220)
        menu.pack(side="left",fill="y",padx=15,pady=15)
        menu.pack_propagate(False)

        ctk.CTkLabel(
            menu,
            text="MENU",
            font=("Arial",20,"bold")
        ).pack(pady=(20,30))

        ctk.CTkButton(
            menu,
            text="🏠 Início",
            command=self.mostrar_inicio
        ).pack(pady=8)

        ctk.CTkButton(
            menu,
            text="📌 Cadastrar Item Perdido",
            command=self.mostrar_item_perdido
        ).pack(pady=8)

        ctk.CTkButton(
            menu,
            text="📋 Itens Perdidos",
            command=self.mostrar_itens_perdidos
        ).pack(pady=8)

        ctk.CTkButton(
            menu,
            text="📦 Cadastrar Item Encontrado",
            command=self.mostrar_item_encontrado
        ).pack(pady=8)

        ctk.CTkButton(
            menu,
            text="📋 Itens Encontrados",
            command=self.mostrar_itens_encontrados
        ).pack(pady=8)

        ctk.CTkButton(
            menu,
            text="🔍 Correspondências",
            command=self.mostrar_correspondencias
        ).pack(pady=8)


        ctk.CTkButton(
            menu,
            text="🔔 Notificações",
            command=self.mostrar_notificacoes
        ).pack(pady=8)


        ctk.CTkButton(
            menu,
            text="📨 Solicitações",
            command=self.mostrar_solicitacoes
        ).pack(pady=8)


        ctk.CTkButton(
            menu,
            text="👤 Usuário",
            command=self.mostrar_usuario
        ).pack(pady=8)

    def trocar_frame(self, frame):

        if self.frame_atual is not None:
            self.frame_atual.destroy()

        self.frame_atual = frame(self.body,self.sistema)

        self.frame_atual.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(0,15),
            pady=15
        )

    def mostrar_inicio(self):
        self.trocar_frame(TelaInicio)

    def mostrar_cadastro(self):
        self.trocar_frame(TelaCadastroItemPerdido)

    def mostrar_usuario(self):
        self.trocar_frame(TelaUsuario)

    def mostrar_item_perdido(self):

        self.trocar_frame(
            TelaCadastroItemPerdido
        )

    def mostrar_itens_perdidos(self):
        self.trocar_frame(TelaItensPerdidos)

    def mostrar_item_encontrado(self):

        self.trocar_frame(
            TelaCadastroItemEncontrado
        )

    def mostrar_itens_encontrados(self):
        self.trocar_frame(TelaItensEncontrados)

    def mostrar_correspondencias(self):

        self.trocar_frame(
            TelaCorrespondencias
        )


    def mostrar_notificacoes(self):

        self.trocar_frame(
            TelaNotificacoes
        )


    def mostrar_solicitacoes(self):

        self.trocar_frame(
            TelaSolicitacoes
        )

    def executar(self):
        self.janela.mainloop()