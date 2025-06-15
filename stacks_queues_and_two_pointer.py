""" CHEATSHEET
    Stacks:
    stack = []
    stack.append(x)
    x = stack.pop()

    Queues: 
    from collections import deque
    queue = deque()
    queue.append(x) # adds to the right 
    queue.appendleft(x) # adds to the left
    queue.popleft() # removes from left
    queue.pop() # removes from right
"""

from collections import deque

# STANDARD SET ######################################################################################################################

# VERSION Set 1 *********************************************************************************************************************
def is_valid_post_format(posts):
    """
    You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

    A post is considered valid if:

    1. Every opening tag has a corresponding closing tag of the same type.
    2. Tags are closed in the correct order.
    """

    openBrackets = []

    for bracket in posts:
        if bracket in ('{', '[', '('):
            openBrackets.append(bracket)
        else:
            match bracket:
                case '}':
                    if openBrackets[-1] == '{':
                        openBrackets.pop()
                    else:
                        return False
                case ']':
                    if openBrackets[-1] == '[':
                        openBrackets.pop()
                    else:
                        return False
                case ')':
                    if openBrackets[-1] == '(':
                        openBrackets.pop()
                    else:
                        return False
                    
    return True

print("\nTESTING is_valid_post_format()...")
assert is_valid_post_format("()") == True
assert is_valid_post_format("()[]{}") == True
assert is_valid_post_format("(]") == False


def reverse_comments_queue(comments):
    """
    Given a queue of comments represented as a list of strings, reverse the order using a stack.
    """

    queue = deque()
    output = []

    for comment in comments:
        queue.append(comment)

    while queue:
        output.append(queue.pop())

    return output
        
print("\nTESTING reverse_comments_queue()...")
assert reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]) == ["Thanks for sharing.", "Love it!", "Great post!"]
assert reverse_comments_queue(["First!", "Interesting read.", "Well written."]) == ["Well written.", "Interesting read.", "First!"]


def is_symmetrical_title(title):
    """
    Determine if a post title is symmetrical, meaning it reads the same forwards and backwards
    when ignoring spaces, punctuation, and case.
    """
    title = title.replace(" ", "").lower()
    front = 0
    end = len(title) - 1

    while front < end:
        if title[front] == title[end]:
            front += 1
            end -= 1
        else:
            return False
    
    return True

print("\nTESTING is_symmetrical_title()...")
assert is_symmetrical_title("A Santa at NASA") == True
assert is_symmetrical_title("Social Media") == False

def engagement_boost(engagements):
    """
    Given an integer array engagements sorted in non-decreasing order, return an array of the
    squares of each number sorted in non-decreasing order using the two-pointer technique.
    """
    output = []

    for number in engagements:
        output.append(abs(number) * abs(number))

    output.sort()

    return output
    
