import unittest
from Score_calculator import calculate_score

class ScoreCalculatorTest(unittest.TestCase):
    """Tests pour le calcul du score de bowling."""

    # --- Cas limites ---

    def test_gutter_game(self):
        """Test pour une partie à 0 (tous dans la gouttière)."""
        rolls = [0] * 20
        self.assertEqual(calculate_score(rolls), 0)

    def test_all_ones(self):
        """Test pour une partie où chaque lancer fait tomber 1 quille."""
        rolls = [1] * 20
        self.assertEqual(calculate_score(rolls), 20)

    # --- Strikes ---

    def test_all_strikes(self):
        """Test pour une partie parfaite (12 strikes)."""
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(calculate_score(rolls), 300)

    def test_single_strike(self):
        """Test avec un seul strike suivi de lancers normaux."""
        rolls = [10, 3, 4] + [0] * 16
        self.assertEqual(calculate_score(rolls), 24)  # 10+3+4 + 3+4 + 0*8frames

    def test_strike_in_last_frame(self):
        """Test avec un strike au 10ème frame."""
        rolls = [0] * 18 + [10, 3, 4]
        self.assertEqual(calculate_score(rolls), 17)

    # --- Spares ---

    def test_all_spares(self):
        """Test pour une partie avec que des spares."""
        rolls = [5, 5] * 10 + [5]
        self.assertEqual(calculate_score(rolls), 150)

    def test_single_spare(self):
        """Test avec un seul spare suivi de lancers normaux."""
        rolls = [6, 4, 3, 0] + [0] * 16
        self.assertEqual(calculate_score(rolls), 16)  # (6+4+3) + (3+0) + 0*8frames

    def test_spare_in_last_frame(self):
        """Test avec un spare au 10ème frame."""
        rolls = [0] * 18 + [7, 3, 5]
        self.assertEqual(calculate_score(rolls), 15)

    # --- Parties mixtes ---

    def test_mixed_game(self):
        """Test pour une partie mixte avec strikes, spares et open frames."""
        rolls = [10, 9, 1, 5, 5, 7, 2, 10, 10, 10, 9, 0, 8, 2, 9, 1, 10]
        self.assertEqual(calculate_score(rolls), 187)

    def test_alternating_strikes_and_gutters(self):
        """Test avec des strikes alternés et des gouttières."""
        rolls = [10, 0, 0] * 5  # 5 frames strike + 5 frames 0,0
        self.assertEqual(calculate_score(rolls), 50)  # Chaque strike: 10+0+0 = 10

    # --- Validation des entrées (robustesse) ---

    def test_empty_rolls(self):
        """Test avec une liste vide."""
        self.assertEqual(calculate_score([]), 0)

    def test_incomplete_game(self):
        """Test avec une partie incomplète."""
        rolls = [3, 4]
        self.assertEqual(calculate_score(rolls), 7)

    # --- Consecutive strikes ---

    def test_two_consecutive_strikes(self):
        """Test avec deux strikes consécutifs."""
        rolls = [10, 10, 3, 4] + [0] * 14
        # Frame 1: 10+10+3 = 23, Frame 2: 10+3+4 = 17, Frame 3: 7
        self.assertEqual(calculate_score(rolls), 47)

    def test_three_consecutive_strikes(self):
        """Test avec trois strikes consécutifs (turkey)."""
        rolls = [10, 10, 10, 0, 0] + [0] * 12
        # Frame 1: 30, Frame 2: 20, Frame 3: 10, rest: 0
        self.assertEqual(calculate_score(rolls), 60)


if __name__ == '__main__':
    unittest.main()