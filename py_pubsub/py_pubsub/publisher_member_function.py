import rclpy
from rclpy.node import Node #imported so we can use nodes

from std_msgs.msg import String #this is the data structure the node passes to the topic
#!Ros2 dependencies need to be added to package.xml!

class MinimalPublisher(Node):
    #subclass of node
    def __init__(self):
        super().__init__('minimal_publisher')#calls node's class's constructure and give it your node name
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)#publish to terminal
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
