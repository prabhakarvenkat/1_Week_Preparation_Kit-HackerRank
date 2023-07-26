

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(headA, headB):
    if headA == None:
        return headB
    if headB == None:
        return headA
    
    if headA.data <= headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
    
    current = head
    while headA != None or headB != None:
        if headA == None:
            current.next = headB
            break
        if headB == None:
            current.next = headA
            break
        if headA.data <= headB.data:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next
    return head

    

