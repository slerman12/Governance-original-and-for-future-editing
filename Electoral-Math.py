import math

# Totals
B = 4850205  # Bernie
D = 5471370  # Biden
E = 2102337  # Warren


# Elizabeth Warren voters needed to turn out for Bernie, and the rest for Biden
def distribute_between_both(bernie, biden, warren):
    """
    Derivation:

    (bernie + x) - (biden + (warren - x)) = 1
    bernie + x - biden - warren + x = 1
    2x = 1 - bernie + biden + warren
    x = (1 - bernie + biden + warren) / 2
    """

    return max(0, math.ceil((1 - bernie + biden + warren) / 2))


# For Bernie
def just_needed_for_bernie(bernie, biden):
    return max(0, biden - bernie + 1)


print('For Bernie to win the popular vote:\n')

# Maximum threshold: Percentage of Elizabeth Warren voters needed to turn out for Bernie, if the rest for Biden
print('Maximum threshold: Percentage of Elizabeth Warren voters needed to turn out for Bernie, if the rest for Biden:')
print(f'{round(distribute_between_both(B, D, E) / E * 100, 1)}%')

# Minimum threshold: Percentage of Elizabeth Warren voters needed to turn out for Bernie
print('\nMinimum threshold: Percentage of Elizabeth Warren voters needed to turn out for Bernie:')
print(f'{round(just_needed_for_bernie(B, D) / E * 100, 1)}%')

