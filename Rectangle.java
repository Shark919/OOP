package u6;

import java.awt.print.Printable;
import java.io.ObjectInputStream.GetField;
import java.nio.file.spi.FileSystemProvider;

import javax.naming.spi.DirStateFactory.Result;
import javax.xml.crypto.dsig.keyinfo.RetrievalMethod;
import javax.xml.ws.AsyncHandler;

public class Rectangle {
	int x;
	int y;
	int width;
	int height;
	
	public Rectangle( int x, int y, int width, int height) {
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;		
	}
	
	public Rectangle() {
		this(0, 0, 10, 10);
	}
	
	public int perimeter() {
		return 2 * (width + height);
	}
	
	public int area() {
		return (width * height);
	}
	
	public Rectangle clone() {
		return new Rectangle(this.x, this.y, this.width, this.height);
	}
	
	public boolean identical (Rectangle r) {
		return r.x == this.x && r.y == this.y && r.width == this.width && r.height == this.height;
	}
	
	public int compareTo(Rectangle r) {
		int result;
		if (r.area() > this.area()) {
			result = -1;
		} else if (r.area() < this.area()) {
			result = 1;
		} else result = 0;
		return result; 
	}
	
	public boolean contains (Rectangle r) {
		Boolean result = false;
		if (r.x > this.x && r.width < this.width) {
			if (r.y > this.y && r.height < this.height) {
				result = true;
			}
		}
		return result;
	}
	
	public boolean overlaps (Rectangle r) {
		return (this.x < r.x + r.width && this.x + this.width > r.x && this.y < r.y + r.height && y + height > r.y);
	}
	//TODO
	public Rectangle section (Rectangle r) {
		if (this.overlaps(r)) {
			
			return new Rectangle();
		}else if (this.contains(r)) {
			return r;
		} else {
			return null;
		}
	}

	public static Rectangle smallestBoundingRectangle ( Rectangle[] recs ) {
		int minX = recs[0].x;
		int maxWidth = recs[0].width + recs[0].x;
		int minY = recs[0].y;
		int maxHeight = recs[0].height + recs[0].y;
		
		for (int i = 1; i < recs.length; i++) {
			if (recs[i].x < minX) {
				minX = recs[i].x;
			}
			if (recs[i].width + recs[i].x > minX + maxWidth) {
				maxWidth = recs[i].width + recs[i].x;
			}
			if (recs[i].y < minY) {
				minY = recs[i].y;
			}
			if (recs[i].height + recs[i].y > minY + maxHeight) {
				maxHeight = recs[i].height + recs[i].y;
			}
		}
		return new Rectangle(minX, minY, maxWidth, maxHeight);
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

