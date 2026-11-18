
# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, seleção aleatória, loops, condicionais e entrada de dados criando um jogo da Forca. O jogador deve descobrir uma palavra oculta antes de esgotar as tentativas disponíveis.

## 📝 Tarefas

### 🛠️ Preparar a palavra e o estado do jogo

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher uma palavra secreta aleatoriamente e inicialize as variáveis necessárias para acompanhar o andamento da partida.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Inicializar o registro de letras escolhidas, o contador de palpites incorretos e o limite de tentativas.
- Exibir a palavra oculta como espaços reservados, por exemplo, `_ _ _ _`.

### 🛠️ Implementar as rodadas da Forca

#### Descrição
Crie o loop principal que recebe palpites de letras, atualiza o progresso e encerra a partida quando o jogador vencer ou ficar sem tentativas.

#### Requisitos
O programa concluído deve:

- Solicitar palpites de letras ao jogador e revelar no progresso as posições correspondentes na palavra secreta.
- Contabilizar palpites incorretos e mostrar quantas tentativas ainda restam.
- Encerrar a partida quando a palavra for adivinhada ou quando as tentativas incorretas se esgotarem.
- Exibir uma mensagem de vitória ou derrota ao final da partida.