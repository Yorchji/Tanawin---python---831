package inventory;

public class TestInventory {
    public static void main(String[] args) {
        Inventory inv = new Inventory();
        try {
            // ใส่ค่าเกิน MAX (MAX = 100)
            inv.add(150);
        } catch (InventoryOverMaxException e) {
            System.out.println("Exception caught: " + e.getMessage());
        }
    }
}
 