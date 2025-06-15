def lineup(artists, set_times):
    """
    Create a dictionary mapping artists to their set times.
    
    :param artists: List of artist names.
    :param set_times: List of set times corresponding to the artists.
    :return: Dictionary mapping each artist to their set time.
    """

    artistsAndTimes = {}

    if len(artists) != len(set_times):
        return []
    
    for i, artist in enumerate(artists):
        if artist not in artistsAndTimes:
            artistsAndTimes[artist] = set_times[i]

    return artistsAndTimes

    
def test_lineup():
    assert lineup(["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"], ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]) == {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalia": "7:30 PM"}


if __name__ == "__main__":
    test_lineup()
    print("All tests passed!")