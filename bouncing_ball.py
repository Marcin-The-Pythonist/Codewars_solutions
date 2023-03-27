def bouncing_ball(h, bounce, window):
    count = 0
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while True:
            if h * bounce > window:
                count += 1
                h = h * bounce
            elif h * bounce <= window:
                return count * 2 + 1
    else:
        return -1
