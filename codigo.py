import csv
from abc import ABC, abstractmethod
from datetime import date

class Usuario:
    """
    Representa um usuário cadastrado no sistema.

    Relacionamentos:
    - Agregação com SistemaAchadosPerdidos.
    - Dependência de Notificacao (destinatário das notificações).
    """


    def __init__(self, id: int, nome: str, telefone: str, email: str, data_cadastro: str):
        self._id = id
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._data_cadastro = data_cadastro

    def get_id(self) -> int:
        return self._id

    def get_nome(self) -> str:
        return self._nome

    def get_telefone(self) -> str:
        return self._telefone

    def get_email(self) -> str:
        return self._email
    
    def get_data_cadastro(self):
        return self._data_cadastro

    def atualizar_dados(self, nome, telefone, email) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email


class Categoria:
    """
    Representa a categoria de um item.

    Relacionamentos:
    - Associação com Item.
    - Dependência de PersistenciaCSV (durante o carregamento dos dados).
    """
    def __init__(self, nome: str):
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome

    def __str__(self):
        return f"Categoria: {self._nome}"


class StatusItem:
    """
    Representa o status atual de um item.

    Relacionamentos:
    - Associação com Item.
    - Dependência de PersistenciaCSV (durante o carregamento dos dados).
    """

    def __init__(self, nome: str, descricao: str):
        self._nome = nome
        self._descricao = descricao

    def get_nome(self) -> str:
        return self._nome

    def get_descricao(self) -> str:
        return self._descricao

    @staticmethod
    def criar_por_nome(nome: str):

        if nome == "Perdido":
            return StatusItem(
                "Perdido",
                "Item perdido."
            )

        if nome == "Encontrado":
            return StatusItem(
                "Encontrado",
                "Item encontrado."
            )

        if nome == "Devolvido":
            return StatusItem(
                "Devolvido",
                "Item devolvido ao proprietário."
            )

        return StatusItem(
            nome,
            ""
        )

    def __str__(self):
        return f"Nome: {self._nome}\nDescrição: {self._descricao}"

class Item(ABC):
    """
    Representa um item cadastrado no sistema.

    Relacionamentos:
    - Associação com Categoria.
    - Associação com StatusItem.
    - Superclasse de ItemEncontrado (Herança).
    """
    def __init__(self, id: int, nome: str, descricao: str, categoria: Categoria, cor: str, status: StatusItem):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._categoria: Categoria = categoria
        self._cor = cor
        self._status: StatusItem = status

    def get_id(self) -> int:
        return self._id

    def get_nome(self) -> str:
        return self._nome

    def get_descricao(self) -> str:
        return self._descricao

    def get_categoria(self) -> Categoria:
        return self._categoria

    def get_cor(self) -> str:
        return self._cor

    def get_status(self) -> StatusItem:
        return self._status


    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass

class ItemEncontrado(Item):
    """
    Representa um item encontrado cadastrado no sistema.

    Relacionamentos:
    - Herança de Item.
    - Agregação com SistemaAchadosPerdidos.
    """
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        categoria: Categoria,
        cor: str,
        status: StatusItem,
        local: str,
        data: str,
        usuario: Usuario
    ):

        super().__init__(
            id,
            nome,
            descricao,
            categoria,
            cor,
            status
        )

        self._local = local
        self._data = data
        self._usuario = usuario

    def exibir_detalhes(self) -> str:
        return (f"""Nome: {self._nome}Descrição: {self._descricao}Local Encontrado:{self._local_perda}""")
    
    def get_local(self):
        return self._local

    def get_data(self):
        return self._data

    def get_usuario(self):
        return self._usuario

class ItemPerdido(Item):

    def __init__(
        self,
        id,
        nome,
        descricao,
        categoria,
        cor,
        status,
        local,
        data,
        usuario
    ):

        super().__init__(
            id,
            nome,
            descricao,
            categoria,
            cor,
            status
        )

        self._local = local
        self._data = data
        self._usuario = usuario

    def get_local(self) -> str:
        return self._local


    def get_data(self) -> str:
        return self._data


    def get_usuario(self):
        return self._usuario

    def exibir_detalhes(self):
        return (f"""Nome: {self._nome}Descrição: {self._descricao}Último local visto:{self._local_perda}""")

