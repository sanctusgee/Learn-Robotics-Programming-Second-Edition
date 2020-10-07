import vpython as vp
import logging
from robot_imu import RobotImu, ComplementaryFilter
from delta_timer import DeltaTimer
import imu_settings


logging.basicConfig(level=logging.INFO)
imu = RobotImu(gyro_offsets=imu_settings.gyro_offsets)
filter = ComplementaryFilter(0.95).filter

vp.graph(xmin=0, xmax=60, scroll=True)
graph_pitch = vp.gcurve(color=vp.color.red)
graph_roll = vp.gcurve(color=vp.color.green)

pitch = 0
roll = 0

timer = DeltaTimer()


while True:
    vp.rate(100)
    dt, elapsed = timer.update()
    accel_pitch, accel_roll = imu.read_accelerometer_pitch_and_roll()
    gyro = imu.read_gyroscope()
    # By filtering 95% gyro (which changes quickly, but drifts) with the 5% accel, which is absolute, but is slow when filtered
    # We get the best of both sensors.
    pitch = filter(pitch + gyro.y * dt, accel_pitch)
    roll = filter(roll + gyro.x * dt, accel_roll)

    graph_pitch.plot(elapsed, pitch)
    graph_roll.plot(elapsed, roll)
