from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Recipe, Recipe_ingredient, Recipe_step, User, Fridge, Ingredient
from django.db import connection


def index(request):
    pass
    return render(request, 'fridge/index.html')

def content(request): #simplified function as login
    # try:
    #     request.session[user_name]
    # except
    #     pass
    # else:
    #先请求session[user_name],如果有，使用；如果没有，get_post。
    uname = request.POST['username']
    m = get_object_or_404(User, user_name=uname) #username不存在, 密码验证
    request.session['user_name'] = m.user_name  # save user name in session
    fridge_list = Fridge.objects.filter(user_name=uname)
    context = {'fridge_list': fridge_list, 'user_name': uname}
    #return render(request, 'fridge/shelf.html', context)
    return render(request, 'fridge/content.html', context)

def search(request):  # search action get from url
    uname = request.session['user_name']
    fridge_list = Fridge.objects.raw('SELECT * FROM fridge_fridge WHERE user_name_id = %s', [uname])
    with connection.cursor() as cursor:
        cursor.execute("""Select r.recipe_id_id, rec.recipe_name From
    (select i.ingredient_id as ingreid
    from fridge_Fridge f, fridge_Ingredient i
    where f.user_name_id = %s
    and f.ingredient_name like i.ingredient_name) as tempingre, fridge_Recipe_ingredient r, fridge_Recipe rec
    where r.ingredient_id_id = tempingre.ingreid
    and r.recipe_id_id = rec.recipe_id
    group by r.recipe_id_id, rec.recipe_name
    order by count(*) desc
    """, [uname])
        recipe_list = cursor.fetchall()
    context = {'recipe_list': recipe_list, 'fridge_list': fridge_list}
    return render(request, 'fridge/search.html', context)

def detail(request, r_id): # 超链接或直接输入：get from url
    recipe = get_object_or_404(Recipe, recipe_id=r_id)
    step_list = Recipe_step.objects.filter(recipe_id=r_id).order_by('step_number')
    ingredient_list = Recipe_ingredient.objects.filter(recipe_id=r_id).select_related('ingredient_id')
    context = {'recipe': recipe, 'ingredient_list': ingredient_list, 'step_list': step_list}
    return render(request, 'fridge/detail.html', context)

'''
add_food:      insert
add,eat,throw: update/ delete
search:        select
'''

def new_food(request):
    pass
    #接收：request.POST.food_name, request.POST.amount
    #try request.session['user_name']
    #check if food name is in the Fridge,#使用正则使得大小写不敏感，quantity根据数据库查找
    #if:
    #registerAdd = Fridge.objects.create_user(user_name=uname, ingredient_name=food_name, quantity = food_amount )
    #else:
    #update
    #redirect

'''
eg:
    def post_comment(request, new_comment):
        if request.session.get('has_commented', False):
            return HttpResponse("You've already commented.")
        c = comments.Comment(comment=new_comment)
        c.save()
        request.session['has_commented'] = True
        return HttpResponse('Thanks for your comment!')
'''

# def add_food(request):
#     food_name =  request.POST['food_name']
#     food_amount = request.POST['food_amount'] #如无输入默认为0，限制输入整数
#
#     try:
#         f = Fridge.objects.get(food_name=food_name)
#     except:
#         pass
#         #create
#     else:
#         f.quantity = f.quantity + food_amount
#         f.save()
#         return HttpResponseRedirect(reverse('fridge:content'))


def add_food(request):
    pass

def eat_food(request):
    #request.POST.edit_amout, update Fridge
    #输入值为0, 跳转至删除
    pass

def delete_food(request):
    # request.POST.food_name_d, delete tuple from Fridge
    pass

def logout(request): #create a log out button
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return render(request, 'fridge/index.html')

def eating_history(request):
    pass