class StatusCorrespondencia:
    """
    Representa o status de uma correspondência.

    Relacionamentos:
    - Associação com Correspondencia.
    """
    def __init__(self, nome: str, descricao: str):
        self._nome = nome
        self._descricao = descricao

    def get_nome(self) -> str:
        return self._nome

    def get_descricao(self) -> str:
        return self._descricao

    def __str__(self) -> str:
        return f"Nome: {self._nome}\nDescrição: {self._descricao}"

    @staticmethod
    def criar_por_nome(nome):

        if nome == "Pendente":
            return StatusCorrespondencia(
                "Pendente",
                "Aguardando confirmação."
            )

        if nome == "Confirmada":
            return StatusCorrespondencia(
                "Confirmada",
                "Correspondência confirmada."
            )

        if nome == "Rejeitada":
            return StatusCorrespondencia(
                "Rejeitada",
                "Correspondência rejeitada."
            )

        return StatusCorrespondencia(
            nome,
            ""
        )

class Correspondencia:
    """
    Representa uma correspondência entre itens.

    Relacionamentos:
    - Associação com StatusCorrespondencia.
    - Agregação com SistemaAchadosPerdidos.
    """

    def __init__(self, id: int, porcentagem: float, data: str, status: StatusCorrespondencia, item_perdido: ItemPerdido, item_encontrado: ItemEncontrado):

        self._id = id
        self._porcentagem = porcentagem
        self._data = data
        self._status = status
        self._item_perdido = item_perdido
        self._item_encontrado = item_encontrado

    def get_id(self):
        return self._id

    def get_item_perdido(self):
        return self._item_perdido

    def get_item_encontrado(self):
        return self._item_encontrado

    def get_porcentagem(self):
        return self._porcentagem

    def get_data(self) -> str:
        return self._data

    def get_item_perdido(self):
        return self._item_perdido

    def get_item_encontrado(self):
        return self._item_encontrado

    def get_status(self):
        return self._status

    def alterar_status(self, status: StatusCorrespondencia) -> None:
        self._status = status

    def exibir_detalhes(self) -> str:
        return (
            f"=== Correspondência ===\n"
            f"ID: {self._id}\n"
            f"Compatibilidade: {self._porcentagem}%\n"
            f"Data da análise: {self._data}\n"
            f"Status: {self._status}\n"
            f"Item Perdido: {self._item_perdido.get_nome()}\n"
            f"Item Encontrado: {self._item_encontrado.get_nome()}"
        )


class StatusSolicitacao:
    """
    Representa o status de uma solicitação de devolução.

    Relacionamentos:
    - Associação com SolicitacaoDevolucao.
    """
    def __init__(self, id: int, nome: str, descricao: str):
        self._id = id
        self._nome = nome
        self._descricao = descricao

    def get_id(self) -> int:
        return self._id

    def get_nome(self) -> str:
        return self._nome

    def get_descricao(self) -> str:
        return self._descricao

    @staticmethod
    def criar_por_nome(nome: str):

        if nome == "Pendente":
            return StatusSolicitacao(
                1,
                "Pendente",
                "Aguardando análise."
            )

        if nome == "Aprovada":
            return StatusSolicitacao(
                2,
                "Aprovada",
                "Solicitação aprovada."
            )

        if nome == "Rejeitada":
            return StatusSolicitacao(
                3,
                "Rejeitada",
                "Solicitação rejeitada."
            )

        return StatusSolicitacao(
            0,
            nome,
            ""
        )

    def __str__(self) -> str:
        return f"ID: {self._id}\nNome: {self._nome}\nDescrição: {self._descricao}"

