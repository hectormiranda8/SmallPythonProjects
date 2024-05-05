"""
Blackjack, also known as 21, is a card game 
where players try to get as close to 21 points 
as possible without going over. This program 
uses images drawn with text characters, called 
ASCII art. American Standard Code for Information 
Interchange (ASCII) is a mapping of text characters 
to numeric codes that computers used before Unicode 
replaced it. The playing cards in this program are an 
example of ASCII art:
 ___   ___
| A | |10 |
| ♣ | | ♦ |
|__A| |_10| ♥ ♠
"""
from __future__ import annotations
from bisect import bisect
from typing import NoReturn
import random
import sys


CARDVALUES  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
CARDDESIGN  = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K"
}
SPADES      = "spades"
HEART       = "heart"
DIAMOND     = "diamond"
CLUBS       = "clubs"
SYMBOLS     = [SPADES, HEART, DIAMOND, CLUBS]
SYMBOLSDICT = {
    SPADES: "♠",
    HEART: "♥",
    DIAMOND: "♦",
    CLUBS: "♣",
}


class Game:
    def __init__(self):
        print("""   Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.""")
        self.money = 5000
        self.run_game = True
        self.bet = 0
        self.gameSetUp()
    
    def quitGame(self) -> NoReturn:
        print("Thanks for playing Blackjack!")
        self.run_game = False
        sys.exit()

    def hit(self, player: Player) -> None:
        player.addCard()

        drawnCard = player.hand[-1]
        print(f"\n{player.name} has drawn a {drawnCard.value_symbol} of {drawnCard.symbol}")
        print(f"{player.name}: {' | '.join(str(ct) for ct in player.curr_total)}")
        player.drawHand()
        print()

        if player == self.player:
            self.checkPlayerHand()

    def stand(self) -> None:
        self.dealerPlay()
        self.checkWinner()

    def dealerReveal(self) -> None:
        print("Revealing DEALER hand: "
              f"{' | '.join(str(ct) for ct in self.dealer.curr_total)}")
        self.dealer.hand[0].hidden = False
        self.dealer.drawHand()
        print()

    def dealerPlay(self) -> None:
        self.dealerReveal()
        if self.blackjackHand(self.dealer):
            return
        elif min(self.dealer.curr_total) < 17:
            while min(self.dealer.curr_total) < 17:
                self.hit(self.dealer)
                if self.blackjackHand(self.dealer):
                    return

    def stageInput(self, can_double: bool=True) -> None:
        valid = False
        while not valid:
            try:
                user_input = input("> ").lower()
                if user_input == "h":
                    valid = True
                    self.hit(self.player)
                elif user_input == "s":
                    valid = True
                    self.stand()
                elif user_input == "d" and can_double:
                    valid = True
                    self.bet *= 2
                    print(f"Double Down! Current bet is now ${self.bet}")
                    self.hit(self.player)
                    if self.run_game: # hit may have changed game state
                        self.stand()
                else:
                    raise Exception()
            except:
                print("Please select a valid option.")
                print("(H)it, (S)tand, (D)ouble down")

    def betInput(self) -> int:
        valid = False
        user_input = -1
        while not valid:
            try:
                user_input = input("> ")
                user_input.lower()
                if user_input == "quit" or user_input == "q":
                    self.quitGame()
                user_input = int(user_input)
                if user_input < 1 or user_input > self.money:
                    raise Exception()
                valid = True
            except Exception:
                print(f"Please select a valid option. (1-{self.money} or (Q)UIT)")
        return user_input

    def blackjackHand(self, player: Player) -> bool:
        if 21 in player.curr_total:
            return True
        return False

    def checkPlayerHand(self, initial: bool=False) -> None:
        if self.blackjackHand(self.player):
            print(f"Amazing! 21 hand!")
            if not initial:
                self.stand()
            else:
                self.dealerReveal()
                self.checkWinner()
        elif min(self.player.curr_total) > 21:
            print(f"BUST! Unfortunate... You've lost ${self.bet}")
            self.playerOutcome(loser=True)
            
    def playerOutcome(self, loser: bool=False) -> None:
        if not loser:
            self.money += self.bet
        else:
            self.money -= self.bet
        self.bet = 0
        self.run_game = False

    def bestHand(self, player: Player) -> int:
        player.curr_total.sort()
        return player.curr_total[bisect(player.curr_total, 21)-1]

    def checkWinner(self) -> None:
        if min(self.dealer.curr_total) > 21:
            print(f"DEALER busted! You've won ${self.bet}!")
            self.playerOutcome()
            return
        elif self.blackjackHand(self.dealer):
            if self.blackjackHand(self.player):
                print("PUSH! Restarting game :/")
                self.bet = 0
                self.run_game = False
                return
            else:
                print(f"How unfortunate is your luck... You've lost ${self.bet}")
                self.playerOutcome(loser=True)
        elif self.blackjackHand(self.player):
            print(f"Nice! a 21! Congratulations, you've won ${self.bet}")
            self.playerOutcome()
        else:
            player_card = self.bestHand(self.player)
            dealer_card = self.bestHand(self.dealer)
            player_loser = False
            if player_card > dealer_card:
                print(f"Congrats! You've won ${self.bet}")
            elif player_card < dealer_card:
                print(f"Unfortunate... Good luck next Time. You've lost ${self.bet}")
                player_loser = True
            else:
                print("PUSH! Restarting game :/")
                self.bet = 0
                self.run_game = False
                return
            self.playerOutcome(loser=player_loser)

    def gameSetUp(self) -> None:
        self.run_game = True

        print(f"\nMoney: ${self.money}")
        print(f"How much do you bet? (1-{self.money}, or (Q)UIT)")
        self.bet = self.betInput()

        self.player = Player("PLAYER")
        self.dealer = Player("DEALER")
        self.dealer.addCard(hidden=True)
        self.dealer.addCard()
        self.player.addCard(other=self.dealer.hand)
        self.player.addCard(other=self.dealer.hand)

        print("\nDEALER: ???")
        self.dealer.drawHand()
        print(f"\nPLAYER: {' | '.join(str(ct) for ct in self.player.curr_total)}")
        self.player.drawHand()
        print()
        self.checkPlayerHand(initial=True)

        self.gameLoop()

    def gameLoop(self) -> None:
        while self.run_game:
            if self.money < 1:
                print("You've ran out of money.. GL next time!")
                self.quitGame()
            if self.run_game: # may have changed during stages
                can_double = self.bet * 2 < self.money
                print(f"\n(H)it, (S)tand{', (D)ouble down' if can_double else ''}")
                self.stageInput(can_double=can_double)

        self.gameSetUp()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []
        self.curr_total = [0]
        self.has_ace = False

    def __getRandomCard(self, hidden: bool=False) -> Card:
        return Card(random.choice(CARDVALUES),
                    random.choice(SYMBOLS),
                    hidden=hidden)

    def addCard(self, other: Player=None, hidden: bool=False) -> None:
        randCard = self.__getRandomCard(hidden=hidden)
        while randCard in self.hand \
            or (other is not None and randCard in other):
            randCard = self.__getRandomCard(hidden=hidden)
        self.hand.append(randCard)

        if randCard.value_symbol == "A":
            self.curr_total = [v + 1 for v in self.curr_total] \
                            + [v + 11 for v in self.curr_total]
        elif randCard.value_symbol in CARDDESIGN.values():
            self.curr_total = [v + 10 for v in self.curr_total]
        else:
            self.curr_total = [v + randCard.value for v in self.curr_total]

    def drawHand(self) -> None:
        top = " ___  " * len(self.hand)
        topr = ""
        mid = ""
        bot = ""

        for c in self.hand:
            if c.hidden:
                v = "# "
                v2 = "_#"
                curr_symbol = "#"
            else:
                v = c.value_symbol
                v2 = v if len(v) == 2 else "_" + v
                if len(v) < 2:
                    v += " "
                curr_symbol = c.symbol

            topr += f"|{v} | "
            mid += f"| {curr_symbol} | "
            bot += f"|_{v2}| "

        print(top)
        print(topr)
        print(mid)
        print(bot)


class Card:
    def __init__(self, value: int, card_type: str, hidden=False):
        self.value = value
        self.value_symbol = self.__getValueSymbol()
        self.symbol = SYMBOLSDICT[card_type]
        self.hidden = hidden
    
    def __eq__(self, other: Card) -> bool:
        if self.value == other.value \
            and self.symbol == other.symbol:
            return True
        return False
    
    def __getValueSymbol(self) -> str:
        if self.value in CARDDESIGN.keys():
            return CARDDESIGN[self.value]
        else:
            return str(self.value)
        

if __name__ == "__main__":
    game = Game()