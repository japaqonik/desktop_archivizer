import os


def iter(iterable, prefix='', suffix='', decimals=1, fill='█', printEnd="\r"):

    total = len(iterable)

    def get_progressbar_length():
        return os.get_terminal_size().columns - len(prefix) - len(suffix) - 12

    def print_progress_bar(iteration):
        barlength = get_progressbar_length()
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(barlength * iteration // total)
        bar = fill * filledLength + '-' * (barlength - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)

    print_progress_bar(0)

    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)

    print()