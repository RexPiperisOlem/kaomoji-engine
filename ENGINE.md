# Kaomoji Emotional Confusion Engine

## Implementation and design note

The Kaomoji Emotional Confusion Engine is a deliberately small terminal program. It starts with one kaomoji, repeatedly changes its character string, and exposes every change as a numbered frame.

The implementation is the claim. There is no trained model, hidden emotional layer, narrative engine, or sentiment analysis behind it.

## The state

The current kaomoji string is the engine's complete state. A frame is both the stored state and the visible output.

The engine does not maintain a separate label such as happy, distressed, or confused. Any emotional reading belongs to the observer.

## The heartbeat

The heartbeat loop performs four operations:

1. Select one mutation from the active cycle.
2. Apply it to the current string.
3. Bound the result to the configured maximum width.
4. Print the new state as the next frame.

The loop continues until it reaches a requested frame count or receives a keyboard interruption.

## The mutation cycles

Every cycle includes four small substitutions:

- lowercase `o` can become uppercase `O`
- a period can become `o`
- a caret can become `o`
- an underscore can become a period

Each cycle adds its own behavior:

### Ripple

Adds a tilde to the left or right edge. The result accumulates visible edge noise.

### Spiral

Reverses the string or places it inside another pair of parentheses. The result can flip or nest.

### Break

Gives every character a 30 percent chance of becoming `x`. The result can degrade quickly and unevenly.

### Echo

Duplicates the current string with a space between copies. Because repeated duplication would otherwise grow exponentially, the engine compresses the middle when the configured width is exceeded.

## Bounded endlessness

The original engine could keep adding characters, especially in `echo` mode, until output and memory use became unreasonable. The current engine separates duration from size:

- duration is unlimited by default
- each visible state has a fixed maximum width
- a finite frame count can be supplied for demonstrations
- a random seed can make a run repeatable

This keeps the continuous behavior without pretending a computer has infinite memory.

## Input and operation

The simplest run is interactive:

```bash
python kaomoji_engine.py
```

The operator chooses a cycle and stops the heartbeat with `Ctrl+C`.

The same engine can run without interactive input:

```bash
python kaomoji_engine.py --cycle break --frames 20 --random-seed 11 --delay 0
```

This makes the artifact easy to demonstrate, test, embed, or capture without changing its basic behavior.

## Design boundaries

The engine intentionally does not:

- understand language
- infer intent
- classify emotion
- remember earlier frames beyond the current string
- assign meaning to its symbols
- optimize toward a goal
- claim psychological realism

It demonstrates one narrow thing: a finite set of symbolic operations can create a changing sequence that observers instinctively try to read.

## Extension points

The code can support additional cycles, alternative seed sets, output logging, or external triggers. Those are extensions, not missing pieces. The contained engine is already complete when it can start, mutate, remain bounded, stop cleanly, and reproduce a finite run when asked.
