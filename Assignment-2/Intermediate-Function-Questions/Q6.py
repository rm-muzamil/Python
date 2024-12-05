# Create a function that accepts a dictionary and returns the key with the highest value.
def get_max_key(d):
    if not d:
        return None
    return max(d,key=d.get)
data = {'a':5,'b':100,'c':15}
print(f"The key with highest value is : {get_max_key(data)}")