import java.awt.*;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Roboter implements Shape, Animation {

    double radius;
    Point center;

    Color color = new Color(1f,0f,0f,.5f );
    ShapesWorld welt;
    double velocity = 0;
    double direction = 0;
    boolean moveForward = false;
    boolean moveBackward = false;


    public Roboter() {
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
        fillRobo(g, center.x-radius, center.y-radius, radius*2);
    }

    public void fillRobo(Graphics g, double ctrX, double ctrY, double radius){
        int x_coords[] = new int[]{(int)ctrX,(int)ctrX,(int)ctrX+100,(int)ctrX+100,(int)ctrX+120,(int)ctrX+50,(int)ctrX-20,(int)ctrX};
        int y_coords[] = new int[]{(int)ctrY,(int)ctrY+50,(int)ctrY+50,(int)ctrY,(int)ctrY-40,(int)ctrY,(int)ctrY-40,(int)ctrY};

        Polygon p = new Polygon(x_coords, y_coords, 8);
        g.fillPolygon(p);
    }

    public Point getCenter() {
        return center;
    }

    public void userClicked(double atX, double atY){

    }

    public void userTyped(char key){
        switch (key) {
            case 'w':
                this.velocity = 2;
                moveForward = !moveForward;
                moveBackward = false;
            break;
            case 'a':
                this.direction += 10;
                this.velocity = 2;
                break;
            case 's':
                this.velocity = 2;
                moveForward = false;
                moveBackward = !moveBackward;
                break;
            case 'd':
                this.direction -= 10;
                this.velocity = 2;
                break;
            case 'j':
                center.x += ThreadLocalRandom.current().nextInt(-100,100);
                center.y += ThreadLocalRandom.current().nextInt(-100,100);
                break;
            default:
                this.direction = 360;
                this.velocity = 0;
            break;
        }
    }

    // implement the Animation-Interface
    public void play()
    {
        if(center.x >= welt.getMin_X() && center.x <= welt.getMax_X()
                && center.y >= welt.getMin_Y() && center.y <= welt.getMax_Y()){
            if(moveForward){
                center.x += velocity * Math.sin(direction);
                center.y -= velocity;
            }
            if(moveBackward){
                center.x += velocity * Math.sin(direction);
                center.y += velocity;
            }
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
