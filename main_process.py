import process
import transfer
file_path = "output/output.txt"

cube_list = []

with open (file_path, 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 3:
            cube_list.append([parts[0], int(parts[1]), int(parts[2])])

for cubes in cube_list:
    r, theta = transfer.transfer_r_theta(cubes[1], cubes[2])
    process.process_once(r, theta, cubes[0])
