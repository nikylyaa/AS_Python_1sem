r = open("input.txt", "r")
w = open("output.txt", "w")

for line in r:
    line = line.rstrip("\n")

    if line != "":
        if len(line) % 2 != 0:
            line = " " + line

        spaces = (50 - len(line)) // 2
        line = " " * spaces + line

    w.write(line + "\n")

r.close()
w.close()
