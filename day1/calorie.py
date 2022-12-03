def get_input(file_name : str) -> list[list[int]]:
    with open(file_name, "r") as file: 
        data = []
        for elf in file.read().split('\n\n'):
            data.append(elf.splitlines())
        return [list(map(int, elf)) for elf in data] 



def get_max_sum(data : list[list[int]]) -> int:
    return max([sum(elf) for elf in data])


def get_max_three(data : list[list[int]]) -> int:
    return sum(sorted([sum(elf) for elf in data], reverse=True)[:3])


def main():
    file_name = "calorie.txt"
    data = get_input(file_name)
    print(get_max_sum(data))
    print(get_max_three(data))


if __name__ == "__main__":
    main()
