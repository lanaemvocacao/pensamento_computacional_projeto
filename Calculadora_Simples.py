'''


'''

print('\n Calculadora simples - Python Vocação\n')

numb_hum = input('Diggite o primeiro número: ')
numb_dois = input('Digite o segundo número: ')

operar_numb = input('Escolha a operação: 1-> +, 2-> -, 3-> *, 4-> /')

if operar_numb == '1' :
    result = int(numb_hum) + int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '2' :
    result = int(numb_hum) - int(numb_dois)
    print(f'O reultado é: {result}') 

elif operar_numb == '3' :
    result = int(numb_hum) * int(numb_dois)
    print(f'O reultado é: {result}') 

elif operar_numb == '4' :
    result = int(numb_hum) / int(numb_dois)
    print(f'O reultado é: {result}') 
    
else:
    print('Número não é válido, tente novamente!')

#     ###Calculadora Alta Dificuldade

# # 
# historico_detalhado = []

# # --- FUNÇÕES DE CÁLCULO ---

# def converter_valor(valor_texto):
#     """Converte string para int ou float dependendo do conteúdo."""
#     return float(valor_texto) if '.' in valor_texto else int(valor_texto)

# def operacao_matematica(n1, n2, op):
#     """Realiza operações básicas e retorna (símbolo, resultado)."""
#     if op == '1': return "+", n1 + n2
#     if op == '2': return "-", n1 - n2
#     if op == '3': return "*", n1 * n2
#     if op == '4':
#         if n2 == 0: return "/", "Indeterminado"
#         return "/", n1 / n2
#     return None, None

# def calcular_porcentagem(valor_p, valor_base, tipo):
#     """Processa os três tipos de cálculo de porcentagem."""
#     parte = (valor_p / 100) * valor_base
#     if tipo == '1':
#         return f"{valor_p}% de {valor_base} é {parte}"
#     if tipo == '2':
#         return f"{valor_base} com acréscimo de {valor_p}% = {valor_base + parte}"
#     if tipo == '3':
#         return f"{valor_base} com desconto de {valor_p}% = {valor_base - parte}"
#     return "Opção Inválida"

# # --- FUNÇÕES DE INTERFACE ---

# def exibir_menu():
#     print("\n" + "="*30)
#     print("      Calculadora - Python")
#     print("="*30)
#     print("1. Calcular (Inteiro/Decimal)")
#     print("2. Porcentagem")
#     print("3. Ver Histórico Detalhado")
#     print("0. Sair")

# def mostrar_historico():
#     print("\n--- HISTÓRICO DE OPERAÇÕES ---")
#     if not historico_detalhado:
#         print("Nenhum cálculo realizado.")
#     else:
#         for i, item in enumerate(historico_detalhado, 1):
#             print(f"{i}. {item}")

# # --- FLUXO PRINCIPAL (MAIN) ---

# def main():
#     while True:
#         exibir_menu()
#         escolha = input("\nOpção: ")

#         if escolha == '1':
#             n1 = converter_valor(input("Primeiro número: "))
#             n2 = converter_valor(input("Segundo número: "))
            
#             print("Operações: [1]+ [2]- [3]* [4]/")
#             op_mat = input("Operação: ")
            
#             simbolo, res = operacao_matematica(n1, n2, op_mat)
            
#             if simbolo:
#                 tipo_res = type(res).__name__
#                 registro = f"Cálculo: {n1} {simbolo} {n2} | Resultado: {res} | Tipo: {tipo_res}"
#                 print(f"\n>> {registro}")
#                 historico_detalhado.append(registro)

#         elif escolha == '2':
#             v_p = float(input("Valor da porcentagem: "))
#             v_b = float(input("Valor base: "))
            
#             print("1. Parte | 2. Acréscimo | 3. Desconto")
#             tipo_p = input("Opção: ")
            
#             msg = calcular_porcentagem(v_p, v_b, tipo_p)
#             print(f"\n>> {msg}")
#             historico_detalhado.append(msg)

#         elif escolha == '3':
#             mostrar_historico()

#         elif escolha == '0':
#             print("Encerrando... Até à próxima!")
#             break

# if __name__ == "__main__":
#     main()