import java.awt.*;
import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class KidnapperBubble implements Shape, Animation {

    double radius;
    Point center;

    Color color = Color.gray;
    ShapesWorld welt;
    double velocity = 2;
    double direction = ThreadLocalRandom.current().nextDouble(360.0);
    ArrayList<Shape> jail = new ArrayList<Shape>(100);

    public KidnapperBubble() {
        this.radius = 25;

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
        fillBubble(g, center.x-radius, center.y-radius, radius*2);
    }

    public void fillBubble(Graphics g, double ctrX, double ctrY, double radius){
        g.fillOval( (int)ctrX, (int)ctrY, (int)radius, (int)radius);
    }

    public Point getCenter() {
        return center;
    }

    public void userClicked(double atX, double atY){
        if(radius >= Math.abs(center.x-atX) && radius >= Math.abs(center.y-atY)){
            welt.removeShape(this);
        }
    }

    public void userTyped(char key){
        System.out.println("key");
    }

    // implement the Animation-Interface
    public void play()
    {
        Shape clostestShape = welt.getClosestShape(this);
        if(clostestShape != null){
            if(jail.contains(clostestShape)) {
                /* Normalerweise würde man an dieser Stelle die Welt abfragen, welche weiteren
                Objekte in der Nähe sind. Da die Welt jedoch keine Schnittstelle außer getClosestShape
                bietet und die bestehenden Klassen nicht angepasst werden dürfen, gibt es für das Objekt
                keine Möglichkeit, weitere Objekte in der Nähe "aufzunehmen"
                */
            }
            if(contains(clostestShape.getCenter().x, clostestShape.getCenter().y)){
                clostestShape.moveTo(center.x, center.y);
                jail.add(clostestShape);
            }
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
