import processing.core.PApplet;

import java.io.FileReader;

public class Apple{
    private Field field;
    private int x, y;
    private int color;

    Apple(Field field, Snake snake, int color){
        this.field = field;

        //do{
            x = (int) (Math.random() * field.getWidth());
            y = (int) (Math.random() * field.getHeight());
        //}while (snake.collides(x, y));

        this.color = color;
    }

    void draw(PApplet applet){
        applet.fill(color);

        float cellSize = field.getCellSize(applet.width, applet.height);
        float screenX = field.getScreenX(cellSize, applet.width, x);
        float screenY = field.getScreenY(cellSize, applet.height, y);
        applet.rect(screenX, screenY, cellSize, cellSize);
    }

    int getX() {
        return x;
    }

    int getY() {
        return y;
    }
}