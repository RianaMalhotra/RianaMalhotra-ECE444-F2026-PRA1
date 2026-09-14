class utils:

    def reversed(self, number):
        if not isinstaance(number,int):
            raise TypeErro("Input must be an integer")
        return int(str(number)[::-1]) 

    def formatter(self, number):
         if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        return bin(int(number)), oct(int(number))

