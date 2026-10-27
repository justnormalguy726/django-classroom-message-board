import flet as ft


def main(page: ft.Page):
    # 1. 设置页面属性
    page.title = "个人任务管理器"
    page.window.width = 500
    page.window.height = 650
    page.padding = 20
    page.spacing = 15

    # 2. 创建标题
    title = ft.Text(
        "个人任务管理器",
        size=26,
        weight=ft.FontWeight.BOLD
    )

    # 3. 创建输入框
    task_input = ft.TextField(
        label="请输入任务名称",
        hint_text="例如：学习 Flet",
        expand=True
    )

    # 4. 创建任务列表
    task_list = ft.Column(spacing=8)

    # 5. 创建任务统计文本
    statistics = ft.Text(size=14)

    # 6. 更新任务统计信息
    def update_statistics():
        total = len(task_list.controls)

        completed = sum(
            1
            for task in task_list.controls
            if task.controls[0].value
        )

        statistics.value = (
            f"任务总数：{total} | 已完成：{completed}"
        )

    # 7. 添加任务
    def add_task(e):
        task_name = task_input.value.strip()

        # 输入为空时，不添加任务
        if not task_name:
            task_input.error_text = "任务名称不能为空"
            page.update()
            return

        # 清除输入错误提示
        task_input.error_text = None

        # 创建复选框
        checkbox = ft.Checkbox(
            label=task_name,
            value=False,
            expand=True
        )

        # 创建删除按钮
        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            tooltip="删除任务"
        )

        # 任务完成状态改变时，更新统计信息
        def change_task(e):
            update_statistics()
            page.update()

        checkbox.on_change = change_task

        # 删除任务
        def delete_task(e):
            task_list.controls.remove(task_row)
            update_statistics()
            page.update()

        delete_button.on_click = delete_task

        # 将复选框和删除按钮放在同一行
        task_row = ft.Row(
            controls=[checkbox, delete_button]
        )

        # 将任务添加到列表
        task_list.controls.append(task_row)

        # 清空输入框
        task_input.value = ""

        # 更新统计信息和页面
        update_statistics()
        page.update()

    # 8. 创建添加按钮
    add_button = ft.Button(
        "添加任务",
        icon=ft.Icons.ADD,
        on_click=add_task
    )

    # 9. 组合页面布局
    page.add(
        title,
        ft.Row(
            controls=[task_input, add_button]
        ),
        ft.Divider(),
        statistics,
        task_list
    )

    # 初始化统计信息
    update_statistics()
    page.update()


# 10. 启动 Flet 应用
ft.run(main)