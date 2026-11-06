import unittest
from app import analyze

class PromptArchitectTests(unittest.TestCase):
    def test_short_prompt_needs_improvement(self):
        result = analyze("Hazme una estrategia")
        self.assertLess(result.score, 60)
        self.assertIn("rol", result.missing)

    def test_complete_prompt_scores_higher(self):
        result = analyze(
            "Actúa como especialista. Analiza esta campaña para una marca "
            "de cosmética. Máximo 200 palabras y responde con bullets."
        )
        self.assertGreaterEqual(result.score, 70)
        self.assertEqual(result.missing, [])

if __name__ == "__main__":
    unittest.main()
