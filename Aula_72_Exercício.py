produtos_lista = open('Aula_72_Exercício.txt', 'r')
produtos = produtos_lista.readlines()
# Tira o '\n' do final de cada frase
produtos = [x.rstrip('\n') for x in produtos]

carrinho = (('0001'), ('0023'), ('0024'), ('0025'), ('0004'))

total = []
for item_c in carrinho:
    for prod_k in produtos:
        if prod_k == '':
            del prod_k
        else:
            # se os primeiros 4 forem iguais ao encontrados vai retornar 0
            if str(prod_k.find(item_c)) == '0':
                print(f'\t{prod_k}\n')
                # esse + 2 é pra pular o R$ e pegar só os números
                valor = prod_k[prod_k.find('R$') + 2:len(prod_k)]
                # troca ',' por '.' e transforma em float
                total.append(float(valor.replace(',', '.')))
                break

total = sum(total)
print(f'Total: {total}\n')
