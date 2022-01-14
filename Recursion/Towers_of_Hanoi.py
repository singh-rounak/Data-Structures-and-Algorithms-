def Hanoi(disk, source, middle, destination):
    if disk == 1:
        print("disk %s from %s to %s" % (disk, source, destination))
        return

    Hanoi(disk-1, source, destination, middle)
    print("disk %s from %s to %s" % (disk, source, destination))

    Hanoi(disk-1, middle, source, destination)


print(Hanoi(3, 'A', 'B', 'C'))

"""
Out - 
disk 1 from A to C
disk 2 from A to B
disk 1 from C to B
disk 3 from A to C
disk 1 from B to A
disk 2 from B to C
disk 1 from A to C
"""
