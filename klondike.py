import random
import copy

class Card:
    numstr_dict = {
        1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven",
        8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"
    }
    color_dict = {
        "Diamond":"Red",
        "Heart"  :"Red",
        "Club"   :"Black",
        "Spade"  :"Black"
    }
    def __init__(self, mark, number, fab=False):
        self.mark = mark = mark
        self.number = number
        self.color = self.color_dict[mark]
        self.numstr = self.numstr_dict[number]
        self.fab = fab

    def getData(self):
        return (self.mark, self.number, self.color, self.numstr, self.fab)

    def getMAN(self):
        
        man = self.mark[0] + "_" + str(self.number)
        if(self.number <= 9):
            man = self.mark[0] + "_" + "_" + str(self.number)
        return man


class Deck:

    def __init__(self):
        self.deck = []
        for mark in ["Diamond", "Heart", "Club", "Spade"]:
            for num in range(1, 14):
                self.deck.append(Card(mark, num))
        self.frontCard = None
        self.index = 0

    def shuffleCards(self):
        random.shuffle(self.deck)

    def getInitCard(self):
        card = self.deck.pop(-1)
        return card

    def turnCard(self):
        
        if (len(self.deck) != 0 and abs(self.index) < len(self.deck)):
            self.index -= 1
            self.frontCard = self.deck[self.index]
        elif(len(self.deck) != 0 and abs(self.index) >= len(self.deck)):
            self.frontCard = None
            self.index = 0
            print("山札をリセットしました。")
        else:
            print("山札にカードがありません。")

    def getTempFrontCard(self):
        if (self.frontCard != None):
            card = copy.deepcopy((self.frontCard))
            card.fab = True
            return card
        return None

    def getFrontCard(self):
        if (self.frontCard != None and (self.frontCard in self.deck)):
            self.deck.remove(self.frontCard)
            card = self.frontCard
            card.fab = True
            if (self.index == -1):
                self.frontCard = None
                self.index = 0
            else:
                self.index += 1
                self.frontCard = self.deck[self.index]
            return card
        print("山札のカードが表示されていないため、選択することができません。")
        return None


class ColumnDeck:

    def __init__(self):
        self.colDeck = []

    def setInitCard(self, card):
        self.colDeck.append(card)

    def confSetCard(self, card, deck=None):
        if (deck == None):
            deck = self.colDeck[:]
        if (len(deck) == 0 and (card.number == 13) and card.fab):
            return True
        elif (len(deck) != 0 and card.fab):
            obj = deck[-1]
            if (obj.color != card.color and (obj.number - card.number) == 1 and obj.fab):
                return True
            else:
                print("色、数字、表裏が正しくありません。")
                print("移動先 : ", obj.getData())
                print("移動元 : ", card.getData())
                return False
        else:
            print("Error : ColumnDeck")
            print(card.getData())
            return False

    def confSetCard(self, cards):
        tmpcolDeck = self.colDeck[:]
        for card in cards:
            if (self.confSetCard(card, tmpcolDeck)):
                tmpcolDeck.append(card)
            else:
                return False
        return True

    def setCard(self, card):
        self.colDeck.append(card)

    def setCards(self, cards):
        for card in cards:
            self.setCard(card)

        def getCards(self, index):

            if (len(self.colDeck) != 0):
                cards = self.colDeck[index:]
                del self.colDeck[index:]
                if (len(self.colDeck) != 0):
                    self.colDeck[-1], fab = True
                return cards
            print("列にカードがないため、選択することができません。(ColumnDeck : getCards)")
            return []

        def getTempCards(self, index):
            if (len(self.colDeck) > index):
                cards = self.colDeck[index:]
                for card in cards:
                    if (card.fab == False):
                        return None
                return cards
            print("列にカードがないため、選択することができません。(ColumnDeck : getTempCards)")
            return None


class MarkDeck:
    def __init__(self, mark):
        self.markDeck = []
        self.mark = mark
        self.topCard = None

    def confSetCard(self, card):
        if (self.mark == card.mark):
            if ((len(self.markDeck) + 1) == card.number):
                return True
            else:
                print("数字が異なります。")
                print("組札に移動できる数字 : ", len(self.markDeck)+1)
                print("cardの数字 : ", card.number)
                return False
        else:
            print("マークが異なります。")
            print("組札のマーク : ", self.mark)
            print("cardのマーク : ", card.mark)
            return False

    def setCard(self, card):
        self.markDeck.append(card)
        self.topCard = card

    def getTempCard(self):
        if (len(self.markDeck) != 0):
            card = self.markDeck[-1]
            return card
        return None

    def getCard(self):
        if (len(self.markDeck) != 0):
            card = self.markDeck.pop(-1)
            if (self.topCard.number == 1):
                self.topCard = None
            else:
                self.topCard = self.markDeck[-1]
            return card
        return None


