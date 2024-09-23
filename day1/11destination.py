from datetime import datetime
from functools import reduce

class MaxVotesError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()

class Destination:

    id: int
    title: str
    description: str
    votes: int
    created_at: datetime

    def __init__(self, id, title ):
        self.id = id
        self.title = title
        self.created_at = datetime.now()
        self.description = ""  # Initialize description as an empty string  
        self.votes = 0
    
    def increment_votes(self):
        self.votes += 1

    def set_votes(self, votes):
        if votes > 100:
            raise MaxVotesError("Cannot exceed 100 votes")
        self.votes = votes

    #setter for description
    def set_description(self, description):
        self.description = description

    def __str__(self) -> str:
        return f"Destination ID: {self.id}, Title: {self.title}, Description: {self.description}, Votes: {self.votes}, Created At: {self.created_at}"
    
# Create instances of Destination

destination1 = Destination(1, "Mount Everest")
destination1.set_description("The highest peak on Earth, standing at 29,032 feet above sea level.")
destination2 = Destination(2, "Machu Picchu")
destination3 = Destination(3, "K2")
destination3.set_votes(13)

destinations = [destination1, destination2, destination3]

for destination in destinations:
    print(destination)
    destination.increment_votes()
    print(destination)
    print("---")

destinations.sort(key=lambda x: x.title)

print("--- Sorted Destinations ---")

for destination in destinations:
    print(destination)

# map function to transform 
titles = list(map(lambda x: x.title, destinations))
print(titles)

def votes_morethan_ten(destination):
    return destination.votes > 10

filtered_list = list(filter(lambda x: x.votes > 10, destinations))
filtered_list = list(filter(votes_morethan_ten, destinations))
for destination in filtered_list:
    print(destination)


def custom_sum(first, second):
    return first + second

total_votes = reduce(custom_sum, [destination.votes for destination in destinations])

print(f"Total votes: {total_votes}")

only_votes = list(map(lambda x: x.votes, destinations))
print(only_votes)
print(max(only_votes))