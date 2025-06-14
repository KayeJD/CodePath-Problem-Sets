def linear_search(lst, target):
    """
    Perform a linear search for the target in the list.
    
    :param lst: List of elements to search
    :param target: Element to find
    :return: Index of target if found, otherwise -1
    """

    # for index, element in enumerate(lst):
    #     if element == target:
    #         return index

    return -1
    
    
def test_linear_search():
    assert linear_search(['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn'], 'hunny') == 3
    assert linear_search(['apple', 'banana', 'cherry'], 'banana') == 1
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    assert linear_search([], 1) == -1
    assert linear_search([10], 10) == 0
    assert linear_search([10], 20) == -1

if __name__ == "__main__":
    test_linear_search()
    print("All tests passed!")