class SolicitacaoDevolucao:
    """
    Representa uma solicitação de devolução de um item.

    Relacionamentos:
    - Associação com StatusSolicitacao.
    - Agregação com SistemaAchadosPerdidos.
    """

    def __init__(self, id: int, usuario, correspondencia: Correspondencia, justificativa: str, data: str, status: StatusSolicitacao):
        self._id = id
        self._usuario = usuario
        self._correspondencia = correspondencia
        self._justificativa = justificativa
        self._data = data
        self._status = status


    def get_id(self):
        return self._id

    def get_usuario(self):
        return self._usuario

    def get_correspondencia(self):
        return self._correspondencia

    def get_justificativa(self):
        return self._justificativa

    def get_data(self):
        return self._data

    def get_status(self):
        return self._status

    def aceitar(self):
        self._status = StatusSolicitacao.criar_por_nome(
            "Aprovada"
        )

    def recusar(self, motivo: str):

        self._status = StatusSolicitacao(
            3,
            "Rejeitada",
            motivo
        )

    def cancelar(self):

        self._status = StatusSolicitacao(
            "Cancelada",
            "Solicitação cancelada."
        )

    def exibir_detalhes(self):

        return (
            f"=== Solicitação ===\n"
            f"ID: {self._id}\n"
            f"Usuário: {self._usuario.get_nome()}\n"
            f"Item: {self._correspondencia.get_item_perdido().get_nome()}\n"
            f"Justificativa: {self._justificativa}\n"
            f"Data: {self._data}\n"
            f"Status: {self._status.get_nome()}"
        )

class Notificacao:
    """
    Representa uma notificação enviada aos usuários.

    Relacionamentos:
    - Dependência de Usuario.
    - Agregação com SistemaAchadosPerdidos.
    """
    def __init__( self, id: int, mensagem: str, data_envio: str, tipo: str, destinatario: Usuario):
        self._id = id
        self._mensagem = mensagem
        self._data_envio = data_envio
        self._tipo = tipo
        self._destinatario = destinatario
        self._lida = False

    def get_id(self) -> int:
        return self._id

    def get_mensagem(self) -> str:
        return self._mensagem

    def get_data_envio(self) -> str:
        return self._data_envio

    def get_tipo(self) -> str:
        return self._tipo

    def enviar(self, destinatario):
        print(f"Notificação enviada para {destinatario.get_nome()}.")

    def get_destinatario(self):
        return self._destinatario
    
    def foi_lida(self) -> bool:
        return self._lida

    def marcar_como_lida(self) -> None:
        self._lida = True

class NotificarMixin:
    """
    Representa o comportamento de notificar um usuário.

        Relacionamentos:
    - Mixin de SistemaAchadosPerdidos
    """

    def notificar(self, usuario, mensagem):
        print(f"Notificação enviada para {usuario.get_nome()}:")
        print(mensagem)

class Relatorio:
    """
    Representa um relatório gerado pelo sistema.

    Relacionamentos:
    - Dependência de SistemaAchadosPerdidos (é criado pelo sistema).
    """
    def __init__(self, id: int, tipo: str, data_emissao: str, conteudo: str):
        self._id = id
        self._tipo = tipo
        self._data_emissao = data_emissao
        self._conteudo = conteudo

    def get_id(self) -> int:
        return self._id

    def get_tipo(self) -> str:
        return self._tipo

    def get_data_emissao(self) -> str:
        return self._data_emissao

    def get_conteudo(self) -> str:
        return self._conteudo

    def exibir_relatorio(self) -> str:
        return f"=== Relatório ===\nID: {self._id}\nTipo: {self._tipo}\nData de emissão: {self._data_emissao}\nConteúdo:\n{self._conteudo}"


