In this assignment, we will be implementing a dice game called pig. The
game will have two modes, a two-player mode and a single player mode
that plays against the computer. We will be applying the data analysis help
create a good, but simple, strategy for the computer to use.
We will also be doing a number of smaller exercises to build up to the
final implementation.
Todd Neller came up with this assignment and has done a crazy amount
of anaylsis, so I’ll use his words to explain the rules below, as well as much
of the sample outputs.

The Rules of Pig
Pig is a folk jeopardy dice game with simple rules: Two players race to
reach 100 points. Each turn, a player repeatedly rolls a die until either a 1
(”pig”) is rolled or the player holds and scores the sum of the rolls (i.e. the
turn total). At any time during a player’s turn, the player is faced with two
decisions:
roll If the player rolls a
1: the player scores nothing and it becomes the opponent’s turn.
2 - 6: the number is added to the player’s turn total and the player’s
turn continues.
hold The turn total is added to the player’s score and it becomes the op-
ponent’s turn.

1 One Automated Turn of Pig
Our first exercise is to simulate a single turn of Pig where a player rolls until
a 1 (“pig”) is rolled, or the turn total is greater than or equal to 20. We will
call this strategy Hold-at-20. The user doesn’t need to make any choices,
the computer will roll automagically, following the hold-at-20 strategy.
• For each roll, print a line with “Roll:” and the random die roll value
(1-6).
• After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a “pig,” this turn total is 0.
1.1 Sample Outputs
The different runs of the program are separated by dots.
Roll: 4
Roll: 5
Roll: 6
Roll: 5
Turn total: 20
...
Roll: 3
Roll: 1
Turn total: 0
...
Roll: 5
Roll: 2
Roll: 3
Roll: 6
Roll: 5
Turn total: 21

2 Hold-at-20 Outcomes
Simulate a given number of hold-at-20 turns, and report the estimated prob-
abilities of the possible scoring outcomes.
Input
Enter a single positive integer indicating the number of turns simulated.
(Larger numbers will tend to yield better estimations.)
Output
• Initially, prompt the user with “Hold-at-20 turn simulations?”
• On the next line, print “Score” and “Estimated Probability” separated
by a tab.
• After the simulations, print a table line for each score outcome that
occurred in increasing order of score. For each score outcome, print
the score, a tab, and the fraction of turn simulations that yielded that
score.

2.1 Sample Outputs
How many Hold-at-20 turn simulations?
1000000
Score Estimated Probability
0 0.624076
20 0.099659
21 0.095310
22 0.074086
23 0.054599
24 0.035313
25 0.016957

3 Hold-at-X Outcomes
As the previous exercise, but allow the user to specify the hold value. What
is the probability of reaching 100 in a single turn if you allow the cpu to
hold at 100?

4 Hold-at-20-or-Goal Turn
Given a player’s score, simulate a single turn of Pig where a player rolls until
a 1 (“pig”) is rolled, or the turn total is greater than or equal to 20, or the
score plus the turn total is greater than or equal to 100.
Input
The input is a single integer representing a Pig player score.
Output
• Initially, prompt the user with “Score?”
• For each roll, print a line with “Roll:” and the random die roll value
(1-6).
• After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a ”pig”, this turn total is 0.
Then print a line with “New score:” followed by the new score.

4.1 Sample Outputs
Score? 90
Roll: 2
Roll: 3
Roll: 4
Roll: 4
Turn total: 13
New score: 103

5 Hold-at-20-or-Goal Game
Simulate a single solitaire (one-player) game of Pig where a player rolls until
a 1 (“pig”) is rolled, or the turn total is greater than or equal to 20, or the
score plus the turn total is greater than or equal to 100.
Output
• For each roll, print a line with “Roll:” and the random die roll value
(1-6).
• After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a “pig,” this turn total is 0.
Then, print a line with “New score:” followed by the new score.

5.1 Sample Outputs
Roll: 4
Roll: 6
Roll: 1
Turn total: 0
New score: 0
Roll: 6
Roll: 5
Roll: 5
Roll: 6
Turn total: 22
New score: 22
Roll: 6
Roll: 2
Roll: 2
Roll: 3
Roll: 3
Roll: 2
Roll: 5
Turn total: 23
New score: 45
Roll: 3
Roll: 4
Roll: 6
Roll: 2
Roll: 6
Turn total: 21
New score: 66
Roll: 3
Roll: 3
Roll: 4
Roll: 4
Roll: 6
Turn total: 20
New score: 86
Roll: 3
Roll: 5
Roll: 5
Roll: 6
Turn total: 19
New score: 105

6 Average Pig Turns
What is the expected number of turns per solitaire game with a hold-at-20-
or-goal play policy? Simulate a given number of solitaire Pig games where
a player rolls until a 1 (“pig”) is rolled, or the turn total is greater than or
equal to 20, or the score plus the turn total is greater than or equal to 100.
Report the average number of turns per game.
Input
Enter a single positive integer indicating the number of games simulated.
(Larger numbers will tend to yield better estimations.)
Output
• Initially, prompt the user with “Games?”
• After the simulations, print “Average turns:” followed by the average
turns taken per simulated game.
6.1 Sample Transcript
Games? 1000000
Average turns: 12.634906

