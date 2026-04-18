# frequency map
import random   # import random module to generate random numbers

# code
while True:   # loop runs forever until we break manually
    try:      # try block to catch errors (like wrong input)

        target = int(input('enter a number between(0,100) : '))
        # take user input and convert it to integer

        nums = [random.randint(0,100) for i in range(0,1000)]
        # create a list of 1000 random numbers between 0 and 100

        dic = {}
        # create an empty dictionary to store frequency

        for i in range(0,len(nums)):
            # loop through all indexes of nums list

            if nums[i] in dic:
                # check if number already exists in dictionary

                dic[nums[i]] += 1
                # if yes, increase its count by 1

            else:
                dic[nums[i]] = 1
                # if not, add it to dictionary with count = 1

        print(dic[target])
        # print how many times target number appears

        break
        # stop the loop after successful execution

    except:
        # if any error occurs (like invalid input or key not found)

        print("error, try again")
        # show error message and repeat loop
