import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO

from std_msgs.msg import Int32

#define variables


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(Int32, "minimal_publisher",  self.listener_callback, 10)
        self.subscription
        GPIO.setmode(GPIO.BCM)
        self.motor_pin = 18
        GPIO.setup(self.motor_pin, GPIO.OUT)
        self.motor = GPIO.PWM(self.motor_pin, 100)
        self.motor.start(0)

    
    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        self.control_motor(msg.data)

    def control_motor(self,sensor_value):
        if sensor_value < 500:
            self.motor.ChangeDutyCycle(100)
        else:
            self.motor.ChangeDutyCycle(0)
        
def main(args=None):
    rclpy.init(args=args)

    node = MinimalSubscriber()

    rclpy.spin(node)



    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
