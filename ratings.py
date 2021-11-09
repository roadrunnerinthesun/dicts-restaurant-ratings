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
        word = line.split(":")
        print(word)
hello
rating_list("scores.txt")

 