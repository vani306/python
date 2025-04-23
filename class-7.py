class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters
    
w = Weather(["sunny", "rainy", "cloudy", "windy"])

print("rainy" in w)   # True
print("spring" in w)   # False
