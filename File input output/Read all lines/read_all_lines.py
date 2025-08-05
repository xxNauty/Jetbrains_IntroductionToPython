with open("input.txt", "r") as infile:
    lines_list = []
    for line in infile.readlines():
        lines_list.append(line)

if __name__ == "__main__":
    print(lines_list)
