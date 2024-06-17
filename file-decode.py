def decode(message_file):
    # Class to create a Pyramid structure
    def create_pyramid(max_num, myDict):
        current_num = 1
        row_length = 1
        keys = []
        while current_num <= max_num:
            row = []
            for _ in range(row_length):
                if current_num > max_num:
                    break
                row.append(current_num)
                current_num += 1
            # print(",".join(map(str, row)))
            keys.append(row[::-1][0])
            row_length += 1
        # print(keys)
        decode_val = []
        for x in keys:
            # print(x)
            myDict.get(x)
            decode_val.append(myDict.get(str(x)))
            # print(myDict.get(str(x)))
        print(" ".join(map(str, decode_val)))
        return " ".join(map(str, decode_val))

    # Get the data from the file
    with open(message_file, "r") as f:
        mylist = [line.rstrip("\n") for line in f]

    # Create a Key Value Pair Object from the Data
    arr = []
    myDict = dict(s.split() for s in mylist)

    # Loop through the List and get only the numeric key
    for s in mylist:
        # convert the num from string into int
        converted_num = int(s.split()[0])
        arr.append(converted_num)

    create_pyramid(len(arr), myDict)


decode("coding_qual_input.txt")
