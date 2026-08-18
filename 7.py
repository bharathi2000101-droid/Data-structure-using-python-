class Node:

  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


def insert(root, key):
  if root is None:
    return Node(key)
  else:
    if key < root.val:
      root.left = insert(root.left, key)
    else:
      root.right = insert(root.right, key)
  return root


def inorder(root):
  if root:
    inorder(root.left)
    print(f"- {root.val}")
    inorder(root.right)


root = None

n = int(input("Enter number of books: "))

for i in range(n):
  book_title = input(f"Enter title of book {i+1}: ")
  root = insert(root, book_title)

print("\n--- Inorder Traversal (Sorted Book Titles) ---")
inorder(root)
