def highest_product_of_three (list_of_ints):

    if len(list_of_ints) < 3:
        raise Exception('В массиве должно быть не менее 3х элементов!')

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = highest * lowest
    lowest_product_of_2  = highest_product_of_2
    highest_product_of_3 = highest_product_of_2 * list_of_ints[2]

    for current in list_of_ints[2:]:

        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        highest = max(highest, current)
        lowest  = min(lowest, current)

    return highest_product_of_3

def main():
    list_of_ints = [-10, 1, -10, 3, 2]
    print(highest_product_of_three(list_of_ints))

if __name__ == "__main__":
    main()
