import processing.core.PApplet;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;

enum State{
    Title,
    Speed,
    Game,
    Result
}
public class Main extends PApplet {
    private int speed = 1;
    private int score = 0;
    private int bestResult = 0;
    private boolean best = false;
    private State currentState = State.Title;
    private int FIELD_COLOR = 0xffe0e0e0;
    private int APPLE_COLOR = 0xfffc5050;
    private int SNAKE_COLOR = 0xfff20404;
    private Field field;
    private Apple apple;
    private Snake snake;
    public void settings() {
        fullScreen();
    }

    public void setup() {}

    private void initializeGame(){
        field = new Field(40, 40, FIELD_COLOR);
        apple = new Apple(field, snake, APPLE_COLOR);
        snake = new Snake(field, SNAKE_COLOR);
    }

    public void draw() {
        switch (currentState){
            case Title:
                drawTitle();
                break;
            case Speed:
                drawSpeedSelection();
                break;
            case Game:
                drawGame();
                break;
            case Result:
                drawResults();
                break;

        }
    }

    private void drawTitle(){
        final int MARGIN = 100;
        final int TEXT_SIZE = 50;

        background(0);

        textAlign(CENTER, CENTER);
        textSize(TEXT_SIZE);

        fill(255, 0, 0);
        text("Super Snake", width / 2.0f, MARGIN);

        fill(255, 0, 0);
        text("Created by Dmitrii\nCopied by Malik", width / 2.0f, height / 2.0f);

        fill(0, 255, 0);
        text("Please ENTER to continue", width / 2.0f, height - MARGIN);
    }

    private void drawSpeedSelection(){
        final int MARGIN = 100;
        final int TEXT_SIZE = 50;

        background(0);

        textAlign(CENTER, CENTER);
        textSize(TEXT_SIZE);

        fill(255, 0, 0);
        text("Choose Speed", width / 2.0f, MARGIN);

        fill(255, 255, 255);
        text(speed, width / 2.0f, height / 2);

        fill(0, 255, 0);
        text("Please ENTER to continue", width / 2.0f, height - MARGIN);
    }

    private void drawGame(){
        background(0);

        snake.move();

        if(snake.isDead()){
            currentState = State.Result;
        }

        if(snake.headCollides(apple)) {
            ++score;
            if(bestResult < score) {
                best = true;
                bestResult = score;
            }

            snake.grow();
            apple = new Apple(field, snake, APPLE_COLOR);
        }

        field.draw(this);
        apple.draw(this);
        snake.draw(this);

        delay(100 - (speed * 10));
    }

    /*String getCompliment(){
        HashMap<Integer, String> compliment = new HashMap<>();
        compliment.put(1, "Great, Great, Great!");
        compliment.put(2, "Good Result!");
        compliment.put(3, "I believe, You can do more!");
        compliment.put(4, "Not bad!");
        compliment.put(5, "GooodLike!");

        return compliment.get(1 + (int) (Math.random() * compliment.size()));
    }*/

    private void drawResults(){
        final int MARGIN = 100;
        final int TEXT_SIZE = 50;



        background(0);

        textAlign(CENTER, CENTER);
        textSize(TEXT_SIZE);

        fill(255, 0, 0);
        text("Your result", width / 2.0f, MARGIN);

        fill(72, 6, 94);
        if(best) {
            text("Not bad!", width / 2.0f, height / 2.0f);
        }else{
            text("You can do more!", width / 2.0f, height / 2.0f);
        }

        fill(0, 255, 0);
        text("Please ENTER to continue", width / 2.0f, height - MARGIN);
    }

    public void keyPressed(){
        switch (currentState){
            case Title:
                keyPressedInTitle();
                break;
            case Speed:
                keyPressedInSpeedSelection();
                break;
            case Game:
                keyPressedInGame();
                break;
            case Result:
                keyPressedInResults();
                break;

        }
    }

    private void keyPressedInTitle(){
        if(keyCode == ENTER)
            currentState = State.Speed;
    }

    private void keyPressedInSpeedSelection(){


            if(keyCode == UP && speed != 10)
                speed += 1;
            else if(keyCode == DOWN && speed != 1)
                speed -= 1;
            else if(keyCode == ENTER) {
                initializeGame();
                currentState = State.Game;
            }
    }


    private void keyPressedInGame(){
        switch (keyCode){
            case UP:
                snake.turnUp();
                break;
            case DOWN:
                snake.turnDown();
                break;
            case LEFT:
                snake.turnLeft();
                break;
            case RIGHT:
                snake.turnRight();
                break;
        }
    }

    private void keyPressedInResults(){
        if(keyCode == ENTER)
            currentState = State.Speed;
    }

    public static void main(String... args) {
        PApplet.main("Main");
    }
}