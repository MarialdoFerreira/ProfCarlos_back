from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    cpf = Column(String(15), unique=True)
    nome = Column(String(140))
    genero = Column(String(20))
    dataNascimento = Column(String(8))
    rg = Column(String(15))
    enderecoEmail = Column(String(60))
    cep = Column(String(9))
    logradouro = Column(String(140))
    complemento = Column(String(140))
    bairro = Column(String(120)) 
    localidade = Column(String(60))
    uf = Column(String(2))      
    cliente_cadastro = Column(DateTime, default=datetime.now())


    def __init__(self, cpf:str, nome:str, genero:str, dataNascimento: datetime, rg:str, enderecoEmail:str, cep:str, logradouro:str, complemento:str, bairro:str, localidade:str, uf:str,
                 cliente_cadastro:Union[DateTime, None] = None):
        """
        Cria um Cliente
        Arguments:
            cpf: cadastro da pessoa fisica receita federal
            nome: nome do Cliente.
            sexo: identifica o genero da pessoa
            data nascimento: data de nascimento do cliente
            rg: registro geral emitido pelo orgao de segurança publica
            logradouro: endereço do cliente
            complemento: aumenta a precisão para localização do endereço
            bairro: bairro do cliente
            cidade: cidade do cliente
            uf: unidade da federaçao
        """
        self.cpf = cpf
        self.nome = nome
        self.genero = genero
        self.dataNascimento = dataNascimento
        self.rg = rg
        self.enderecoEmail = enderecoEmail
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf

        # se não for informada, será o data exata do cadastro no banco
        if cliente_cadastro:
            self.cliente_cadastro = cliente_cadastro

