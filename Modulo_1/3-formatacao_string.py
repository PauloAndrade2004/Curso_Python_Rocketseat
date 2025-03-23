# Descrição: Formatação de string

# %s - String
# %d - Inteiro
# %f - Float
# %r - Booleano

nome_completo = 'Paulo Cesar'
nome_completo_aspas = 'Oliveira'

print('Noem completo  (1a forma) ', nome_completo)
print('Noem completo  (2a forma) ' + nome_completo)

print('Noem completo  (3a forma) ' + 'Paulo' + 'Cesar')
print('Noem completo  (4a forma) ' + 'Paulo', 'Cesar')

print('Nome completo  (6a forma) %s %s' % (nome_completo, nome_completo_aspas))

print(f'Nome completo (7a forma) {nome_completo} {nome_completo_aspas}')
