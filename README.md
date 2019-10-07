# Design Document: blackjack.py 

blackjack.py is a single player blackjack game written for the 2019 Kleiner Perkins Engineering Fellow Challenge

## Usage

Use python3 to run the game 

```bash
python3 blackjack.py
```
The player starts with 1000 units of currency in the player's bank. Instructions are given through the terminal. 

## Design Choices


The object oriented approach (with separate `Card`, `Deck`, `Hand`, and `Player` being separate classes) allows for easy, modularized manipulation and makes future improvements (such as adding more players) easy. In hindsight, Java would have been just as good, if not a better language. 

I stored each `Card` in a list to represent a `Hand` and `Deck`. Because the code only `pop()`s and `appends()`s cards, the time complexity is O(1), constant time. 
    

## Choice of Tooling
Language: Python OOP

I chose an OOP approach with Python. Python was selected because building a card game does not require the efficiencies one might be able to leverage with a low level language like C. In addition, libraries like `random` make deck management easy. 


## Future Improvements

Hand win/lose was not efficient and not well designed. A lot of end game (or end hand) behavior can be optimized. The checks could be moved into one of the classes and called after each action. 

I intended to build a Blackjack trainer for basic strategy (to help players memorize the correct move) , utilizing a dictionary. The value on the board (key) would compare the users decision with a definition (correct/incorrect). The time complexity of dictionary is constant time O(1) and efficient in this case. 
