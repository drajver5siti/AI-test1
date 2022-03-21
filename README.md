# AI-test1
Task 1
        
        Given a grid size (self.gridSize), food represented by coordinates (self.points),
        walls given like a array of coordinates, current orientation of the pacman (N, S, W, E) and
        coordinates for the pacman (player), eat all the food from the grid
        in the least possible steps.
        The pacman can move in four directions( GoForward, GoBackwards, TurnLeft, TurnRight )
        
Task 2

        Given a row with rowLen spaces and numOfDisk disks where
        the disks are in an ascending order and start at the beginning
        of the row, take minimal amount of steps to rearrange the disks
        so they get sorted in ascending order but from the end of the row.

        Example:
            [1, 2, 3, 0, 0, 0, 0] -> [0, 0, 0, 0, 3, 2, 1]

        Possible steps for each disk are:
            D1: Disk x -> Disk x goes one space to the right if that space is free
            L1: Disk x -> Disk x goes one space to the left if that space is free
            D2: Disk x -> Disk x goes two spaces to the right if that space is free
                          and the space between the current position and next position
                          is not free ( it's not zero )
            L2: Disk x -> Disk x goes two spaces to the left if that space is free
                          and the space between the current position and the next position
                          is not free ( it's not zero).
