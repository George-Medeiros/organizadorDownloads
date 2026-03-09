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