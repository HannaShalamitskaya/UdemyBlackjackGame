"""Game test suit."""

from source.game import Game


def test_game():
    game = Game('player_1', 'player_2')

    assert game.player_1 == 'player_1'
    assert game.player_2 == 'player_2'
