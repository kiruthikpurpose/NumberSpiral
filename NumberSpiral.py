def print_spiral(n):
    spiral = [[0] * n for _ in range(n)]
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    num = 1
    
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            spiral[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            spiral[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral[i][left] = num
                num += 1
            left += 1

    for row in spiral:
        print(" ".join(f"{x:02d}" for x in row))

def main():
    n = 5
    print_spiral(n)

if __name__ == "__main__":
    main()
