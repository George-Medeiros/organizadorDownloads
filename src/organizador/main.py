from pathlib import Path
import shutil

from .config import PASTA_DOWNLOADS
from .funcoes import identificar_categoria
from .logger import configurar_logger

def organizar_downloads():

    logger = configurar_logger()

    pasta = Path(PASTA_DOWNLOADS)

    logger.info("Organizador iniciado")

    for arquivo in pasta.iterdir():

        if not arquivo.is_file():
            continue

        categoria = identificar_categoria(arquivo)

        pasta_destino = pasta / categoria

        pasta_destino.mkdir(exist_ok=True)

        destino = pasta_destino / arquivo.name

        try:

            shutil.move(str(arquivo), str(destino))

            logger.info(f"{arquivo.name} movido para {categoria}")

        except Exception as erro:

            logger.error(f"Erro ao mover {arquivo.name}: {erro}")

if __name__ == "__main__":
    organizar_downloads()