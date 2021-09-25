class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
def create_link_list(nums):
    ptr_head = ListNode(nums[0])
    ptr = ptr_head
    for x in range(1, len(nums)):
        n = ListNode(nums[x])
        ptr.next = n
        ptr = ptr.next
    return ptr_head

def reverseList(head):
    ptr = head
    mylist = []
    while ptr:
        mylist.insert(0, ptr.val)
        ptr = ptr.next
        
    ptr = head
    for data in mylist:
        ptr.val = data
        ptr = ptr.next
    return head

def removeElements(head, val):
    new_ptr = ptr = ListNode[0]
    ptr.next = head
    while head:
        if head.val == val:
            ptr.next = head.next
        else:
            ptr = head.next
        head = head.next
    return new_ptr.next
    
data = create_link_list([1, 2, 3, 4, 5])
data1 = create_link_list([2, 3, 4])

for i in data and data1:
    print(i.val)
    