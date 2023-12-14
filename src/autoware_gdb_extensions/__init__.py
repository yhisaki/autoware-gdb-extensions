import gdb
import matplotlib.pyplot as plt

print("Loading autoware_gdb_extensions")


def plot_autoware_path(val):
    plot_path_point_vector(val["points"])
    plot_point_vector(val["left_bound"])
    plot_point_vector(val["right_bound"])


def plot_autoware_path_with_lane_id(val):
    plot_path_point_with_lane_id_vector(val["points"])
    plot_point_vector(val["left_bound"])
    plot_point_vector(val["right_bound"])


def plot_path_point_vector(val):
    start_ptr = val["_M_impl"]["_M_start"]
    end_ptr = val["_M_impl"]["_M_finish"]
    length = int(end_ptr - start_ptr)
    x, y = [], []
    for i in range(length):
        ptr = start_ptr + i
        path_point = ptr.dereference()
        x.append(float(path_point["pose"]["position"]["x"]))
        y.append(float(path_point["pose"]["position"]["y"]))

    plt.plot(x, y, ".-")


def plot_point_vector(val):
    # vector_size: int = eval(str(gdb.parse_and_eval(f"{val_name}.size()")))
    start_ptr = val["_M_impl"]["_M_start"]
    end_ptr = val["_M_impl"]["_M_finish"]
    length = int(end_ptr - start_ptr)
    x, y = [], []
    for i in range(length):
        ptr = start_ptr + i
        point = ptr.dereference()
        x.append(float(point["x"]))
        y.append(float(point["y"]))

    plt.plot(x, y, ".-")


def plot_path_point_with_lane_id_vector(val):
    start_ptr = val["_M_impl"]["_M_start"]
    end_ptr = val["_M_impl"]["_M_finish"]
    length = int(end_ptr - start_ptr)
    x, y = [], []
    for i in range(length):
        ptr = start_ptr + i
        path_point = ptr.dereference()
        x.append(float(path_point["point"]["pose"]["position"]["x"]))
        y.append(float(path_point["point"]["pose"]["position"]["y"]))

    plt.plot(x, y, ".-")


def plot_odometry(val):
    x = float(val["pose"]["pose"]["position"]["x"])
    y = float(val["pose"]["pose"]["position"]["y"])
    # x_vel = float(val["twist"]["twist"]["linear"]["y"])
    # y_vel = float(val["twist"]["twist"]["linear"]["x"])
    plt.plot(x, y, "o")
    # plt.quiver(x, y, x_vel, y_vel)


class GDBPlot(gdb.Command):
    def __init__(self):
        super(GDBPlot, self).__init__("plot", gdb.COMMAND_OBSCURE)
        print("Loading GDBPlot")

    def invoke(self, arg: str, from_tty: bool):
        args = arg.split()

        for arg in args:
            val: gdb.Value = gdb.parse_and_eval(arg)

            if val.type.name.find("std::vector<geometry_msgs::msg::Point>") != -1:
                plot_point_vector(val)
            elif (
                val.type.name.find("autoware_auto_planning_msgs::msg::PathWithLaneId")
                != -1
            ):
                plot_autoware_path_with_lane_id(val)
            elif val.type.name.find("autoware_auto_planning_msgs::msg::Path") != -1:
                plot_autoware_path(val)
            elif val.type.name.find("nav_msgs::msg::Odometry") != -1:
                plot_odometry(val)

            else:
                print(f"No plot function for {val.type.name}")

        plt.axis("equal")
        plt.show()


GDBPlot()
