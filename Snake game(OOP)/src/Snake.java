import processing.core.PApplet;

import java.awt.*;
import java.util.ArrayList;

class Snake{

    private ArrayList<Point> body;
    private int head;
    private Field field;
    private boolean isDead;
    private int dx, dy;
    private int color;

    Snake(Field field, int color){
        this.field = field;

        int x = 8;
        int y = 20;
        dx = 1;
        dy = 0;

        body = new ArrayList<>();
        body.add(new Point(x, y));
        head = 0;

        this.color = color;
        isDead = false;
    }

    private int getX() {
        return body.get(head).x;
    }

    private void setX(int x) {
        body.get(head).x = x;
    }

    private int getY() {
        return body.get(head).y;
    }

    private void setY(int y) {
        body.get(head).y = y;
    }

    void turnUp(){
        if(body.size() > 1) {
            if (dy != 1) {
                dx = 0;
                dy = -1;
            }
        }else{
            dx = 0;
            dy = -1;
        }
    }

    void turnDown(){
        if(body.size() > 1) {
            if (dy != -1) {
                dx = 0;
                dy = 1;
            }
        }else{
            dx = 0;
            dy = 1;
        }
    }

    void turnRight(){
        if(body.size() > 1) {
            if (dx != -1) {
                dx = 1;
                dy = 0;
            }
        }else{
            dx = 1;
            dy = 0;
        }
    }

    void turnLeft(){
        if(body.size() > 1) {
            if (dx != 1) {
                dx = -1;
                dy = 0;
            }
        }else{
            dx = -1;
            dy = 0;
        }
    }

    /*boolean collides(int nextX, int nextY) {
        for (Point bodyPart: body) {
            if(bodyPart.x == nextX || bodyPart.y == nextY){
                return true;
            }
        }
        return false;
    }*/

    boolean headCollides(Apple apple) {
        return getX() == apple.getX() && getY() == apple.getY();
    }

    boolean headCollidesWithBody(){
        if(body.size() > 1) {
            for (int i = 1; i < body.size(); ++i) {
                if (getX() == body.get(i).x && getY() == body.get(i).y) return true;
            }
        }
        return false;
    }

    boolean isDead(){
        return isDead;
    }

    void move(){

        if(isDead) return;
        int nextX = getX() + dx;
        int nextY = getY() + dy;
        head = (head + 1) % body.size();

        if(!field.isInside(nextX, nextY)){
            isDead = true;
        }
        /*if(headCollidesWithBody()){
            isDead = true;
        }*/
        else{
            setX(nextX);
            setY(nextY);
        }

    }

    void grow(){
        body.add(head + 1, new Point(getX(), getY())); move();
    }
    void draw(PApplet applet){
        applet.fill(isDead ? 0xff000000 : color);
        float cellSize = field.getCellSize(applet.width, applet.height);
        for (Point bodyPart: body) {
            float screenX = field.getScreenX(cellSize, applet.width, bodyPart.x);
            float screenY = field.getScreenY(cellSize, applet.height, bodyPart.y);
            applet.rect(screenX, screenY, cellSize, cellSize);
        }
    }
}