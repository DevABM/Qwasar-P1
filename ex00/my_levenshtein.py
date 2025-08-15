def my_levenshtein(s1: str, s2: str) -> int:
    # If strings are not the same length, return -1
    if len(s1) != len(s2):
        return -1
    
    # Count the number of positions where the characters differ
    diff_count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff_count += 1
    
    return diff_count
