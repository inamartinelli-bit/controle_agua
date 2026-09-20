import os # Verifica o sistema e limpa a tela
# os.name =='nt' identifica se o sistema é Windows, executando o comando o comando 'cls' para limpar a tela. 
# Caso contrário (else), para sistemas Linux ou Mac (baseados em Unix), o comando 'clear' é utilizado.
# os.name == 'nt' significa que o sistema operacional é Windows, enquanto 'posix' indica Linux ou Mac.
# os.name retorna 'nt' para Windows e 'posix' para Linux/Mac
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Linux/Mac
    os.system('clear')

# **Início do programa:**
print("=" * 51)
print("Classificador de Consumo de Água em Imóveis Urbanos")
print("=" * 51)

# **Entrada de dados pelos usuários:**
# Solicita ao usuário que insira o tipo de imóvel.
imovel = input("Prezado cliente!\nQual é o seu tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
# .strip() remove espaços em branco no início e no final da string, enquanto .lower() converte a string para letras minúsculas.

# **Processamento e saída de dados:**
# Validação do tipo de imóvel inserido pelo usuário. 
# O programa utiliza a estrutura de decisão match:case para classificar o consumo mensal de água (em m³) de diferentes tipos de imóveis urbanos.
# Aplicação das regras de negócio para classificar o tipo de imóvel e no consumo mensal informado.
if imovel in ["comercial"]: # Aplica a tarifa comercial para imóveis comerciais.
    print("Tarifa comercial aplicada – Consulte o Plano corporativo.")
elif imovel in ["casa", "apartamento"]: # Continuação da aplicação das regras de negócio com base no tipo de imóvel e no consumo mensal de água.
    consumo = float(input("E qual é o seu consumo mensal de água em m³ (Utilize pontos para no lugar de vírgulas): ")) 
    # Validação e classificação do consumo de água.
    match consumo:
        case _ if imovel == "apartamento" and consumo < 10:
            print(f"Valor do consumo: {consumo:.2f} m³")
            print("CONSUMO ECONÔMICO – excelente controle de água!") # Imovvel tipo apartamento com consumo menor que 10 m³.
        case _ if (imovel == "apartamento" and 10 <= consumo <= 25) or (imovel == "casa" and consumo <= 25):
            # Como o caso consumo < 10 para apartamento já foi tratado acima, aqui entram os apartamentos com 10 m³ ou mais.
            print(f"Valor do consumo: {consumo:.2f} m³")
            print("CONSUMO MODERADO – dentro do padrão residencial.") # Imovveis tipo apartamento e casa com consumo entre 10 e 25 m³.
        case _:
            print(f"Valor do consumo: {consumo:.2f} m³")
            print("CONSUMO EXCESSIVO – adote medidas de economia e verifique vazamentos.") # Imovveis tipo apartamento e casa com consumo acima de 25 m³.
else:
    print("Tipo de imóvel inválido. Escolha comercial, casa ou apartamento.")
# Finalização do programa com uma mensagem de agradecimento ao usuário.
print("=" * 51)
print("Obrigado por utilizar nosso Classificador de Consumo de Água!")
print("=" * 51)








