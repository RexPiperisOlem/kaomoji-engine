# Kaomoji Emotional Confusion Engine

**A small, inspectable Python terminal artifact that repeatedly mutates a symbolic face through bounded rules.**

The engine begins with one kaomoji, applies one randomly selected mutation at a time, prints each result as a numbered frame, and continues until it reaches a requested frame count or the operator stops it.

It does **not** understand emotion. It does not classify the faces it produces, maintain a hidden emotional state, or decide what the symbols mean. The “confusion” comes from symbolic drift and from the observer’s instinct to interpret changing marks as expression.

## Why this exists

This repository demonstrates a narrow systems idea in working code:

- a finite rule set can produce an evolving sequence;
- the entire state can remain visible and inspectable;
- indefinite duration does not require unbounded state growth;
- deterministic options make an otherwise random artifact testable;
- a strange conceptual idea can be turned into a contained, documented, working prototype without pretending it is more sophisticated than it is.

The implementation is the claim. There is no trained model, hidden narrative engine, sentiment analysis, or artificial emotional intelligence behind the output.

## Requirements

- Python 3.10 or newer is recommended;
- only the Python standard library is used;
- no installation step or external package is required.

## Run it interactively

From the repository directory:

```bash
python kaomoji_engine.py
```

The program selects one of three seed faces, asks you to choose a mutation cycle, and then begins the heartbeat loop.

Available cycles:

- `ripple`
- `spiral`
- `break`
- `echo`

Press `Ctrl+C` to stop an unlimited run cleanly.

## Run a finite, repeatable demonstration

```bash
python kaomoji_engine.py --cycle echo --frames 12 --random-seed 7 --delay 0
```

This command:

- skips the interactive cycle prompt;
- prints exactly twelve mutated frames;
- uses a repeatable random sequence;
- removes the delay between frames.

Finite deterministic runs are useful for testing, screen capture, documentation, demonstrations, or comparing code changes.

## Command-line options

See the built-in help:

```bash
python kaomoji_engine.py --help
```

| Option | Purpose | Default |
| --- | --- | --- |
| `--cycle` | Select `ripple`, `spiral`, `break`, or `echo` without a prompt | interactive prompt |
| `--frames` | Stop after a fixed number of frames; `0` means continue until interrupted | `0` |
| `--delay` | Seconds between frames | `0.4` |
| `--random-seed` | Make seed selection and mutation choices repeatable | random |
| `--max-width` | Maximum state width before the middle is compressed | `120` |

Invalid negative frame counts or delays are rejected. The maximum width must be at least five characters.

## What the engine actually does

The current kaomoji string is the engine’s complete state.

For every frame, the heartbeat loop:

1. selects one mutation allowed by the active cycle;
2. applies it to the current string;
3. bounds the result to the configured maximum width;
4. prints the new string as the next numbered frame;
5. stores that visible result as the complete state for the next cycle.

The engine remembers no earlier frame beyond the current string. It does not maintain a separate label such as happy, distressed, calm, or confused.

## Seed faces

One of three baseline strings is selected at the start of a run:

```text
{o_o}
{._.}
{^_^}
```

A supplied random seed makes both the starting face and later mutation choices reproducible.

## Mutation cycles

Every cycle includes four base substitutions:

- lowercase `o` may become uppercase `O`;
- `.` may become `o`;
- `^` may become `o`;
- `_` may become `.`.

Each cycle adds a distinct transformation.

| Cycle | Additional operation | Typical visible effect |
| --- | --- | --- |
| `ripple` | Add `~` to the left or right edge | Accumulating edge noise |
| `spiral` | Reverse the string or wrap it in parentheses | Flipping and nesting |
| `break` | Give each character a 30% chance of becoming `x` | Uneven symbolic degradation |
| `echo` | Duplicate the current string with a space between copies | Repetition and rapid expansion |

