import java.awt.*;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Bubble implements Shape, Animation {

    double radius;
    Point center;

    Color color = new Color(1f,0f,0f,.5f );
    ShapesWorld welt;
    double velocity = 2;

    public Bubble() {
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
        this.radius += 2;

        if(radius >= Math.abs(center.x-atX) && radius >= Math.abs(center.y-atY)){
            welt.removeShape(this);
            welt.addShape(new MiniBubble(center.x, center.y));
            welt.addShape(new MiniBubble(center.x, center.y));
            welt.addShape(new MiniBubble(center.x, center.y));
            welt.addShape(new MiniBubble(center.x, center.y));
            welt.addShape(new MiniBubble(center.x, center.y));
            welt.addShape(new MiniBubble(center.x, center.y));
        }
    }

    public void userTyped(char key){
        System.out.println("key");
    }

    // implement the Animation-Interface
    public void play()
    {

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
