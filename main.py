def main():
    user_input = input("Enter number: ")
    number = int(user_input)
    if number  > 7:
        print("Hello")

    user_name = input("Enter your name: ")
    if user_name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

    numeric_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    multiples_of_3 = []
    for number in numeric_array:
        if number % 3 == 0:
            multiples_of_3.append(number)

    print("Multiples of 3 are: ", multiples_of_3)


if __name__ == "__main__":
    main()