A cycle does not force its special operation every time. The program chooses randomly from the base substitutions and the cycle-specific operations.

## Bounded endlessness

The program can run indefinitely, but the stored state cannot grow indefinitely.

This distinction matters most in `echo` and `spiral` modes. Repeated duplication or nesting would otherwise produce unreasonable output and memory use. When a state exceeds `--max-width`, the engine preserves both visible ends and replaces the middle with `...`.

The result is:

- unlimited duration by default;
- bounded state size;
- finite demonstrations when requested;
- repeatable runs when a random seed is supplied.

The system remains continuous without pretending a computer has infinite memory.

## Use it as a Python module

The functions can also be imported directly:

```python
import random

from kaomoji_engine import heartbeat

heartbeat(
    seed="{o_o}",
    cycle="ripple",
    frames=5,
    delay=0,
    rng=random.Random(7),
)
```

Useful public functions include:

- `generate_seed()` — choose one baseline face;
- `distort()` — apply one bounded mutation;
- `bound_output()` — limit state width while preserving both ends;
- `choose_cycle()` — run the interactive cycle prompt;
- `heartbeat()` — run the mutation loop and return the final state;
- `build_parser()` — construct the command-line argument parser.

## Tests

Run the test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests cover bounded output, deterministic behavior, valid mutation cycles, finite heartbeat runs, and invalid input handling. They use only the Python standard library.

## Repository map

| File | Purpose |
| --- | --- |
| `kaomoji_engine.py` | The working engine and command-line interface |
| `ENGINE.md` | Detailed implementation and design note |
| `ON THE BUILDER.md` | Context about the broader system-building practice behind the artifact |
| `tests/test_kaomoji_engine.py` | Unit tests for bounded runs and core behavior |
| `README.md` | Operation, orientation, limitations, and repository navigation |

## What it is not

This is not:

- a chatbot;
- an artificial-intelligence model;
- an emotional model;
- a sentiment detector;
- a realistic simulation of human feeling;
- a psychological assessment tool;
- a system that infers intent;
- a claim that kaomoji possess objective emotional meanings.

It is a small inspectable system for watching finite symbolic rules create drift over time. It is also funny when left running in a terminal, which is not a defect.

## Extension points

The contained engine is complete when it can start, mutate, remain bounded, stop cleanly, and reproduce a finite run when asked. Possible extensions include:

- additional mutation cycles;
- alternative seed sets;
- output logging;
- external triggers;
- visual or web-based renderers;
- structured run export;
- mutation statistics.

Those are possible branches, not missing requirements. Any extension should preserve the central honesty of the project: visible rules, bounded state, and no invented claim of emotional understanding.

## Project status

The current version is a working, tested artifact. Its narrow scope is intentional.

Known boundaries:

- state consists only of the current string;
- no history is retained by the engine;
- random output has no semantic score;
- the terminal interface is the only included renderer;
- no packaging or installer is included;
- no external service is contacted.

## Copyright and reuse

No separate open-source license is currently included in this repository. Unless a license is added, default copyright applies and publication of the source does not automatically grant permission to copy, modify, redistribute, or sell it.

## About the builder

Built and documented by **Roger Crosby** as a small, inspectable experiment in symbolic mutation, bounded state, observer interpretation, and honest technical description.

The project demonstrates the ability to move from an unusual concept to:

- a working prototype;
- bounded operating rules;
- deterministic testing;
- clear documentation;
- an explicit statement of what the system does and does not do.

Roger is available for remote contract work and project-based collaboration involving artificial-intelligence evaluation, human-gated workflows, documentation systems, operational writing, and unusual working prototypes.

Contact: [info@paranoidpeoplelivelonger.com](mailto:info@paranoidpeoplelivelonger.com)  
Portfolio: [PPLL Signal Archive](https://github.com/RexPiperisOlem/PPLL-Signal-Archive)  
Profile: [RexPiperisOlem](https://github.com/RexPiperisOlem)
