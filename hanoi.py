from hanoi_viz import *

TOWERS = ['tower A', 'tower B', 'tower C']


def move_tower(towers, target_tower, source_tower):
    if len(towers[target_tower]) == 1:
        return
    move_disk(source_tower, target_tower, towers)
    return move_tower(source_tower, target_tower, towers)

def main():

    disk_count = int(input('how many disks?'))
    towers = initialize_towers(disk_count,
                               TOWERS[0],
                               TOWERS[1],
                               TOWERS[2])
    #print_towers(towers)

main()
