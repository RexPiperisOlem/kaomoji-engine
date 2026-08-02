import random
import unittest

import kaomoji_engine as engine


class LastChoiceRandom:
    """Select the cycle-specific mutation at the end of a mutation pool."""

    @staticmethod
    def choice(values):
        return values[-1]

    @staticmethod
    def random():
        return 1.0


class KaomojiEngineTests(unittest.TestCase):
    def test_generate_seed_uses_known_seed(self):
        seed = engine.generate_seed(random.Random(3))
        self.assertIn(seed, engine.SEEDS)

    def test_invalid_cycle_is_rejected(self):
        with self.assertRaises(ValueError):
            engine.distort("{o_o}", "sideways")

    def test_each_cycle_remains_bounded(self):
        for cycle in engine.CYCLES:
            with self.subTest(cycle=cycle):
                value = "{o_o}"
                rng = random.Random(17)
                for _ in range(500):
                    value = engine.distort(value, cycle, rng=rng, max_width=40)
                    self.assertLessEqual(len(value), 40)

    def test_echo_growth_is_compressed(self):
        value = "a" * 40
        result = engine.distort(
            value,
            "echo",
            rng=LastChoiceRandom(),
            max_width=50,
        )
        self.assertEqual(len(result), 50)
        self.assertIn("...", result)

    def test_finite_heartbeat_emits_requested_frames(self):
        output = []
        final_state = engine.heartbeat(
            "{o_o}",
            "ripple",
            delay=0,
            frames=4,
            rng=random.Random(9),
            output_fn=output.append,
        )

        self.assertEqual(len(output), 4)
        self.assertTrue(output[0].startswith("Frame 1 [ripple]:"))
        self.assertTrue(output[-1].startswith("Frame 4 [ripple]:"))
        self.assertIsInstance(final_state, str)

    def test_bound_output_preserves_requested_width(self):
        result = engine.bound_output("abcdefghijklmnopqrstuvwxyz", max_width=11)
        self.assertEqual(result, "abcd...wxyz")
        self.assertEqual(len(result), 11)


if __name__ == "__main__":
    unittest.main()
