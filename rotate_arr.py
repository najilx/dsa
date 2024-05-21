def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n=len(arr)
    k=k%n
    rotated_arr = arr[k:]+arr[:k]
    return rotated_arr