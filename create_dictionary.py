def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    ans={}
    for i in range(len(key)):
        ans[key[i]]=value[i]
    
    return ans

key=[4,1,2,3]
value=["Four", "One", "Two", "Three"]

print(create_dictionary(key,value))

