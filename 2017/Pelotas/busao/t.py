class SearchError(object): 
    def __init__(self,severity=0,message=''): 
        self.severity = severity
        self.message = message

    def __getitem__(self,val): 
        if isinstance(val,slice): 
            return [self.__getitem__(i) for i in xrange(val.start,val.stop,val.step)]
        elif val==0: 
            return self.severity
        elif val==1: 
            return self.message
        else: 
            raise IndexError

    def __len__(self):
        return 2

a = SearchError(1,"Fatal")
print(len(a))
