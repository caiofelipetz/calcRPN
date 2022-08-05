import re,time



# Caio Felipe Trindade Zehnder
# Trabalho utiliza menos bibliotecas possiveis, para solução mais rapida (biblioteca para cronometro e uma para extração dos dados do input, apenas)

#entrada = str('3.5 4 2 * 1 5 - 2 3 ^ * / +')
entrada = input("Digite a operação matematica: ")
entradaSplit = re.findall('[\d]*[.][\d]+|[\d]+|\+|\-|\*|\/|\^',entrada)      #retira todos os numeros e sinais matematicos e apenda, em ordem, na lista 'entradaSplit'

start_time = time.time() # Starta o cronometro de execução logo após o input do usuario

counter=0 # Variavel para gerir as posições do index da lista para as operações de substituição e pop() de valores

while (len(entradaSplit) > 1):  #Se tiver mais de um valor dentro da lista, vai continuar rodando até que sobre apenas 1 termo (1 valor = solução encontrada)
    
    if entradaSplit[counter] == '*':  #a logica consiste em achar algum operador matemático {(exemplo:  1 3 +) -> [neste exemplo] vai aumentar o valor de 'counter' até que entradaSplit[counter] = +, depois disso, faz a operação
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) * float(entradaSplit[counter-1])  # matematica e substitui o valor de index anterior para o resultado da operação, deleta o outro numero usado na operação e o sinal matematico,
        entradaSplit.pop(counter)                                                                  # depois volta o valor de 'counter' para 'counter=counter-2' , pois excluimos 2 termos via pop(), e repete o ciclo
        entradaSplit.pop(counter-2)                                                                # até que tenha apenas um numero na lista 'entradaSplit'}
        print(entradaSplit)
        counter=counter-2
    if entradaSplit[counter] == '/':
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) / float(entradaSplit[counter-1])
        entradaSplit.pop(counter)
        entradaSplit.pop(counter-2)
        print(entradaSplit)
        counter=counter-2
    if entradaSplit[counter] == '-':
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) - float(entradaSplit[counter-1])
        entradaSplit.pop(counter)
        entradaSplit.pop(counter-2)
        print(entradaSplit)
        counter=counter-2
    if entradaSplit[counter] == '+':
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) + float(entradaSplit[counter-1])
        entradaSplit.pop(counter)
        entradaSplit.pop(counter-2)
        print(entradaSplit)
        counter=counter-2

    counter=counter+1

print('\n','Resultado: ','\n',entradaSplit[0])
print('\n','--- %s seconds ---' % (time.time() - start_time))
