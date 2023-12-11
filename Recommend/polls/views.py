from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import CheckBox
from .forms import NumberInput
from pulp import LpProblem, LpVariable, LpMaximize

def foodrecommend(request):
    weights = []
    values = []
    name = []
    result = None
    total_weight = None
    select_name = None

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
        formNum = NumberInput(request.POST)
        if formNum.is_valid():
            # フォームのデータを処理
            number = formNum.cleaned_data['number']
            result = number
    else:
        formNum = NumberInput()

    if request.method == 'POST':
        formBox = CheckBox(request.POST)
        # 選択した要素一覧
        if formBox.is_valid():
            formBox_reg = formBox.cleaned_data.get('chickin_reg')
            formBox_chest = formBox.cleaned_data.get('chickin_chest')
            formBox_brrocori = formBox.cleaned_data.get('brrocori')
            formBox_carrot = formBox.cleaned_data.get('carrot')
            formBox_onion = formBox.cleaned_data.get('onion')
            formBox_beef = formBox.cleaned_data.get('beef')
            formBox_pork = formBox.cleaned_data.get('pork')
            formBox_rice = formBox.cleaned_data.get('rice')
            formBox_potato = formBox.cleaned_data.get('potato')
            selected_options = [formBox.fields[key].label for key, value in formBox.cleaned_data.items() if value]
            # タンパク質とカロリーを定義
            if formBox_reg:
                values.append(25)
                weights.append(200)
                name.append("鶏もも肉")
            if formBox_chest:
                values.append(23)
                weights.append(150)
                name.append("鶏むね肉")
            if formBox_brrocori:
                values.append(4)
                weights.append(50)
                name.append("ブロッコリー")
            if formBox_carrot:
                values.append(1)
                weights.append(28)
                name.append("にんじん")
            if formBox_onion:
                values.append(1)
                weights.append(33)
                name.append("たまねぎ")
            if formBox_beef:
                values.append(20)
                weights.append(148)
                name.append("牛もも肉")
            if formBox_pork:
                values.append(14)
                weights.append(386)
                name.append("豚バラ肉")
            if formBox_rice:
                values.append(1000)
                weights.append(168)
                name.append("ごはん")
            if formBox_potato:
                values.append(3)
                weights.append(59)
                name.append("じゃがいも")
            knapsack_result = knapsack_solver(weights, values, number)
            selected_items = knapsack_result['selected_items']
            total_value = sum(values)
            if total_value >= 1000:
                total_value = total_value - 998
            total_weight = knapsack_result['total_weight']
            select_name = [name[i] for i in selected_items]
        else:
            selected_options = []
            return render(request, 'polls/index.html', {'formNum': formNum, 'result': result,'weights': weights,'option':name, 'values':values, 'formBox': formBox, 'selected_options': selected_options, 'calory': total_weight, 'name':select_name, 'value': total_value})
    else:
        formBox = CheckBox()
        selected_options = []
        return render(request, 'polls/index.html', {'formNum': formNum, 'result': result,'weights': weights,'option':name, 'values':values, 'formBox': formBox, 'selected_options': selected_options, 'calory': total_weight, 'name':select_name})
    return render(request, 'polls/result.html', {'formNum': formNum, 'result': result,'weights': str(weights)[1:-1],'option':",".join(name), 'values':str(values)[1:-1], 'formBox': formBox, 'selected_options': selected_options, 'calory': total_weight, 'name':",".join(select_name), 'value': total_value})

def insertFood(request):
    return render(request, 'polls/insertFood.html')

def about(request):
    return render(request, 'polls/about.html')
