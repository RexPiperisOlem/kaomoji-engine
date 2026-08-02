"""Kaomoji Emotional Confusion Engine.

A small terminal artifact that repeatedly mutates a kaomoji. It models no
human emotion and assigns no meaning to its output.
"""

import argparse
import random
import time


CYCLES = ("ripple", "spiral", "break", "echo")
SEEDS = ("{o_o}", "{._.}", "{^_^}")
DEFAULT_DELAY = 0.4
DEFAULT_MAX_WIDTH = 120


def generate_seed(rng=None):
    """Return one starting face."""
    rng = rng or random
    return rng.choice(SEEDS)


def bound_output(text, max_width=DEFAULT_MAX_WIDTH):
    """Keep a mutation bounded while preserving both visible ends."""
    if max_width < 5:
        raise ValueError("max_width must be at least 5")
    if len(text) <= max_width:
        return text

    marker = "..."
    remaining = max_width - len(marker)
    left_width = (remaining + 1) // 2
    right_width = remaining // 2
    return text[:left_width] + marker + text[-right_width:]


def distort(kaomoji, cycle, rng=None, max_width=DEFAULT_MAX_WIDTH):
    """Apply one randomly selected mutation from the requested cycle."""
    rng = rng or random
    cycle = cycle.lower()

    if cycle not in CYCLES:
        raise ValueError("cycle must be one of: " + ", ".join(CYCLES))

    base = [
        lambda value: value.replace("o", "O"),
        lambda value: value.replace(".", "o"),
        lambda value: value.replace("^", "o"),
        lambda value: value.replace("_", "."),
    ]

    pools = {
        "ripple": base
        + [
            lambda value: "~" + value,
            lambda value: value + "~",
        ],
        "spiral": base
        + [
            lambda value: value[::-1],
            lambda value: "(" + value + ")",
        ],
        "break": base
        + [
            lambda value: "".join(
                character if rng.random() > 0.3 else "x"
                for character in value
            )
        ],
        "echo": base
        + [
            lambda value: value + " " + value,
        ],
    }

    mutation = rng.choice(pools[cycle])
    return bound_output(mutation(kaomoji), max_width=max_width)


def choose_cycle(input_fn=input, output_fn=print):
    """Prompt until a valid cycle is selected; blank selects ripple."""
    prompt = "Choose cycle (ripple, spiral, break, echo) [ripple]: "

    while True:
        cycle = input_fn(prompt).strip().lower() or "ripple"
        if cycle in CYCLES:
            return cycle
        output_fn("Unknown cycle. Choose ripple, spiral, break, or echo.")


def heartbeat(
    seed,
    cycle,
    delay=DEFAULT_DELAY,
    frames=None,
    rng=None,
    output_fn=print,
    max_width=DEFAULT_MAX_WIDTH,
):
    """Run mutations until the requested frame count is reached.

    A frame count of ``None`` runs continuously until interrupted.
    The final kaomoji is returned so finite runs can be inspected or tested.
    """
    if delay < 0:
        raise ValueError("delay cannot be negative")
    if frames is not None and frames < 0:
        raise ValueError("frames cannot be negative")

    rng = rng or random
    kaomoji = seed
    frame = 1

    while frames is None or frame <= frames:
        kaomoji = distort(
            kaomoji,
            cycle,
            rng=rng,
            max_width=max_width,
        )
        output_fn(f"Frame {frame} [{cycle}]: {kaomoji}")
        frame += 1
        if delay:
            time.sleep(delay)

    return kaomoji


def build_parser():
    parser = argparse.ArgumentParser(
        description="Continuously mutate a kaomoji through one confusion cycle."
    )
    parser.add_argument(
        "--cycle",
        choices=CYCLES,
        help="skip the prompt and select a cycle directly",
    )
    parser.add_argument(
        "--frames",
        type=int,
        default=0,
        help="stop after this many frames; 0 runs until Ctrl+C",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help="seconds between frames (default: 0.4)",
    )
    parser.add_argument(
        "--random-seed",
        type=int,
        help="make a run repeatable for demonstrations or tests",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=DEFAULT_MAX_WIDTH,
        help="maximum output width before the middle is compressed",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.frames < 0:
        parser.error("--frames cannot be negative")
    if args.delay < 0:
        parser.error("--delay cannot be negative")
    if args.max_width < 5:
        parser.error("--max-width must be at least 5")

    rng = random.Random(args.random_seed)
    seed = generate_seed(rng)
    cycle = args.cycle or choose_cycle()
    frames = args.frames or None

    print("Kaomoji Emotional Confusion Engine")
    print()
    print("Frame Zero Baseline:", seed)
    print("Cycle selected:", cycle)
    print()
    print("Starting heartbeat. Press Ctrl+C to stop.")
    print()

    try:
        heartbeat(
            seed,
            cycle,
            delay=args.delay,
            frames=frames,
            rng=rng,
            max_width=args.max_width,
        )
    except KeyboardInterrupt:
        print("\nHeartbeat stopped.")


if __name__ == "__main__":
    main()
