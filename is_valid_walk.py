def is_valid_walk(walk):
    print(walk.count("s"))
    if len(walk) != 10:
        return False 
    elif walk.count("s") == walk.count("n") and walk.count("w") == walk.count("e"):
        return True
        
        
