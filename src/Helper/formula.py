class Formula:
    @staticmethod
    def triangular_accumulate(number, value):
        """
        Triangular accumulation function.
        
        Updates 'number' using a triangular-number-based growth formula:
            n_new = ((value + number) * (value + number - 1)) // 2 + number

        Args:
            number (int): The current number (e.g., focus.data.number)
            value (int): The input increment value

        Returns:
            int: The updated number
        """
        return ((value + number) * (value + number - 1)) // 2 + number