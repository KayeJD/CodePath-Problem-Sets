# STANDARD SET ######################################################################################################################

# VERSION Set 1 *********************************************************************************************************************
def extract_nft_names(nft_collection):
    """
    You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

    Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING extract_nft_names()...")
# assert extract_nft_names([
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
# ]) == ['Abstract Horizon', 'Pixel Dreams', 'Future City']

# assert extract_nft_names([
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
# ]) == ['Crypto Kitty', 'Galactic Voyage']

# assert extract_nft_names([
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]) == ['Golden Hour']


def quality_extract_nft_names(nft_collection):
    """
    You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

    Task:
    - Review the provided code and identify the bug(s).
    - Explain what the bug is and how it affects the output.
    - Refactor the code to fix the bug(s) and provide the correct implementation.
    """
    pass

# print("\nTESTING fixed extract_nft_names()...")
# assert quality_extract_nft_names([
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]) == ['Abstract Horizon', 'Pixel Dreams']
# assert quality_extract_nft_names([
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]) == ['Golden Hour']
# assert quality_extract_nft_names([]) == []


def identify_popular_creators(nft_collection):
    """
    Identify the most popular NFT creators in your collection.
    A creator is considered "popular" if they have created more than one NFT.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING identify_popular_creators()...")
# assert identify_popular_creators([
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]) == ['ArtByAlex']
# assert identify_popular_creators([
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
#     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# ]) == ['SpaceArt']
# assert identify_popular_creators([
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]) == []


def average_nft_value(nft_collection):
    """
    Calculate the average value of the NFTs in the collection.
    If the collection is empty, return 0.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING average_nft_value()...")
# assert average_nft_value([
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]) == 5.7
# assert average_nft_value([
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]) == 9.15
# assert average_nft_value([]) == 0


def search_nft_by_tag(nft_collections, tag):
    """
    Given a nested list of NFT collections, search for all NFT names that include the given tag.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING search_nft_by_tag()...")
# nft_collections = [[{"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
#                     {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}],
#                    [{"name": "Urban Jungle", "tags": ["urban", "landscape"]},
#                     {"name": "City Lights", "tags": ["modern", "landscape"]}]]
# assert search_nft_by_tag(nft_collections, "landscape") == ['Urban Jungle', 'City Lights']

# nft_collections_2 = [[{"name": "Golden Hour", "tags": ["sunset", "landscape"]},
#                       {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}],
#                      [{"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}]]
# assert search_nft_by_tag(nft_collections_2, "sunset") == ['Golden Hour', 'Sunset Serenade']

# nft_collections_3 = [[{"name": "The Last Piece", "tags": ["finale", "abstract"]}],
#                      [{"name": "Ocean Waves", "tags": ["seascape", "calm"]},
#                       {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}]]
# assert search_nft_by_tag(nft_collections_3, "modern") == []


def process_nft_queue(nft_queue):
    """
    Given a list of NFTs in a queue, return a list of names in the order they are processed (FIFO).

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING process_nft_queue()...")
# assert process_nft_queue([
#     {"name": "Abstract Horizon", "processing_time": 2},
#     {"name": "Pixel Dreams", "processing_time": 3},
#     {"name": "Urban Jungle", "processing_time": 1}
# ]) == ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']

# assert process_nft_queue([
#     {"name": "Golden Hour", "processing_time": 4},
#     {"name": "Sunset Serenade", "processing_time": 2},
#     {"name": "Ocean Waves", "processing_time": 3}
# ]) == ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']

# assert process_nft_queue([
#     {"name": "Crypto Kitty", "processing_time": 5},
#     {"name": "Galactic Voyage", "processing_time": 6}
# ]) == ['Crypto Kitty', 'Galactic Voyage']


def validate_nft_actions(actions):
    """
    Return True if all "add" actions have matching "remove" actions, and no "remove" occurs before an "add".

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING validate_nft_actions()...")
# assert validate_nft_actions(["add", "add", "remove", "remove"]) == True
# assert validate_nft_actions(["add", "remove", "add", "remove"]) == True
# assert validate_nft_actions(["add", "remove", "remove", "add"]) == False


