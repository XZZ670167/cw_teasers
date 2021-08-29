# Triangle Inequality Theorem One
def is_triangle(side_length_array):
    side_length_array.sort()
    largest_side = side_length_array.pop()
    return largest_side < side_length_array[0] + side_length_array[1]


def ask_for_lengths():
    lengths = []
    for n in range(3):
        val = input("Enter your value: ")
        lengths.append(int(val))
    if is_triangle(lengths):
        print("This is a triangle")
    else:
        print("This is not a triangle")


result = is_triangle([2, 3, 4])
print(result)  # this is a triangle

result = is_triangle([2, 13, 4])
print(result)  # this is not a triangle

ask_for_lengths()
