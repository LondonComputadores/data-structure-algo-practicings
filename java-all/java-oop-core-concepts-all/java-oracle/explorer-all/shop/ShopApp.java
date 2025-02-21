// package shop;

public class ShopApp {
    public static void main(String[] args) {

        double tax = 0.2, total = 0.0;

        Customer c1 = new Customer();
        c1.name = "Alex";
        c1.size = "Medium";

        Clothing item1 = new Clothing();
        Clothing item2 = new Clothing();

        item1.description = "Blue Jacket";
        item1.price = 20.9;
        item1.size = "Medium";

        item2.description = "Orange T-shirt";
        item2.price = 10.5;
        item2.size = "Small";

        System.out.println("Item 1: " + item1.description + ", " + item1.price + ", " + item1.size);
        System.out.println("Item 2: " + item2.description + ", " + item2.price + ", " + item2.size);
        
        total = (item1.price + item2.price * 2) * (1 + tax);

        System.out.println("Total: " + total);

        int measurement = 3;

        switch (measurement) {
            case 1, 2, 3:
                c1.size = "Small";
                break;
            case 4, 5, 6:
                c1.size = "Medium";
                break;
            case 7, 8, 9:
                c1.size = "Large";
                break;
            default:
                c1.size = "Extra Large";    
        }
    }

}
