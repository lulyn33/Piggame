import random
def roll():
    minvalue = 1
    maxvalue = 6
    roll = random.randint(minvalue,maxvalue)
    return roll
#x = roll()
#print(x)

while True:
     players = input('Enter the number of players (2-4): ')
     if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 - 4 players')
     else:
        print('Invalid,try again')
print(players)

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for players_idx in range(players):
        print('\nPlayers number', players_idx +1,'turn has just started!\n')
        print('Your total score is:',players_scores[players_idx],'\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)? ')
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a: ', value)
                print('Your score is:', current_score)

        players_scores[players_idx] += current_score
        print('Your total score is :',players_scores[players_idx])

max_score = max(players_scores)
winning = players_scores.index(max_score)
print('Player number', winning+1,
      'is the winner with a score of: ',max_score)
