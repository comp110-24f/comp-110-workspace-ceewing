"""Practicing Recursion with Dog110"""

# scores: list[dict[str, str]]
# list of dictionaries of dogs' names and scores

# thresh: int
# Threshold we're using to determine if dog was good

# idx: int
# Index of dog of interest for the function call

pack: list[dict[str,str]] = [
  {"name": "Nelli", "score": "10"},
  {"name": "Ada", "score": "9"},
  {"name": "Pip", "score": "7"} 
]

def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """All good function that is a recursion function"""
    is_good: bool = = int(scores[inx]["score"]) >= thresh
    is_last: bool = len(scores) == idx + 1

    # let python deal with the edge case
    if is_good:
        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    else:
        return False
    


print(all_good(pack, 8 , 0))