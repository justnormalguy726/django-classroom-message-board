import flet as ft
import pandas as pd

# 1. 用 pandas 读取 Excel，得到 DataFrame
df = pd.read_excel("students.xlsx")


def main(page: ft.Page):
    page.title = "学生成绩管理系统"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.window.width = 800
    page.window.height = 600

    # 2. 根据 DataFrame 的列名生成 DataColumn
    columns = [
        ft.DataColumn(
            ft.Text(str(col), weight=ft.FontWeight.BOLD),
            numeric=pd.api.types.is_numeric_dtype(df[col]),  # 数值列右对齐
        )
        for col in df.columns
    ]

    # 3. 遍历 DataFrame 的每一行生成 DataRow
    rows = [
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(str(value))) for value in row]
        )
        for row in df.itertuples(index=False)
    ]

    # 4. 组装 DataTable
    table = ft.DataTable(
        columns=columns,
        rows=rows,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        heading_row_color=ft.Colors.BLUE_50,
        horizontal_lines=ft.BorderSide(1, ft.Colors.GREY_200),
        column_spacing=40,
    )

    page.add(
        ft.Column(
            [
                ft.Text("学生成绩一览表", size=28, weight=ft.FontWeight.BOLD),
                ft.Text(f"数据来源：students.xlsx | 共 {len(df)} 名学生",
                        size=14, color=ft.Colors.GREY_600),
                ft.Container(
                    content=table,
                    border_radius=10,
                    padding=10,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )


ft.run(main)
