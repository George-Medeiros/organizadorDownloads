from pathlib import Path
from .config import CATEGORIAS

def obter_extensao(arquivo: Path) -> str:
    return arquivo.suffix.lower()

def identificar_categoria(arquivo: Path) -> str:
    extensao = obter_extensao(arquivo)
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"

def gerar_nome_unico(destino: Path) -> Path:

    contador = 1
    novo_destino = destino

    while novo_destino.exists():

        nome = destino.stem
        extensao = destino.suffix
        pasta = destino.parent

        novo_nome = f"{nome}_{contador}{extensao}"

        novo_destino = pasta / novo_nome

        contador += 1

    return novo_destino