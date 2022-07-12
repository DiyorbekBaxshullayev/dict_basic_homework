def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    cities = {
        1:'a',
        2:'b'
        }
    
    return cities[1]

print(cities_dict(1))
    