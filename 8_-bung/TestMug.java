package u8;

import java.awt.Color;

public class TestMug {

	public static void main(String[] args) {
		Poison ratPoison = new Poison("Rat", Color.GREEN, false);
		Coffee aLungo = new Coffee("Lungo", Color.BLACK, true);
		
		Mug poisonMug = new Mug(ratPoison);
		Mug coffeeMug = new Mug(aLungo);
		
		
	}

}
