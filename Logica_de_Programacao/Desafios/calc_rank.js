/*
# 2️⃣ Calculadora de partidas Ranked
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Ranked deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nível}**"
*/

function calculateWinLoss(victoryCount, defeatCount) {
  const winLossBalance = victoryCount - defeatCount;
  return winLossBalance;
}

function rankValidate() {
  let rank = '';

  switch (true) {
    case (result <= 10):
      rank = 'Ferro';
      return rank;
    case (result >= 11 && result <= 20):
      rank = 'Bronze';
      return rank;
    case (result >= 21 && result <= 50):
      rank = 'Prata';
      return rank;
    case (result >= 51 && result <= 80):
      rank = 'Ouro';
      return rank;
    case (result >= 81 && result <= 90):
      rank = 'Diamante';
      return rank;
    case (result >= 91 && result <= 100):
      rank = 'Lendário';
      return rank;
    default:
      rank = 'Imortal';
      return rank;
  }
}

let result = calculateWinLoss(20, 5);
let tier = rankValidate();

console.log(`O Herói tem o saldo de "${result}" vitória e está no nível de "${tier}"`);
