import flet as ft


def main(page: ft.Page):
    # 设置页面标题和背景颜色
    page.title = "Flet 布局组件演示"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20

    # 1. 创建 Container：展示容器的样式
    container1 = ft.Container(
        content=ft.Text(
            "我是 Container",
            size=20,
            color=ft.Colors.WHITE
        ),
        bgcolor=ft.Colors.BLUE,
        padding=20,
        border_radius=10,
        width=300
    )

    # 2. 创建 Row：让三个文本横向排列
    row1 = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("左边"),
                bgcolor=ft.Colors.BLUE,
                padding=15
            ),
            ft.Container(
                content=ft.Text("中间"),
                bgcolor=ft.Colors.GREEN,
                padding=15
            ),
            ft.Container(
                content=ft.Text("右边"),
                bgcolor=ft.Colors.YELLOW,
                padding=15
            )
        ],
        spacing=10
    )

    # 3. 创建 Column：让多个控件纵向排列
    column1 = ft.Column(
        controls=[
            ft.Text("第一行内容", size=16),
            ft.Text("第二行内容", size=16),
            ft.Text("第三行内容", size=16)
        ],
        spacing=10
    )

    # 4. 将三个演示区域放到页面上
    page.add(
        ft.Text("一、Container 容器", size=22),
        container1,

        ft.Text("二、Row 横向布局", size=22),
        row1,

        ft.Text("三、Column 纵向布局", size=22),
        column1
    )


if __name__ == "__main__":
    ft.run(main)