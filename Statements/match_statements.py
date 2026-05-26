# Match Statemets:
# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
#  This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages),
#  but it’s more similar to pattern matching in languages like Rust or Haskell. Only the first pattern that matches gets executed and
#  it can also extract components (sequence elements or object attributes) from the value into variables. If no case matches, 
# none of the branches is executed.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case 200:
            return "Successfully update or retrieve data"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    GREY = 'grey'

color = Color(input("Enter your choice of color:"))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues")
    case Color.GREY:
        print("Grey color is good!")

