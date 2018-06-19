package u8;

import java.awt.Color;

public class TestMug {

	public static void main(String[] args) throws UndrinkableException, NotEnoughLiquidException, NotEnoughCapacityException {
		Poison ratPoison = new Poison("Rat", Color.GREEN, false);
		Coffee aLungo = new Coffee("Lungo", Color.BLACK, true);
		
		Mug poisonMug = new Mug(ratPoison);
		Mug coffeeMug = new Mug(aLungo);
		
		poisonMug.drink(10);
		coffeeMug.drink(10);
		coffeeMug.pour(1000);
		coffeeMug.drink(100);
		poisonMug.empty();
		poisonMug.takeOut(10);
		poisonMug.pour(50);
		coffeeMug.isHot();
	}

}
