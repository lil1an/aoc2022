def get_input(file_name : str) -> list[list[str]]:
    with open(file_name, "r") as file:
        return [round.split() for round in file]

def get_score1(data : list[list[str]]) -> int:
    score = 0
    for round in data:
        if round[1] == "X": # player chose rock
            if round[0] == "C":
                score += 6
            elif round[0] == "A":
                score += 3
            score += 1
        elif round[1] == "Y": # player chose paper
            if round[0] == "A":
                score +=6
            elif round[0] == "B":
                score += 3
            score += 2
        elif round[1] == "Z": # player chose scissors
            if round[0] == "B":
                score += 6
            elif round[0] == "C":
                score += 3
            score += 3
    return score

def get_score2(data : list[list[str]]) -> int:
    score = 0
    for round in data:
        if round[1] == "X": # player loses
            if round[0] == "A":
                score += 3
            elif round[0] == "B":
                score += 1
            elif round[0] == "C":
                score += 2
        elif round[1] == "Y": # player draws
            if round[0] == "A":
                score += 1
            elif round[0] == "B":
                score += 2
            elif round[0] == "C":
                score += 3
            score += 3
        elif round[1] == "Z": # player wins
            if round[0] == "A":
                score += 2
            elif round[0] == "B":
                score += 3
            elif round[0] == "C":
                score += 1
            score += 6
    return score


def main():
    file_name = "strategy_guide.txt"
    data = get_input(file_name)
    part1 = get_score1(data)
    print(part1)
    part2 = get_score2(data)
    print(part2)


if __name__ == "__main__":
    main()
