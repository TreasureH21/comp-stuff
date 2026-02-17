import java.util.*;

class ShoppingCart {
    class Item {
        private String itemName;
        private int quantity;
        private double price;

        Item(String itemName, int quantity, double price) {
            this.itemName = itemName;
            this.quantity = quantity;
            this.price = price;
        }

        public void displayItem() {
            System.out.println("Item: " + itemName + 
                               ", Quantity: " + quantity + 
                               ", Price: " + price);
        }

        public double getTotalPrice() {
            return quantity * price;
        }
    }

    private Item[] items;
    private int itemCount;

    ShoppingCart(int maxItems) {
        items = new Item[maxItems];
        itemCount = 0;
    }

    public void addItem(String name, int quantity, double price) {
        if (itemCount < items.length) {
            items[itemCount] = new Item(name, quantity, price);
            itemCount++;
        } else {
            System.out.println("Cannot add more items.");
        }
    }

    public void displayCart() {
        System.out.println("Shopping Cart Contents:");
        for (int i = 0; i < itemCount; i++) {
            items[i].displayItem();
        }
    }

    public double calculateTotal() {
        double total = 0;
        for (int i = 0; i < itemCount; i++) {
            total += items[i].getTotalPrice();
        }
        return total;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter maximum number of items:");
        int maxItems = sc.nextInt();
        sc.nextLine();
        ShoppingCart cart = new ShoppingCart(maxItems);

        for (int i = 0; i < maxItems; i++) {
            System.out.println("Enter item name:");
            String name = sc.nextLine();
            System.out.println("Enter quantity:");
            int quantity = sc.nextInt();
            System.out.println("Enter price per unit:");
            double price = sc.nextDouble();
            sc.nextLine(); 
            cart.addItem(name, quantity, price);
        }

        cart.displayCart();
        System.out.println("Total Price: " + cart.calculateTotal());
    }

}
