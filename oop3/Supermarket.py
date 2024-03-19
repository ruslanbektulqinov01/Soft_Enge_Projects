class SupermarketSalesAnalyzer:
    def __init__(self, quantity_array, price_array, sales_array):
        self.quantity_array = quantity_array
        self.price_array = price_array
        self.sales_array = sales_array

    def analyze_sales(self):
        total_sales = sum(qty * price for qty, price in zip(self.quantity_array, self.price_array))
        remaining_quantity = list(qty - sales for qty, sales in zip(self.quantity_array, self.sales_array))
        return total_sales, remaining_quantity


if __name__ == "__main__":
    quantity_array = [10, 25, 35]
    price_array = [2, 3, 4]
    sales_array = [9, 20, 32]
    analyzer = SupermarketSalesAnalyzer(quantity_array, price_array, sales_array)
    total_sales, remaining_quantity = analyzer.analyze_sales()
    print("Total sales:", total_sales)
    for remaining in remaining_quantity:
        print("Remaining quantity:", remaining)
