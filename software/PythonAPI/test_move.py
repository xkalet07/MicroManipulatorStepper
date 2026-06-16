from numpy import random
from open_micro_stage_api import OpenMicroStageInterface

# create interface and connect
oms = OpenMicroStageInterface(show_communication=True, show_log_messages=True)

port = 'COM15'      # change for the real port
if not oms.connect(port):
    raise SystemExit(f'Could not connect to {port}.')

# run this once to calibrate joints
for i in range(3): oms.calibrate_joint(i, save_result=True)

# home device
oms.home()


# move to several x,y,z positions [mm]
for i in range (30):
    # move to random x,y,z positions [mm]
    oms.move_to(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10), f=random.uniform(10, 50))

    # wait for moves to finish
    oms.wait_for_stop()
