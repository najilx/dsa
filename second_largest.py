def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    largest = max(sequenceOfNumbers)
    second_largest=float(-inf)
    for num in sequenceOfNumbers:
        if num < largest and num > second_largest:
            second_largest=num
    if second_largest == float(-inf):
        return -1
    else:
        return second_largest