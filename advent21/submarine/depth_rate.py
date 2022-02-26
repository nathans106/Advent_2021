def depth_rate(depths):
    prev = None
    count = 0
    for depth in depths:
        if prev and prev < depth:
            count += 1

        prev = depth

    return count


def sliding_depth_rate(depths):
    slides = [0] * 3
    prev = None
    count = 0

    for i, depth in enumerate(depths):
        slides[0] += depth

        if i >= 1:
            slides[1] += depth
        if i >= 2:
            slides[2] += depth
            mod = (i+1) % 3

            if prev and slides[mod] > prev:
                count += 1

            prev = slides[mod]
            slides[mod] = 0

    return count
