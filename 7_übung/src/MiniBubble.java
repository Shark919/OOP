import java.awt.*;
import java.util.concurrent.ThreadLocalRandom;

public class MiniBubble implements Shape, Animation {

    double radius;
    Point center;

    Color color = new Color(1f,1f,0f,.5f );
    ShapesWorld welt;
    double velocity = 2;
    double direction = ThreadLocalRandom.current().nextDouble(360.0);

    public MiniBubble(double initX, double initY) {
        this.radius = 15;
        this.center = new Point(initX,initY);
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
        if(center.x >= welt.getMin_X() && center.x <= welt.getMax_X()
                && center.y >= welt.getMin_Y() && center.y <= welt.getMax_Y()){
            center.x += velocity * Math.sin(direction);
            center.y += velocity * Math.cos(direction);
        } else {
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
