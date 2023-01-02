class sudoku2 {
    public static void main(String[] args) {
        int[][] s = new int[9][9];
        makePuzzle(s);
        hidePuzzle(s);
        // game loop
        // game loop
        printPuzzle(s);
    }
    public static void makePuzzle(int s[][]) {    
        int x = 0;
        int y = 0;
        while (true) {
            // try the next value for the cell
            s[x][y] += 1;
            while (s[x][y] <= 9) {
                if (validCell(s, s[x][y], x, y)) {
                    if (x == 8 && y == 8) {
                        System.out.println("Puzzle generated successfully.");
                        return;
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

    // hide certain pieces from full puzzle board
    public static int[][] hidePuzzle(int s[][]){
        return s;
    }

    // fill in one cell as play selects
    public static int[][] fillPuzzle(int s[][], int n, int x, int y){
        return s;
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
                if (!(xs == x && ys == y) && s[xs][ys] == n) {
                    return false;
                }
            }
        }

        return true;
    }

    public static void printPuzzle(int mat[][]) {
        System.out.println("Full Puzzle Board:");
        System.out.println("  A B C D E F G H I");
        for (int i = 0; i < 9; i++) {
            System.out.print((char)(65+i) + " ");
            for (int j = 0; j < 9; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }

}
