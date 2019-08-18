package catalog.graphs.searchmaze;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a 2D array of black and white entries representing a maze with designated entrance and exit
 * points, find a path from the entrance to the exit, if one exists, through only white pixels.
 */
public class SearchMaze {
  public static class Coordinate {
    public int x, y;

    public Coordinate(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
      if (this == obj) {
        return true;
      }
      if (!(obj instanceof Coordinate)) {
        return false;
      }
      Coordinate that = (Coordinate) obj;
      return this.x == that.x && this.y == that.y;
    }
  }

  public enum Color {
    WHITE,
    BLACK
  };

  public static List<Coordinate> searchMaze(
      List<List<Color>> maze, Coordinate start, Coordinate end) {
    List<Coordinate> path = new ArrayList<>();
    maze.get(start.x).set(start.y, Color.BLACK);
    path.add(start);
    if (!searchMazeHelper(maze, start, end, path)) {
      path.remove(path.size() - 1);
    }
    return path;
  }

  private static boolean searchMazeHelper(
      List<List<Color>> maze, Coordinate start, Coordinate end, List<Coordinate> path) {
    if (start.equals(end)) {
      return true;
    }
    final int[][] SHIFT = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (int[] shift : SHIFT) {
      Coordinate next = new Coordinate(start.x + shift[0], start.y + shift[1]);
      if (isFeasible(maze, next)) {
        maze.get(next.x).set(next.y, Color.BLACK);
        path.add(next);
        if (searchMazeHelper(maze, next, end, path)) return true;
        else path.remove(path.size() - 1);
      }
    }
    return false;
  }

  private static boolean isFeasible(List<List<Color>> maze, Coordinate point) {
    return 0 <= point.x
        && point.x < maze.size()
        && 0 <= point.y
        && point.y < maze.get(point.x).size()
        && maze.get(point.x).get(point.y) == Color.WHITE;
  }
}
