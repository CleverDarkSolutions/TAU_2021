import pytest
from game import GameBoard

@pytest.fixture
def game_board():
    board = GameBoard(7, 7)
    board.generate_board()
    return board

def test_board_size(game_board):
    assert game_board.width == 7
    assert game_board.height == 7

def test_start_stop_positions(game_board):
    assert game_board.start_position is not None
    assert game_board.stop_position is not None
    assert game_board.start_position != game_board.stop_position

def test_obstacle_generation(game_board):
    assert game_board.obstacles is not None

def test_path_finding(game_board):
    path = game_board.find_path()
    assert path is not None
    assert game_board.start_position in path
    assert game_board.stop_position in path
    assert all(point not in game_board.obstacles for point in path)

@pytest.mark.parametrize("width, height", [(5, 5), (10, 10), (20, 20)])
def test_board_size_parametrized(width, height):
    board = GameBoard(width, height)
    board.generate_board()
    assert board.width == width
    assert board.height == height

@pytest.mark.skip(reason="This test is currently failing.")
def test_buggy_test():
    assert 2 + 2 == 5

@pytest.mark.skipif(not hasattr(GameBoard, "find_path"), reason="The find_path() method is not implemented.")
def test_path_finding_skipif(game_board):
    path = game_board.find_path()
    assert path is not None

@pytest.mark.xfail(reason="The path may not exist.")
def test_path_finding_xfail(game_board):
    path = game_board.find_path()
    assert path is not None
    assert game_board.start_position in path
    assert game_board.stop_position in path

@pytest.mark.usefixtures("game_board")
class TestGameBoard:
    def test_board_size(self, game_board):
        assert game_board.width == 7
        assert game_board.height == 7

    def test_start_stop_positions(self, game_board):
        assert game_board.start_position is not None
        assert game_board.stop_position is not None
        assert game_board.start_position != game_board.stop_position

    def test_obstacle_generation(self, game_board):
        assert game_board.obstacles is not None

    def test_path_finding(self, game_board):
        path = game_board.find_path()
        assert path is not None
        assert game_board.start_position in path
        assert game_board.stop_position in path
        assert all(point not in game_board.obstacles for point in path)
