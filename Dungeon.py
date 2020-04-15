class MapGrid:

    def __init__(self, width, height):
        self.width = width
        self.height = height


def drawGrid(mapGrid, width=1):
    for x in range(mapGrid.height):
        for y in range(mapGrid.width):
            print("%%-%ds" % width % '.', end="")
        print()

def main():
    g = MapGrid(30,15)
    drawGrid(g)

if __name__ == "__main__":
    main()
