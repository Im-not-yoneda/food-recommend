from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import CheckBox, calorie_form, insert_name, insert_calorie, insert_value, test_form
from pulp import LpProblem, LpVariable, LpMaximize
from .models import food

def foodrecommend(request):
    def knapsack_solver(weights, values, capacity):
        num_items = len(weights)
        # 合計価値を最大化するための線形プログラム問題を作成
        knapsack_problem = LpProblem("ナップサック問題", LpMaximize)
        # 各アイテムのための0または1のバイナリ決定変数を作成
        x = [LpVariable(f'x_{i}', cat='Binary') for i in range(num_items)]
        # 目的関数：合計価値を最大化
        knapsack_problem += sum(float(values[i]) * x[i] for i in range(num_items)), "TotalValue"
        # 制約：合計重量が容量を超えないようにする
        knapsack_problem += sum(float(weights[i]) * x[i] for i in range(num_items)) <= float(capacity), "TotalWeight"
        # 問題を解く
        knapsack_problem.solve()
        # 選択されたアイテムを抽出
        selected_items = [i for i in range(num_items) if x[i].varValue == 1]
        return {
            'selected_items': selected_items,
            'total_value': sum(float(values[i]) for i in selected_items),
            'total_weight': sum(float(weights[i]) for i in selected_items)
        }
    
    if request.method == 'POST':
        calorie = calorie_form(request.POST)
        checkbox = CheckBox(request.POST)
        selected_calorie_list = []
        selected_value_list = []
        result_foods_list = []

        if checkbox.is_valid() and calorie.is_valid:
            input_calorie = calorie.data['calorie']
            selected_foods_list = checkbox.cleaned_data['food_names']
            selected_foods = "、".join(selected_foods_list)

            for selected_food in selected_foods_list:
                food_data = food.objects.get(name=selected_food)
                selected_calorie_list.append(food_data.calorie)
                selected_value_list.append(food_data.value)

            selected_calorie_list_new = [str(a) for a in selected_calorie_list]
            selected_calorie = "、".join(selected_calorie_list_new)
            selected_value_list_new = [str(a) for a in selected_value_list]
            selected_value = "、".join(selected_value_list_new)\

            result = knapsack_solver(selected_calorie_list,selected_value_list,input_calorie)
            for result_food in result['selected_items']:
                result_foods_list.append(selected_foods_list[result_food])
            result_foods = "、".join(result_foods_list)
            result_value = result['total_value']
            # ごはん差分
            if result_value > 1000:
                result_value = result['total_value'] - 998
            result_calorie = result['total_weight']

            return render(request, 'polls/result.html', {'input_calorie': input_calorie,'selected_foods': selected_foods,'selected_calories': selected_calorie,'selected_values':selected_value,'result_calorie': result_calorie,'result_value': result_value,'result_foods': result_foods})
    else:
        calorie = calorie_form()
        checkbox = CheckBox()
    return render(request, 'polls/index.html', {'calorie': calorie,'food_names': checkbox})

def insertFood(request):
    if request.method == 'POST':
        name_form = insert_name(request.POST)
        calorie_value = insert_calorie(request.POST)
        value_form = insert_value(request.POST)
        if name_form.is_valid() and calorie_value.is_valid() and value_form.is_valid():
            insert = food(name=name_form.data['name'], calorie=calorie_value.data['calorie'], value=value_form.data['value'])
            insert.save()
            success_name = name_form.data['name']
            success_calorie = calorie_value.data['calorie']
            success_value = value_form.data['value']
            return render(request, 'polls/insertFood.html', {'name_form': name_form, 'calorie_form': calorie_value, 'value_form': value_form, 'success_name': success_name, 'success_calorie': success_calorie, 'success_value': success_value})
    else:
        name_form = insert_name()
        calorie_value = insert_calorie()
        value_form = insert_value()
    return render(request, 'polls/insertFood.html', {'name_form': name_form, 'calorie_form': calorie_value, 'value_form': value_form})

def about(request):
    return render(request, 'polls/about.html')

def test(request):
    if request.method == 'POST':
        form = test_form(request.POST)
    else:
        form = test_form()
    return render(request, 'polls/test.html', {'db_list': food.objects.all(),'food_name': form})