package Inventory;

public class Inventory {
    public static final int CRITICAL = 10;
    public static final int MIN = 0;
    public static final int MAX = 100;

    private int stockLevel;

    public Inventory() {
        stockLevel = 0;
    }

    public boolean inventoryTooLow() {
        return stockLevel < CRITICAL;
    }

    public void add(int amount) throws InventoryOverMaxException {
        if (amount < 0) {
            throw new IllegalArgumentException("Amount must be positive.");
        }

        int temp = stockLevel + amount;

        if (temp > MAX) {
            throw new InventoryOverMaxException(
                "Adding " + amount + 
                " item(s) will cause stock to become greater than " 
                + MAX + " units."
            );
        }

        stockLevel = temp;
    }

    public void remove(int amount) throws InventoryUnderMinException {
        if (amount < 0) {
            throw new IllegalArgumentException("Amount must be positive.");
        }

        int temp = stockLevel - amount;

        if (temp < MIN) {
            throw new InventoryUnderMinException(
                "Removing " + amount + 
                " item(s) will cause stock to become less than " 
                + MIN + " units (understock)."
            );
        }

        stockLevel = temp;
    }

    public int getStockLevel() {
        return stockLevel;
    }

    @Override
    public String toString() {
        return "Inventory: " + stockLevel;
    }
}
