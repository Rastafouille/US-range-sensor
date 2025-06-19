import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from gpiozero import DistanceSensor
from time import sleep

class UltrasonicNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_node')

        # Capteur GPIO : TRIG = GPIO23, ECHO = GPIO24
        self.sensor = DistanceSensor(echo=24, trigger=23, max_distance=4.0)

        self.publisher_ = self.create_publisher(Range, 'ultrasonic_range', 10)
        self.timer = self.create_timer(0.2, self.publish_distance)  # 5 Hz

        self.frame_id = 'ultrasonic_frame'  # Nom de la frame TF
        self.get_logger().info("Ultrasonic node started")

    def publish_distance(self):
        distance_m = self.sensor.distance  # valeur en mètres (float)

        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id

        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = 0.26  # ~15°
        msg.min_range = 0.02
        msg.max_range = 4.0
        msg.range = distance_m

        self.publisher_.publish(msg)
        self.get_logger().debug(f"Distance: {distance_m:.2f} m")

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
if __name__ == '__main__':
    main()
