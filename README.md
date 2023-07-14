# Pequeno Sistema Bancário em Python com Usuários

Trata-se de uma pequeno sistema bancário de apenas com possibilidade de adição de usuários. Esta aplicação tem mais funções do que a sem usuários. E as funções de depósito, saque e visualização de extrato passa por validação de conta e usuário: se a conta não existir, o usuário não existir ou a conta não estiver vinculada ao usuário, a operação é cancelada.

## Cadastro de Usuário:

Um usuário é cadastrado informando nome, CPF, data de aniversário e endereço. Se não houver outro usuário cadastrado com o mesmo CPF, o usuário é adicionado na lista de usuários.

## Cadastro de Conta Bancária:

Após ser informado o CPF, uma conta bancária é cadastrada. O número dela é de o número de contas mais um. O usuário é o que tem o CPF informado. O número da agência é "0001". O saldo começa zerado. E a lista de movimentações (depósitos e saques) se inicia vazia.

## Depósito:

Após validação de conta e usuário, o programa pede que o valor seja informado. E o depósito só é feito se o valor for positivo.

## Saque:

Após validação de conta e usuário, o programa pede que o valor seja informado. Então o programa verifica se o valor é menor ou igual a R$500,00; se é menor que o saldo que o usuário tem na conta informada; ou se já houve menos que três saques na data de tentativa do saque. Se passar por todas essas verificações, o programa permite ao usuário o saque do valor e subtrai do saldo.

## Visualização de Extrato:

Após validação de conta e usuário, o programa mostra todas as movimentações na ordem em que foram feitas na conta informada. Por fim mostra o saldo.

## Lista de Usuários:

Exibe todos os usuários cadastrados no sistema. As informações de cada usuário que é exibida são: nome, data de nascimento, endereço e números das contas.

## 
## 

Esta aplicação foi desenvolvido como avaliação do Curso Ciências de Dados com Python, oferecido na plataforma DIO (Digital Innovation One.