def find_closest_nft_values(nft_values, budget):
    """
    Given a sorted list of NFT values and a budget, return the two closest values (one below, one above) near the budget.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    """
    pass

# print("\nTESTING find_closest_nft_values()...")
# nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
# nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
# nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]
# assert find_closest_nft_values(nft_values, 8.0) == (7.2, 9.0)
# assert find_closest_nft_values(nft_values_2, 6.5) == (6.3, 7.8)
# assert find_closest_nft_values(nft_values_3, 3.0) == (2.5, 4.0)

# STANDARD VERSION Set 2 *********************************************************************************************************************


# ADVANCED SET ######################################################################################################################

# ADVANCED VERSION Set 1 *********************************************************************************************************************

# Q1
def filter_sustainable_brands(brands, criterion):
    """
    You're tasked with filtering out brands that are not sustainable from a list of fashion brands.
    A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly
    materials, ethical labor practices, or being carbon-neutral.

    Write the filter_sustainable_brands() function, which takes a list of brands and a criterion,
    then returns a list of brands that meet the criterion.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
    for why you believe your solution has the stated time and space complexity.
    """
    # Create ouput list
    # Loop through the brands list
        # access "criteria" and loop through the list
            # compare each list element to criterion 
            # if comparison hit, add to output list
    # return output list
    
    res = []
    for brand in brands: 
        if criterion in brand["criteria"]: 
            res.append(brand["name"])
    return res


print("\nTESTING filter_sustainable_brands()...")
brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]
brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]
brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]
assert filter_sustainable_brands(brands, "eco-friendly") == ['EcoWear', 'GreenThreads']
assert filter_sustainable_brands(brands_2, "ethical labor") == ['Earthly']
assert filter_sustainable_brands(brands_3, "carbon-neutral") == ['GreenLife']
print("All passed!")


# Q2
def count_material_usage(brands):
    '''
    Certain materials are recognized as eco-friendly due to their low environmental impact. You need to track which materials are used by various brands and count how many times each material appears across all brands.

    Write the count_material_usage() function, which takes a list of brands (each with a list of materials) and returns the material names and the number of times each material appears across all brands.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    '''
    hash_map = {}
    for brand in brands: 
        for m in brand["materials"]: 
            if m in hash_map: 
                hash_map[m] += 1
            else: 
                hash_map[m] = 1

    print(hash_map)
    return hash_map
    

print("\\nTESTING count_material_usage()...")
assert count_material_usage([
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]) == {'organic cotton': 2, 'recycled polyester': 2, 'bamboo': 2}
assert count_material_usage([
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]) == {'hemp': 2, 'linen': 2, 'organic cotton': 1, 'recycled wool': 1}
assert count_material_usage([
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]) == {'organic cotton': 1, 'recycled polyester': 2, 'hemp': 1, 'bamboo': 1}


# Q3
def find_trending_materials(brands):
    '''
    In the fast-changing world of fashion, certain materials and practices become trending based on how frequently they are adopted by brands. You want to identify which materials and practices are trending. A material or practice is considered "trending" if it appears in the dataset more than once.

    Write the find_trending_materials() function, which takes a list of brands (each with a list of materials or practices) and returns a list of materials or practices that are trending.
    '''
    pass

# print("\\nTESTING find_trending_materials()...")
# assert find_trending_materials([
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]) == ['organic cotton', 'recycled polyester', 'bamboo']
# assert find_trending_materials([
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]) == ['hemp', 'linen']
# assert find_trending_materials([
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]) == ['recycled polyester']

