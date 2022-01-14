def Hanoi(disk, source, M, destination):
    # Base Case: if the smallest disk
    if disk == 1:
        print("disk %s from %s to %s" % (disk, source, destination))
        return

    Hanoi(disk-1, source, destination, M)
    print("disk %s from %s to %s" % (disk, source, destination))

    Hanoi(disk-1, M, source, destination)


print(Hanoi(3, 'A', 'B', 'C'))
