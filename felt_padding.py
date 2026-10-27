import flet as ft


def main(page: ft.Page):

    # 设置程序窗口的标题
    page.title = "Padding 与 Margin 演示"

    # 设置整个页面的内边距为 20
    # 这里的 page.padding 指页面内容与页面边缘之间的距离
    # 注意：这是页面的内边距，不是下面 Container 的内边距
    page.padding = 20

    # 设置页面背景颜色为白色
    # 使用十六进制颜色值，避免部分 Flet 版本的颜色名称不兼容问题
    page.bgcolor = "#FFFFFF"



    # 创建一个 Container（容器）组件，并将其赋值给变量 padding_box
    padding_box = ft.Container(

        # content 表示容器内部要显示的内容
        # 这里放入一个 Text（文本）组件
        content=ft.Text(
            "Padding：内边距",  # 设置文本内容
            size=18,            # 设置文字大小为 18
            color="#FFFFFF"     # 设置文字颜色为白色
        ),

        # bgcolor 表示容器的背景颜色
        # 这里设置为蓝色，方便观察容器的边界
        bgcolor="#2196F3",

        # padding 表示容器的内边距
        # 设置为 30，表示容器内部的内容与容器边缘之间留出空间
        # 可以理解为：给文字周围留出更多空间
        padding=30,

        # border_radius 表示容器边框的圆角半径
        # 设置为 8，让蓝色容器的四个角变得圆润
        border_radius=8
    )


    # ==================== 三、创建 Margin 演示区域 ====================

    # 创建另一个 Container 组件
    # 这个容器主要用于演示 Margin（外边距）的作用
    margin_box = ft.Container(

        # 设置容器内部显示的文本
        content=ft.Text(
            "Margin：外边距",  # 文本内容
            size=18,           # 字体大小
            color="#FFFFFF"    # 字体颜色为白色
        ),

        # 设置容器的背景颜色为绿色
        # 通过绿色区域，可以观察容器本身的位置和大小
        bgcolor="#4CAF50",

        # 设置容器的内边距为 10
        # 这只是为了让文字与绿色容器边缘保持一定距离
        # 注意：这里的 padding 和 margin 是两个不同的属性
        padding=10,

        # 设置容器的外边距为 30
        # margin 表示容器外部留出的间距
        # 这样可以让绿色容器与周围的内容保持距离
        margin=30,

        # 设置容器的圆角半径为 8
        border_radius=8
    )


    # ==================== 四、将组件添加到页面 ====================

    # page.add() 用于将组件添加到页面中
    # 只有添加到页面中，或者放入已显示的父组件中，组件才能显示出来
    page.add(

        # 添加第一个标题
        ft.Text(
            "一、Padding 内边距",
            size=22  # 标题字体大小
        ),

        # 添加前面创建的蓝色 Container
        padding_box,


        # 添加一条水平分隔线
        # 用于将 Padding 和 Margin 两个演示区域分开
        ft.Divider(),


        # 添加第二个标题
        ft.Text(
            "二、Margin 外边距",
            size=22
        ),

        # 添加前面创建的绿色 Container
        margin_box
    )


# ==================== 五、程序入口 ====================

# 判断当前 Python 文件是否作为主程序运行
# 如果是直接运行这个文件，就执行下面的代码
if __name__ == "__main__":

    # 启动 Flet 应用，并将 main 函数作为程序入口
    # Flet 会创建页面对象 page，然后调用 main(page)
    ft.run(main)