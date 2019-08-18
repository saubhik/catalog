package catalog.graphs.searchmaze;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SearchMazeTest {
  @org.junit.jupiter.api.Test
  void testSearchMaze() {
    List<List<SearchMaze.Color>> maze = new ArrayList<>();

    maze.add(Arrays.asList(SearchMaze.Color.BLACK, SearchMaze.Color.WHITE, SearchMaze.Color.WHITE));
    maze.add(Arrays.asList(SearchMaze.Color.BLACK, SearchMaze.Color.WHITE, SearchMaze.Color.BLACK));
    maze.add(Arrays.asList(SearchMaze.Color.WHITE, SearchMaze.Color.WHITE, SearchMaze.Color.BLACK));

    SearchMaze.Coordinate start = new SearchMaze.Coordinate(2, 0);
    SearchMaze.Coordinate end = new SearchMaze.Coordinate(0, 2);

    List<SearchMaze.Coordinate> path =
        new ArrayList<>(
            Arrays.asList(
                new SearchMaze.Coordinate(2, 0),
                new SearchMaze.Coordinate(2, 1),
                new SearchMaze.Coordinate(1, 1),
                new SearchMaze.Coordinate(0, 1),
                new SearchMaze.Coordinate(0, 2)));

    assertEquals(path, SearchMaze.searchMaze(maze, start, end));
  }
}
