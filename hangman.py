# This game has been created just for practice and fun.
# If you have a copyright, please contact me, and I'll make this repository private

import random

# List of words to choose from
words = ["abuse","actor","admit","adore","adult","agent","agree","alarm","album","alien","alive","allow","alone","amaze","angel","anger","apple","apply","arena","argue","arise","armor","arrow","asset","attack","audio","avoid","awake","award","awful","bacon","badge","bagel","baker","ballet","banana","bandit","banner","barge","basin","batch","beach","beard","beast","beech","begin","beige","belay","bench","berry","betty","bible","biker","bingo","birch","birth","bison","black","blade","blank","blast","blend","bless","blimp","blink","bliss","block","blond","blown","blues","blunt","bonus","boost","booth","bosom","bound","bowel","boxer","brace","brake","brand","brave","bread","break","breed","brick","bride","brief","bring","brisk","broad","broil","broom","brown","brush","buddy","buggy","build","bulge","bulky","bunch","burly""abuse","actor","admit","adore","adult","agent","agree","alarm","album","alien","alive","allow","alone","amaze","angel","anger","apple","apply","arena","argue","arise","armor","arrow","asset","attack","audio","avoid","awake","award","awful","bacon","badge","bagel","baker","ballet","banana","bandit","banner","barge","basin","batch","beach","beard","beast","beech","begin","beige","belay","bench","berry","betty","bible","biker","bingo","birch","birth","bison","black","blade","blank","blast","blend","bless","blimp","blink","bliss","block","blond","blown","blues","blunt","bonus","boost","booth","bosom","bound","bowel","boxer","brace","brake","brand","brave","bread","break","breed","brick","bride","brief","bring","brisk","broad","broil","broom","brown","brush","buddy","buggy","build","bulge","bulky","bunch","burly","burnt","burst","bushy","butter","button","buyer","cabin","cable","cactus","calmly","camera","campus","cancer","candle","cannon","canoe","canvas","canyon","capable","capital","capture","carbon","cardio","careful","carpet","carrot","cartel","casino","castle","casual","cattle","caucus","cavern","cease","celery","cement","center","chance","change","charge","charm","cheap","cheer","cheese","cherry","chess","chest","chick","chief","child","chill","chime","choice","chord","chorus","chosen","chrome","church","cigar","cinema","circle","circus","citrus","cityscape","civil","clammy","clash","classic","clawed","clean","clear","clergy","cliff","climax","clinic","cloned","closer","closet","cloud","clover","cluster","clutch","coarse","coast","cobalt","cocoa","coerce","coffee","cohort","collar","collect","colon","color","combat","combine","comedy","comfort","command","comment","commit","common","compel","comply","concur","condor","confirm","conflict","confuse","conjure","connect","consul","consume","contact","contain","content","contest","context","control","convert","cooling","copper","coral","corner","corona","correct","costly","cotton","cougar","council","counsel","counter","country","courage","courier","cousin","cowboy","coyote","cradle","craft","crammed","cranky","crater","crayon","crazy","cream","credit","creek","creepy","crewed","cringe","crispy","critic","crochet","crouch","crowd","crown","crunch","crust","crutch","cruxes","crying","crystal","cubism","cuddle","culled","cultivator","cupcake","curled","cursor","curtly","cushion","custard","cutely","cutlass","cutout","cycling","cyclone","cynical"]

# Function to choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Function to initialize the game state
def init_game(word):
    # Create a list of underscores with the same length as the word
    return ["_" for letter in word]

# Function to update the game state based on the user's guess
def update_game(word, game_state, guess, num_guesses):
    # Check if the guess is in the word
    if guess in word:
        # Update the game state with the guess
        for i in range(len(word)):
            if word[i] == guess:
                game_state[i] = guess
    else:
        # Decrement the number of guesses
        num_guesses -= 1
    return game_state, num_guesses

# Function to check if the game is over
def is_game_over(word, game_state, num_guesses):
    # Check if the game state matches the word
    if "".join(game_state) == word:
        print("Congratulations, you won!")
        return True
    # Check if the user has run out of guesses
    elif num_guesses == 0:
        print("Sorry, you lost. The word was", word)
        return True
    return False

# Function to print the stickman figure
def print_figure(num_guesses):
    if num_guesses == 6:
        print("  _______")
        print(" |       |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif num_guesses == 5:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif num_guesses == 4:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|_")
    elif num_guesses == 3:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|")
        print(" |")
        print(" |")
        print("_|_")
    elif num_guesses == 2:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |")
        print(" |")
        print("_|_")
    elif num_guesses == 1:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      /")
        print(" |")
        print("_|_")
    else:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      / \\")
        print(" |")
        print("_|_")

# Main game loop
def play_game():
    # Choose a random word
    word = choose_word(words)
    # Initialize the game state
    game_state = init_game(word)
    # Set the number of guesses
    num_guesses = 6
    # Loop until the game is over
    while not is_game_over(word, game_state, num_guesses):
        # Print the current game state
        print(" ".join(game_state))
        # Print the stickman figure
        print_figure(num_guesses)
        # Get the user's guess
        guess = input("Guess a letter: ")
        # Update the game state based on the guess
        game_state, num_guesses = update_game(word, game_state, guess, num_guesses)
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        play_game()

# Start the game
play_game()
