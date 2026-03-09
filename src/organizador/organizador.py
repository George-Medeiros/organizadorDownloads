from pathlib import Path
import shutil
from datetime import datetime

from .config import PASTA_DOWNLOADS
from .funcoes import identificar_categoria, gerar_nome_unico
from .logger import configurar_logger


def organizar_downloads():

    logger = configurar_logger()

    pasta = Path(PASTA_DOWNLOADS)

    logger.info("Organizador iniciado")

    for arquivo in pasta.iterdir():

        if not arquivo.is_file():
            continue

        categoria = identificar_categoria(arquivo)

        info = arquivo.stat()

        data_criacao = datetime.fromtimestamp(info.st_birthtime)

        ano = str(data_criacao.year)
        mes = f"{data_criacao.month:02d}"

        pasta_destino = pasta / categoria / ano / mes
        pasta_destino.mkdir(parents=True, exist_ok=True)

        destino = pasta_destino / arquivo.name
        destino = gerar_nome_unico(destino)

        try:

            shutil.move(str(arquivo), str(destino))

            logger.info(f"{arquivo.name} movido para {categoria}/{ano}/{mes}")

        except Exception as erro:

            logger.error(f"Erro ao mover {arquivo.name}: {erro}")