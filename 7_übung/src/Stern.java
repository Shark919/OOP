import java.awt.*;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Stern implements Shape, Animation {

    double radius;
    Point center;

    Color color = Color.lightGray;
    ShapesWorld welt;
    double velocity = 2;

    public Stern() {
        this.radius = 25;
        this.color = Color.CYAN;

        Random r = new Random();
        double x = ThreadLocalRandom.current().nextDouble(-250, 250);
        double y = ThreadLocalRandom.current().nextDouble(-200, 200);
        this.center = new Point(x,y);
    }

    public Color getColor()
    { return color; }

    public void moveTo(double x, double y){
        center.x = (int) x;
        center.y = (int) y;
    }

    public void setShapesWorld( ShapesWorld theWorld )
    {
        this.welt = theWorld;
    }

    public void draw(Graphics g) {
        g.setColor(color);
        fillStar(g, center.x-radius, center.y-radius, radius*2, 8, .55);
    }

    public void fillStar(Graphics g, double ctrX, double ctrY, double radius, int numberOfSpikes, double spike){
        int np = numberOfSpikes * 2 + 1;
        int x_coords[] = new int[np];
        int y_coords[] = new int[np];
        int i = 0;
        while (i < np) {
            double degree = (i * 360.0) / (2*numberOfSpikes);

            double rad = 0.0;
            if(i % 2 == 0) {
                rad = radius;
            } else {
                rad = radius*spike;
            }
            x_coords[i] = getXCoords(ctrX, rad, degree);
            y_coords[i] = getYCoords(ctrY, rad, degree);
            i++;
        }
        Polygon p = new Polygon(x_coords, y_coords, np);
        g.fillPolygon(p);
    }
    // source for math: https://stackoverflow.com/questions/40663087/java-drawing-a-star-and-connecting-points-w-drawing-panel
    private int getXCoords(double ctrX, double rad, double angle){
        return (int) (ctrX + rad * Math.cos(Math.toRadians(angle - 90)));
    }
    // same source for math
    private int getYCoords(double ctrY, double rad, double angle){
        return (int) (ctrY + rad * Math.sin(Math.toRadians(angle - 90)));
    }

    public Point getCenter() {
        return center;
    }

    public void userClicked(double atX, double atY){
        this.radius += 2;
        this.welt.addShape(new Stern());
    }

    public void userTyped(char key){
        System.out.println("key");
    }

    // implement the Animation-Interface
    public void play()
    {
        if ( (center.y-radius)<=welt.getMax_Y() ){
            center.y = center.y + velocity;
            if(this.radius > 0) {
                this.radius = this.radius/1.025;
            }
        } else {
            radius = 0;
            welt.removeShape(this);
        }
    }

    public boolean contains(double x, double y) {
        if (x<(center.x-radius) || x>center.x+radius || y<(center.y-radius) || y>(center.y+radius))
            return false;
        else
            return true;
    }

    public double getRadius() {
        return radius;
    }
}
