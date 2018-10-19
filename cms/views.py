# coding:utf-8
from django.shortcuts import render
from cms.models import BlogPost
from django.shortcuts import HttpResponse
import json
from django.db.models.aggregates import Count
from django.db import connection
from django.shortcuts import redirect
# from django.contrib.auth import models
# Create your views here.

# reload(BlogPost)
def index(request):

    return render(request, 'index.html')


def notfound(request):

    return render(request, '404.html')


def favorite(request):

    return render(request, 'favorite.html')


def blog(request):

    blog_list = BlogPost.objects.all()
    # print blog_list
    return render(request, 'blog.html', {'blog_list': blog_list})


def sub_article(request):

    if request.method == 'POST':
        # 获取ajax传过来的参数值
        data = request.POST
        id = data.get('blogId')
        print 'id:%s' % id
        title = data.get('title')
        body = data.get('body')
        print type(title)
        if title != '' and body != '':
            # msg = '请输入标题'
            # print msg
            # return render(request, 'edit_article.html', {'msg': msg})

            # body = request.POST.get("blog-body")#此种方式不能获取到值
            print "title:%s" % title
            print "body:%s" % body
            BlogPost.objects.filter(id=int(id)).update(title=title)
            BlogPost.objects.filter(id=int(id)).update(body=body) # 更改数据
            # BlogPost.objects.create(title=title)
            # BlogPost.objects.create(body=body)#提交时插入两条半截数据很可能是这里分开执行引起的，需要通过id来准确定位修改哪条数据
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"请输入标题和正文"}', content_type='application/json')
        # return render(request, 'blog_detail.html')


def edit_article(request,id):
    # if request.method == 'GET':
    #     id = request.GET.get(id) #不是使用？传参数的不用这样获得参数值，直接获取
    print 'id is:%s' % id
    print type(id)
    blog = BlogPost.objects.filter(id=int(id))
    return render(request, 'edit_article.html',{'blog': blog})


def blog_detail(request):
    # if request.method == 'POST':
    #     title = request.POST.get("blog-title", None)
    #     body = request.POST.get("blog-body", None)
    #     BlogPost.objects.create(title=title)
    #     BlogPost.objects.create(body=body)

    blog_detail = BlogPost.objects.all()
    print '博客：', blog_detail
    return render(request, 'blog_detail.html', {'blog_detail': blog_detail})


def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        # 插入数据库
        BlogPost.objects.create(title=title, body=body)
        return HttpResponse('{"status":"success"}')
    return render(request, 'create_blog.html')


def count_blog(request):
    # 下面等价于：select distinct auth,count() as blog_count from cms_blogpost group by auth
    auth_count_blog=BlogPost.objects.values('auth').distinct().annotate(blog_count=Count('auth')).all()
    # 从数据库中取出的数据格式如下，是一个列表，其中每个元素都是字典
    # auth_count_blog=[{'blog_count': 1, 'auth': u'guchen'}, {'blog_count': 1, 'auth': u'\u6c6a\u5a07'},
     # {'blog_count': 7, 'auth': u'\u8c37\u6668'}]
    blog_count = []
    auth = []
    for i in auth_count_blog:
        print i['blog_count']
        # 将作者和文章数分别放到列表中，i代表每一个字典，然后通过Dict['key']的方式取出对应值
        blog_count.append(i['blog_count'])
        auth.append(i['auth'])
        # 将数据组装为字典格式
        auth_count_blog = {'blog_count': blog_count,
                           'auth': auth}

    # auth_count_blog={'blog_count': [10, 15, 20],
    #                  'auth': ["张三", "维鲁斯", "爱卡西亚"]}
    #  向js中传递数据必须json.dumps()处理
    return render(request, 'count_blog.html', {'auth_count_blog': json.dumps(auth_count_blog)})


def tag_manage(request):
    pass
    return render(request,'tag_manage.html')