def find_best_fabric_pair(fabrics, budget):
    """""""""
    '''
    You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget. Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics whose combined cost is the highest possible without exceeding the budget.

    Write the find_best_fabric_pair() function, which takes a list of fabrics (each with a name and cost) and a budget. The function should return the names of the two fabrics whose combined cost is the closest to the budget without exceeding it.
    '''
    pass
    """
    
    sorted_fabric = sorted(fabrics, key=lambda item: item[1])
    print("sorted fabric", sorted_fabric)
    l = 0
    r = len(sorted_fabric) - 1
    min_dif = float('inf')
    best_pair = (None, None)
    while l <= r: 
        sum_fabrics = fabrics[l][1] + fabrics[r][1]
        print("sum is ", sum_fabrics)
        if sum_fabrics == budget: 
            print(fabrics[l][0])
            print(fabrics[r][0])
            return (fabrics[r][0], fabrics[l][0])
        elif sum_fabrics < budget:
            if min_dif > (budget - sum_fabrics): 
                min_dif = budget - sum_fabrics
                best_pair = (fabrics[l], fabrics[r]) 
            l += 1
        else: 
            r -= 1
    print('yip')
    return best_pair

    """new = {}
    for fabric, cost in fabrics:
        complement = budget - cost
        if complement in new:
            return [new[complement], fabric]
        
        new[cost] = fabrics"""

