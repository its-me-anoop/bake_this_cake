def cakes(recipe, available):
    """
    Calculate the maximum number of cakes that can be baked based on a recipe and available ingredients.

    Args:
    recipe (dict): A dictionary with ingredients as keys and amounts required for one cake as values.
    available (dict): A dictionary with ingredients as keys and amounts available as values.

    Returns:
    int: The maximum number of cakes that can be baked, or 0 if not all ingredients are available.

    Example:
    >>> recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    >>> available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    >>> cakes(recipe, available)
    2
    """
    number_of_cakes = []
    for ingredient in recipe:
        if ingredient in available:
            cakes_from_ingredient = available[ingredient] // recipe[ingredient]
            number_of_cakes.append(cakes_from_ingredient)
        else:
            return 0
    return min(number_of_cakes)


print(
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
)

print(
    cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
)
