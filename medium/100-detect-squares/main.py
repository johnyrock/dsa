from detect_squares import DetectSquares

squares = DetectSquares()

squares.add([3, 10])
squares.add([11, 2])
squares.add([3, 2])
print(squares.count([11, 10]))   # 1
print(squares.count([14, 8]))    # 0
squares.add([11, 2])
print(squares.count([11, 10]))   # 2
