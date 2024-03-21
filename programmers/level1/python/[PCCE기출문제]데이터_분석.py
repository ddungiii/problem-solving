def filter(data, ext, val_ext):
    ext_cand = ["code", "date", "maximum", "remain"]
    index = ext_cand.index(ext)

    return [d for d in data if d[index] < val_ext]


def sort(data, sort_by):
    ext_cand = ["code", "date", "maximum", "remain"]
    index = ext_cand.index(sort_by)

    data.sort(key=lambda x: x[index])


def solution(data, ext, val_ext, sort_by):
    # 1. filter
    data = filter(data, ext, val_ext)

    # 2. sort
    sort(data, sort_by)

    return data
