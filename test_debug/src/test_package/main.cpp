#include <cmath>

#include "autoware_auto_planning_msgs/msg/path.hpp"
#include "autoware_auto_planning_msgs/msg/path_with_lane_id.hpp"
#include "geometry_msgs/msg/point.hpp"
#include "rclcpp/rclcpp.hpp"

int main(int argc, char const *argv[])
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("test_debug");

  autoware_auto_planning_msgs::msg::Path path;
  // path.points.;
  // generate sin path
  constexpr int N = 100;
  for (int i = 0; i < N; i++)
  {
    autoware_auto_planning_msgs::msg::PathPoint point;
    point.pose.position.x = i * 0.1;
    point.pose.position.y = std::sin(point.pose.position.x);
    point.pose.position.z = 0.0;
    path.points.emplace_back(point);

    geometry_msgs::msg::Point left_bound, right_bound;
    left_bound.x = point.pose.position.x;
    left_bound.y = point.pose.position.y + 0.5;
    left_bound.z = 0.0;
    right_bound.x = point.pose.position.x;
    right_bound.y = point.pose.position.y - 0.5;
    right_bound.z = 0.0;
    path.left_bound.emplace_back(left_bound);
    path.right_bound.emplace_back(right_bound);
  }

  RCLCPP_INFO(node->get_logger(), "path size: %d", (int)path.points.size());

  // path.left_bound
  return 0;
}
