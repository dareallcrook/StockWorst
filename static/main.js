
const board = Chessboard('board', { draggable: true });
const game = new Chess();

function findWorstMove() {
    fetch('/worstmove?fen=' + game.fen())
        .then(response => response.json())
        .then(data => {
            game.move(data.worst_move);
            board.position(game.fen());
        });
}
