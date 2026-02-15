import re
import pathlib

avg_diff = lambda list1, list2: sum(abs(a - b) for a, b in zip(list1, list2))/len(list1)
no_space = lambda l: [cur.lstrip() for cur in l]
remove_line_whitespace = lambda s: "\n".join([line.strip() for line in s.splitlines()])
has_dup = lambda l: len(set(l)) < len(l)
flatten = lambda l: [item for elem in l for item in elem]
grep = lambda folder, st: [f.name for f in pathlib.Path(folder).iterdir() if f.is_file() and st in f.read_text()]

def main() -> None:
    print(avg_diff([1, 1, 2, 1], [2, 2, 4, 2]))
    print(no_space(["  search  ", "  ", "\tsearch"]))
    print(remove_line_whitespace("  Hello \n\tWorld \n"))
    print(has_dup([1, 2, 3, 4, 4]))
    print(flatten([[1, 2], [3, 4]]))
    print(grep(".", "lambda"))

if __name__ == "__main__":
    main()