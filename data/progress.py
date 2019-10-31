def spinning_cursor():
    while 1:
        for cursor in '|/-\\':
            yield cursor


cursor = spinning_cursor()


def progress_bar(index, total, steps):
    per = round((index + 1) / total * 100, 2)
    bar = int(per / 100 * steps)
    print("\r Progress: | {0}{1} | {2:0.2f}% {3}".format(
        "■" * bar, "□" * (steps - bar), per, next(cursor)), end="")
