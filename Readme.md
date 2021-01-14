# Task ideas

### Getting familiar w/ Python

_I've never taught someone who was totally new to programming,
and I'm going to assume you know things that you don't know.
Please ask questions!_

#### Math operations

```python
1 + 1 == 2 # addition
1 - 1 == 0 # subtraction
1 * 1 == 1 # multiplication
1 / 2 == 0.5 # floating point division
2 ** 2 == 4 # exponential
1 // 2 == 0 # integer division
1 % 2 == 1 # modulo (remainder after integer division)
```

#### Data types

* Immutable - These are _things_ like strings, ints, floats
```python
x = 1 # int
y = "hello" # string
z = 420.69 # float
```

* Data structures - These are collections of things like [lists and sets](https://docs.python.org/3/tutorial/datastructures.html)
```python
x = [1, "hello", 420.69, ["cheese", "pizza"]] # list
y = (1, 2, 3) # tuple
z = {1, 2, 3} # set
t = {1: "a", 2: "b"} # map
```

* Functions - These takes things and turn them into other things
```python
def square(x: float) -> float:
    return x*x

def concatenate_strings(string_a: str, string_b: str) -> str:
    return string_a + string_b
```

#### Flow control
* If and Switch
```python
if 10 % 2 == 0:
    print("even")
else:
    print("odd")

{0: "even", 1: "odd"}.get(9 % 2, "something else")
```

* Loops
```python
for i in range(10):
    print(i)
```

* Continue and break
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

i = 0
while True:
    if i == 10:
        break
    print(i)
    i += 1
```

### Intro Challenges

#### Numbers
1. Square all the numbers in a list.
1. Calculate the max and min in a list.
1. Calculate the standard deviation and mean of a list.

#### Numbers Challenge
1. Determine if a number is prime.
1. Return all prime factors of a number as a set.
1. Return a set of all the prime numbers from 2 to N.

#### Strings
1. Find the middle letter of a string. Print two letters if there is an even number of letters.
1. Determine if two words are palindromes
1. Find the frequency of each word in a text. Dont worry about punctuation, but ignore capitalization). 

#### Operations
1. Mapper - Apply a unary (one input) function to all items in a list and return a new list with the results.
1. Reducer - Apply a binary (two inputs) function to all items in a list and return a single item.
If the list is empty, return `None`.

### FOASS

* Good for introduction to interacting w/ apis.
* Also, good for telling people to fuck off.

### Flight data

* This seems like a nice project [create flight tracking app](https://www.geodose.com/2020/08/create-flight-tracking-apps-using-python-open-data.html).

* We can get flight data from [opensky](https://opensky-network.org/)
    * Force and energy calculations (assuming we can get mass). _What is the kinetic energy of flight X?_
    * Momentum vectors. We're given vertical and ground velocity and direction.
    
* We can draw maps with [bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/geo.html).
    * We can draw momentum vectors and label flights with energy calculations.
    * Rank the flights with the most energy consumption.
