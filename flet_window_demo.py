import flet as ft
#窗体常用属性

def main(page: ft.Page):
    page.add(
        # 文本内容
        ft.Text("Hello, Flet!"),   
        #输入内容                                 
        #ft.TextField(label="请输入内容",hint_text="请输入内容")       
    )
    #系统黑白主题
    #page.theme_mode = ft.ThemeMode.DARK                        
    #系统背景颜色 
    page.bgcolor = ft.Colors.BLUE_100
    #系统窗体宽高
    page.window.width = 500
    page.window.height = 500
    #纵向和横向显示位置
    page.vertical_alignnment = ft.MainAxisAlignment.END
if __name__ == "__main__":
    ft.run(main)