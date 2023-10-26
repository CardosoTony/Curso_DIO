/*
# 1️⃣ Desafio Classificador de nível de Herói

** O Que deve ser utilizado **

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência(XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 6.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000 = Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nível}**"
*/

const nameHero = 'Link';
const experience = 11000;
let rank = '';

switch (true) {
  case (experience >= 1001 && experience <= 2000):
    rank = 'Bronze';
    break;
  case (experience >= 2001 && experience <= 6000):
    rank = 'Prata';
    break;
  case (experience >= 6001 && experience <= 7000):
    rank = 'Ouro';
    break;
  case (experience >= 7001 && experience <= 8000):
    rank = 'Platina';
    break;
  case (experience >= 8001 && experience <= 9000):
    rank = 'Ascendente';
    break;
  case (experience >= 9001 && experience <= 10000):
    rank = 'Imortal';
    break;
  case (experience >= 10001):
    rank = 'Radiante';
    break;
  default:
    rank = 'Ferro';
    break;
}

console.log(`O Herói de nome "${nameHero}" está no nível de "${rank}"`);
