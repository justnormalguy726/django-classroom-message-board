import flet as ft


def main(page: ft.Page):
    # 设置页面标题
    page.title = "Flet 导航栏示例"

    # 创建导航栏
    navigation_bar = ft.NavigationBar(
        destinations=[
            # 首页
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="首页"
            ),
            # 消息页
            ft.NavigationBarDestination(
                icon=ft.Icons.MESSAGE,
                label="消息"
            ),
            # 个人中心
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                label="我的"
            ),
        ]
    )

    # 将导航栏添加到页面底部
    page.navigation_bar = navigation_bar

    # 页面主体内容
    page.add(
        ft.Text(
            "欢迎使用 Flet！",
            size=24
        )
    )


# 启动程序
ft.run(main)