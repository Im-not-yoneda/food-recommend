from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import CheckBox
from .forms import calorie_form
from .forms import test_form
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
        if calorie.is_valid():
            return render(request, 'polls/result.html')
    else:
        calorie = calorie_form()
        checkbox = CheckBox()
    return render(request, 'polls/index.html', {'calorie': calorie,'food_names': checkbox})

def insertFood(request):
    return render(request, 'polls/insertFood.html')

def about(request):
    return render(request, 'polls/about.html')

def test(request):
    if request.method == 'POST':
        form = test_form(request.POST)
    else:
        form = test_form()
    return render(request, 'polls/test.html', {'db_list': food.objects.all(),'food_name': form})