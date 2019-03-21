class Node(object):

	"""节点"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node


class Single_List(object):
    def __init__(self):
        self.head = None

    def append_item(self, item):
        if self.head is None:
            self.head = Node(item)
            return 
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(item)

    def remove_item(self, item):
        index = self.index(item)
        if index:
            self.remove_by_index(index)

    def remove_by_index(self, index):
        num = self.size()
        p = self.head
        if p == None or index>num - 1:
            return False
        if index == 0:
            p = p.next
            self.head = p
            return True

        while index:
            pre = p
            p = p.next
            index -= 1
        pre.set_next(p.next)

    def add_item(self, item, index):
        if index<0:
            return
        node = Node(item)
        if index == 0:
            node.set_next(self.head)
            self.head = node
            return True
        p = self.head
        # num = self.size()
        # if index>num-1:
        #     print('out of list')
        #     return False
        while index:
            pre = p
            p = p.next
            if p == None and index>=1:
                return 
            index -= 1

        pre.set_next(node)
        pre.next.next = p

    def size(self):
        p, size = self.head, 0
        while p is not None:
            size += 1
            p = p.next
        return size

    def get_item(self, index):
        p, i = self.head, index
        num = self.size()

        while i:
            if p is None:
                print('out')
                return None
            p = p.next
            i -= 1
        return p.data if p is not None else None

    def index(self, item):
        p, n= self.head, 0
        while p is not None:
            if p.data == item:
                return n
            p = p.next
            n += 1
        return None

    def __str__(self):
        num = self.size()
        print('size=', num)
        res = str([self.get_item(i) for i in range(num)])
        return res


link_list = Single_List()
link_list.append_item('a1')
link_list.append_item('a2')
link_list.append_item('a3')
link_list.append_item('a4')
link_list.append_item('a5')
link_list.add_item('add1',-1)
print(link_list)
k = link_list.index('a5')
print("index==",k)
link_list.remove_by_index(33)
link_list.remove_item(1)
print(link_list)



