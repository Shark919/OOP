import org.omg.CosNaming._BindingIteratorImplBase;

/**
 * 
 * @author Christop Meise, Tim Walz
 * @version 1.0
 * OOP Tutorium Freitag 08-10:00 Uhr
 *
 */

public class Rectangle {
	int x;
	int y;
	int width;
	int height;
	
	/**
	 * Constructor. As defined by exercise.
	 * @param x defines x value of rectangle
	 * @param y defines y value of rectangle
	 * @param width defines width value of rectangle
	 * @param height defines height value of rectangle
	 */
	public Rectangle( int x, int y, int width, int height) {
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;		
	}

	/**
	 * Constructor. As defined by exercise.
	 * Creates Rectangles with the following values (x=0, y=0, width=10, height=10)
	 */
	public Rectangle() {
		this(0, 0, 10, 10);
	}
	
	/**
	 * As defined on lecture slides.
	 * @return perimeter of calling rectangle
	 */
	public int perimeter() {
		return 2 * (width + height);
	}
	
	/**
	 * As defined on lecture slides.
	 * @return area of calling rectangle
	 */
	public int area() {
		return (width * height);
	}
	
	//  Ein zweites identisches Rectangle-Objekt wird erstellt 
	public Rectangle clone() {
		return new Rectangle(this.x, this.y, this.width, this.height);
	}
	
	/**
	 * Ein Rectangle-Objekt vergleicht alle seine Instanzvariablen mit den Instanzvariablen eines zweiten Rectangle-Objekts
	 * @param r
	 * @return true | false
	 */
	public boolean identical (Rectangle r) {
		return r.x == this.x && r.y == this.y && r.width == this.width && r.height == this.height;
	}
	
	/**
	 * Ein Rectangle-Objekt vergleicht seine Fläche mit der Fläche eines zweiten Rectangle-Objekts
	 * @param r
	 * @return -1, 0, 1
	 */
	public int compareTo(Rectangle r) {
		int result;
		if (r.area() > this.area()) {
			result = -1;
		} else if (r.area() < this.area()) {
			result = 1;
		} else result = 0;
		return result; 
	}
	
	/**
	 * Testet, ob ein Rectangle r komplett in dem Rectangle-Objekt, das gerade die Methode ausführt, beinhaltet ist
	 * @param r
	 * @return true | false 
	 */
	public boolean contains (Rectangle r) {
		Boolean result = false;
		if (r.x > this.x && r.width < this.width) {
			if (r.y > this.y && r.height < this.height) {
				result = true;
			}
		}
		return result;
	}
	
	/**
	 * Ein Rechtecks-Objekt überprüft, ob eine Überlappung mit dem Rechteck r existiert
	 * @param r
	 * @return true | false
	 */
	public boolean overlaps (Rectangle r) {
		Boolean result = false;
		if (r.x + r.width > this.x && r.x < this.x + this.width) {
			if (r.y + r.height > this.y && r.y < this.y + this.height) {
				result = true;
			}
		}
		return result;
	}

	public Rectangle section (Rectangle r) {
		
		if (this.overlaps(r)) {
			System.out.println("1");
			return new Rectangle();
		} else {
			System.out.println("3");
			return null;
		}
	}
	
	/**
	 * Berechnet das kleinste Rectangle-Objekt, das ein Array von Rectangle-Objekten umrahmen kann.
	 * @param recs
	 * @return Rectangle
	 */
	public static Rectangle smallestBoundingRectangle ( Rectangle[] recs ) {
		int minX = recs[0].x;
		int minY = recs[0].y;
		int maxWidth = recs[0].width + recs[0].x;
		int maxHeight = recs[0].height + recs[0].y;
		
		for (Rectangle r : recs) {
			if (r.x < minX) {
				minX = r.x;
			}
			if (r.y < minY) {
				minY = r.y;
			}
			if (maxWidth < r.width + r.x) {
				maxWidth = r.width + r.x;
			}
			if (maxHeight < r.height + r.y) {
				maxHeight = r.height + r.y;
			}
		}
		return new Rectangle(minX, minY, maxWidth-minX, maxHeight-minY);
	}
	
	public int getX() {
		return this.x;
	}
	public void setX(int x) {
		this.x = x;
	}
	public int getY() {
		return this.y;
	}
	public void setY(int y) {
		this.y = y;
	}
	public int getWidth() {
		return this.width;
	}
	public void setWidth(int width) {
		this.width = width;
	}
	public int getHeight() {
		return this.height;
	}
	public void setHeight(int height) {
		this.height = height;
	}
 }

