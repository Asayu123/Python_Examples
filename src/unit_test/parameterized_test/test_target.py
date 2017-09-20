# Test Target for Python Subtest Examples.


def rock_paper_scissors(p1_shape, p2_shape):
    """ Evaluate both player's hand shape and return winner.
    :param p1_shape: Player 1's hand shape, must be either of "Rock", "Paper", "Scissor".
    :type p1_shape: str
    :param p2_shape: Player 2's hand shape, must be either of "Rock", "Paper", "Scissor".
    :type p2_shape: str
    :return: winner
    Either of "Player1" or "Player2" "Even" will be returned.
    :rtype : str
    :raises ValueError when invalid hand shape has given.
    """

    # Define valid shape constants.
    _valid_shapes = ["Rock", "Paper", "Scissor"]

    # Define result constants.
    _EVEN = "Even"
    _PLAYER_1 = "Player1"
    _PLAYER_2 = "Player2"

    # Initialize judgement table.
    _win_loss_judgement_table = {
        ("Rock", "Rock"): _EVEN,
        ("Rock", "Paper"): _PLAYER_2,
        ("Rock", "Scissor"): _PLAYER_2,  # Bug! Correct result is _PLAYER1
        ("Paper", "Rock"): _PLAYER_1,
        ("Paper", "Paper"): _EVEN,
        ("Paper", "Scissor"): _PLAYER_1,  # Bug! Correct result is _PLAYER2
        ("Scissor", "Rock"): _PLAYER_2,
        ("Scissor", "Paper"): _PLAYER_1,
        ("Scissor", "Scissor"): _EVEN,
    }

    # Main logic starts from here.
    # Validation
    if p1_shape not in _valid_shapes or p2_shape not in _valid_shapes:
        raise ValueError("Shape must be either of {0}".format(_valid_shapes))

    # Judgement
    winner = _win_loss_judgement_table[(p1_shape, p2_shape)]
    return winner


if __name__ == "__main__":
    # Execute only if run as a script
    p1_shape = input("Please Enter Player1's hand shape\n")
    p2_shape = input("Please Enter Player2's hand shape\n")
    result = rock_paper_scissors(p1_shape=p1_shape, p2_shape=p2_shape)
    print("Result : {0}".format(result))
