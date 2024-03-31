from typing import List
def add_array(array: List[float], number: int):
    """
        Add a number to each element in the array
        @param array a list of numbers
        @param number a number to add
        
        @return an array
    """
    return [i+number for i in array]

def add_arrays(array_a: List[float], array_b: List[float]):
    """
        Add a number to each element in the array
        @param array_a a list of numbers
        @param array_b a list of numbers
        
        @return an array
    """
    return [i+y for i, y in zip(array_a, array_b)]
    
    
if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]
    b = add_array(array=a, number=10)
    print(b)
    c = add_array(array_a=a, array_b=b)
    print(c)
