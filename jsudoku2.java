import java.util.Random;

class Sudoku {
    public static void main(String[] args) {
        int[][] s = new int[9][9];
        fillBoard(s);
        print2D(s);
    }

    public static void fillBoard(int[][] s) {
        int x = 0;
        int y = 0;
        Random random = new Random();
        while (true) {
            // try the next value for the cell
            s[x][y] += 1;
            while (s[x][y] <= 9) {
                if (validCell(s, s[x][y], x, y)) {
                    if (x == 8 && y == 8) {
                        System.out.println("Puzzle filled");
                        return s;
                    }
                    // move to next cell
                    x += 1;
                    if (x > 8) {
                        y += 1;
                        x = 0;
                        if (y > 8) {
                            System.out.println("Failed to generate puzzle (y > 8)");
                            return;
                        }
                    }
                    break;
                } else {
                    s[x][y] += 1;
                }
            }
            // if there's no valid number go back one cell
            if (s[x][y] > 9) {
                s[x][y] = 0;
                x -= 1;
                if (x < 0) {
                    y -= 1;
                    x = 8;
                    if (y < 0) {
                        System.out.println("All iterations complete");
                        return;
                    }
                }
            }
        }
    }

    public static boolean validCell(int[][] s, int n, int x, int y) {
        // 0 is invalid
        if (n == 0) {
            return false;
        }
        // check row
        for (int xx = 0; xx < 9; xx++) {
            if (xx != x && s[xx][y] == n) {
                return false;
            }
        }
        // check column
        for (int yy = 0; yy < 9; yy++) {
            if (yy != y && s[x][yy] == n) {
                return false;
            }
        }
        // check square
        for (int xs = x / 3 * 3; xs < x / 3 * 3 + 3; xs++) {
            for (int ys = y / 3 * 3; ys < y / 3 * 3 + 3; ys++) {
                if (!(xs == x && ys == y) && s[xs][ys] == n)

    public static void print2D(int mat[][]) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }
}