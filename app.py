
from asyncore import loop
from characterai import pyCAI
import asyncio
from flask import Flask, render_template, request

token = '78e48c076edb65b7cad37810bb9b871c9923a33a'
character = 'nlI-zcyxVngHJ0EdAECYG5AsqjyZdrwd79cXuDwkcBo'




app = Flask(__name__)

def game_logic(send):
    print("yeyeyyeyee")
    if send == "exit()":
        return "Exiting the game..."
    else:
        client = pyCAI(token)

        output = (client.chat.send_message(character, send))
        print(output)
        return f'Astronaut Friend: {output}'

@app.route('/')
def index():
    if request.method == 'POST':
        send = request.form['send']
        result = loop.run_until_complete(game_logic(send))
        return render_template('game.html', response=result)
    else:
        return render_template('game.html')


@app.route('/play', methods=['POST'])
def play():
    user_input = request.form['user_input']
    # Process user input and update game state
    # Generate appropriate game text based on user input

    game_output = f"{game_logic(user_input)}"
    return render_template('game.html', game_text= game_output)


if __name__ == '__main__':
    app.run(debug=True)



'''
app = Flask(__name__, template_folder='Users/thomaslee/game/templates/')



async def game_logic(send):
    if send == "exit()":
        return "Exiting the game..."
    else:
        client = pyCAI(token)
        return f'Astronaut Friend: {client.chat.send_message(character, send)}'


@app.route('/game')
def game():
    if request.method == 'POST':
        send = request.form['send']
        result = loop.run_until_complete(game_logic(send))
        return render_template('game.html', response=result)
    else:
        return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)

'''