import processing.core.PApplet;

class Field{
    private int width;
    private int height;
    private int color;

    Field(int width, int height, int color){
        this.width = width;
        this.height = height;
        this.color = color;
    }

     boolean isInside(int x, int y) {
        return  x >= 0 && x < width &&
                y >= 0 && y < height;
    }

     int getWidth() {
        return width;
    }

     int getHeight() {
        return height;
    }

     float getCellSize(int screenWidth, int screenHeight) {
        return Math.min( screenWidth / width, screenHeight / height);
    }

     float getScreenX(float cellSize, int screenWidth, int x) {
        float fieldScreenWidth = width * cellSize;
        float CenterShiftX = (screenWidth - fieldScreenWidth) / 2;
        return CenterShiftX + x * cellSize;
    }

     float getScreenY(float cellSize, int screenHeight, int y) {
        float fieldScreenHeight = height * cellSize;
        float CenterShiftY = (screenHeight - fieldScreenHeight) / 2;
        return CenterShiftY + y * cellSize;
    }

    void draw(PApplet applet){
        float cellSize = getCellSize(applet.width, applet.height);
        applet.fill(color);
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                float screenX = getScreenX(cellSize, applet.width, x);
                float screenY = getScreenY(cellSize, applet.height, y);
                applet.rect(screenX, screenY, cellSize, cellSize);
            }
        }
    }
}