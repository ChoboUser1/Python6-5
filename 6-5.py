#두 점 사이의 거리
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

dist = distance(x1, y1, x2, y2)
print(f"({x1},{y1})과 ({x2},{y2}) 사이의 거리는 {dist}")