print("\nTESTING engagement_boost()...")
assert engagement_boost([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert engagement_boost([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

def clean_post(post):
    """
    Given a string post of lowercase and uppercase English letters, remove any pairs of adjacent
    characters where one is the lowercase version and the other is the uppercase version of the same letter.
    """
    pass

def edit_post(post):
    """
    Reverse the order of characters in each word within the post while preserving whitespace
    and initial word order, using a queue.
    """
    pass

def post_compare(draft1, draft2):
    """
    Given two draft strings, return true if they are equal when typed into text editors.
    '#' means a backspace character.
    """
    pass

def manage_stage_changes(changes):
    """
    You are given a list changes of strings where each string represents a change action. The actions can be:

    - "Schedule X": Schedule a performance with ID X on the stage.
    - "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
    - "Reschedule": Reschedule the most recently canceled performance to be the next on stage.

    Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.
    """
    pass

def process_performance_requests(requests):
    """
    Use a queue to process performance requests based on priority. Each request has a priority,
    and requests with higher priorities are processed before those with lower priorities.
    """
    pass

def collect_festival_points(points):
    """
    Use a stack to simulate collecting points at various booths and return the total points collected.
    """
    pass

def booth_navigation(clues):
    """
    Simulate a participant's booth navigation using a list of clues with "back" instructions,
    returning the final sequence of booths visited.
    """
    pass

def merge_schedules(schedule1, schedule2):
    """
    Merge two performance schedules by adding performances in alternating order. If one schedule
    is longer, append the rest to the end.
    """
    pass

def next_greater_event(schedule1, schedule2):
    """
    For each event in schedule1, find its position in schedule2 and determine the next event in
    schedule2 with a higher popularity score. If none, return -1.
    """
    pass

def sort_performances_by_type(performances):
    """
    Rearrange the performances so that all even-type performances appear first, followed by odd-type performances.
    """
    pass

# def test_standard_set():S
    # assert clean_post("poOost") == "post"
    # assert clean_post("abBAcC") == ""
    # assert clean_post("s") == "s"

    # assert edit_post("Boost your engagement with these tips") == "tsooB ruoy tnemegegna htiw esehT spit"
    # assert edit_post("Check out my latest vlog") == "kcehC tuo ym tseval golv"

    # assert post_compare("ab#c", "ad#c") == True
    # assert post_compare("ab##", "c#d#") == True
    # assert post_compare("a#c", "b") == False


# VERSION Set 2 *********************************************************************************************************************
def time_required_to_stream(movies, k):
    """
    Return the time taken for the user at position k to finish streaming all their movies.
    Each user takes 1 second per movie and goes to the back of the queue if they have movies left.
    """
    pass
# assert time_required_to_stream([2, 3, 2], 2) == 6
# assert time_required_to_stream([5, 1, 1, 1], 0) == 8

def reverse_watchlist(watchlist):
    """
    Reverse the order of the watchlist in-place using the two-pointer technique.
    Do not use slicing.
    """
    pass

def remove_duplicate_shows(schedule):
    """
    Remove adjacent duplicates in a string representing shows until no duplicates remain.
    """
    pass

def minimum_average_view_count(view_counts):
    """
    Repeatedly remove the min and max values from view_counts and calculate their average.
    Return the minimum average computed.
    """
    pass

def min_remaining_watchlist(watchlist):
    """
    Remove pairs of movies "AB" or "CD" from a string watchlist repeatedly and
    return the length of the remaining string.
    """
    pass

def apply_rating_operations(ratings):
    """
    Apply operations to merge identical adjacent ratings and then push all 0s to the end.
    """
    pass

def make_smallest_watchlist(watchlist):
    """
    Convert the input to a palindrome with the minimum number of changes.
    If multiple options, return the lexicographically smallest.
    """
    pass

def final_supply_costs(costs):
    """
    Given the cost of supplies, apply a special discount where if costs[j] <= costs[i]
    and j > i, then you get a discount of costs[j]. Otherwise, no discount applies.
    Return the final cost after discounts.
    """
    pass

def first_symmetrical_landmark(landmarks):
    """
    Return the first landmark name that is symmetrical (palindrome).
    If none exists, return an empty string.
    """
    pass

def terrain_elevation_match(terrain):
    """
    Given a string of 'I' and 'D', reconstruct a sequence of elevations that satisfies the
    conditions of increasing ('I') and decreasing ('D') between adjacent values.
    """
    pass

def find_the_log_conc_val(logs):
    """
    Simulate log concatenation by combining the first and last elements and summing the results
    until no logs remain.
    """
    pass

def count_explorers(explorers, supplies):
    """
    Simulate a queue where explorers take from the supply stack if the top item matches their
    preference. Return how many explorers are unable to gather supplies.
    """
    pass

def count_balanced_terrain_subsections(terrain):
    """
    Count how many balanced subsections exist in a terrain string, where a balanced section has
    equal and grouped consecutive '0's and '1's.
    """
    pass

def is_prefix_of_signal(transmission, searchSignal):
    """
    Return the 1-indexed position of the first signal in the transmission for which searchSignal
    is a prefix. If none, return -1.
    """
    pass

# def test_version_2():

    # wl = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
    # assert reverse_watchlist(wl) == ["The Witcher", "The Crown", "Stranger Things", "Breaking Bad"]

    # assert remove_duplicate_shows("abbaca") == "ca"
    # assert remove_duplicate_shows("azxxzy") == "ay"

    # assert minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1]) == 5.5
    # assert minimum_average_view_count([1, 9, 8, 3, 10, 5]) == 5.5
    # assert minimum_average_view_count([1, 2, 3, 7, 8, 9]) == 5.0

    # assert min_remaining_watchlist("ABFCACDB") == 2
    # assert min_remaining_watchlist("ACBBD") == 5

    # assert apply_rating_operations([1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]
    # assert apply_rating_operations([0, 1]) == [1, 0]

    # assert make_smallest_watchlist("egcfe") == "efcfe"
    # assert make_smallest_watchlist("abcd") == "abba"
    # assert make_smallest_watchlist("seven") == "neven"


# ADVANCED SETS ######################################################################################################

# VERSION Set 1 ******************************************************************************************************

def blueprint_approval(blueprints):
    """
    Simulate the blueprint approval process using a queue. Blueprints with lower complexity
    are approved before higher ones. Return the order in which blueprints are approved.
    """
    pass

def build_skyscrapers(floors):
    """
    Build skyscrapers from floors with the rule that each floor must be placed on top of a floor
    with equal or greater height. Start a new skyscraper when this is not possible. Return the number of skyscrapers.
    """
    pass

def max_corridor_area(segments):
    """
    Given corridor segment widths, find two segments such that the minimum width between them times
    the distance gives the maximum possible area.
    """
    pass

def min_swaps(s):
    """
    Given a string with equal number of '[' and ']', return the minimum number of swaps needed
    to make the building layout balanced.
    """
    pass

def make_balanced_room(s):
    """
    Remove the minimum number of parentheses to make a room layout string balanced.
    Return any valid layout.
    """
    pass

def time_to_complete_dream_designs(design_times):
    """
    Given an array of design times, return an array where each element is the number of days
    until a more complex design is available.
    """
    pass

def next_greater_dream(dreams):
    """
    Given a circular array, return the next greater element for each dream.
    If none exists, return -1.
    """
    pass

def score_of_mystical_market_chains(chain):
    """
    Given a balanced string with '()', return the score based on mystical power rules.
    () -> 1, (A) -> 2 * A, AB -> A + B
    """
    pass

def arrange_magical_orbs(orbs):
    """
    Sort 0s, 1s, and 2s in-place to order magical orbs as red, white, blue (0, 1, 2).
    """
    pass

def match_buyers_and_sellers(buyers, sellers):
    """
    Maximize the number of transactions where buyers buy from sellers if they can afford the price.
    Each buyer/seller can transact only once.
    """
    pass

def maximum_value(items, x, y):
    """
    Maximize value gained from removing 'AB' and 'BA' pairs from the items string.
    Gain x for 'AB' and y for 'BA'.
    """
    pass

# def get_strongest_artifacts(artifacts, k):
#     """
#     Return the strongest k artifacts relative to the median strength of the full list.
#     """
#     pass

def num_enchanted_boats(creatures, limit):
    """
    Given creature powers and a boat limit, return the minimum number of boats needed
    where each boat can carry up to two creatures within the limit.
    """
    pass

def token_value(token):
    """
    Compute the value of a token string made of balanced '()' using:
    () -> 1, (A) -> 2*A, AB -> A + B
    """
    pass

# def test_advanced_version_1():
    # assert blueprint_approval([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]
    # assert blueprint_approval([7, 4, 6, 2, 5]) == [2, 4, 5, 6, 7]

    # assert build_skyscrapers([10, 5, 8, 3, 7, 2, 9]) == 4
    # assert build_skyscrapers([7, 3, 7, 3, 5, 1, 6]) == 4
    # assert build_skyscrapers([8, 6, 4, 7, 5, 3, 2]) == 2

    # assert max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    # assert max_corridor_area([1, 1]) == 1

    # assert min_swaps("][][" ) == 1
    # assert min_swaps("]]][[[" ) == 2
    # assert min_swaps("[]") == 0

    # assert make_balanced_room("art(t(d)e)sign)") == "art(t(d)e)s)ign"
    # assert make_balanced_room("d)e(s)ign") == "de(s)ign"
    # assert make_balanced_room(")((") == ""

    # assert time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3]) == [1, 1, 3, 2, 1, 1, 0, 0]
    # assert time_to_complete_dream_designs([2, 3, 1, 4]) == [1, 2, 1, 0]
    # assert time_to_complete_dream_designs([5, 5, 5, 5]) == [0, 0, 0, 0]

    # assert next_greater_dream([1, 2, 1]) == [2, -1, 2]
    # assert next_greater_dream([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]

# VERSION Set 2 **********************************************************************************************************************

def arrange_guest_arrival_order(arrival_pattern):
    """
    Given a pattern of 'I' and 'D', return the lexicographically smallest guest order using digits 1–9
    such that guest_order[i] < or > guest_order[i+1] based on the pattern.
    """
    pass

def reveal_attendee_list_in_order(attendees):
    """
    Rearrange attendees so that when revealed in steps (reveal, move next to bottom),
    the numbers appear in increasing order.
    """
    pass

def arrange_attendees_by_priority(attendees, priority):
    """
    Rearrange attendees by priority: less than -> equal to -> greater than, preserving relative order.
    """
    pass

def rearrange_guests(guests):
    """
    Rearrange the guests list of equal attendees and absences such that each positive value
    is followed by a negative one and vice versa, starting with a positive.
    """
    pass

def min_changes_to_make_balanced(schedule):
    """
    Return the minimum number of insertions needed to make the parenthesis string schedule balanced.
    """
    pass

def mark_event_timeline(event, timeline):
    """
    Return the index positions used to convert a blank timeline string into a target timeline using
    overlays of the event string.
    """
    pass

def predictAdoption_victory(votes):
    """
    Given votes of 'C' and 'D', simulate the ban/victory rules to return who will announce victory.
    """
    pass

def pair_up_animals(discomfort_levels):
    """
    Pair animals into n/2 groups such that the max discomfort among pairs is minimized.
    Return that minimum max discomfort.
    """
    pass

def rearrange_animal_names(s):
    """
    Reverse animal names or slogans within each pair of matching parentheses from innermost
    to outermost and return the final result without any parentheses.
    """
    pass

def append_animals(available, preferred):
    """
    Return the number of characters that must be appended to 'available' so 'preferred' is a subsequence.
    """
    pass

def group_animals_by_habitat(habitats):
    """
    Partition string into as many groups as possible such that no character appears in more than one group.
    Return the size of each group.
    """
    pass

def validate_shelter_sequence(admitted, adopted):
    """
    Return True if the adopted sequence could result from popping items off a stack after they were pushed
    in the order of 'admitted'. Otherwise return False.
    """
    pass


# def test_advanced_version_2():
#     assert score_of_mystical_market_chains("()") == 1
#     assert score_of_mystical_market_chains("(())") == 2
#     assert score_of_mystical_market_chains("()()") == 2

#     orbs1 = [2, 0, 2, 1, 1, 0]
#     arrange_magical_orbs(orbs1)
#     assert orbs1 == [0, 0, 1, 1, 2, 2]

#     orbs2 = [2, 0, 1]
#     arrange_magical_orbs(orbs2)S
#     assert orbs2 == [0, 1, 2]

#     assert match_buyers_and_sellers([4, 7, 9], [8, 2, 5, 8]) == 3
#     assert match_buyers_and_sellers([1, 1, 1], [10]) == 0

#     assert maximum_value("cdbcbbaaabab", 4, 5) == 19
#     assert maximum_value("aabbaaxybbaabb", 5, 4) == 20

#     # assert sorted(get_strongest_artifacts([1, 2, 3, 4, 5], 2)) == sorted([5, 1])
#     # assert sorted(get_strongest_artifacts([1, 1, 3, 5, 5], 2)) == sorted([5, 5])
#     # assert len(get_strongest_artifacts([6, 7, 11, 7, 6, 8], 5)) == 5

#     assert num_enchanted_boats([1, 2], 3) == 1
#     assert num_enchanted_boats([3, 2, 2, 1], 3) == 3
#     assert num_enchanted_boats([3, 5, 3, 4], 5) == 4

#     assert token_value("()") == 1
#     assert token_value("(())") == 2
#     assert token_value("()()") == 2


# if __name__ == "__main__":
#     # test_standard_set()
#     # test_version_2()
#     # test_advanced_version_1()
#     # test_advanced_version_2()
#     print("All tests passed!")