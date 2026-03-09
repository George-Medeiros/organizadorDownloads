import logging
from pathlib import Path
from .config import PASTA_DOWNLOADS, ARQUIVO_LOG


def configurar_logger():

    caminho_log = Path(PASTA_DOWNLOADS) / ARQUIVO_LOG

    logging.basicConfig(
        filename=caminho_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger(__name__)