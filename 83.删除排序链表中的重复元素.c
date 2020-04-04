/*
 * @lc app=leetcode.cn id=83 lang=c
 *
 * [83] 删除排序链表中的重复元素
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    if (head)
    {
        struct ListNode * prev = head;
        struct ListNode * p = head->next;
        while (p)
        {
            if (p->val == prev->val)
            {
                prev->next = p->next;
            }
            else
            {
                prev = p;
            }
            p = p->next;
        }
    }
    return head;
}


// @lc code=end

