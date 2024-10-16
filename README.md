# GreyHeron

## Requirements:

### Product Class (Abstract Class):

- Define an abstract class Product that includes the following:
- Private attributes for product name and price (use encapsulation).
- Abstract methods get_name() and get_price(), which subclasses must implement.

### Product Types (Inheritance):

- Create at least three subclasses of Product:
- Electronics: A product category for electronic items.
- Groceries: A product category for grocery items.
- Clothing: A product category for clothing items.
- Each subclass should implement get_name() and get_price().
- Ensure product price is protected (encapsulated) and accessible only through methods.

### Customer Class:

- Create a Customer class that stores the customer's name and shopping cart (a list of products).
- The shopping cart can hold any type of product.

### Customer Types (Polymorphism):

- Create two types of customers:
- RegularCustomer: A regular customer who pays full price for products.
- VIPCustomer: A customer who gets a discount (e.g., 10%) on the total price.
- Both customer types should implement a get_discounted_price() method:
- This method should take a list of products and return the total price.
- For VIPCustomer, apply a discount on the total.

### Add Products to Cart:

- Allow customers to add different types of products to their shopping cart.
- Calculate Total Price (Polymorphism):
- Create a method that calculates the total price of all items in the cart for both RegularCustomer and VIPCustomer.
- Use polymorphism so that the method works the same way for both types of customers, but the behavior changes (e.g., discount applied for VIP customers).

## Goals:

- Demonstrate inheritance by creating specialized product types and customer types.
- Use an abstract class to enforce the presence of methods in product types.
- Encapsulate sensitive data like product prices and ensure it's only accessible through controlled methods.
- Implement polymorphism so that different types of products and customers can be processed through common methods.
