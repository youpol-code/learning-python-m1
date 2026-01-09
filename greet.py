def greet_with_name(name:str):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

def greet_with(name: str,location: str):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#greet_with_name("angela")
#greet_with("Jack","London")
greet_with(location="London",name="Jack")