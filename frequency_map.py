# frequency map
import random 


# code
while True:
    try: 
        target = int(input('enter a number between(0,100) : '))
        nums = [ random.randint(0,100) for i in range(0,1000) ]
    

        dic = {}
        for i in range(0,len(nums)):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]]=1

        print(dic[target])
        break
    except:
        print("error, try again")
