class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""

        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate spending percentages
    spent_percentages = []
    total_spent = 0
    category_spent = []
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        category_spent.append(spent)
        total_spent += spent
    
    for spent in category_spent:
        if total_spent > 0:
            percentage = (spent / total_spent) * 100
        else:
            percentage = 0
        # Round down to nearest 10
        spent_percentages.append(int(percentage // 10 * 10))
    
    # Create chart
    chart = "Percentage spent by category\n"
    
    # Percentage labels and bars
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in spent_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # Horizontal line
    chart += "    -" + "---" * len(categories) + "\n"
    
    # Category names vertically
    max_len = max(len(category.name) for category in categories)
    
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"
    
    return chart.rstrip("\n")