def Hanoi(disk, source, middle, destination):
    if disk == 1:
        print("disk %s from %s to %s" % (disk, source, destination))
        return

    Hanoi(disk-1, source, destination, middle)
    print("disk %s from %s to %s" % (disk, source, destination))

    Hanoi(disk-1, middle, source, destination)


print(Hanoi(3, 'A', 'B', 'C'))
