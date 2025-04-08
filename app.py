
from flask import Flask, request, jsonify, render_template
import chess
import chess.engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/worstmove')
def worst_move():
    fen = request.args.get('fen')
    board = chess.Board(fen)
    engine = chess.engine.SimpleEngine.popen_uci('stockfish')
    worst_eval = float('inf')
    worst_move = None
    for move in board.legal_moves:
        board.push(move)
        info = engine.analyse(board, chess.engine.Limit(depth=10))
        score = info['score'].relative.score(mate_score=10000) or 0
        if score < worst_eval:
            worst_eval = score
            worst_move = move.uci()
        board.pop()
    engine.quit()
    return jsonify({'worst_move': worst_move})

if __name__ == '__main__':
    app.run(debug=True)
