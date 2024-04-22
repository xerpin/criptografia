import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def criptografar_arquivo(arquivo_entrada, arquivo_saida, chave):
    """
    Criptografa um arquivo usando uma chave simétrica.

    Args:
        arquivo_entrada (str): Caminho para o arquivo de entrada.
        arquivo_saida (str): Caminho para o arquivo de saída criptografado.
        chave (bytes): Chave simétrica.
    """
    # Gera um IV para o AES
    iv = os.urandom(16)

    # Cria um objeto de criptografia com a chave e o IV
    criptografia = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())

    with open(arquivo_entrada, 'rb') as arquivo_leitura:
        dados = arquivo_leitura.read()

    # Adiciona preenchimento PKCS7 aos dados
    padder = padding.PKCS7(128).padder()
    dados = padder.update(dados) + padder.finalize()

    # Criptografa os dados usando a chave e o IV
    cifrador = criptografia.encryptor()
    dados_criptografados = cifrador.update(dados) + cifrador.finalize()

    # Grava os dados criptografados e o IV no arquivo de saída
    with open(arquivo_saida, 'wb') as arquivo_escrita:
        arquivo_escrita.write(iv)
        arquivo_escrita.write(dados_criptografados)

def main():
    """
    Função principal do script.
    """

    # Solicita ao usuário os arquivos de entrada e saída
    arquivo_entrada = input("Digite o caminho do arquivo a ser criptografado: ")
    arquivo_saida = input("Digite o caminho do arquivo de saída criptografado: ")

    # Gera uma chave simétrica aleatória
    chave = os.urandom(32)  # Chave de 256 bits (32 bytes) para AES-256

    # Criptografa o arquivo
    criptografar_arquivo(arquivo_entrada, arquivo_saida, chave)

    print("Arquivo criptografado com sucesso!")

if __name__ == "__main__":
    main()
