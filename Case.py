class Case:

    def __init__(self,x = 0,y = 0,val = 1):
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.val = val
        self.hasMerged = False

    def can_merge(self,other):
        if (isinstance(other,Case)):
            return not(self.hasMerged) and not(other.hasMerged) and self.val == other.val and self.val != 1
        return False

    