find_best_fabric_pair([("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)], 45)
find_best_fabric_pair([("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)], 70)
find_best_fabric_pair([("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)], 60)

# print("\\nTESTING find_best_fabric_pair()...")
# assert find_best_fabric_pair([("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)], 45) == ('Hemp', 'Organic Cotton')
# assert find_best_fabric_pair([("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)], 70) == ('Tencel', 'Recycled Wool')
# assert find_best_fabric_pair([("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)], 60) == ('Bamboo', 'Linen')


# ADVANCED VERSION Set 2 *********************************************************************************************************************

# Q1
def track_screen_time(logs):
    """
    You need to track how much time users spend on different apps throughout the day.

    Write the track_screen_time() function, which takes a list of logs, where each log contains
    an app name and the number of minutes spent on that app during a specific hour.
    The function should return the app names and the total time spent on each app.
    """
    pass

# print("\nTESTING track_screen_time()...")
# assert track_screen_time([("Instagram", 30), ("YouTube", 20), ("Instagram", 25), ("Snapchat", 15), ("YouTube", 10)]) == {'Instagram': 55, 'YouTube': 30, 'Snapchat': 15}
# assert track_screen_time([("Twitter", 10), ("Reddit", 20), ("Twitter", 15), ("Instagram", 35)]) == {'Twitter': 25, 'Reddit': 20, 'Instagram': 35}
# assert track_screen_time([("TikTok", 40), ("TikTok", 50), ("YouTube", 60), ("Snapchat", 25)]) == {'TikTok': 90, 'YouTube': 60, 'Snapchat': 25}


# Q2
def most_used_app(screen_time):
    """
    Find the app with the highest total screen time from a dictionary of screen time usage.

    Return any one app if there's a tie for the highest screen time.
    """
    pass

# print("\nTESTING most_used_app()...")
# assert most_used_app({"Instagram": 55, "YouTube": 30, "Snapchat": 15}) == "Instagram"
# assert most_used_app({"Twitter": 25, "Reddit": 20, "Instagram": 35}) == "Instagram"
# assert most_used_app({"TikTok": 90, "YouTube": 90, "Snapchat": 25}) in ["TikTok", "YouTube"]


# Q3
def most_varied_app(app_usage):
    """
    Identify the app with the most varied usage pattern over the week,
    measured as the difference between the max and min daily usage.
    """
    pass

# print("\nTESTING most_varied_app()...")
# app_usage = {
#     "Instagram": [60, 55, 65, 60, 70, 55, 60],
#     "YouTube": [100, 120, 110, 100, 115, 105, 120],
#     "Snapchat": [30, 35, 25, 30, 40, 35, 30]
# }
# app_usage_2 = {
#     "Twitter": [15, 15, 15, 15, 15, 15, 15],
#     "Reddit": [45, 50, 55, 50, 45, 50, 55],
#     "Facebook": [80, 85, 80, 85, 80, 85, 80]
# }
# app_usage_3 = {
#     "TikTok": [80, 100, 90, 85, 95, 105, 90],
#     "Spotify": [40, 45, 50, 45, 40, 45, 50],
#     "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
# }
# assert most_varied_app(app_usage) == "YouTube"
# assert most_varied_app(app_usage_2) == "Reddit"
# assert most_varied_app(app_usage_3) == "TikTok"


# Q4
def peak_usage_hours(screen_time):
    """
    Return the start hour and total screen time of the three-hour window with the highest screen time.
    If multiple windows have the same usage, return the earliest one.
    """
    pass

# print("\nTESTING peak_usage_hours()...")
# assert peak_usage_hours([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]) == (21, 690)
# assert peak_usage_hours([5, 15, 10, 20, 30, 25, 50, 40, 35, 45, 60, 55, 65, 75, 70, 85, 95, 90, 100, 110, 105, 115, 120, 125]) == (21, 360)
# assert peak_usage_hours([0]*24) == (0, 0)


# Q5
def find_longest_repeating_pattern(app_logs):
    """
    Find the longest repeating pattern in hourly app logs, and return the pattern and how many times it repeats.
    If multiple patterns are the same length, return the first one found.
    """
    pass

# print("\nTESTING find_longest_repeating_pattern()...")
# assert find_longest_repeating_pattern(["Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Facebook", "Twitter", "Instagram"]) == (['Instagram', 'YouTube', 'Snapchat'], 3)
# assert find_longest_repeating_pattern(["Facebook", "Instagram", "Facebook", "Instagram", "Facebook", "Instagram", "Snapchat", "Snapchat", "Snapchat", "Instagram"]) == (['Facebook', 'Instagram'], 3)
# assert find_longest_repeating_pattern(["WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook", "WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook"]) == (['WhatsApp', 'TikTok', 'Instagram', 'YouTube', 'Snapchat', 'Twitter', 'Facebook'], 2)


# Q6
def manage_screen_time_sessions(actions):
    """
    Verify app session integrity based on OPEN and CLOSE logs.
    Return True if all opens are closed in the correct order; otherwise, False.
    """
    pass

# print("\nTESTING manage_screen_time_sessions()...")
# assert manage_screen_time_sessions(["OPEN Instagram", "OPEN Facebook", "CLOSE Facebook", "CLOSE Instagram"]) == True
# assert manage_screen_time_sessions(["OPEN Instagram", "CLOSE Instagram", "CLOSE Facebook"]) == False
# assert manage_screen_time_sessions(["OPEN Instagram", "OPEN Facebook", "CLOSE Instagram", "CLOSE Facebook"]) == False


# Q7
def analyze_weekly_usage(weekly_usage):
    """
    Analyze a week's worth of app usage by category.
    Return a dictionary with total category usage, the busiest day, and the most-used category.
    """
    pass

# print("\nTESTING analyze_weekly_usage()...")
# weekly_usage = {
#     "Monday": {"Social Media": 120, "Entertainment": 60, "Productivity": 90},
#     "Tuesday": {"Social Media": 100, "Entertainment": 80, "Productivity": 70},
#     "Wednesday": {"Social Media": 130, "Entertainment": 70, "Productivity": 60},
#     "Thursday": {"Social Media": 90, "Entertainment": 60, "Productivity": 80},
#     "Friday": {"Social Media": 110, "Entertainment": 100, "Productivity": 50},
#     "Saturday": {"Social Media": 180, "Entertainment": 120, "Productivity": 40},
#     "Sunday": {"Social Media": 160, "Entertainment": 140, "Productivity": 30}
# }
# assert analyze_weekly_usage(weekly_usage) == {
#     'total_category_usage': {'Social Media': 890, 'Entertainment': 630, 'Productivity': 420},
#     'busiest_day': 'Saturday',
#     'most_used_category': 'Social Media'
# }


# Q8
def find_best_break_pair(break_times, target):
    """
    Find the pair of break durations whose total is closest to the target.
    Return the pair as a tuple. If < 2 breaks, return ().
    """
    pass

# print("\nTESTING find_best_break_pair()...")
# assert find_best_break_pair([10, 20, 35, 40, 50], 60) == (20, 40)
# assert find_best_break_pair([5, 10, 25, 30, 45], 50) == (5, 45)
# assert find_best_break_pair([15, 25, 35, 45], 70) == (25, 45)
# assert find_best_break_pair([30], 60) == ()



