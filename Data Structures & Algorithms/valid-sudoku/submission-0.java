class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Set<Character>> rows_check = new HashMap<> ();
        HashMap<Integer, Set<Character>> cols_check = new HashMap<> ();
        HashMap<List<Integer>, Set<Character>> sub_box_check = new HashMap<> ();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;

                List<Integer> sub_box = List.of(i/3, j/3);
                if (rows_check.computeIfAbsent(j, k -> new HashSet<>()).contains(board[i][j]) ||
                    cols_check.computeIfAbsent(i, k -> new HashSet<>()).contains(board[i][j]) ||
                    sub_box_check.computeIfAbsent(sub_box, k -> new HashSet<>()).contains(board[i][j])
                ) {
                    return false;
                }

                rows_check.get(j).add(board[i][j]);
                cols_check.get(i).add(board[i][j]);
                sub_box_check.get(sub_box).add(board[i][j]);
            }
        }
        return true;
    }
}