# DeckとMarkDeckの表示設定
def printDeck(deck, markDecks):

    print("")
    print(" +------+             +------+------+------+------+")
    print(" | Deck |             |   S  |   H  |   C  |   D  |")
    print(" +------+             +------+------+------+------+")
    print(" | ", end="")
    man = " "*4
    if (type(deck.frontCard) == Card):
        man = deck.frontCard.getMAN()
    print("{0} |             ".format(man), end="")
    #print("| ---- |             | ---- | ---- | ---- | ---- |")
    print("| ", end="")
    for markDeck in markDecks.values():
        man = " "*4
        card = markDeck.topCard
        if(type(card) == Card):
            man = card.getMAN()
        print("{0} | ".format(man), end="")
    print("")
    #print("| ---- |             | ---- | ---- | ---- | ---- |")
    print(" +------+             +------+------+------+------+")
    print("")

#カラム見出しの表示設定
def printHeader():

    colList = ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7"]
    print(" +------+------+------+------+------+------+------+")
    print(" | ", end="")
    for col in colList:
        print(col, "| ", end="")
    print("")
    print(" ==================================================")

def printColDeck(decklist):
    printHeader()
    # data
    leng = 0
    for obj in decklist:
        if (leng < len(obj.colDeck)):
            leng = len(obj.colDeck)
    #print(leng)
    #        1   2   3   4   5   6   7   8   9   10
    llist = [[], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], []]
    for obj in decklist:
        objleng = len(obj.colDeck)
        for i in range(objleng):
            card = obj.colDeck[i]
            if(card.fab):
                s = card.mark[0] + "_" + str(card.number)
                if (card.number <= 9):
                    s = card.mark[0] + "_" + "_" + str(card.number)
                    llist[i].append(s)
                else:
                    llist[i].append("Back")
            for i in range(objleng, leng):
                llist[i].append('    ')

    for i in range(leng):
        print(" | ", end="")
        for card in llist[i]:
            print(card, "| ", end="")
        if(i <= 9):
            print("  {0} ".format(i+1))
        else:
            print(" {0} ".format(i+1))
        print(" +------+------+------+------+------+------+------+")
    print("")

#コマンド表示設定
def printCmd():
    cmddict = {
        "山札を見る":"Turn",
        "山札のカードを指定する":"Deck",
        "列のカードを指定する":"Row, Column",
        "組札のカードを指定する":"Spade or Heart or Club or Diamond",
    }
    print(" +" + "-"*24 + "+" + "-"*35 + "+")
    header = ["行動", "コマンド"]
    print(" | " + header[0].center(11, "　") + " | " + header[1].center(29, " ") + " |")
    print(" " + "="*62)
    for k, v in cmddict.items():
        print(" | " + k.ljust(11, '　') + " | " + v.ljust(33, " ") + " |")
        print(" +" + "-"*24 + "+" + "-"*35 + "+")

#選択されたカード一覧
def printCards(cards):
    if (type(cards) in [list, Card]):
        print("Card : ", end="")
        if (type(cards) == list):
            for card in cards:
                print(card.getMAN(), ",", end="")
            print("")
        elif (type(cards) == Card):
            print(cards.getMAN())
    pass

# cmd : row, col判定
def confRowCol(cmd):
    if ("," in cmd):
        cmdlist = cmd.split(",")
        confRow = True if cmdlist[0] in rowNumList else False
        confCol = True if cmdlist[1] in corNumList else False
        if (confRow and confCol):
            return True
    return False

# 勝利条件の確認
def CheckEnd(mdd):
    #mdd = markDeckDict
    for v in mdd.values():
        if (len(v.markDeck) == 13): pass
        else: return False
    return True

