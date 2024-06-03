let Score = [0, 0];
let currentPlayer = 'X';
let board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']];

const scoreElement = document.getElementById('score');
const boardElement = document.getElementById('board');

function createBoard() {
    boardElement.innerHTML = '';
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.addEventListener('click', () => onCellClick(row, col));
            boardElement.appendChild(cell);
        }
    }
}

function onCellClick(row, col) {
    if (board[row][col] === ' ' && currentPlayer === 'X') {
        board[row][col] = currentPlayer;
        updateBoard();
        if (checkWin(currentPlayer)) {
            Score[0]++;
            alert(`Player ${currentPlayer} wins!`);
            resetGame();
        } else if (checkDraw()) {
            alert('The game is a draw!');
            resetGame();
        } else {
            currentPlayer = 'O';
            setTimeout(computerMove, 500);
        }
    }
}

function computerMove() {
    const move = findBestMove();
    if (move) {
        const [row, col] = move;
        board[row][col] = 'O';
        updateBoard();
        if (checkWin('O')) {
            Score[1]++;
            alert('Computer wins!');
            resetGame();
        } else if (checkDraw()) {
            alert('The game is a draw!');
            resetGame();
        } else {
            currentPlayer = 'X';
        }
    }
}

function findBestMove() {
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (board[row][col] === ' ') {
                board[row][col] = 'O';
                if (checkWin('O')) {
                    board[row][col] = ' ';
                    return [row, col];
                }
                board[row][col] = ' ';
            }
        }
    }

    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (board[row][col] === ' ') {
                board[row][col] = 'X';
                if (checkWin('X')) {
                    board[row][col] = ' ';
                    return [row, col];
                }
                board[row][col] = ' ';
            }
        }
    }

    const emptyCells = [];
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (board[row][col] === ' ') {
                emptyCells.push([row, col]);
            }
        }
    }

    if (emptyCells.length > 0) {
        return emptyCells[Math.floor(Math.random() * emptyCells.length)];
    }
    return null;
}

function checkWin(player) {
    for (let row = 0; row < 3; row++) {
        if (board[row].every(cell => cell === player)) return true;
    }

    for (let col = 0; col < 3; col++) {
        if (board.every(row => row[col] === player)) return true;
    }

    if (board[0][0] === player && board[1][1] === player && board[2][2] === player) return true;
    if (board[0][2] === player && board[1][1] === player && board[2][0] === player) return true;

    return false;
}

function checkDraw() {
    return board.flat().every(cell => cell === 'X' || cell === 'O');
}

function updateBoard() {
    const cells = document.getElementsByClassName('cell');
    for (let i = 0; i < cells.length; i++) {
        const row = Math.floor(i / 3);
        const col = i % 3;
        cells[i].innerText = board[row][col];
    }
    scoreElement.innerText = `You ${Score[0]} - ${Score[1]} Computer`;
}

function resetGame() {
    currentPlayer = 'X';
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']];
    updateBoard();
}

createBoard();
