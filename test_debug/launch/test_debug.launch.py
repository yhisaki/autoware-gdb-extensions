from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="test_package",
                namespace="test_package",
                executable="test_package",
                name="test_package",
            )
        ]
    )
