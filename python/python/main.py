import sys

import numpy as np

from gui import Animation
from d_star_lite import DStarLite

OBSTACLE = 255
UNOCCUPIED = 0
np.set_printoptions(threshold=sys.maxsize)

if __name__ == '__main__':

    """
    set initial values for the map occupancy grid
    |----------> y, column
    |           (x=0,y=2)
    |
    V (x=2, y=0)
    x, row
    """
    x_dim = 100
    y_dim = 80
    start = (10, 10)
    goal = (40, 70)
    view_range = 5

    gui = Animation(title="D* Lite Path Planning",
                    width=10,
                    height=10,
                    margin=0,
                    x_dim=x_dim,
                    y_dim=y_dim,
                    start=start,
                    goal=goal,
                    viewing_range=view_range)

    new_map = gui.world
    old_map = new_map

    new_position = start
    last_position = start

    # new_observation = None
    # type = OBSTACLE

    # D* Lite (optimized)
    dstar = DStarLite(map=new_map,
                      s_start=start,
                      s_goal=goal)

    # move and compute path
    path, g, rhs = dstar.move_and_replan(robot_position=new_position)

    while not gui.done:
        # update the map
        # drive gui
        gui.run_game(path=path)

        new_position = gui.current

        if new_position != last_position:
            last_position = new_position

            path, g, rhs = dstar.move_and_replan(robot_position=new_position)
