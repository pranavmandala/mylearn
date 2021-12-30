car = {
    "brand": "Ford",
    "model": "Mustang",
    "vin": 1974,
    "year": 1974
}

# print variable - see how it prints
print(car)

# use type 
print(type(car))

# length
print(len(car))


# get all keys
keys = car.keys()
print(type(keys))
print(keys)


# get all values
vals = car.values()
print(type(vals))
print(vals)


# get all items
items = car.items()
print(type(items))
print(items)

# check if exists
# checks for the key

if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Accessing the value
# 2 ways

# 1 use attribute as index
print(car["model"])


#2 use get function
print(car.get("model"))