class Node(object):

    def __init__(self, data=None, next=None):

        self.data = data

        self.next = next


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))


def rev(link):

    pre = link

    cur = link.next

    pre.next = None

    while cur:

        tmp = cur.next

        cur.next = pre

        pre = cur

        cur = tmp

    return pre


root = rev(link)

while root:


print root.data

    root = root.next

