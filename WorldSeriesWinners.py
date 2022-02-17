infile = open("WorldSeriesWinners.txt", "r")
infile_2 = open("WorldSeriesWinners.txt", "r")

# prompts the user to input a year
output = int(input("Type in a year: "))

# for the years without a world series
if output == 1904:
    print("No world series that year")
elif output == 1994:
    print("No world series that year")
else:
    winners = {}

    for line in infile:
        line = line.rstrip("\n")

        if line in winners:
            winners[line] = winners[line] + 1
        else:
            winners[line] = 1

    winners[line]

    # this is once it has been determined there was a world series that year
    year = {}

    # 1902 is our zero in this scenario
    counter = 1902

    for line in infile_2:
        line = line.rstrip("\n")

        if counter == 1903:
            counter += 2
            year[counter] = line
        elif counter == 1993:
            counter += 2
            year[counter] = line
        else:
            counter += 1
            year[counter] = line
    year[counter] = line

    counter = output
    champion = year[counter]
    amount = winners[champion]

    # output message and answer
    print("World Series Champion: ", champion)
    print("Number of World Series Championships Won: ", amount)
