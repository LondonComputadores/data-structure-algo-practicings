# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):
    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    # Percorra cada registro de log:
    for registro in registros:
        # Separe o ID do usuário e o status do registro (sucesso ou falha):
        id_usuario, status = registro.split(":")

        # Verifique se o usuário atual é o mesmo da iteração anterior:
        if id_usuario == usuario_atual:
            if status == "falha":
                tentativas_consecutivas += 1  # Incremente o contador de tentativas falhas
                if tentativas_consecutivas > 3:
                    invasor_detectado = id_usuario  # Marque como invasor detectado
                    break
            else:
                tentativas_consecutivas = 0  # Resete o contador de falhas
        else:
            # Se mudar de usuário, verifique se o usuário anterior teve mais de 3 falhas consecutivas:
            if tentativas_consecutivas > 3:
                invasor_detectado = usuario_atual
                break

            # Atualize para o novo usuário e reinicie a contagem de tentativas falhas:
            usuario_atual = id_usuario
            tentativas_consecutivas = 1 if status == "falha" else 0  # Reseta contagem

    # Após o loop, verifique se o último usuário teve mais de 3 tentativas de falha:
    if tentativas_consecutivas > 3 and not invasor_detectado:
        invasor_detectado = usuario_atual

    # Retorna o resultado final
    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"

# Função principal para executar o programa
def main():
    # Solicita ao usuário que insira os registros de log
    entrada = input()
    
    registros = [registro.strip().strip('"') for registro in entrada.split(",")]

    # Chama a função para detectar tentativas de invasão:
    resultado = detectar_invasao(registros)

    # Imprime o resultado
    print(resultado)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
