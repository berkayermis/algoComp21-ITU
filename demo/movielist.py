movies = {"Pulp Fiction" : 9, "Goodfellas" : 8}
finalRes = []

while True:
    userInp = input()

    if userInp == "0":
        for i in finalRes:
            print(i)

        for key, value in movies.items():
            print(f"{key} {value}")
        break

    elif userInp == "1":
        try:
            newToAdd = input()
            splittedNew = newToAdd.split()
            movies[' '.join([str(elem) for elem in splittedNew[:-1]])] = int(splittedNew[-1])

        except ValueError:
            pass


    elif userInp == "2":
        newToAdd = input()

        if newToAdd in movies:
            finalRes.append(f"{movies[newToAdd]}")
        else:
            finalRes.append("You haven't added this movie")