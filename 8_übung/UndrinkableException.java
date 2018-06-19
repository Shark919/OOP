package u8;

class UndrinkableException extends Exception {

	public UndrinkableException (Mug mug) {
		System.err.println("It is not possible to drink from " + mug.getLiquid().getName() + " as it is not drinkable");
	}
}
