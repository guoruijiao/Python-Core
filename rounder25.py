
def rounder25(amount):
    '''
    Return amount rounded UP to nearest
    quarter dollar.
        ...$1.89 becomes $2.00
        ...but $1.00/$1.25/$1.75/etc.
           remain unchanged
    '''
    dollars = int(amount)
    cents = round((amount - dollars) * 100)
    quarters = cents // 25
    if cents % 25:
        quarters += 1
    amount = dollars + 0.25 * quarters

    return amount

