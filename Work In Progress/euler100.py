for t in range(5800000, 5900000):
    for b in range(t//2, int(0.8 * t)):
        if (b**2 - b) == (t**2 - t)/2:
            r = t - b
            print(f"r = {r}, b = {b}, t = {t}, b/t = {b/t}")
