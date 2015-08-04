from operator import getitem

def make_unit(catchphrase, damage):
    return (catchphrase, damage)

def get_catchphrase(unit):
    return getitem(unit, 0)

def get_damage(unit):
    return getitem(unit, 1)

def battle(first, second):
    """Simulates a battle between the first and second unit
    >>> zealot = make_unit('My life for Aiur!', 16)
    >>> zergling = make_unit('GRAAHHH!', 5)
    >>> winner = battle(zergling, zealot)
    GRAAHHH!
    My life for Aiur!
    >>> winner is zealot
    True
    """
    print(get_catchphrase(first))
    print(get_catchphrase(second))
    if get_damage(first) >= get_damage(second):
        return first
    return second

def get_pair(pair, i):
    return pair[i]

def make_resource_bundle(minerals, gas):
    def dispatch(m):
        if m == 0:
            return minerals
        elif m == 1:
            return gas
    return dispatch

def get_minerals(bundle):
    #import pdb
    #pdb.set_trace()
    return bundle(0)

def get_gas(bundle):
    return bundle(1)

def make_building(unit, bundle):
    return (unit, bundle)

def get_unit(building):
    return get_pair(building, 0)

def get_bundle(building):
    return building[1]

def build_unit(building, bundle):
    """Constructs a unit if given the minimum amount of resources.
    Otherwise, prints an error message
    >>> barracks = make_building(make_unit('Go go go!', 6),
    ... make_resource_bundle(50, 0))
    >>> marine = build_unit(barracks, make_resource_bundle(20, 20))
    We require more minerals!
    >>> marine = build_unit(barracks, make_resource_bundle(50, 0))
    >>> print(get_catchphrase(marine))
    Go go go!
    """
    if get_minerals(bundle) < get_minerals(get_bundle(building)):
        print("We require more minerals!")
    if get_gas(bundle) < get_gas(get_bundle(building)):
        print("We require more gas!")
    return get_unit(building)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
