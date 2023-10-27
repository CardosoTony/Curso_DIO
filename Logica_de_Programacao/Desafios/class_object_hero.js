/*
# 3️⃣ Escrevendo as classes de um Jogo

** O Que deve ser utilizado **

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
- Classes e Objetos

## Objetivo:

Crie uma classe genérica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo(ex: guerreiro, mago, monge, ninja)

além disso, deve ter um método chamado atacar que deve atender os seguintes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}")
- aonde o { tipo } deve ser concatenando o tipo que está na propriedade da classe
- e no { ataque } deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir(usou magia)
se guerreiro -> no ataque exibir(usou espada)
se monge -> no ataque exibir(usou artes marciais)
se ninja -> no ataque exibir(usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
ex: mago atacou usando magia
    guerreiro atacou usando espada
*/

const attackTypes = {
  warrior: 'espada',
  mage: 'magia',
  monk: 'artes marciais',
  ninja: 'shuriken'
};

class Hero {
  constructor(name, age, heroType) {
    this.name = name;
    this.age = age;
    this.heroType = heroType;
    this.attackType = attackTypes[heroType];
  }

  attack() {
    console.log(`O ${this.heroType} atacou usando ${this.attackType}.`);
  }
}

const hero1 = new Hero('Zeno', 321, 'ninja');
const hero2 = new Hero('Zero', 539, 'mage');

hero1.attack();
hero2.attack();
