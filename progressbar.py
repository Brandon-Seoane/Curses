class ProgressBar():
    """
    Simple ProgressBar
    33% [#############                               ] 33/100
    """
    def __init__(self,max:int,desc:str = ""):
        self.__max:int = max
        self.__current = 0
        self.__desc:str = desc

    def update(self,amount:int):
        self.__current += amount
        if self.__current > self.__max: self.__current=self.__max

        precent =  round(self.__current/self.__max*100)
        full = round(precent*1/2)
        empty = 50-full
        return f"{self.__desc} " +f"{precent}%" + f" [{'':#>{full}}" + f"{'':.>{empty}}] " + f"{self.__current}/{self.__max}"

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        del self

