from collections import Counter
list = [
    ["Monday", "PowerGrid", "Coconut", "Balenciaga", "July", "Socks", "Butterfly", "Balenciaga"],
    ["January", "Milkshake", "Cement", "Beetroot", "Saturday", "Monday", "Elephant", "Laptop"],
    ["Trousers", "Octopus", "Remix", "Oxford", "Salon", "Rainbow", "Ocean", "Milkshake"],
    ["Friday", "Yaka", "Monopoly", "Puzzle", "October", "Coconut", "Songs", "Hyena"],
    ["Wednesday", "Tuesday", "Saturday", "Hyena", "Socks", "Socks", "Tyres", "shock-absorbers"],
    ["Saturday", "Puzzle", "Python", "Balenciaga", "July", "Socks", "Butterfly", "Rain-coat"],
    ["Flowers", "Memories", "Juice", "January", "July", "Socks", "Butterfly", "Ocean"],
    ["powerGrid", "PowerGrid", "Banana", "Beetroot", "July", "Socks", "Internship", "Church"],
    ["Salon", "Socks", "saturday", "Python", "rain-coat", "Socks", "Ocean", "Bullet"],
    ["rain-water", "Toast", "juice", "left", "Right", "Wrong", "Butterfly", "Balenciaga"],
    ["Monday", "Friday", "Wednesday", "Thursday", "Saturday", "monday", "friday", "bullet"],
    ["Monday", "PowerGrid", "Cocunt", "Balenciaga", "July", "Socks", "Butterfly", "Balenciaga"],
    ["Monday", "Monopoly", "Python", "left", "rain-water", "Hyena", "Church", "Ocean"],
    ["Monday", "Thursday", "Saturday", "salon", "July", "Socks", "Elephant", "Milkshake"],
    ["Memories", "Yaka", "Dicitionaries", "Rolex", "Rainbow", "Socks", "Tyres", "October"]
]

list_of_words = [word.lower() for sublist in list for word in sublist]  
word_count = Counter(list_of_words)

print()
print(list_of_words)
print()
for word, count in word_count.items():
    print(f"'{word}': {count}")
print("\nWord Frequencies:")
print()
print(dict(word_count))
print()
sorted_word_count = dict(sorted(word_count.items()))
print("\nWord and frequency in alphabetical order")
print()
print(sorted_word_count)
print()
print("\nWords arranged in the order  they were most used")
print()
sorted_by_frequency = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_frequency)
print()
print("\nWords arranged in the order  they were least used")
print()
sorted_by_frequency = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=False))
print(sorted_by_frequency)
print()