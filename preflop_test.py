import csv
from deck_of_cards import deck_of_cards

FILE_PATH="data/Pre_Flop/RFI/UTG.csv"
# card.suit: 0=spades, 1=hearts, 2=diamonds, 3=clubs, 4=joker
# card.rank   1=Ace, 11=Jack, 12=Queen, 13=King, 14=B&W Joker, 15=Color Joker


def load_pre_flop_chart_to_dict(file_path):
    hand_action_dict = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hand_action_dict[row['hand']] = row['action']
    return hand_action_dict

def rank_to_symbol(card)->str:
    if(card.rank >=2 and card.rank<=9):
        return str(card.rank)
    else:
        match card.rank:
            case 1:
                return "A"
            case 10:
                return "T"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K" 
            case _:
                raise Exception(f"Couldn't format hand {card.name}")

def format_hand(c1,c2)->str:
    s1=rank_to_symbol(c1)
    s2=rank_to_symbol(c2)
    formatted_hand=f"{s1}{s2}"
    if c1.rank!=c2.rank:

        if(c1.suit==c2.suit):
            formatted_hand+="s"
        else:
            formatted_hand+="o"
    return formatted_hand

if __name__=="__main__":
    pf_action=load_pre_flop_chart_to_dict(FILE_PATH)
    deck = deck_of_cards.DeckOfCards()

    card1 = deck.give_random_card()
    card2 = deck.give_random_card()
    print(card1.name)
    print(card2.name)
    hand=format_hand(card1,card2)
    print(f"hand is {hand}, according to GTO the play here is: {pf_action.get(hand)}")