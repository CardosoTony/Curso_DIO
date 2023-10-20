const state = {
  view: {
    squares: document.querySelectorAll('.square'),
    enemy: document.querySelector('.enemy'),
    timeLeft: document.querySelector('#time-left'),
    score: document.querySelector('#score'),
    lives: document.querySelector('#count-lives')
  },
  values: {
    gameVelocity: 1000,
    hitPosition: 0,
    result: 0,
    currentTime: 30,
    lives: 3
  },
  actions: {
    timerId: setInterval(randomSquare, 1000),
    countDownTimerId: setInterval(countDown, 1000)
  }
};

function countDown() {
  state.values.currentTime--;
  state.view.timeLeft.textContent = state.values.currentTime;

  if (state.values.currentTime <= 0) {
    clearInterval(state.actions.countDownTimerId);
    clearInterval(state.actions.timerId);
    setTimeout(() => {
      alert("Time's up! Your score is: " + state.values.result);
    }, 100);
  }
};

function playSound(audioName) {
  let audio = new Audio(`./src/sounds/${audioName}.m4a`);
  audio.volume = .05;
  audio.play();
};

function randomSquare() {
  state.view.squares.forEach((square) => {
    square.classList.remove('enemy');
  });

  let randomNumber = Math.floor(Math.random() * 9);
  let randomSquare = state.view.squares[randomNumber];
  randomSquare.classList.add('enemy');
  state.values.hitPosition = randomSquare.id;
};

function addListenerHitBox() {
  state.view.squares.forEach((square) => {
    square.addEventListener('mousedown', () => {
      if (square.id === state.values.hitPosition) {
        state.values.result++;
        state.view.score.textContent = state.values.result;
        state.values.hitPosition = null;
        playSound('hit');
      } else {
        state.values.lives--;
        state.view.lives.textContent = 'x' + state.values.lives;

        if (state.values.lives === 0) {
          setTimeout(() => {
            const playAgain = confirm('Game Over! Your score is: ' + state.values.result + '. Play again?');

            if (playAgain) {
              resetGame();
            } else {
              clearInterval(state.actions.timerId);
              clearInterval(state.actions.countDownTimerId);

              state.values.hitPosition = null;
            }

          }, 100);
        } else {
          state.values.hitPosition = null;
        }

        playSound('error');
      }
    });
  });
};

function resetGame() {
  clearInterval(state.actions.timerId);
  clearInterval(state.actions.countDownTimerId);

  state.values.result = 0;
  state.view.score.textContent = 0;
  state.values.lives = 3;
  state.view.lives.textContent = 'x' + state.values.lives;
  state.values.currentTime = 30;
  state.view.timeLeft.textContent = state.values.currentTime;
  state.actions.timerId = setInterval(randomSquare, 1000);
  state.actions.countDownTimerId = setInterval(countDown, 1000);
};

function main() {
  addListenerHitBox();
};

main();
