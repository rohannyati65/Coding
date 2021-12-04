# zig-zag challenge
import math


def next_int(n):
    """Returns nearest larger integer value. If n is integer, it return n+1."""
    if int(n) == n:
        return int(n + 1)

    return int(math.ceil(n))


def prev_int(n):
    """Returns nearest smaller integer value. If n is integer, it return n-1."""
    if int(n) == n:
        return int(n - 1)

    return int(math.floor(n))


def get_ranges(h1, s1, h2, s2):
    """Returns periods, when two trees are not equal.
    Parameters: initial height and growth speed of two trees.
    Returns: tuple of tuples of three elements: string of "<" or ">" representing
    the relation of the trees in that period, then two ints - first and last point
    in time of the period. If trees are always equal tuple will be empty, if they
    are never equal - there will be only one period, if they growth trajectories
    intersect - the will be two periods.
    If upper bound of a period is infinity - then second int is -1."""

    infinity = float("inf")

    if h1 == h2 and s1 == s2:
        return tuple()

    if h1 == h2:
        return (("<" if s1 < s2 else ">", 1, infinity),)

    initial_relation = "<" if h1 < h2 else ">"

    if s1 == s2:
        return ((initial_relation, 0, infinity),)

    intersect = (h2 - h1) / (s1 - s2)

    if intersect < 0:
        return ((initial_relation, 0, infinity),)

    reversed_relation = ">" if initial_relation == "<" else "<"

    return (
        (initial_relation, 0, prev_int(intersect)),
        (reversed_relation, next_int(intersect), infinity),
    )


def intersect_ranges(range1, range2):
    """Return range which is intersection of two ranges.
    Parameters: two ranges with two values - lower and upper limits (both are included in the range).
    Returns: range which is an intersection of both, None if the do not intersect."""
    if range1[0] > range2[1] or range2[0] > range1[1]:
        return None

    return (max(range1[0], range2[0]), min(range1[1], range2[1]))


def merge_adjacent_ranges(ranges):
    if len(ranges) == 0:
        return []

    temp = [
        list(ranges[0]),
    ]
    for i in range(1, len(ranges)):
        if temp[-1][1] + 1 == ranges[i][0]:
            temp[-1][1] = ranges[i][1]
        else:
            temp.append(ranges[i])

    return temp


def get_zig_zag_ranges(ranges1, ranges2):
    """Return ranges, when trees are in zig-zag pattern.
    Parameters: inequality ranges between first and second and second and third trees.
    Both ranges are expected with 0-2 ranges, non-intersecting, alternating in their
    relation.
    Returns: tuple with tuples with two values each: first and last point in time
    when trees are in zig-zag pattern."""

    if len(ranges1) == 0 or len(ranges2) == 0:
        return tuple()

    result = []

    for r1 in ranges1:
        for r2 in ranges2:
            if r1[0] != r2[0]:
                intersection = intersect_ranges((r1[1], r1[2]), (r2[1], r2[2]))
                if intersection:
                    result.append(intersection)

    return tuple(result)


def read_and_run_test():
    tree_count = int(input())
    trees = list()
    for i in range(tree_count):
        trees.append([int(v) for v in input().split()])

    if tree_count == 1:
        print("1\n0 Inf")
        # print( "0" )
        return

    infinity = float("inf")
    prev_ranges = get_ranges(trees[0][0], trees[0][1], trees[1][0], trees[1][1])
    results = [(s, e) for r, s, e in prev_ranges]

    for i in range(2, tree_count):
        curr_ranges = get_ranges(
            trees[i - 1][0], trees[i - 1][1], trees[i][0], trees[i][1]
        )
        new_results = []

        for new_range in get_zig_zag_ranges(prev_ranges, curr_ranges):
            for existing_range in results:
                intersection = intersect_ranges(new_range, existing_range)
                if intersection:
                    new_results.append(intersection)

        results = new_results
        prev_ranges = curr_ranges

    results = merge_adjacent_ranges(results)

    print(len(results))
    for r in results:
        if r[1] == infinity:
            print(int(r[0]), "Inf")
        else:
            print(int(r[0]), int(r[1]))


def main():
    test_cases_count = int(input())
    for i in range(test_cases_count):
        read_and_run_test()


main()
