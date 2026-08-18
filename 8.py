class Node:

  def __init__(self, name, time, purpose):
    self.name = name
    self.time = time
    self.purpose = purpose
    self.left = None
    self.right = None


class VisitorLogBST:

  def __init__(self):
    self.root = None

  def insert(self, root, name, time, purpose):
    if root is None:
      return Node(name, time, purpose)
    if name < root.name:
      root.left = self.insert(root.left, name, time, purpose)
    else:
      root.right = self.insert(root.right, name, time, purpose)
    return root

  def search(self, root, name):
    if root is None or root.name == name:
      return root
    if name < root.name:
      return self.search(root.left, name)
    return self.search(root.right, name)

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print(
          f"Visitor: {root.name} | Time: {root.time} | Purpose: {root.purpose}"
      )
      self.inorder(root.right)

  def postorder(self, root):
    if root:
      self.postorder(root.left)
      self.postorder(root.right)
      print(
          f"Visitor: {root.name} | Time: {root.time} | Purpose: {root.purpose}"
      )

  def count_nodes(self, root):
    if root is None:
      return 0
    return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

  def min_value_node(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def delete(self, root, name):
    if root is None:
      return root
    if name < root.name:
      root.left = self.delete(root.left, name)
    elif name > root.name:
      root.right = self.delete(root.right, name)
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      temp = self.min_value_node(root.right)
      root.name = temp.name
      root.time = temp.time
      root.purpose = temp.purpose
      root.right = self.delete(root.right, temp.name)
    return root


bst = VisitorLogBST()

while True:
  print("\n--- VISITOR LOG BOOK SYSTEM (BST) ---")
  print("1. Add Visitor Entry")
  print("2. Search Visitor")
  print("3. Display All Entries (Inorder)")
  print("4. Display All Entries (Postorder)")
  print("5. Count Total Visitors")
  print("6. Delete Visitor Entry")
  print("7. Exit")

  choice = input("Enter choice (1-7): ")

  if choice == "1":
    name = input("Enter Visitor Name: ")
    time = input("Enter Entry Time (e.g., 10:30 AM): ")
    purpose = input("Enter Purpose: ")
    bst.root = bst.insert(bst.root, name, time, purpose)
    print("Entry added successfully!")

  elif choice == "2":
    name = input("Enter Visitor Name to Search: ")
    res = bst.search(bst.root, name)
    if res:
      print(
          f"\nFound! Name: {res.name}, Time: {res.time}, Purpose:"
          f" {res.purpose}"
      )
    else:
      print("\nVisitor Entry Not Found!")

  elif choice == "3":
    print("\n--- Visitors List (Inorder - Alphabetical) ---")
    bst.inorder(bst.root)

  elif choice == "4":
    print("\n--- Visitors List (Postorder) ---")
    bst.postorder(bst.root)

  elif choice == "5":
    print(f"\nTotal Log Entries: {bst.count_nodes(bst.root)}")

  elif choice == "6":
    name = input("Enter Visitor Name to Delete: ")
    bst.root = bst.delete(bst.root, name)
    print("Entry deleted if present.")

  elif choice == "7":
    print("Exiting Program.")
    break
  else:
    print("Invalid choice! Try again.")

