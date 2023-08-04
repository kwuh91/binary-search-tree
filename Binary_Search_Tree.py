class Node:
    # constructor
    def __init__(self, key: int = None) -> None:
        self.__val = key
        self.__left = None
        self.__right = None

    # insert method
    def insert(self, key: int) -> None:
        if not self.__val:
            self.__val = key
            return

        if self.__val == key:
            return

        if key < self.__val:
            if self.__left:
                Node.insert(self.__left, key)
                # self.__left.insert(key)
                return
            self.__left = Node(key)
            return

        if key > self.__val:
            if self.__right:
                Node.insert(self.__right, key)
                # self.__right.insert(key)
                return
            self.__right = Node(key)
            return

    # min
    def min(self) -> int:
        curr = self
        while curr.__left is not None:
            curr = curr.__left
        return curr.__val

    # max
    def max(self) -> int:
        curr = self
        while curr.__right is not None:
            curr = curr.__right
        return curr.__val

    # delete
    def delete(self, val: int):
        # base case
        if self is None:
            return self

        # recursively reach one of three cases
        if self.__val > val:
            self.__left = Node.delete(self.__left, val)
            return self
        elif self.__val < val:
            self.__right = Node.delete(self.__right, val)
            return self

        # case 1 (leaf node)
        # case 2 (one child)
        if self.__left is None:
            temp = self.__right
            del self
            return temp
        elif self.__right is None:
            temp = self.__left
            del self
            return temp

        # case 3 (both children)
        else:
            currParent = self
            curr = self.__right
            while curr.__left is not None:
                currParent = curr
                curr = curr.__left
            if currParent == self:
                currParent.__right = curr.__right
            else:
                currParent.__left = curr.__right
            self.__val = curr.__val
            del curr
            return self

    # exists
    def exists(self, val: int) -> bool:
        if val == self.__val:
            return True

        if val > self.__val:
            if self.__right is None:
                return False
            return Node.exists(self.__right, val)

        elif val < self.__val:
            if self.__left is None:
                return False
            return Node.exists(self.__left, val)

    # inorder
    def inorder(self) -> None:
        if self:
            Node.inorder(self.__left)
            print(self.__val, end=" ")
            Node.inorder(self.__right)

    # preorder
    def preorder(self) -> None:
        if self:
            print(self.__val, end=" ")
            Node.preorder(self.__left)
            Node.preorder(self.__right)

    # postorder
    def postorder(self) -> None:
        if self:
            Node.postorder(self.__left)
            Node.postorder(self.__right)
            print(self.__val, end=" ")


if __name__ == '__main__':
    #         100
    #       /     \
    #      20     200
    #     /  \    /  \
    #   10   30 150  300
    arr = [100, 20, 30, 10, 200, 150, 300]
    root = Node()
    for i in arr:
        Node.insert(root, i)

    print(f"inorder traversal = ", end="")
    root.inorder()
    print(f"\npreorder traversal = ", end="")
    root.preorder()
    print(f"\npostorder traversal = ", end="")
    root.postorder()

    print(f"\n\ndeleting 10")
    #         100
    #       /     \
    #      20     200
    #        \    /  \
    #        30 150  300
    root.delete(10)
    print(f"inorder traversal = ", end="")
    root.inorder()
    print(f"\npreorder traversal = ", end="")
    root.preorder()
    print(f"\npostorder traversal = ", end="")
    root.postorder()

    print(f"\n\ndeleting 100")
    #         150
    #       /     \
    #      20     200
    #        \       \
    #        30      300
    root.delete(100)
    print(f"inorder traversal = ", end="")
    root.inorder()
    print(f"\npreorder traversal = ", end="")
    root.preorder()
    print(f"\npostorder traversal = ", end="")
    root.postorder()

    print(f"\n\ndeleting 20")
    #         150
    #       /     \
    #      30     200
    #                \
    #                300
    root.delete(20)
    print(f"inorder traversal = ", end="")
    root.inorder()
    print(f"\npreorder traversal = ", end="")
    root.preorder()
    print(f"\npostorder traversal = ", end="")
    root.postorder()

    print(f"\n\nmax = {root.max()}")
    print(f"min = {root.min()}")
    print(f"30 exists in a tree = {root.exists(30)}")
    print(f"31 exists in a tree = {root.exists(31)}")
P