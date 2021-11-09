"""Restaurant rating lister."""

# define a function where we pass a file as parameter
    # open text file
    # iterate through each line
        # strip empty space at end of line
                # Split words in each line


def rating_list(file):

    opened_file = open(file)

    r_ratings = {}

    for line in opened_file:
        line = line.rstrip()
        # sorted(line)
        # print(line)
        restaurant, score = line.split(":")
        # print(restaurant)
        r_ratings[restaurant] = score
        # print(r_ratings)

    key_and_value = r_ratings.items()
    sorted_key_and_value = sorted(key_and_value)
    # print(sorted_key_and_value)


    for t in sorted_key_and_value:
        print(f"{t[0]} is rated at {t[1]}.")

    # for restaurant, score in r_ratings.items():
    #     sorted_dict = sorted(r_ratings)
    #     print(sorted_dict)

        # print(f"{restaurant} is rated at {score}.")

rating_list("scores.txt")

 