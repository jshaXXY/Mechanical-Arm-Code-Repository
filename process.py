import servo
import airPump
import servo_angle_2
import time

file_path = "output/output.txt"
cube_list = []
with open (file_path, 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 3:
            cube_list.append([parts[0], int(parts[1]), int(parts[2])])
color = ''
for i in cube_list:
    color = i[0]

drop_servo_angle_dict = {'r':[180, 60.92, 39.35, 129.73], 'g':[135, 60.92, 39.35, 129.73], 'y':[157.5,  60.92, 39.35, 129.73]}

if (color != ''):
    servo.servo_init()
    angle1, angle2, angle3 = servo_angle_2.servo_angles(15)
    airPump.pick()
    servo.servo_angle(0, 30)
    servo.servo_angle(1, 90)
    servo.servo_angle(2, 50)
    servo.servo_angle(3, 90)
    time.sleep (1)
    servo.servo_angle(3, angle3)
    servo.servo_angle(2, angle2)
    servo.servo_angle(1, angle1)
    time.sleep(1)
    servo.servo_angle(1, angle1 - 10)
    time.sleep(1)


# drop cube
    servo.servo_angle(1, 90)
    servo.servo_angle(2, 50)
    servo.servo_angle(3, 90)
    time.sleep(1)
    servo.servo_angle(0, drop_servo_angle_dict[color][0])
    time.sleep(1)
    servo.servo_angle(1, drop_servo_angle_dict[color][1])
    servo.servo_angle(2, drop_servo_angle_dict[color][2])
    servo.servo_angle(3, drop_servo_angle_dict[color][3])
    time.sleep(2)
    airPump.drop()
