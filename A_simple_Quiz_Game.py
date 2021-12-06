class Node:
    def __init__(self,q):
        self.q=q
        self.right=None
        self.left=None
        
    def n(self):
      node=self
      s=0
      while node!=None:
          print(node.q)
          s1=input('answer=')
          s2=input('T/F?')
          if s2=='T':
              node=node.left
              print(t)
              s+=1
              print('s=',s)
          else:
               node=node.right
               print('s=',s)
          if node==None:
               print('-----------------Finish-----------------')
              

q1='q1:2+2='
q2='q2:2-2='
q3='q3:2/2='
q4='q4:2**2='
q5='q5:2*2='
q6='q6:2e2='



node1=Node(q1)
node2=Node(q2)
node3=Node(q3)
node4=Node(q4)
node5=Node(q5)
node6=Node(q6)
node7=Node(q5)

node1.left=node2
node1.right=node3
node2.left=node4
t='stop'
node2.right=node5
node3.left=node5
node4.left=node7
node4.right=node6
node5.left=node6
node1.n()
