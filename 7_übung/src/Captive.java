import java.awt.*;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Captive implements Shape, Animation {

    double radius;
    Point center;

    Color color = Color.lightGray;
    ShapesWorld welt;
    double velocity = 2;
    int direction = ThreadLocalRandom.current().nextInt(4);

    public Captive() {
        this.radius = 100;
        this.color = Color.CYAN;

        Random r = new Random();
        double x = ThreadLocalRandom.current().nextDouble(-150, 250);
        double y = ThreadLocalRandom.current().nextDouble(-100, 200);
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
        fillCaptive(g, center.x-radius, center.y-radius, radius*2);
    }

    public void fillCaptive(Graphics g, double ctrX, double ctrY, double radius){
        int x_coords[] = new int[]{(int)ctrX+0,(int)ctrX+50,(int)ctrX+50,(int)ctrX+100,(int)ctrX+150,(int)ctrX+0};
        int y_coords[] = new int[]{(int)ctrY+0,(int)ctrY+50,(int)ctrY+100,(int)ctrY+100,(int)ctrY+60,(int)ctrY+0};

        Polygon p = new Polygon(x_coords, y_coords, 6);
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
        this.welt.addShape(new Captive());
    }

    public void userTyped(char key){
        System.out.println("key");
    }

    // implement the Animation-Interface
    public void play()
    {
        //0 = down, 1 = up, 2 = right, 3 = left
        boolean bottomOrRightMovement = (direction == 0 || direction == 2)
                &&((center.y-radius)>=welt.getMin_Y() && (center.x-radius)>=welt.getMin_X()
                && (center.y-radius)<welt.getMax_Y() && (center.x-radius)<welt.getMax_X());

        boolean upOrLeftMovement = (direction == 1 || direction == 3)
                &&((center.y-radius)>=welt.getMin_Y() && (center.x-radius)>=welt.getMin_X()
                && (center.y-radius)<welt.getMax_Y() && (center.x-radius)<welt.getMax_X());

        if (bottomOrRightMovement){
            if(direction == 0) {
                center.y = center.y + velocity;
            } else {
                center.x = center.x + velocity;
            }
        }
        if (upOrLeftMovement) {
            if (direction == 1) {
                center.y = center.y - velocity;
            } else {
                center.x = center.x - velocity;
            }
        }
        if (direction == 0 && (center.y-radius+100)>welt.getMax_Y()) {
            changeDirection();
            center.y = welt.getMax_Y()-1;
        }
        if (direction == 1 && (center.y-radius)<welt.getMin_Y()) {
            changeDirection();
            center.y = welt.getMin_Y()+100;
        }
        if (direction == 2 && (center.x-radius+150)>welt.getMax_X()) {
            changeDirection();
            center.x = welt.getMax_X()-50;
        }
        if (direction == 3 && (center.x-radius)<welt.getMin_X()) {
            changeDirection();
            center.x = welt.getMin_X()+100;
        }
    }

    private void changeDirection() {
        direction = ThreadLocalRandom.current().nextInt(4);
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
