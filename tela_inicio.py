import customtkinter as ctk


class TelaInicio(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="Bem-vindo!",
            font=("Arial",24,"bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            self,
            text="Selecione uma opção no menu."
        ).pack()

        cards = ctk.CTkFrame(self,fg_color="transparent")
        cards.pack(pady=40)

        for texto,coluna in [
            ("Cadastrar\nItem",0),
            ("Tabela\nItens",1),
            ("Cadastro\nUsuário",2)
        ]:

            card = ctk.CTkFrame(
                cards,
                width=180,
                height=140
            )

            card.grid(row=0,column=coluna,padx=15)
            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=texto,
                font=("Arial",18,"bold")
            ).pack(expand=True)