# 📂 Organizador de Downloads

Script em Python que organiza automaticamente arquivos da pasta **Downloads** em categorias e subpastas por **ano e mês**.

## 🚀 Funcionalidades

- Organiza arquivos automaticamente por categoria
- Cria pastas automaticamente
- Evita sobrescrever arquivos com nomes iguais
- Gera logs das operações realizadas

### Estrutura criada

Downloads/

imagens/
2025/
03/
foto.png

pdf/
2025/
03/
contrato.pdf

## 🛠 Tecnologias utilizadas

- Python
- pathlib
- shutil
- logging

## 📦 Estrutura do projeto

organizadorDownloads/

docs/
src/
organizador/
config.py
funcoes.py
logger.py
main.py
organizador.py

tests/
README.md
requirements.txt

## ▶️ Como executar

Clone o repositório:


git clone https://github.com/George-Medeiros/organizadorDownloads.git


Entre na pasta do projeto:


cd organizadorDownloads/src


Execute o programa:


python -m organizador.main


## 📊 Exemplo de funcionamento

Antes:


Downloads/
foto.png
contrato.pdf
planilha.xlsx


Depois:


Downloads/
imagens/
2025/
03/
foto.png

pdf/
2025/
03/
contrato.pdf

planilhas/
2025/
03/
planilha.xlsx


## 📌 Melhorias futuras

- Monitorar automaticamente a pasta Downloads
- Interface gráfica
- Configuração de categorias customizadas
- Modo simulação (`--dry-run`)

## 👨‍💻 Autor

George Emerson de Araujo Medeiros