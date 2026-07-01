from project import get_computer_choice, determine_winner, is_valid_choice

def test_get_computer_choice():
    # Make sure the computer always chooses one of the valid options
    for _ in range(100):
        assert get_computer_choice() in ["rock", "paper", "scissors"]

def test_determine_winner():
    assert determine_winner("rock", "scissors") == "You win!"
    assert determine_winner("rock", "paper") == "You lose!"
    assert determine_winner("paper", "rock") == "You win!"
    assert determine_winner("paper", "scissors") == "You lose!"
    assert determine_winner("scissors", "paper") == "You win!"
    assert determine_winner("scissors", "rock") == "You lose!"
    assert determine_winner("rock", "rock") == "It's a tie!"

def test_is_valid_choice():
    assert is_valid_choice("rock")
    assert is_valid_choice("paper")
    assert is_valid_choice("scissors")
    assert not is_valid_choice("lizard")
    assert not is_valid_choice("")