7 Two-Player Pig
Simulate a single solitaire game of Pig where a player rolls until a 1 (“pig”)
is rolled, or the turn total is greater than or equal to 20, or the score plus
the turn total is greater than or equal to 100.
Output
• Before each turn, print a line with “Player 1 score:” and player 1’s
score. Print another line with “Player 2 score:” and player 2’s score.
Finally, print a line with “It is player #’s turn.”, where “#” is replaced
by the current player number. Play starts with player 1 and then
alternates.
• For each roll, print a line with “Roll:” and the random die roll value
(1-6).
• After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a “pig,” this turn total is 0.
Then, print a line with “New score:” followed by the new score for the
current player.

7.1 Sample Transcript
Player 1 score: 0
Player 2 score: 0
It is player 1’s turn.
Roll: 5
Roll: 6
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 0
It is player 2’s turn.
Roll: 2
Roll: 5
Roll: 4
Roll: 5
Roll: 4
Turn total: 20
New score: 20
Player 1 score: 0
Player 2 score: 20
...
Player 1 score: 90
Player 2 score: 66
It is player 1’s turn.
Roll: 2
Roll: 2
Roll: 6
Turn total: 10
New score: 100

8 Pig Game
Implement a game of Pig where the user plays against a “hold at 20 or
goal” computer player that rolls until a 1 (“pig”) is rolled, or the turn total
is greater than or equal to 20, or the score plus the turn total is greater than
or equal to 100. The first player is chosen randomly.
Input
An empty input (i.e., Enter) indicates that the user wishes to roll. Any
entered line of non-zero length indicates that the user wishes to hold.
Output
• Before the game, randomly select which player the user will be, and
print the line “You will be player #.”, where # is the user’s player
number. Then, print an instruction line “Enter nothing to roll; enter
anything to hold.”
• Before each turn, print a line with “Player 1 score:” and player 1’s
score. Print another line with “Player 2 score:” and player 2’s score.
Finally, print a line with “It is player #’s turn.”, where “#” is replaced
by the current player number. Play starts with player 1 and then
alternates.
• For each roll, print a line with “Roll:” and the random die roll value
(1-6). For each non-“pig” roll 2-6 on the user’s turn, prompt the user
with “Turn total:”, the turn total, a tab, and “Roll/Hold?”.
• After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a “pig,” this turn total is 0.
Then, print a line with “New score:” followed by the new score for the
current player.

8.1 Sample Transcript
You will be player 2.
Enter nothing to roll; enter anything to hold.
Player 1 score: 0
Player 2 score: 0
It is player 1’s turn.
Roll: 5
Roll: 3
Roll: 5
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 0
It is player 2’s turn.
Roll: 6
Turn total: 6 Roll/Hold? (Enter)
Roll: 5
Turn total: 11 Roll/Hold? (Enter)
Roll: 6
Turn total: 17 Roll/Hold? (Enter)
Roll: 2
Turn total: 19 Roll/Hold? (Enter)
Roll: 2
Turn total: 21 Roll/Hold? h
Turn total: 21
New score: 21
Player 1 score: 0
Player 2 score: 21
It is player 1’s turn.
Roll: 5
Roll: 6
Roll: 3
Roll: 5
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 21
It is player 2’s turn.
Roll: 6
Turn total: 6 Roll/Hold? (Enter)
Roll: 6
Turn total: 12 Roll/Hold? (Enter)
Roll: 2
Turn total: 14 Roll/Hold? (Enter)
Roll: 6
Turn total: 20 Roll/Hold? h
Turn total: 20
New score: 41
Player 1 score: 0
Player 2 score: 41
It is player 1’s turn.
Roll: 3
Roll: 3
Roll: 6
Roll: 4
Roll: 4
Turn total: 20
New score: 20
Player 1 score: 20
Player 2 score: 41
It is player 2’s turn.
Roll: 3
Turn total: 3 Roll/Hold? (Enter)
Roll: 3
Turn total: 6 Roll/Hold? (Enter)
Roll: 2
Turn total: 8 Roll/Hold? (Enter)
Roll: 2
Turn total: 10 Roll/Hold? (Enter)
Roll: 4
Turn total: 14 Roll/Hold? (Enter)
Roll: 2
Turn total: 16 Roll/Hold? (Enter)
Roll: 4
Turn total: 20 Roll/Hold? h
Turn total: 20
New score: 61
Player 1 score: 20
Player 2 score: 61
It is player 1’s turn.
Roll: 5
Roll: 1
Turn total: 0
New score: 20
Player 1 score: 20
Player 2 score: 61
It is player 2’s turn.
Roll: 3
Turn total: 3 Roll/Hold? (Enter)
Roll: 3
Turn total: 6 Roll/Hold? (Enter)
Roll: 5
Turn total: 11 Roll/Hold? (Enter)
Roll: 2
Turn total: 13 Roll/Hold? (Enter)
Roll: 6
Turn total: 19 Roll/Hold? h
Turn total: 19
New score: 80
Player 1 score: 20
Player 2 score: 80
It is player 1’s turn.
Roll: 3
Roll: 1
Turn total: 0
New score: 20
Player 1 score: 20
Player 2 score: 80
It is player 2’s turn.
Roll: 2
Turn total: 2 Roll/Hold? (Enter)
Roll: 2
Turn total: 4 Roll/Hold? (Enter)
Roll: 4
Turn total: 8 Roll/Hold? (Enter)
Roll: 2
Turn total: 10 Roll/Hold? (Enter)
Roll: 3
Turn total: 13 Roll/Hold? (Enter)
Roll: 6
Turn total: 19 Roll/Hold? (Enter)
Roll: 5
Turn total: 24 Roll/Hold? h
Turn total: 24
New score: 104
