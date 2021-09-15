tabela = 'Café', 5.60, 'Pão', 2.50, 'Toalha', 30.00, 'Boneca', 46.30
print(len(tabela))
print('='* 30)
print('      Listagem de preços')
print('=' * 30)
print(f'{tabela[0]}.....................R${tabela[1]}\n'
      f'{tabela[2]}......................R${tabela[3]}\n'
      f'{tabela[4]}...................R${tabela[5]}\n'
      f'{tabela[6]}...................R${tabela[7]}\n')
print('=' * 30)