def main():
    #山札
    myDeck = Deck()
    myDeck.shuffleCards()

    #組札
    DDeck = MarkDeck("Diamond")
    HDeck = MarkDeck("Heart")
    SDeck = MarkDeck("Spade")
    CDeck = MarkDeck("Club")
    markDeckDict = {"Spade":SDeck, "Heart":HDeck, "Club":CDeck, "Diamond":DDeck}

    #場札の列
    fieldDecks = []
    for _ in range(7):
        fieldDecks.append(ColumnDeck())

    #初期カード設定
    for i in range(7):
        colDeck = fieldDecks[i]
        for _ in range(i+1):
            colDeck.setInitCard(myDeck.getInitCard())

    # 1番手前のカードを表向きに
    for deck in fieldDecks:
        deck.colDeck[-1].fab = True

    
    global rowNumList
    global colNumList
    rowNumList = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
    colNumList = ["1", "2", "3", "4", "5", "6", "7"]
    markList = ["Spade", "Heart", "Club", "Diamond"]

    # 初期状態表示
    printDeck(myDeck, markDeckDict)
    printColDeck(fieldDecks)
    printCmd()

    # ループ処理
    play_count = 0
    while(True):
        cmd = input("コマンド : ")
        if ((cmd == "Turn") or (cmd == "turn")):
            print("Turn up a card.")
            myDeck.turnCard()
        elif (cmd in ["Deck", "deck"]):
            card = myDeck.getTempFrontCard()
            printCards(card)
            if (type(card) == Card):
                print("Please select destination. ex) Column, Spade, etc...")
                dest = input("Destination : ")
                if (dest in colNumList):
                    if (fieldDecks[int(dest)-1].confSetCard(card)):
                        card = myDeck.getFrontCard()
                        fieldDecks[int(dest)-1].setCard(card)
                    else:
                        print("")
                        continue
                elif (dest in markList):
                    if (markDeckDict[dest].confSetCard(card)):
                        card = myDeck.getFrontCard()
                        markDeckDict[dest].setCard(card)
                    else:
                        print("")
                        continue
                else:
                    print("その移動先は選択できません。")
                    print("Destination : ", dest)
                    continue
            else:
                print("The deck has no opend card. Do Turn.")
                print("")
                continue
        elif (confRowCol(cmd)):
            cmdlist = comd.split(",")
            row = int(re.sub("\\D", "", cmdlist[0]))
            col = int(re.sub("\\D", "", cmdlist[1]))
            if (str(row) in rowNumList and str(col) in colNumList):
                cards = fieldDecks[col-1].getTempCards(row-1)
                if (cards != None):
                    printCards(cards)
                    print("Please select destination. ex) Column, Spade, etc...")
                    dest = input("Destination : ")
                    if (dest in colNumList):
                        if (fieldDecks[int(dest)-1].confSetCard(cards)):
                            cards = fieldDecks[col-1].getCards(row-1)
                            fieldDecks[int(dest)-1].setCards(cards)
                    elif (dest in markList):
                        print(dest, " : ", markList)
                        if (markDeckDict[dest].confSetCard(cards[0])):
                            cards = fieldDecks[col-1].getCards(row-1)
                            markDeckDict[dest].setCard(cards[0])
                    else:
                        print("その移動先は選択できません。")
                        print("")
                        continue
                else:
                    print("{0}, {1}にカードがありません。".format(row, col))
                    print("")
                    continue
            else:
                print("カードの選択の仕方が間違っています。正例：2, 3")
        elif (cmd in markList):
            card = markDeckDict[cmd].getTempCard()
            if (card != None):
                printCards(card)
                print("Please select destination.", end="")
                print("ex) Column(1~7)")
                dest = input("Destination : ")
                if (dest in colNumList):
                    if (fieldDecks[int(dest)-1].confSetCard(card)):
                        card = markDeckDict[cmd].getCard()
                        fieldDecks[int(dest)-1].setCards(card)
                    else:
                        print("")
                        continue
                else:
                    print("その移動先は選択できません。")
                    print("Destination : ", dest)
                    continue
            else:
                print("{0}にカードがありません。".format(cmd))
                print("")
                continue
        elif (cmd == "End" or cmd == "end"):
            print("終了します。")
            break
        else:
            print("That command is wrong.")
            print("")
            continue

        printDeck(myDeck, markDeckDict)
        printColDeck(fieldDecks)
        play_count += 1
        if (CheckEnd(markDeckDict)):
            print("お疲れさまでした！")
            print("play_count : ", play_count)
            break
        printCmd()

if __name__ == '__main__':
    main()