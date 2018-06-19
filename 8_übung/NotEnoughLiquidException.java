package u8;

class NotEnoughLiquidException extends Exception {

	public NotEnoughLiquidException(Mug mug, int ml) {
		System.err.println("You cannot remove " + ml + "ml from " + mug.getLiquid().getName() + 
				" as it contains just " + mug.getCapacity() + "ml!");
	}
}
