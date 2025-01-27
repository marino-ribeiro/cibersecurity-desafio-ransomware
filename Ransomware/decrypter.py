from cryptography.fernet import Fernet

# Função para carregar a chave de criptografia
def carregar_chave():
    return open("chave_secreta.key", "rb").read()

# Função para descriptografar um arquivo
def descriptografar_arquivo(nome_arquivo, chave):
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as arquivo_criptografado:
        dados_criptografados = arquivo_criptografado.read()
    dados_descriptografados = fernet.decrypt(dados_criptografados)
    with open(nome_arquivo, "wb") as arquivo_descriptografado:
        arquivo_descriptografado.write(dados_descriptografados)

# Exemplo de uso
if __name__ == "__main__":
    # Carregar a chave
    chave = carregar_chave()

    # Descriptografar um arquivo de exemplo
    arquivo_para_descriptografar = "teste.txt"  # Substitua pelo nome do seu arquivo
    descriptografar_arquivo(arquivo_para_descriptografar, chave)
    print(f"Arquivo '{arquivo_para_descriptografar}' descriptografado com sucesso!")