class SistemaAchadosPerdidos(NotificarMixin):
    """
    Gerencia o funcionamento do sistema de Achados e Perdidos.

    Relacionamentos:
    - Agregação com Usuario.
    - Agregação com ItemEncontrado.
    - Agregação com Correspondencia.
    - Agregação com SolicitacaoDevolucao.
    - Agregação com Notificacao.
    - Associação com PersistenciaCSV.
    - Dependência de Relatorio.
    """
    def __init__(self):

        self._persistencia = PersistenciaCSV()
        self._usuarios = self._persistencia.carregar_usuarios()
        self._itens_perdidos = (self._persistencia.carregar_itens_perdidos(self._usuarios))
        self._itens_encontrados = (self._persistencia.carregar_itens_encontrados(self._usuarios))
        self._correspondencias = (self._persistencia.carregar_correspondencias(self._itens_perdidos, self._itens_encontrados))
        self.carregar_dados()
        self._solicitacoes = (self._persistencia.carregar_solicitacoes(self._usuarios, self._correspondencias))
        self._notificacoes = (self._persistencia.carregar_notificacoes(self._usuarios))

    def listar_itens_perdidos(self):
        return self._itens_perdidos

    def listar_itens_encontrados(self):
        return self._itens_encontrados

    def cadastrar_usuario( self, nome, telefone, email):

        usuario = Usuario(self.gerar_proximo_id_usuario(), nome, telefone, email, date.today().strftime("%d/%m/%Y"))

        self._usuarios.append(usuario)
        self._persistencia.salvar_usuarios(self._usuarios)

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios
    
    def gerar_proximo_id_usuario(self):
        return len(self._usuarios)+1


    def gerar_proximo_id_perdido(self):
        return len(self._itens_perdidos)+1

    def gerar_proximo_id_encontrado(self):
        return len(self._itens_encontrados)+1

    def gerar_proximo_id_solicitacao(self) -> int:
        if not self._solicitacoes:
            return 1
        return self._solicitacoes[-1].get_id() + 1


    def buscar_usuario_por_nome( self, nome: str) -> Usuario | None:
        for usuario in self._usuarios:

            if usuario.get_nome() == nome:
                return usuario

        return None

    def buscar_usuario_por_id( self, id_usuario: int) -> Usuario | None:
        for usuario in self._usuarios:

            if usuario.get_id() == id_usuario:
                return usuario

        return None

    def cadastrar_item_perdido(self, nome, descricao, categoria, cor, local, data, usuario):

        item = ItemPerdido(self.gerar_proximo_id_perdido(), nome, descricao, categoria, cor, StatusItem("Perdido", "Item perdido"), local, data, usuario)

        self._itens_perdidos.append(item)
        self._persistencia.salvar_itens_perdidos(self._itens_perdidos)

    def buscar_correspondencias(self, item_encontrado):

        for item_perdido in self._itens_perdidos:

            porcentagem = self.calcular_compatibilidade(
                item_perdido,
                item_encontrado
            )

            if porcentagem >= 70:

                correspondencia = self.criar_correspondencia(
                    item_perdido,
                    item_encontrado,
                    porcentagem
                )

                self.notificar_usuario(
                item_perdido.get_usuario(),
                correspondencia
                )

    def buscar_correspondencia_por_id(
        self,
        id: int
    ) -> Correspondencia | None:

        for correspondencia in self._correspondencias:

            if correspondencia.get_id() == id:
                return correspondencia

        return None

    def buscar_solicitacao_por_id(
        self,
        id
    ):

        for solicitacao in self._solicitacoes:

            if solicitacao.get_id() == id:
                return solicitacao

        return None

    def cadastrar_item_encontrado(self, nome, descricao, categoria, cor, local, data, usuario):

        item = ItemEncontrado(
            self.gerar_proximo_id_encontrado(),
            nome,
            descricao,
            categoria,
            cor,
            StatusItem(
                "Encontrado",
                "Item encontrado"
            ),
            local,
            data,
            usuario
        )

        self._itens_encontrados.append(item)

        self._persistencia.salvar_itens_encontrados(self._itens_encontrados)
        self.buscar_correspondencias(item)

    def criar_correspondencia( self, item_perdido, item_encontrado, porcentagem):

        status = StatusCorrespondencia(
            "Pendente",
            "Aguardando confirmação."
        )

        correspondencia = Correspondencia(
            len(self._correspondencias) + 1,
            porcentagem,
            date.today().strftime("%d/%m/%Y"),
            status,
            item_perdido,
            item_encontrado
        )

        self._correspondencias.append(correspondencia)

        self._persistencia.salvar_correspondencias(self._correspondencias)

        return correspondencia


    def calcular_compatibilidade(self,item_perdido,item_encontrado):

        pontos = 0

        if (
            item_perdido.get_nome().lower()
            ==
            item_encontrado.get_nome().lower()
        ):
            pontos += 40

        
        if (
            item_perdido.get_categoria().get_nome().lower()
            ==
            item_encontrado.get_categoria().get_nome().lower()
        ):
            pontos += 20

        if (
            item_perdido.get_cor().lower()
            ==
            item_encontrado.get_cor().lower()
        ):
            pontos += 20

        palavras_perdido = set(
            item_perdido.get_descricao().lower().split()
        )

        palavras_encontrado = set(
            item_encontrado.get_descricao().lower().split()
        )

        palavras_em_comum = palavras_perdido.intersection(
            palavras_encontrado
        )

        if len(palavras_perdido) > 0:

            porcentagem_descricao = (
                len(palavras_em_comum)
                /
                len(palavras_perdido)
            )

            pontos += porcentagem_descricao * 20

        return round(pontos, 2)

    def combina(
        self,
        perdido,
        encontrado
    ):

        if (
            perdido.get_nome().lower()
            !=
            encontrado.get_nome().lower()
        ):
            return False

        if (
            perdido.get_categoria().get_nome()
            !=
            encontrado.get_categoria().get_nome()
        ):
            return False

        if (
            perdido.get_cor().lower()
            !=
            encontrado.get_cor().lower()
        ):
            return False

        return True

    def listar_correspondencias(self):
        return self._correspondencias

    def criar_solicitacao(
        self,
        usuario,
        correspondencia,
        justificativa
    ):

        status = StatusSolicitacao(
            "Pendente",
            "Aguardando análise.",
            ""
        )

        solicitacao = SolicitacaoDevolucao(
            len(self._solicitacoes) + 1,
            usuario,
            correspondencia,
            justificativa,
            date.today().strftime("%d/%m/%Y"),
            status
        )

        self._solicitacoes.append(
            solicitacao
        )

        self._persistencia.salvar_solicitacoes(
            self._solicitacoes
        )

        return solicitacao

    def listar_solicitacoes(self):
        return self._solicitacoes

    def listar_notificacoes(self):
        return self._notificacoes

    def listar_notificacoes_usuario(self, usuario: Usuario) -> list[Notificacao]:
        return [
            n
            for n in self._notificacoes
            if n.get_destinatario() == usuario
        ]

    def notificar_usuario(
        self,
        usuario: Usuario,
        correspondencia: Correspondencia
        ):

        mensagem = (
            f"Encontramos um item compatível com "
            f"'{correspondencia.get_item_perdido().get_nome()}'."
        )

        notificacao = Notificacao(
            len(self._notificacoes) + 1, mensagem, date.today().strftime("%d/%m/%Y"), "Correspondência", usuario)

        self._notificacoes.append(notificacao)

        self.notificar(usuario, mensagem)

    def carregar_dados(self):

        self._itens_perdidos = (
            self._persistencia.carregar_itens_perdidos(self._usuarios)
        )

        self._itens_encontrados = (
            self._persistencia.carregar_itens_encontrados(self._usuarios)
        )

    def aceitar_solicitacao(
        self,
        id_solicitacao: int
    ):

        solicitacao = self.buscar_solicitacao_por_id(
            id_solicitacao
        )

        if solicitacao is None:
            return False

        solicitacao.aceitar()

        correspondencia = solicitacao.get_correspondencia()

        item_perdido = correspondencia.get_item_perdido()
        item_encontrado = correspondencia.get_item_encontrado()

        if item_perdido in self._itens_perdidos:
            self._itens_perdidos.remove(item_perdido)

        if item_encontrado in self._itens_encontrados:
            self._itens_encontrados.remove(item_encontrado)

        if correspondencia in self._correspondencias:
            self._correspondencias.remove(correspondencia)

        self._persistencia.salvar_itens_perdidos(
            self._itens_perdidos
        )

        self._persistencia.salvar_itens_encontrados(
            self._itens_encontrados
        )

        self._persistencia.salvar_correspondencias(
            self._correspondencias
        )

        self._persistencia.salvar_solicitacoes(
            self._solicitacoes
        )

        return True

    def recusar_solicitacao(
        self,
        id_solicitacao: int
    ):

        solicitacao = self.buscar_solicitacao_por_id(
            id_solicitacao
        )

        if solicitacao is None:
            return False

        solicitacao.recusar(
            "Solicitação recusada pelo usuário."
        )

        self._persistencia.salvar_solicitacoes(
            self._solicitacoes
        )

        return True

