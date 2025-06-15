def remove_low_rated_destinations(destinations, rating_threshold):
    """
    You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations and a rating_threshold as parameters. The function should iterate through the dictionary and remove all destinations that have a rating strictly below the rating_threshold. Return the updated dictionary.
    """

    
def test_lineup():
    assert remove_low_rated_destinations({"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}, 4.0) == {"Paris": 4.8, "Addis Ababa": 4.9}


if __name__ == "__main__":
    test_lineup()
    print("All tests passed!")