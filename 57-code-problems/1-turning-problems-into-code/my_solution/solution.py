"""
    ToDo: 

    - Create a simple tip calculator. The program should prompt
    for a bill amount and a tip rate input. The program must calculate
    the tip and then print both the tip and the total amount of
    the bill
    
    Requirements:

    - bill amount
    - tip rate
    - tip
    - total amount

    Parameters:

    :param input_bill_amount
    :type input_bill_amount: float
    :param input_tip_rate
    :type input_tip_rate: int
    :param calculate_tip
    :type calculate_tip: float
    :param calculate_total_bill
    :type calculate_total_bill: float
    :param print(calculate_tip)
    :param print(calculate_total_bill)

"""
class MyOwnSolution:    
    # bill_amount = input("Enter the bill amount: ")
    # tip_rate = input("Enter the tip rate: ")

    def __init__(self, tip_rate: int, bill_amount: float):
        self.calculate_tip = bill_amount * tip_rate / 100
        self.calculate_total_bill = bill_amount + self.calculate_tip

    def tip(self):
        return f"{f'${self.calculate_tip:0.2f}'}"

    def total_bill(self):
        return f"{f'${self.calculate_total_bill:0.2f}'}"

if __name__ == '__main__':
    computation = MyOwnSolution(10, 350.00)
    print(computation.tip())
    print(computation.total_bill())
