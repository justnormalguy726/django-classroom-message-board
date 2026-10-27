from django.shortcuts import render, redirect
from .models import Message

#视图函数，负责处理请求并决定返回什么响应
def home(request):
    # 处理用户提交的留言
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        content = request.POST.get('content', '').strip()

        # 检查输入是否为空
        if name and content:
            Message.objects.create(
                name=name,
                content=content
            )

            # 提交成功后跳转回首页
            return redirect('home')

    # 查询数据库中的全部留言
    messages = Message.objects.order_by('-create_time')

    # 将留言数据传递给网页模板
    return render(
        request,
        'classroom/home.html',
        {'messages': messages}
    )
# Create your views here.
