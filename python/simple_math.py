from typing import List
def add_array(array: List[float], number: int):
    """
        Add a number to each element in the array
        @param array a list of numbers
        @param number a number to add
        
        @return an array
    """
    return [i+number for i in array]

def subtract_array(array: List[float], number:int):
    """
        Add a number to each element in the array
        @param array a list of numbers
        @param number a number to subtract
        
        @return an array
    """
    return [i-number for i in array]

def multiply_array(array: List[float], number:int):
    """
        Add a number to each element in the array
        @param array a list of numbers
        @param number a number to multiply
        
        @return an array
    """
    return [i*number for i in array]

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]
    b = add_array(array=a, number=10)
    print(b)
    b = subtract_array(array=a, number=5)
    print(b)
    b = multiply_array(array=a, number=5)
    print(b)
