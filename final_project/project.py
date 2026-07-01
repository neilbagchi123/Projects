import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter rock, paper, or scissors (or quit to exit): ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)


def get_computer_choice():
    """Randomly return 'rock', 'paper', or 'scissors'."""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player, computer):
    """Return the result of the game as a string."""
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"


def is_valid_choice(choice):
    """Return True if the choice is valid, False otherwise."""
    return choice in ["rock", "paper", "scissors"]


if __name__ == "__main__":
    main()