import random

hashtags = []

class Node:
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.count = 1
        self.next = None

head = None

n = int(input("Enter number of posts: "))

for i in range(n):
    hashtag = input("Enter hashtag: ").lower()

    current = head
    found = False

    while current:
        if current.hashtag == hashtag:
            current.count += 1
            found = True
            break
        current = current.next

    if not found:
        new_node = Node(hashtag)
        new_node.next = head
        head = new_node

current = head
trending = head

print("===== HASHTAG TREND ANALYZER =====\n")
print("Analyzed Posts:", n, "\n")

while current:
    print(current.hashtag, "->", current.count)

    if current.count > trending.count:
        trending = current

    current = current.next

if trending:
    print("\nMost Trending Hashtag:", trending.hashtag)
    print("Trend Count:", trending.count)