class PersistenciaCSV:
    """
    Realiza a persistência dos dados em arquivos CSV.

    Relacionamentos:
    - Associação com SistemaAchadosPerdidos.
    - Dependência de Usuario.
    - Dependência de ItemEncontrado.
    - Dependência de Categoria.
    - Dependência de StatusItem.
    """
    
    def __init__(self):

        self._arquivo_usuarios = "usuarios.csv"
        self._arquivo_itens_perdidos = "itens_perdidos.csv"
        self._arquivo_itens_encontrados = "itens_encontrados.csv"
        self._arquivo_correspondencias = "correspondencias.csv"
        self._arquivo_solicitacoes = "solicitacoes.csv"
        self._arquivo_notificacoes = "notificacoes.csv"

    def salvar_itens_perdidos(self, itens):

        with open(
            self._arquivo_itens_perdidos,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            writer = csv.writer(arquivo)

            writer.writerow([
                "ID",
                "Nome",
                "Descrição",
                "Categoria",
                "Cor",
                "Status",
                "Local",
                "Data",
                "Usuário"
            ])

            for item in itens:

                writer.writerow([
                    item.get_id(),
                    item.get_nome(),
                    item.get_descricao(),
                    item.get_categoria().get_nome(),
                    item.get_cor(),
                    item.get_status().get_nome(),
                    item.get_local(),
                    item.get_data(),
                    item.get_usuario().get_id()
                ])

    def carregar_itens_perdidos(self, usuarios):

        itens = []

        try:

            with open(
                self._arquivo_itens_perdidos,
                "r",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    categoria = Categoria(
                        linha["Categoria"]
                    )

                    status = StatusItem.criar_por_nome(
                        linha["Status"],
                    )

                    usuario = None

                    for u in usuarios:

                        if u.get_id() == int(linha["Usuário"]):
                            usuario = u
                            break

                    item = ItemPerdido(
                        int(linha["ID"]),
                        linha["Nome"],
                        linha["Descrição"],
                        categoria,
                        linha["Cor"],
                        status,
                        linha["Local"],
                        linha["Data"],
                        usuario
                    )

                    itens.append(item)

        except FileNotFoundError:
            pass

        return itens

    def salvar_itens_encontrados(self, itens):

        with open(
            self._arquivo_itens_encontrados,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            writer = csv.writer(arquivo)

            writer.writerow([
                "ID",
                "Nome",
                "Descrição",
                "Categoria",
                "Cor",
                "Status",
                "Local",
                "Data",
                "Usuário"
            ])

            for item in itens:

                writer.writerow([
                    item.get_id(),
                    item.get_nome(),
                    item.get_descricao(),
                    item.get_categoria().get_nome(),
                    item.get_cor(),
                    item.get_status().get_nome(),
                    item.get_local(),
                    item.get_data(),
                    item.get_usuario().get_id()
                ])

    def carregar_itens_encontrados(self, usuarios):

        itens = []

        try:

            with open(
                self._arquivo_itens_encontrados,
                "r",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    categoria = Categoria(
                        linha["Categoria"]
                    )

                    status = StatusItem.criar_por_nome(
                        linha["Status"],
                    )

                    usuario = None

                    for u in usuarios:

                        if u.get_id() == int(linha["Usuário"]):
                            usuario = u
                            break

                    item = ItemEncontrado(
                        int(linha["ID"]),
                        linha["Nome"],
                        linha["Descrição"],
                        categoria,
                        linha["Cor"],
                        status,
                        linha["Local"],
                        linha["Data"],
                        usuario
                    )

                    itens.append(item)

        except FileNotFoundError:
            pass

        return itens
    
    def salvar_usuarios(self, usuarios):

        with open(self._arquivo_usuarios,
                  "w",
                  newline="",
                  encoding="utf-8") as arquivo:

            writer = csv.writer(arquivo)

            writer.writerow([
                "ID",
                "Nome",
                "Telefone",
                "Email",
                "DataCadastro"
            ])

            for usuario in usuarios:

                writer.writerow([
                    usuario.get_id(),
                    usuario.get_nome(),
                    usuario.get_telefone(),
                    usuario.get_email(),
                    usuario._data_cadastro
                ])

    def carregar_usuarios(self):

        usuarios = []

        try:

            with open(self._arquivo_usuarios,
                      "r",
                      encoding="utf-8") as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    usuario = Usuario(

                        int(linha["ID"]),
                        linha["Nome"],
                        linha["Telefone"],
                        linha["Email"],
                        linha["DataCadastro"]

                    )

                    usuarios.append(usuario)

        except FileNotFoundError:

            pass

        return usuarios
    
    def salvar_correspondencias(self, correspondencias):
        with open(
            self._arquivo_correspondencias,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            writer = csv.writer(arquivo)

            writer.writerow([
                "ID",
                "Porcentagem",
                "Data",
                "Status",
                "ItemPerdido",
                "ItemEncontrado"
            ])

            for correspondencia in correspondencias:

                writer.writerow([
                    correspondencia.get_id(),
                    correspondencia.get_porcentagem(),
                    correspondencia.get_data(),
                    correspondencia.get_status().get_nome(),
                    correspondencia.get_item_perdido().get_id(),
                    correspondencia.get_item_encontrado().get_id()
                ])

    def carregar_correspondencias(
        self,
        itens_perdidos,
        itens_encontrados
    ):

        correspondencias = []

        try:

            with open(
                self._arquivo_correspondencias,
                "r",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    item_perdido = None
                    item_encontrado = None

                    for item in itens_perdidos:

                        if item.get_id() == int(linha["ItemPerdido"]):
                            item_perdido = item
                            break

                    for item in itens_encontrados:

                        if item.get_id() == int(linha["ItemEncontrado"]):
                            item_encontrado = item
                            break

                    status = StatusCorrespondencia.criar_por_nome(
                        linha["Status"]
                    )

                    correspondencia = Correspondencia(
                        int(linha["ID"]),
                        float(linha["Porcentagem"]),
                        linha["Data"],
                        status,
                        item_perdido,
                        item_encontrado
                    )

                    correspondencias.append(
                        correspondencia
                    )

        except FileNotFoundError:
            pass

        return correspondencias

    def salvar_solicitacoes(self, solicitacoes):

        with open(
            self._arquivo_solicitacoes,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            writer = csv.writer(arquivo)

            writer.writerow([
                "ID",
                "Usuario",
                "Correspondencia",
                "Data",
                "Status"
            ])

            for solicitacao in solicitacoes:

                writer.writerow([
                    solicitacao.get_id(),
                    solicitacao.get_usuario().get_id(),
                    solicitacao.get_correspondencia().get_id(),
                    solicitacao.get_data(),
                    solicitacao.get_status().get_nome()
                ])

    def carregar_solicitacoes(self, usuarios, correspondencias):

        solicitacoes = []

        try:

            with open(
                self._arquivo_solicitacoes,
                "r",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    usuario = None

                    for u in usuarios:

                        if u.get_id() == int(linha["Usuario"]):
                            usuario = u
                            break

                    correspondencia = None

                    for c in correspondencias:

                        if c.get_id() == int(
                            linha["Correspondencia"]
                        ):
                            correspondencia = c
                            break

                    status = StatusSolicitacao.criar_por_nome(
                        linha["Status"]
                    )

                    solicitacao = SolicitacaoDevolucao(
                        int(linha["ID"]),
                        usuario,
                        correspondencia,
                        "",
                        linha["Data"],
                        status
                    )

                    solicitacoes.append(
                        solicitacao
                    )

        except FileNotFoundError:
            pass

        return solicitacoes

    def salvar_notificacoes(self, notificacoes):

        with open(
            self._arquivo_notificacoes,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            writer = csv.writer(arquivo)

            writer.writerow([
                "ID",
                "Mensagem",
                "Data",
                "Tipo",
                "Destinatario",
                "Lida"
            ])

            for notificacao in notificacoes:

                writer.writerow([
                    notificacao.get_id(),
                    notificacao.get_mensagem(),
                    notificacao.get_data(),
                    notificacao.get_tipo(),
                    notificacao.get_destinatario().get_id(),
                    notificacao.foi_lida()
                ])

    def carregar_notificacoes(self, usuarios):
        notificacoes = []

        try:

            with open(
                self._arquivo_notificacoes,
                "r",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    destinatario = None

                    for usuario in usuarios:

                        if usuario.get_id() == int(
                            linha["Destinatario"]
                        ):
                            destinatario = usuario
                            break

                    notificacao = Notificacao(
                        int(linha["ID"]),
                        linha["Mensagem"],
                        linha["Data"],
                        linha["Tipo"],
                        destinatario
                    )

                    if linha["Lida"] == "True":
                        notificacao.marcar_como_lida()

                    notificacoes.append(
                        notificacao
                    )

        except FileNotFoundError:
            pass

        return notificacoes

    def ler_itens(self):

        itens = []

        try:
            with open(
                self._arquivo_itens,
                "r",
                newline="",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.reader(arquivo)

                next(leitor, None)

                for linha in leitor:
                    itens.append(linha)

        except FileNotFoundError:
            pass

        return itens