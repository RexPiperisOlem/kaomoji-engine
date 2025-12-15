import random
import time

def cmd_cycle():
    cycle = input("Choose cycle (ripple, spiral, break, echo): ")
    print("Cycle selected:", cycle)
    return cycle

def generate_seed():
    seeds = ["{o_o}", "{._.}", "{^_^}"]
    return random.choice(seeds)

def distort(kaomoji, cycle):
    cycle = cycle.lower()

    base = [
        lambda k: k.replace("o", "O"),
        lambda k: k.replace(".", "o"),
        lambda k: k.replace("^", "o"),
        lambda k: k.replace("_", ".")
    ]

    ripple = base + [
        lambda k: "~" + k,
        lambda k: k + "~"
    ]

    spiral = base + [
        lambda k: k[::-1],
        lambda k: "(" + k + ")"
    ]

    breakc = base + [
        lambda k: "".join(ch if random.random() > 0.3 else "x" for ch in k)
    ]

    echo = base + [
        lambda k: k + " " + k
    ]

    mapping = {
        "ripple": ripple,
        "spiral": spiral,
        "break":  breakc,
        "echo":   echo
    }

    pool = mapping.get(cycle, ripple)
    return random.choice(pool)(kaomoji)

def heartbeat(seed, cycle):
    frame = 1
    kaomoji = seed

    while True:
        kaomoji = distort(kaomoji, cycle)
        print("Frame", frame, "[" + cycle + "]:", kaomoji)
        frame += 1
        time.sleep(0.4)

def main():
    print("Kaomoji Emotional Confusion Engine")
    print()

    seed = generate_seed()
    print("Frame Zero Baseline:", seed)
    print()

    cycle = cmd_cycle()
    print()
    print("Starting heartbeat")
    print()

    heartbeat(seed, cycle)

if __name__ == "__main__":
    main()
