from collections import defaultdict
from datetime import datetime

class UserController:
    def calculate_profit_loss(self):
        # Get current month and year
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year

        # Initialize profit/loss data
        profit_loss_data = {
            'last_12_months': [],
            'months_data': defaultdict(lambda: {'total_income': None, 'total_expenses': None, 'profit_loss': None})
        }

        # Get all payment data
        all_payment_data = self.get_all_payment_data()

        # Iterate over payment data to calculate profit/loss for each month
        for payment_data in all_payment_data:
            payment_date = datetime.fromisoformat(payment_data['payment_date'])
            payment_month = payment_date.month
            payment_year = payment_date.year

            # Include payments from the last 12 months, including previous years
            if (current_year == payment_year and current_month >= payment_month) or \
               (current_year - 1 == payment_year and current_month < payment_month):
                month_year = payment_date.strftime("%B %Y")
                if month_year not in profit_loss_data['last_12_months']:
                    profit_loss_data['last_12_months'].append(month_year)
                
                if profit_loss_data['months_data'][month_year]['total_income'] is None:
                    profit_loss_data['months_data'][month_year] = {'total_income': 0, 'total_expenses': 0}
                
                profit_loss_data['months_data'][month_year]['total_income'] += payment_data['amount']
                # Assuming expenses are not available in the given payment data, you need to add logic to calculate expenses
        
        # Calculate profit/loss for each month
        for month_year, data in profit_loss_data['months_data'].items():
            if data['total_income'] is not None:
                # Assuming expenses are not available, you need to calculate them before calculating profit/loss
                total_expenses = 0  # You need to calculate expenses here
                profit_loss_data['months_data'][month_year]['total_expenses'] = total_expenses
                profit_loss_data['months_data'][month_year]['profit_loss'] = round(data['total_income'] - total_expenses, 2)
        
        return profit_loss_data
