# working and final version

"""
    Para resolver esses problemas sem alterar significativamente a estrutura do seu código, vamos:

    Converter as palavras da mensagem para minúsculas antes de compará-las com a lista de palavras suspeitas.
    Remover a pontuação das palavras na mensagem para garantir correspondências exatas.
"""

import string

# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    # Quebra a mensagem em palavras para verificar individualmente
    # Converte todas as palavras para minúsculas e remove pontuação
    mensagem = mensagem.strip().split()
    
    for palavra in mensagem:
        """
            palavra.lower(): Converte a palavra para minúsculas, garantindo que a comparação não seja sensível a maiúsculas/minúsculas.
            .strip(string.punctuation): Remove quaisquer caracteres de pontuação do início e do fim da palavra. Isso assegura que, por exemplo, "promoção!" seja convertido para "promoção".
        """
        # Remove pontuação do início e do fim da palavra e converte para minúsculas
        palavra_limpa = palavra.lower().strip(string.punctuation)
        if palavra_limpa in palavras_suspeitas:  # Verifica palavras completas
            return "Phishing"
    return "Seguro"  # Se nenhuma palavra suspeita for encontrada

# Entrada do usuário
email_usuario = input().strip()

# Chamada da função e exibição do resultado
resultado = verificar_phishing(email_usuario)

# Exibição da classificação exatamente como no código inicial
print(f"Classificação: {resultado}")



#----------------------------------------------------------------------------------


# # Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
# def verificar_phishing(mensagem):
#     # Lista de palavras que indicam possíveis e-mails de phishing
#     palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
#     # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:
    
#     for i in palavras_suspeitas: 
# 
#       # Essa estrutura de repetição não está correta, pois ela não verifica se a palavra suspeita está presente na mensagem       
#         if i in palavras_suspeitas and mensagem:
#             return "Phishing"
#         else:
#             return "Seguro"


# email_usuario = input()#.split()

# resultado = verificar_phishing(email_usuario)

# print(f"Classificação: {resultado}")

# #--------------------------------------------

# def verificar_phishing(mensagem):
#     # Lista de palavras que indicam possíveis e-mails de phishing
#     palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
#     # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:
    
#     for i in email_usuario.split():

        # Essa estrutura de repetição não está correta, pois ela não verifica se a palavra suspeita está presente na mensagem
#         if i in palavras_suspeitas:            
#              #print("Phishing")
#             return "Phishing"
#         else:
#              #print("Seguro")
#             return "Seguro" 
       # return something return "Seguro"  # Aqui SEMPRE deve-se fechar o for loop com um "return"! 

# email_usuario = input().split()

# resultado = verificar_phishing(email_usuario)

# print(f"Classificação: {resultado}")