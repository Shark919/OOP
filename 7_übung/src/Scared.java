import java.awt.*;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Scared implements Shape, Animation {

    double radius;
    Point center;

    Color color = new Color(1f,1f,0f);
    ShapesWorld welt;
    double velocity = 2;
    boolean moved = false;

    public Scared() {
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

    }

    public void userTyped(char key){
        System.out.println("key");
    }

    // implement the Animation-Interface
    public void play()
    {
        Shape clostestShape = welt.getClosestShape(this);
        if(clostestShape != null){
            if (!contains(clostestShape.getCenter().x, clostestShape.getCenter().y)
                    && Math.abs(clostestShape.getCenter().x - center.x) <= 50
                    && Math.abs(clostestShape.getCenter().y - center.y) <= 50){
                if(moved){
                    this.center.x += 3;
                    this.center.y += 3;
                } else{
                    this.center.x -= 3;
                    this.center.y -= 3;
                }
                moved = !moved;
            } else {
                if(contains(clostestShape.getCenter().x, clostestShape.getCenter().y)){
                    double x = ThreadLocalRandom.current().nextDouble(-250, 250);
                    double y = ThreadLocalRandom.current().nextDouble(-200, 200);
                    this.moveTo(x, y);
                    if(contains(clostestShape.getCenter().x, clostestShape.getCenter().y)) {
                        welt.removeShape(this);
                        welt.addShape(new Stern());
                        welt.addShape(new Stern());
                        welt.addShape(new Stern());
                        welt.addShape(new Stern());
                    }
                }
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
