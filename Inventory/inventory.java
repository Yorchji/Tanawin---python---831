package inventory;

public class Inventory {
    public static final int CRITICAL = 10;
    public static final int MIN = 0;
    public static final int MAX = 100;
    private int stockLevel;

    public Inventory() {
        stockLevel = 0;
    }

    public boolean inventoryTooLow() {
        if (stockLevel < CRITICAL)
            return true;
        else
            return false;
    }

    public void add(int amount) throws InventoryOverMaxException {
        int temp;
        temp = stockLevel + amount;
        if (temp > MAX) {
            InventoryOverMaxException anException = new
                    InventoryOverMaxException
                    ("Adding" + amount + "item will cause stock to become greater" + "than" + MAX + "units");
            throw anException;
        } else {
            stockLevel = temp;
        }
    } //end of method add

    public void remove(int amount) throws InventoryUnderMinException {
        int temp;
        temp = stockLevel - amount;
        if (temp < MIN) {
            throw new InventoryUnderMinException
                    ("Removing" + amount + "item will cause stock to become less than" + MIN + "units(understock)");
        } else {
            stockLevel = temp;
        }
    } //end of method remove

    public String toString() {
        return ("Inventory: " + stockLevel);
    }

    public int getStockLevel()
    {
        return stockLevel;
    }
} //end of class Inventory