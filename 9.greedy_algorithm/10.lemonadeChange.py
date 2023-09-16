class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill_dict = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                bill_dict[5]+=1
            elif bill == 10:
                bill_dict[10]+=1
                bill_dict[5]-=1
                if bill_dict[5]<0:
                    return False
            else:
                if bill_dict[5]>0 and bill_dict[10]>0:
                    bill_dict[5]-=1
                    bill_dict[10]-=1
                elif bill_dict[5]>2:
                    bill_dict[5]-=3
                else:
                    return False
        return True
