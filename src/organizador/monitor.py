import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .organizador import organizar_downloads
from .config import PASTA_DOWNLOADS


EXTENSOES_TEMP = [".crdownload", ".part", ".tmp"]


class DownloadHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        arquivo = event.src_path.lower()

        if any(arquivo.endswith(ext) for ext in EXTENSOES_TEMP):
            return

        print(f"Novo arquivo detectado: {event.src_path}")

        time.sleep(3)

        organizar_downloads()


def iniciar_monitor():

    event_handler = DownloadHandler()

    observer = Observer()
    observer.schedule(event_handler, PASTA_DOWNLOADS, recursive=False)

    observer.start()

    print("Monitorando pasta Downloads...")

    try:
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()