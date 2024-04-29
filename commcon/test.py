"""
@File    :   test.py   
@Modify Time      
@Author       wujie 
2024/4/28 14:04      
# >>>TODO 
"""


class A(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        pass


a = A()
# a.m1(1) # self: <__main__.A object at 0x000001E596E41A90>
# A.m2(1) # cls: <class '__main__.A'>
# A.m3(1)