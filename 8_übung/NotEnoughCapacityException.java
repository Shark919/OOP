package u8;

class NotEnoughCapacityException extends Exception {

	public NotEnoughCapacityException(Mug mug, int ml, int maxCapacity) {
		System.err.println("It is not possible to add " + ml + "ml to " + mug.getLiquid().getName() +
				" as it contains already " + mug.getCapacity() + "ml and has a maximum capacity of " +
				mug.getMaxCapacity() + "ml!");
	}
}