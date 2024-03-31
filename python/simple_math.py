from typing import List
def add_array(array: List[float], number: int):
    """
        Add a number to each element in the array
        @param array a list of numbers
        @param number a number to add
        
        @return an array
    """
    return [i+number for i in array]


if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]
    b = add_array(array=a, number=10)
    print(b)