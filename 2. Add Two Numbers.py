# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        result = ptr = ListNode(0)

        while l1 or l2 or carry:

            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next

            ptr.next = ListNode(carry%10)
            ptr = ptr.next

            
            carry = carry // 10
        
        return result.next

  #############################################
  class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 9999999
        # 9999
        # 89990001
        one = l1
        two = l2
        len_l1 = 0
        len_l2 = 0

        while one:
            len_l1 += 1
            one = one.next
        
        while two:
            len_l2 += 1
            two = two.next

        if len_l1 < len_l2:
            min_list = l1
            max_list = l2
            min_len = len_l1
            max_len = len_l2
        else:
            min_list = l2
            max_list = l1
            min_len = len_l2
            max_len = len_l1

        
        carry_over = 0
        result = ListNode(0)
        ptr = result
        computed = 0

        while computed < min_len:
            res = min_list.val + max_list.val + carry_over
            ones_digit = res%10
            carry_over = res//10
            # result.append(to_append)
            curr_node = ListNode(ones_digit)
            ptr.next = curr_node
            ptr = curr_node


            min_list = min_list.next
            max_list = max_list.next
            computed += 1
        
        while computed < max_len:
            res = max_list.val + carry_over
            ones_digit = res%10
            carry_over = res//10

            # result.append(to_append)
            curr_node = ListNode(ones_digit)
            ptr.next = curr_node
            ptr = curr_node

            max_list = max_list.next
            computed += 1
        
        if carry_over > 0:
            # result.append(carry_over)
            curr_node = ListNode(carry_over)
            ptr.next = curr_node
            curr_node.next = None
        
        # print(result)
        return result.next
