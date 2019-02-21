from hanoi_viz import *

TOWERS = ['A', 'B', 'C']
SOURCE_TOWER = TOWERS[0]
TARGET_TOWER = TOWERS[1]
MID_TOWER = TOWERS[2]


def move_tower(disk_count, towers, target, source, mid):
    # when disk_count is 1, we are at bottom disk.
    # recursion unwinds when disk_count is 0
    if disk_count > 0:
        # moves disk_count - 1 disks from source
        # this will get us to the bottom/last disk at source
        print('top', disk_count)
        move_tower(disk_count - 1, towers, mid, source, target)
        # move a disk from source to target
        move_disk(source, target, towers)
        # move disk from mid to target
        print('bottom', disk_count)
        move_tower(disk_count - 1, towers, target, mid, source)



def main():
    while True:
        disk_count = input('how many disks? ')
        if disk_count.isdigit():
            disk_count = int(disk_count)
            if disk_count >= 1 and disk_count <= 8:
                break

    towers = initialize_towers(disk_count,
                               TOWERS[0],
                               TOWERS[1],
                               TOWERS[2])
    move_tower(disk_count,
               towers,
               TARGET_TOWER,
               SOURCE_TOWER,
               MID_TOWER
               )

main()
