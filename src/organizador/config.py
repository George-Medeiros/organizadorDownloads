from pathlib import Path

# pasta que será organizada
PASTA_DOWNLOADS = Path.home() / "Downloads"

# nome do arquivo de log
ARQUIVO_LOG = "log_organizador.txt"

# categorias de arquivos
CATEGORIAS = {
    "PDF": [".pdf"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documentos": [".docx", ".txt", ".json"],
    "Programas": [".exe", ".py"],
    "Compactados": [".zip", ".rar"],
    "Audio": [".mp3", ".wav"]
}