from collections import defaultdict

# Word Count Mapper
def wc_mapper(input_file):
    intermediate = []
    with open(input_file, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                intermediate.append((word.strip(), 1))
    return intermediate

# Word Count Reducer
def wc_reducer(intermediate):
    word_counts = defaultdict(int)
    for word, count in intermediate:
        word_counts[word] += count
    return word_counts

# Line Search Mapper
def line_mapper(input_file):
    intermediate = []
    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, 1):
            intermediate.append((line_number, line.strip()))
    return intermediate

# Line Search Reducer
def line_reducer(intermediate):
    line_dict = {}
    for line_number, content in intermediate:
        line_dict[line_number] = content
    return line_dict

# Main function
if __name__ == "__main__":
    input_file = "input.txt"

    # Word Count
    print("Word Count:")
    intermediate_wc = wc_mapper(input_file)
    word_count_result = wc_reducer(intermediate_wc)
    for word, count in word_count_result.items():
        print(f"{word}: {count}")

    # Line Search
    print("\nLine Search:")
    intermediate_ls = line_mapper(input_file)
    line_search_result = line_reducer(intermediate_ls)
    for line_number, content in line_search_result.items():
        print(f"{line_number}: {content}")
