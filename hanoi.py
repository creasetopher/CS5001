from hanoi_viz import *

TOWERS = ['A', 'B', 'C']
SOURCE_TOWER = TOWERS[0]
TARGET_TOWER = TOWERS[1]
MID_TOWER = TOWERS[2]
MAX_HEIGHT = 8
MIN_HEIGHT = 0


def move_tower(disk, towers, target, source, mid, disk_count):
    if disk == disk_count:
        move_disk(source, target, towers)
        return
    disk += 1
    # move disk_count - 1 disks to mid
    # mid is now target and target is now mid
    move_tower(disk, towers, mid, source, target, disk_count)
    print('called move_tower on target =', mid, 'and mid = ', target )
    print('move from', source, 'to', target)
    input('')
    move_disk(source, target, towers)

    move_tower(disk, towers, target, mid, source, disk_count)


def main():
    disk = 0
    disk_count = int(input('how many disks?'))
    recursive_thresh = (2 * disk_count) - 1
    towers = initialize_towers(disk_count,
                               TOWERS[0],
                               TOWERS[1],
                               TOWERS[2])
    move_tower(disk,
               towers,
               TARGET_TOWER,
               SOURCE_TOWER,
               MID_TOWER,
               disk_count)


        # print('tar:', TARGET_TOWER[-1], 'src:', SOURCE_TOWER)
    # else:
        # print('tar:', TARGET_TOWER[-1], 'src:', MID_TOWER)

    #print('test123')

main()
