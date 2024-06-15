# write 'hello world' to the console
## print('hello world')


## crea una aplicacion donde el ganador del juego estará determinado por tres reglas simples:
## La Rock gana a las tijeras.
## Las Scissors ganan al papel.
## El Paper gana a la piedra.
## El jugador podrá elegir una de las tres opciones, rock, paper o scissors, y se le debería advertir en caso de ## introducir una opción no válida.
## En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
## Al final de cada ronda, el jugador elegirá si vuelve a jugar.
## Muestra la puntuación del jugador al final del juego.
## El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.

import random
import sys

def game():
    player_score = 0
    computer_score = 0
    while True:
        print(f'Player score: {player_score} Computer score: {computer_score}')
        player_choice = input('Choose rock, paper or scissors: ').lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print('Invalid choice')
            continue
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f'Computer choice: {computer_choice}')
        if player_choice == computer_choice:
            print('Tie')
        elif player_choice == 'rock' and computer_choice == 'scissors':
            print('You win')
            player_score += 1
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('You win')
            player_score += 1
        elif player_choice == 'paper' and computer_choice == 'rock':
            print('You win')
            player_score += 1
        else:
            print('You lose')
            computer_score += 1
        if input('Play again? (y/n): ').lower() != 'y':
            break
    print(f'Player score: {player_score} Computer score: {computer_score}')

## ejecuta la app
game()