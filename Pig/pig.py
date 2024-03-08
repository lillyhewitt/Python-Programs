#Lilly Hewitt
import random

#One Automated Turn
def oneRound():
  score = 0
  while score < 20:
    num = random.randint(1,6)
    print("Roll:\t" , num)
    if num == 1:
      score = 0
    else:
      score += num
  print("Turn total:\t" , score)
  return score
  
oneRound()

#Hold-at-20 Outcomes
def round():
  score = 0
  while score < 20:
    num = random.randint(1,6)
    if num == 1:
      return 0
    else:
      score += num
  return score

def hold20():
  turns = int(input("How many Hold-at-20 turn simulations?\n"))
  print("Score\tEstimated Probability")
  outcomes = {}
  result = 0
  for i in range(turns):
    result = round()
    if result not in outcomes:
      outcomes[result] = 1
    else:
      outcomes[result] += 1
    result = 0
  for result in sorted(outcomes.keys()):
    print(result, "\t" , (outcomes[result]/turns))
    
hold20()

#Hold-at-X Outcomes
def specialRound(key):
  score = 0
  while score < key:
    num = random.randint(1,6)
    if num == 1:
      return 0
    else:
      score += num
  return score

def holdX():
  turns = int(input("How many Hold-at-20 turn simulations?\n"))
  key = int(input("Enter a holding value:\n"))
  print("Score\tEstimated Probability")
  outcomes = {}
  result = 0
  for i in range(turns):
    result = specialRound(key)
    if result not in outcomes:
      outcomes[result] = 1
    else:
      outcomes[result] += 1
    result = 0
  for result in sorted(outcomes.keys()):
    print(result, "\t" , (outcomes[result]/turns))

holdX()

#Hold-at-20-or-Goal Turn
def round20():
  score = 0
  while score < 20:
    num = random.randint(1,6)
    print("Roll:\t" , num)
    if num == 1:
      print("Turn Total:\t", 0)
      score = 0
      return 0
    else:
      score += num
  print("Turn total:\t" , score)
  return score

def hold():
  value = int(input("Score:\t"))
  while value < 100:
    value += round20()
    print("New Score:\t" , value)
    
hold()

#Hold-at-20-or-Goal Game
def holdGame():
  value = 0
  while value < 100:
    value += round20()
    print("New Score:\t" , value)

holdGame()

#Average Pig Turns
def avgTurns():
  games = int(input("How many games:\t"))
  score = 0
  total = 0
  turns = 0
  for i in range(games):
    score = 0
    while (score < 20 or score == -1) and total < 100:
      turns += 1
      num = random.randint(1,6)
      if num == 1:
        score = -1
      else:
        score += num
      total += score
  print("Average turns:\t" , (turns/games))

avgTurns()

#Two-Player Pig
def twoPlayer():
  p1 = 0
  p2 = 0
  rounds = 1
  while p1 < 100 and p2 < 100:
    print("Player 1 score:\t" , p1)
    print("Player 2 score:\t" , p2)
    print("It is player 1's turn.")
    p1 += round20()
    print("New Score:\t" , p1)
    print("\nPlayer 1 score:\t" , p1)
    print("Player 2 score:\t" , p2)
    print("It is player 2's turn.")
    p2 += round20()
    print("New Score:\t" , p2)
    rounds += 1
    print()

twoPlayer()

#Pig Game
def playerRound():
  turn = ""
  turnTotal = 0
  score = 0
  while turn == "":
    num = random.randint(1,6)
    print("Roll:\t" , num)
    if num == 1:
      turnTotal = 0
      turn = "lk"
      print("Turn Total:\t" , turnTotal)
      return 0
    else:
      turnTotal = num
      score += num
      print("Turn Total:\t" , turnTotal , end = "")
      turn = input("\tRoll/Hold? (Enter)")
  return score

def pigGame():
  p1 = 0
  p2 = 0
  value = 0
  computer = random.randint(1,2)
  player = 0
  if computer == 1:
    computer = p1
    player = p2
    value = 1
    print("You will be player 2.\nEnter nothing to roll; enter anything to
    hold.")
  else:
    computer = p2
    player = p1
    print("You will be player 1.\nEnter nothing to roll; enter anything to
    hold.")
  while p1 < 100 and p2 < 100:
    turn = ""
    print("Player 1 score:\t" , p1)
    print("Player 2 score:\t" , p2)
    print("It is player 1's turn.")
    if value == 1:
      p1 += round20()
      print("New Score:\t" , p1)
      print("\nPlayer 1 score:\t" , p1)
      print("Player 2 score:\t" , p2)
      print("It is player 2's turn.")
      p2 += playerRound()
      print("New Score:\t" , p2)
      print()
    else:
      p1 += playerRound()
      print("New Score:\t" , p1)
      print("\nPlayer 1 score:\t" , p1)
      print("Player 2 score:\t" , p2)
      print("It is player 2's turn.")
      p2 += round20()
      print("New Score:\t" , p2)
      print()
  print("Thank you for playing pig!")
  
pigGame()
