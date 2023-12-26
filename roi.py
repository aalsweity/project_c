class ROI:
    
    def questions(self):
        total_income = self.total_income()
        total_expenses = self.expenses()
        cash_flow = total_income-total_expenses
        annual_cash_flow = cash_flow * 12
        roi_percent_value = self.roi_calc(annual_cash_flow)
        print(f"Your ROI perecentage is {roi_percent_value:.2f}%")

    
    def total_income(self):
        global rent_inc
        
        rent_inc = int(input("What is your rental incomme? "))
        
        laundry_inc_q = input("Do you have any Laundry Income? Yes/No ").lower()
        while laundry_inc_q not in {"yes", "no"}:
            laundry_inc_q = input("Invalid Answer. Please say Yes or No only. ").lower()
        if laundry_inc_q == "yes":
            laundry_inc = int(input("What is your Laundry Income? "))
        else:
            laundry_inc = 0
        storage_inc_q = input("Do you have any Storage Income? Yes/No? ").lower()
        while storage_inc_q not in {"yes", "no"}:
            storage_inc_q = input("Invalid Answer. Please say Yes or No only. ").lower()
        if storage_inc_q == "yes":
            storage_inc = int(input("What is your Laundry Income? "))
        else:
            storage_inc = 0
        misc_inc_q = input("Do you have any Misc. Income? Yes/No ").lower()
        while misc_inc_q not in {"yes", "no"}:
            misc_inc_q = input("Invalid Answer. Please say Yes or No only. ").lower()
        if misc_inc_q == "yes":
            misc_inc = int(input("What is your Laundry Income? "))
        else:
            misc_inc = 0
        
        total_income = rent_inc + laundry_inc + storage_inc + misc_inc
        return total_income
    
    def expenses(self):
        taxes = int(input("How much tax do you pay? "))
        insurance = int(input("How much insurance do you pay? "))
        utility_q = input("Do you pay the utility bill? Yes/No?").lower()
        while utility_q not in {"yes", "no"}:
            utility_q = input("Invalid Answer. Please say Yes or No only. ").lower()
        if utility_q == "yes":
            utility = int(input("What is the utility bill? "))
        else:
            utility = 0
            
        hoa_q = input("Do you have to pay an HOA fee? Yes/No? ").lower()
        while hoa_q not in {"yes","no"}:
            hoa_q = input("Invalid Answer. Please say Yes or No only. ").lower()
        if hoa_q == "yes":
            hoa = int(input("What is the HOA fee? ")) 
        else:
            hoa = 0
                
        vaccancy = rent_inc * 0.05
        
        repairs = int(input("How much does repairs cost? "))
        
        prop_mang_q = input("Do you have a Property Manager? Yes/No? ").lower()
        while prop_mang_q not in {"yes","no"}:
            prop_mang_q = input("Invalid Answer. Please say Yes or No only. ").lower()
        if prop_mang_q == "yes":
            prop_man = int(input("How much do you pay the Property manager? ")) 
        else:
            prop_man = 0
        
        global mortgage_q
        mortgage_q = int(input("How much is your Mortgage Loan? "))
        mortgage = mortgage_q * (0.05/12*(1+0.05/12)**360)/(((1+0.05/12)**360)-1)
        
        total_expenses = mortgage + prop_man + repairs + vaccancy + utility + insurance + taxes +hoa
        print(total_expenses)
        
        return total_expenses
    
    def roi_calc(self, annual_cash_flow):
        down_payment_q = int(input("What was the total cost of the property? "))
        down_payment = down_payment_q * 0.2
        closing_costs = int(input("How much was the closing cost? "))
        rehab = int(input("How much was Rehab cost for the building? "))
        total_investment = down_payment + closing_costs + rehab
        
        roi_percentage = (annual_cash_flow/total_investment)*100
        
        return roi_percentage
        
    
    
person1 = ROI()
person1.questions()