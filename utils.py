class utils:

    def reversed(self, number):
        return int(str(number)[::-1]) 

    def formatter(self, number):
        return bin(int(number)), oct(int(number))
