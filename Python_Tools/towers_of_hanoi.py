def hanoi(n, start_pole, end_pole, inter_pole):
    if n >= 1:
        hanoi(n - 1, start_pole, inter_pole, end_pole)
        print("Disk moves from", start_pole, "to", end_pole, "pole")
        hanoi(n - 1, inter_pole, end_pole, start_pole)

hanoi(4, "a", "b", "c")
