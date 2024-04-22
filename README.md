# Criptografia de Arquivos com Python

## Descrição

Este é um simples script Python para criptografar arquivos usando o algoritmo AES (Advanced Encryption Standard) com uma chave simétrica. Ele utiliza a biblioteca `cryptography` para realizar a criptografia.

## Funcionalidades

- Criptografa um arquivo de entrada usando AES com uma chave simétrica.
- Utiliza preenchimento PKCS7 para garantir a compatibilidade com o tamanho do bloco AES.

## Requisitos

- Python 3
- Biblioteca `cryptography`

## Instalação

1. Certifique-se de ter o Python 3 instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale a biblioteca `cryptography` usando o pip:

   ```
   pip install cryptography
   ```

## Uso

1. Clone este repositório ou baixe o arquivo `criptografia.py`.

2. Execute o script `criptografia.py` em um terminal ou prompt de comando:

   ```bash
   python criptografia.py
   ```

3. Você será solicitado a fornecer o caminho do arquivo que deseja criptografar e o caminho onde deseja salvar o arquivo criptografado.

4. O script irá gerar automaticamente uma chave de criptografia aleatória e usá-la para criptografar o arquivo especificado.

## Notas

- Certifique-se de ter permissões adequadas para acessar os arquivos mencionados no script.

## Contribuindo

Sinta-se à vontade para enviar sugestões, relatar bugs ou contribuir para o projeto.
