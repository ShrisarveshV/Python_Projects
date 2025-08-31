#Blackjack Game
import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
player1,player2=[],[]
cards={1:1,2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
 'J': 10, 'Q': 10, 'K': 10, 'Ace': 11}
def less16():
    global player1,player2
    while sum(player1)<16:
        player1.append(random.choice(list(cards.values())))
    while sum(player2)<16:
        player2.append(random.choice(list(cards.values())))
def exceptions():
    if 11 in player1 and not sum(player1)<16:
        player1.remove(11)
        player1.append(1)
    if 11 in player2 and not sum(player2)<16:
        player2.remove(11)
        player2.append(1)
def winorlose():
    global player1, player2
    if sum(player1) == sum(player2) and (sum(player1)) < 22 and (sum(player2)) < 22:
        return "draw"
    elif (sum(player1)) > 21:
        print("Bust")
        return "you lose"
    elif (sum(player2)) > 21:
        print("Bust")
        return "you won"
    elif sum(player1) > sum(player2):
        return "you win"
    else:
        return "you lose"
def game():
    global player1, player2
    player1=random.sample(list(cards.values()),2)
    print("Your cards:",player1)
    player2 = random.sample(list(cards.values()), 2)
    print("Opponent:",player2[0])
    player1choice=input("Enter y to hit n to stand")
    while player1choice=="yes":
        player1.append(random.choice(list(cards.values())))
        print(player1)
        if (sum(player1)) > 21 or sum(player2) > 21:
            break
        player1choice = input("Enter yes to hit or no to stand")
    while(sum(player2)>21):
        player2.append(random.choice(list(cards.values())))

    if (sum(player1)) < 16 or (sum(player2)) < 16:
        less16()
    if (sum(player1)) > 21 or sum(player2) > 21:
        exceptions()
cont="yes"
while cont=="yes":
    print(logo)
    game()
    print("Your Deck:", player1, "\nOpponent Deck:", player2)
    print(winorlose())
    input("To play again type yess or noo to stop")
    player1,player2=[],[]
    print("\n"*100)
print("Good bye!!!")
