# write a python scrip using class to reverce a string world by world
class rev:
    def __init__(self,str1) -> None:
        self.str1=str1
    
    def rev(self):
        reve=self.str1.split()
        reve_words=reve[::-1]
        reve_text=' '.join(reve_words)
        return reve_text
    
a=rev("asdf fdgh rtyhg")
print(a.rev())