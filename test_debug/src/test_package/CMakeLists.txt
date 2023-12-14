cmake_minimum_required(VERSION 3.8)
project(test_package)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(autoware_auto_planning_msgs REQUIRED)

add_executable(test_package main.cpp)
ament_target_dependencies(test_package rclcpp autoware_auto_planning_msgs)


install(TARGETS
  test_package
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
