package u8;

public class Mug {
	
	private static final int MAX_CAPACITY = 100;
	private static final int HOT_TEMPERATURE = 50;
	private Liquid liquid;
	private int capacity;
	
	public Mug(Liquid in) {
		liquid = in;
		capacity = MAX_CAPACITY;
	}

	public void pour(int ml) throws NotEnoughCapacityException {
		if (capacity + ml > MAX_CAPACITY) {
			throw new NotEnoughCapacityException(this, ml, MAX_CAPACITY);
		} else {
			capacity += ml;
		}
	}
	
	public void takeOut( int ml ) throws NotEnoughLiquidException {
		if (capacity - ml > 0) {
			throw new NotEnoughLiquidException(this, ml);
		} else {
			capacity -= ml;
		}
		
	}
	
	public void drink(int ml) throws UndrinkableException, NotEnoughLiquidException {
		if (!liquid.isDrinkable()) {
			throw new UndrinkableException(this);
		} else if (capacity - ml < 0) {
			throw new NotEnoughLiquidException(this, ml);
		} else {
			capacity -= ml;
		}
	}
	
	public int empty() {
		int to_empty = capacity;
		capacity = 0;
		return to_empty;
	}
	
	public boolean isEmpty() {
		if (capacity == 0) {
			return true;
		} else {
			return false;
		}	
	}
	
	public boolean isHot() {
		if (liquid.getTemperature() >= HOT_TEMPERATURE) {
			return true;
		} else {
			return false;
		}
	}
	
	public Liquid getLiquid() {
		return this.liquid;
	}
	
	public int getCapacity() {
		return this.capacity;
	}
	
	public int getMaxCapacity() {
		return Mug.MAX_CAPACITY;
	}
}
