from models.produto import Produto
from sqlalchemy import select
from sqlalchemy.orm import Session

def incluir(motor):
    print("Incluindo ")
    nome = input("Qual o nome da categoria que você quer adicionar? ")
    with Session(motor) as sessao:
        categoria = Categoria()
        categoria.nome = nome
        sessao.add(categoria)
        sessao.commit()
    print(f"Categoria {nome} adicionada.")

