from amath.constants import nan


def linspace(start, stop, num=50, endpoint=True, retstep=False):
    num = int(num)
    if num < 0:
        raise ValueError("Number of samples, %s, must be non-negative." % num)
    div = (num - 1) if endpoint else num

    # Convert float/complex array scalars to float, gh-3504
    start *= 1.
    stop = stop * 1.

    y = range(0, num)

    delta = stop - start
    if num > 1:
        step = delta / div
        if step == 0:
            # Special handling for denormal numbers, gh-5437
            y /= div
            y = y * delta
        else:
            # One might be tempted to use faster, in-place multiplication here,
            # but this prevents step from overriding what class is produced,
            # and thus prevents, e.g., use of Quantities; see gh-7142.
            y = y * step
    else:
        # 0 and 1 item long sequences have an undefined step
        step = nan
        # Multiply with delta to allow possible override of output class.
        y = y * delta

    y += start

    if endpoint and num > 1:
        y[-1] = stop

    if retstep:
        return y.astype(dtype, copy=False), step
    else:
        return y.astype(dtype, copy=False)
