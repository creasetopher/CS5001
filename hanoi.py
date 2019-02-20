from hanoi_viz import *

TOWERS = ['tower A', 'tower B', 'tower C']
SOURCE_TOWER = TOWERS[0]
TARGET_TOWER = TOWERS[1]
MID_TOWER = TOWERS[2]
MAX_HEIGHT = 8
MIN_HEIGHT = 0

def move_tower(towers, target_tower, source_tower, mid_tower, cnt, disk_count):
    if cnt == (2**disk_count) - 1:
        return
    if len(towers[target_tower][cnt]) < len(source_tower[0]):
        move_disk(source_tower, target_tower, towers)
        #print(towers[target_tower], towers[source_tower])
        #return
    else:
        move_disk(source_tower, target_tower, towers)
    move_tower(towers, target_tower, source_tower, mid_tower, cnt+1, disk_count)

def main():
    cnt = 0
    disk_count = int(input('how many disks?'))
    towers = initialize_towers(disk_count,
                               TOWERS[0],
                               TOWERS[1],
                               TOWERS[2])
    move_tower(towers, TARGET_TOWER, SOURCE_TOWER, MID_TOWER, cnt, disk_count)


        # print('tar:', TARGET_TOWER[-1], 'src:', SOURCE_TOWER)
    # else:
        # print('tar:', TARGET_TOWER[-1], 'src:', MID_TOWER)

    #print_towers(towers)

main()
