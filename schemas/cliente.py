from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente


class ClienteSchema(BaseModel):
    """ Define como um novo doce a ser inserido deve ser representado
    """
    cpf: str = "23563800278"
    nome: str = "Jose"
    genero: str = "Unisex"
    dataNascimento: str = "25/04/1964"
    rg: str = "2195039"
    enderecoEmail: str = "marialdoferreira@gmail.com"
    cep: Optional[str] = "66080-300"
    logradouro: str = "Passagem Joana Darc "
    complemento: Optional[str] = "Entre Eneias Pinheiro e Piraja"
    bairro: str = "Pedreira"
    localidade: str = "Belem"
    uf: str = "PA"    

class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    cpf: str = "23563800278"

class ClienteBuscaSchemaId(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do Cliente.
    """
    id: str = ''

class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    cliente:List[ClienteSchema]


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do doce seguindo o schema definido em
        DoceViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "cpf": cliente.cpf,
            "nome": cliente.nome,
            "genero": cliente.genero,
            "dataNascimento": cliente.dataNascimento,
            "rg": cliente.rg,
            "enderecoEmail": cliente.enderecoEmail,
            "cep": cliente.cep,
            "logradouro": cliente.logradouro,
            "complemento": cliente.complemento,
            "bairro": cliente.bairro,
            "localidade": cliente.localidade,
            "uf": cliente.uf,
            "id": cliente.id
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado.
    """
    id: int = 1
    cpf: str = "23563800278"
    nome: str = "Jose Maria"
    genero: str = "Masculino"
    dataNascimento: str = "25/04/1964"
    rg: str = "2195039"
    enderecoEmail: str = "marialdoferreira@gmail.com"
    cep: Optional[str] = "66080-300"
    logradouro: str = "Passagem Joana Darc"
    complemento: str = "Entre Eneias Pinheiro e Piraja"
    bairro: str = "Pedreira",
    localidade: str = "Belem"
    uf: str = "PA"
    

class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    cpf: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do doce seguindo o schema definido em
        DoceViewSchema.
    """
    return {
    "id": cliente.id,
    "cpf": cliente.cpf,
    "nome": cliente.nome,
    "genero": cliente.genero,
    "dataNascimento": cliente.dataNascimento,
    "rg": cliente.rg,
    "enderecoEmail": cliente.enderecoEmail,
    "cep": cliente.cep,
    "logradouro": cliente.logradouro,
    "complemento": cliente.complemento,
    "bairro": cliente.bairro,
    "localidade": cliente.localidade,
    "uf": cliente.uf
    }
