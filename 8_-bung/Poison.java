package u8;

import java.awt.Color;

public class Poison extends Liquid {

	protected Poison(String name, Color color, boolean drinkable) {
		super(name, color, drinkable);
	}

	@Override
	public String getName() {
		return this.name;
	}

	@Override
	public Color getColor() {
		return this.color;
	}

	@Override
	public boolean isDrinkable() {	
		return this.drinkable;
	}

	@Override
	public void hitUp(int temperature) {
		this.temperature += temperature;
		
	}

	@Override
	public int getTemperature() {
		return this.temperature;
	}
}
