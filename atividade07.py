# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
produto =int(input("digite o valor do produto"))
imposto = produto * 1.12
print(f"o seu produto com imposto fica:R$ {imposto}")