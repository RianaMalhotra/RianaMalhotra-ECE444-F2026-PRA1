class utils:

    @staticmethod
    def reversed(number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("number must be an integer")

        sign = -1 if number < 0 else 1
        number = abs(number)

        reversed_number = int(str(number)[::-1])

        return sign * reversed_number

    @staticmethod
    def formatter(number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("number must be an integer")

        return bin(number), oct(number)