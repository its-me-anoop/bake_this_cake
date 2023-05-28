# Bake this cake

This is a simple Python script that calculates the maximum number of cakes that can be baked based on a recipe and the available ingredients.

## Function

`cakes(recipe, available)`

The function takes two arguments: 

- `recipe`: A dictionary where keys represent ingredients and values represent the amount of each ingredient required for one cake. 
- `available`: A dictionary where keys represent ingredients and values represent the amount of each ingredient that is available.

The function returns the maximum number of cakes that can be baked given the available ingredients. If not all ingredients are available, the function returns 0.

```python
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
```
