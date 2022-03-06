# https://leetcode.com/problems/flood-fill/
import Queue
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return image
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        rows, cols = len(image), len(image[0])
        dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        queue = Queue.Queue()
        queue.put([sr, sc])
        visit = {}
        visit[str(sr) + ',' + str(sc)] = True # visited or not
        while not queue.empty():
            sr, sc = queue.get()
            image[sr][sc] = newColor
            for dx, dy in dir: # search neighbors
                x, y = sr + dx, sc + dy
                if x >= 0 and x < rows and y >=0 and y < cols and not visit.has_key(str(x) + ',' + str(y)) and image[x][y] == oldColor:
                    queue.put([x, y])
                    visit[str(x) + ',' + str(y)] = True
        return image