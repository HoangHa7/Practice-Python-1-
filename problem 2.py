nums = []
x = None


def ascending():
    # print ascending list
    for u in range(len(nums) ** 4):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
            else:
                i += 1
        u += 1
    print(nums)


def descending():
    # print descending list
    for u in range(len(nums) ** 4):
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
            else:
                i += 1
        u += 1
    print(nums)


# In function so I can stop the while loop
def stop():
    while x is None:
        # Can store up to 10 numbers
        for y in range(10):
            try:
                # Input from user
                nums.append(input("In the list, add number: "))
                # check if the user done with fill the number or not
                if nums[y] == "done":
                    nums[y] = int(nums[y])
                elif y == 9:
                    nums.insert(9, "Stop")
                    nums[9] = int(nums[9])
                y += 1
            except ValueError:
                nums.pop(y)
                # print original list
                print(nums)
                ascending()
                descending()
                return 0


stop()
