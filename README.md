# Kaomoji Emotional Confusion Engine

A tiny terminal artifact that chooses a face, applies random mutations, and keeps printing the results until it is told to stop.

It does not understand emotion. It does not interpret the faces it produces. The confusion comes from symbolic drift and from whatever the observer thinks the symbols mean.

## Run it

The engine uses only the Python standard library.

```bash
python kaomoji_engine.py
```

Choose one of four mutation cycles:

- `ripple` adds edge noise and makes small substitutions.
- `spiral` reverses or nests the current face.
- `break` replaces random characters with `x`.
- `echo` duplicates the current face.

The default run continues until you press `Ctrl+C`.

## Run a finite demonstration

```bash
python kaomoji_engine.py --cycle echo --frames 12 --random-seed 7 --delay 0
```

That command skips the prompt, prints exactly 12 frames, and uses a repeatable random sequence. This is useful for demonstrations, tests, and recording output.

See every option with:

```bash
python kaomoji_engine.py --help
```

## What the engine actually does

1. It selects one of three seed faces.
2. It keeps the current character string as its complete state.
3. It randomly selects one mutation allowed by the chosen cycle.
4. It prints the result as the next frame.
5. It repeats.

Output length is bounded so `echo` and `spiral` can continue without uncontrolled string growth. The mutation loop can still run indefinitely; the stored state cannot grow indefinitely.

## What it is not

This is not a chatbot, emotional model, sentiment detector, trained model, or realistic simulation of human feeling. There is no hidden emotional state and no claim that a kaomoji has an objective meaning.

It is a small inspectable system for watching finite symbolic rules produce drift over time. It is also funny when left running in a terminal, which is not a defect.

## Tests

```bash
python -m unittest discover -s tests -v
```

The tests use only the Python standard library.

## Repository map

- `kaomoji_engine.py` — the working engine
- `ENGINE.md` — the implementation and design note
- `ON THE BUILDER.md` — contextual notes about the broader system-building approach
- `tests/test_kaomoji_engine.py` — bounded-run and behavior checks

## About the builder

Built and documented by **Roger Crosby** as a small, inspectable experiment in symbolic mutation, bounded state, and observer interpretation.

Roger is available for remote contract work and project-based collaboration involving artificial-intelligence evaluation, agent workflows, documentation systems, operational writing, and unusual working prototypes.

Contact: [info@paranoidpeoplelivelonger.com](mailto:info@paranoidpeoplelivelonger.com)  
Portfolio: [PPLL Signal Archive](https://github.com/RexPiperisOlem/PPLL-Signal-Archive)
