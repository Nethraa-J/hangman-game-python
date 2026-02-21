import random
def play_hangman():
    word_list=["python","apple","tiger","chair","ocean"]
    seceret_word=random.choice(word_list)
    gussed_letters=[]
    incorrect_gusses=0
    max_attempts=6
    display=["_"]*len(seceret_word)

    print("Welcome to Hangman!")
    print("All the best!!")
    print("Guess the word letter by letter.\n")

    while incorrect_gusses < max_attempts and "_" in display:
        print("\nWord: ","".join(display))
        print("Gussed letters:","".join(sorted(gussed_letters)))
        print("attempts left:",max_attempts-incorrect_gusses)
        guess=input("Enter a letter: ").lower().strip()
        if len(guess)!=1:
            print("Enter only ONE letter")
            continue
        if not guess.isalpha():
            print("only alphabets allowed")
            continue
        if guess in gussed_letters:
            print("You already gussed that letter")
            continue
        gussed_letters.append(guess)
        if guess in seceret_word:
            print("Correct guess!")
            for i in range(len(seceret_word)):
                if seceret_word[i]==guess:
                    display[i]=guess
        else:
            print("Wrong guess!")
            incorrect_gusses+=1
                

    print("\n"+"="*40)
    if "_" not in display:
        print("CONGRATULATIONS!!!YOU WON!!!")
        print("The word was:",seceret_word)
        print("You guessed it in ",len(gussed_letters),",attemps.")
    else:
        print("GAME OVER!")
        print("The correct word was:",seceret_word)
        print("Better luck next time!")
        print("\n"+"="*40)
while True:
    play_hangman()
    play_again=input("Play again ?(yes/no)").lower()

    if play_again!="yes":
        print("thanks for playing!")
play_hangman()