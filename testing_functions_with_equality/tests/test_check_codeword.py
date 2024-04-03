from lib.check_codeword import *

def test_check_codeword_exact_guess_like_horse():
    exact_guess = check_codeword("horse")
    assert exact_guess == "Correct! Come in."

def test_check_codeword_close_guess():
    exact_guess = check_codeword("horse")
    close_guess = check_codeword("hmmm this maybe")
    assert close_guess == "Close, but nope."

def test_check_codeword_wrong_guesses():
    wrong_guess_begin = check_codeword("horsey")
    wrong_guess_end = check_codeword("apple")
    assert wrong_guess_begin == "WRONG!"
    assert wrong_guess_end == "WRONG!"
    