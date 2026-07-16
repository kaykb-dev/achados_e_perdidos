import customtkinter as ctk

from codigo import StatusSolicitacao


class TelaSolicitacoes(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        ctk.CTkLabel(
            self,
            text="Solicitação de Devolução",
            font=("Arial",22,"bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            self,
            text="Correspondência"
        ).pack()

        correspondencias = [

            f"{c.get_id()} - "
            f"{c.get_item_perdido().get_nome()} "
            f"↔ "
            f"{c.get_item_encontrado().get_nome()}"

            for c in self.sistema.listar_correspondencias()

        ]

        self.combo = ctk.CTkComboBox(
            self,
            values=correspondencias
            if correspondencias
            else ["Nenhuma correspondência"],
            width=400
        )

        self.combo.pack(pady=10)

        self.texto = ctk.CTkTextbox(
            self,
            width=400,
            height=120
        )

        self.texto.pack(pady=15)

        self.label_resultado = ctk.CTkLabel(
            self,
            text=""
        )

        self.label_resultado.pack()

        ctk.CTkButton(
            self,
            text="Solicitar Devolução",
            command=self.solicitar
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="Aceitar",
            command=self.aceitar
        ).pack(pady=5)

        ctk.CTkButton(
            self,
            text="Recusar",
            command=self.recusar
        ).pack(pady=5)

    def solicitar(self):

        try:
            id_correspondencia = int(
                self.combo.get().split(" - ")[0]
            )

        except ValueError:
            self.label_resultado.configure(
                text="Selecione uma correspondência.",
                text_color="red"
            )
            return

        justificativa = self.texto.get(
            "1.0",
            "end"
        ).strip()

        if not justificativa:
            self.label_resultado.configure(
                text="Digite uma justificativa.",
                text_color="red"
            )
            return

        correspondencia = self.sistema.buscar_correspondencia_por_id(
            id_correspondencia
        )

        if correspondencia is None:
            self.label_resultado.configure(
                text="Correspondência não encontrada.",
                text_color="red"
            )
            return

        usuario = (
            correspondencia
            .get_item_perdido()
            .get_usuario()
        )

        self.sistema.criar_solicitacao(
            usuario,
            correspondencia,
            justificativa
        )

        self.label_resultado.configure(
            text="Solicitação enviada!",
            text_color="green"
        )

        self.texto.delete(
            "1.0",
            "end"
        )

    def aceitar(self):

        try:
            id_solicitacao = int(
                self.combo.get().split(" - ")[0]
            )
        except:
            return

        self.sistema.aceitar_solicitacao(
            id_solicitacao
        )

        self.carregar_solicitacoes()

    def recusar(self):

        try:
            id_solicitacao = int(
                self.combo.get().split(" - ")[0]
            )
        except:
            return

        self.sistema.recusar_solicitacao(
            id_solicitacao
        )

        self.carregar_solicitacoes()

    def carregar_solicitacoes(self):

        solicitacoes = [

            f"{s.get_id()} - "
            f"{s.get_correspondencia().get_item_perdido().get_nome()}"

            for s in self.sistema.listar_solicitacoes()
        ]

        if not solicitacoes:
            solicitacoes = ["Nenhuma solicitação"]

        self.combo.configure(
            values=solicitacoes
        )

        self.combo.set(solicitacoes[0])