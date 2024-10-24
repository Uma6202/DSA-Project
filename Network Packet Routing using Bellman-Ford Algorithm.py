# Binary Search Tree Searching operation

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insert a new node
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Search for a node in the BST
def search(root, key):
    # Base case: root is null or key is present at root
    if root is None or root.val == key:
        return root
    
    # Key is greater than root's key
    if key > root.val:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# Helper function to create a BST from user input
def create_bst():
    root = None
    print("Enter the elements to insert into the BST (space-separated):")
    elements = list(map(int, input().split()))
    for elem in elements:
        root = insert(root, elem)
    return root

# Main code for search operation
if __name__ == "__main__":
    bst_root = create_bst()
    key_to_search = int(input("Enter the value to search: "))
    
    result = search(bst_root, key_to_search)
    if result:
        print(f"Value {key_to_search} found in the BST.")
    else:
        print(f"Value {key_to_search} not found in the BST.")
