#反转链表
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
    ListNode *p,*t;
int q;
//存链表节点的值
stack<int> s;
p=pHead;
//遍历链表，将链表节点的值压栈
while(p!=NULL){
s.push(p->val);
p=p->next;
}
ListNode* ret=new ListNode(0);
p=ret;
//从栈中取出节点值重新分配节点并构建新链表
while(!s.empty()){
q=s.top();
s.pop();
t=new ListNode(q);
p->next=t;
p=t;
}
return ret->next;
}
};