import unittest
from statistics import Statistics
from player import Player
from enum import Enum

#jos tehtövönannossa annettua koodia ei saa käyttää, sori, sen olisi voinut kirjottaa materiaaaliin

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub)
        
    def test_search_works_correct_name(self):
        result = self.statistics.search("Kurri")

        self.assertEqual(str(result), "Kurri EDM 37 + 53 = 90")
    
    def test_search_works_incorrect_name(self):
        result = self.statistics.search("Kuri")

        self.assertIsNone(result)
    
    def test_team_function(self):
        result = self.statistics.team("EDM")

        self.assertEqual(len(result), 3)
    
    def test_team_function_incorrect_team(self):
        result = self.statistics.team("AAA")

        self.assertEqual(len(result), 0)
    
    def test_top_point_getters(self):
        result = self.statistics.top(3)

        self.assertEqual(str(result[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(result[1]), "Lemieux PIT 45 + 54 = 99")
        
    def test_top_points_second_parameter_optional(self):
        result = self.statistics.top(3, SortBy.POINTS)
        result2 = self.statistics.top(3)

        self.assertEqual(str(result[0]), str(result2[0]))
    
    def test_top_goals(self):
        result = self.statistics.top(3, SortBy.GOALS)

        self.assertEqual(str(result[0]), "Lemieux PIT 45 + 54 = 99")

    def test_top_assists(self):
        result = self.statistics.top(3, SortBy.ASSISTS)

        self.assertEqual(str(result[0]), "Gretzky EDM 35 + 89 = 124")