from cryptography.fernet import Fernet

# Função para gerar uma chave de criptografia e salvá-la em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave_secreta.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)

# Função para carregar a chave de criptografia
def carregar_chave():
    return open("chave_secreta.key", "rb").read()

# Função para criptografar um arquivo
def criptografar_arquivo(nome_arquivo, chave):
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as arquivo:
        dados = arquivo.read()
    dados_criptografados = fernet.encrypt(dados)
    with open(nome_arquivo, "wb") as arquivo_criptografado:
        arquivo_criptografado.write(dados_criptografados)

# Exemplo de uso
if __name__ == "__main__":
    # Gerar e salvar a chave
    gerar_chave()
    chave = carregar_chave()

    # Criptografar um arquivo de exemplo
    arquivo_para_criptografar = "teste.txt"  # Substitua pelo nome do seu arquivo
    criptografar_arquivo(arquivo_para_criptografar, chave)
    print(f"Arquivo '{arquivo_para_criptografar}' criptografado com sucesso!")