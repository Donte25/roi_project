def calculator(property_cost):
     property_cost = int(input("What is the buying cost of your property?"))
     print(property_cost)

def income(rental_income,extra_income, misc_income):
      rental_income = int(input("What is your rental income"))
      extra_income = int(input("Do you have any other income? If none, enter 0 to proceed."))
      misc_income = int(input("Enter any other income"))
      total_income = {rental_income} + {extra_income} + {misc_income}
      print(total_income)

def expenses(rental_income,tax,insurance,utilities,hoa,lawn,vacancy,repairs,capex,property_manage,mortgage):
    tax = int(input("What is the cost of taxes?"))
    insurance = int(input("What is the cost of insurance?"))
    utilities = int(input("What is the cost of utilities?"))
    hoa = int(input("What is the HOA cost?"))
    lawn = int(input("What is the cost of maintaining the lawn?"))
    vacancy = (5 * {rental_income}) / 100
    repairs = 100
    capex = 100
    property_manage = (10 * {rental_income}) / 100
    mortgage = int(input("What is your estimated mortgage?"))
    total_expenses = {tax} + {insurance} + {utilities} + {hoa} + {lawn} + {vacancy} + repairs + capex + {property_manage} + {mortgage}
    print(total_expenses)

def cash_flow(total_expenses, total_income):
    net = total_income - total_expenses
    print(net)
        
def investment(property_cost,down_payment,closing_cost,rehab_budget,misc_investmet):
    down_payment = (20 * {property_cost}) /100
    closing_cost = int(input("Estimated Closing Cost?"))
    rehab_budget = int(input("What is your rehab budget?"))
    misc_investmet = int(input("Any other investment income?"))
    total_investment = {down_payment} + {closing_cost} + {rehab_budget} + {misc_investmet}
    print(total_investment)

def ROI(total_investment,net):
    annual_net = (net * 12)
    roi = (annual_net / total_investment) * 100
    print(roi)
