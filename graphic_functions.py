import numpy as np
from matplotlib import pyplot as plt

def paint_click_show_compare(df_click_amount_for_ad_types, df_show_amount_for_ad_types):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫ ДЛЯ ДИАГРАММЫ
    x_list = np.arange(3)
    click_list = df_click_amount_for_ad_types.loc[:, "ad_type_click_amount"]
    show_list = df_show_amount_for_ad_types.loc[:, "ad_type_show_amount"]
    w = 0.3
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    fig, ax = plt.subplots()
    ax.bar(x_list - w / 2, click_list, width=w)
    ax.bar(x_list + w / 2, show_list, width=w)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.xticks(x_list, ['contextual', 'email', 'social'])
    plt.yticks(np.arange(0, 450000, step=25000))
    plt.title('Клики и просмотры на всех типах рекламы')
    plt.grid(axis="y")
    plt.legend(['Клики', 'Просмотры'])
    plt.show()

def paint_activity_of_types(df_click_amount_for_ad_types, df_show_amount_for_ad_types):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ ДЛЯ ДИАГРАММЫ
    val1 = [df_click_amount_for_ad_types.loc[0, "ad_type_click_amount"],
            df_show_amount_for_ad_types.loc[0, "ad_type_show_amount"]]
    val2 = [df_click_amount_for_ad_types.loc[1, "ad_type_click_amount"],
            df_show_amount_for_ad_types.loc[1, "ad_type_show_amount"]]
    val3 = [df_click_amount_for_ad_types.loc[2, "ad_type_click_amount"],
            df_show_amount_for_ad_types.loc[2, "ad_type_show_amount"]]
    # ОПРЕДЕЛЯЕМ КОНСТАНТЫ ДЛЯ ДИАГРАММЫ
    labels1 = ["contextual", "email", "social"]
    labels2 = ["click", "show", "click", "show", "click", "show"]
    offset = 0.7
    data = np.array([val1, val2, val3])
    cmap = plt.get_cmap("tab20b")
    b_colors = cmap(np.array([2, 10, 14]))
    sm_colors = cmap(np.array([0, 1, 8, 9, 12, 13]))
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ
    fig, ax = plt.subplots(figsize=(7,8))
    # ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    w, l, p = ax.pie(data.sum(axis=1), radius=1.4, colors=b_colors,
       autopct='%1.1f%%', pctdistance=0.75, labels = labels1,
       wedgeprops=dict(width=offset, edgecolor='w'))
    [t.set_fontsize(20) for t in p] # меняем шрифты всех меток

    w, l, p = ax.pie(data.flatten(), radius=1.4 - offset,  colors=sm_colors,
        autopct='%1.1f%%', pctdistance=0.6,
        labels = labels2, labeldistance=1.02,
        wedgeprops=dict(width=offset, edgecolor='w'))
    [t.set_fontsize(15) for t in p] # меняем шрифты всех меток
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.title("Активность\nтипов\nреклам", loc="left", fontsize=20)
    plt.show()

def paint_clickability(df_clickability):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = df_clickability.loc[:, "Ad_type"]
    y_list = df_clickability.loc[:, "clickability"]
    y_list = y_list.sort_values()
    colors = ['#ec5353', '#ec5353', '#47A76A']
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = plt.barh(x_list, y_list, height=0.8, color=colors)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    ax.bar_label(bars, padding=-110, color='white',
        fontsize=12, label_type='edge', fmt='%1.2f%% руб.',
        fontweight='bold')
    ax.spines[['right', 'top', 'bottom']].set_visible(False)
    ax.xaxis.set_visible(False)
    plt.title('CTR - показатель кликабельности рекламной компании')
    plt.show()

def paint_cpm(df_cpm):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = df_cpm.loc[:, "Ad_key"]
    y_list = df_cpm.loc[:, "cpm"]
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    plt.figure(figsize=(7, 7))
    plt.bar(x_list, y_list, linewidth=1, color='#F4A460', edgecolor='black', width=0.5)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.xticks(rotation=25)
    plt.grid()
    plt.title("CPM РЕКЛАМНЫХ КОМПАНИЙ")
    plt.ylabel("CPM, руб", fontsize=12, fontweight="bold")
    plt.yticks(np.arange(1000, 26000, step=2000))
    plt.show()

def paint_type_expense(df_type_expense):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = np.arange(3)
    equipment_selection =(
        df_type_expense.loc[df_type_expense["expense_type"]=="equipment"].loc[:, "expense_of_type"])
    furniture_selection = (
        df_type_expense.loc[df_type_expense["expense_type"] == "furniture"].loc[:, "expense_of_type"])
    hr_work_selection = (
        df_type_expense.loc[df_type_expense["expense_type"] == "hr_work"].loc[:, "expense_of_type"])
    outer_source_selection = (
        df_type_expense.loc[df_type_expense["expense_type"] == "outer_source"].loc[:, "expense_of_type"])
    server_maintenance_selection = (
        df_type_expense.loc[df_type_expense["expense_type"] == "server_maintenance"].loc[:, "expense_of_type"])
    wage_fund_selection = (
        df_type_expense.loc[df_type_expense["expense_type"] == "wage_fund"].loc[:, "expense_of_type"])
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    plt.figure(figsize=(10, 7))
    plt.plot(x_list, equipment_selection, 'g-o', linewidth=3)
    plt.plot(x_list, furniture_selection, 'r-o', linewidth=3)
    plt.plot(x_list, hr_work_selection, 'b-o', linewidth=3)
    plt.plot(x_list, outer_source_selection, 'c-o', linewidth=3)
    plt.plot(x_list, server_maintenance_selection, 'm-o', linewidth=3)
    plt.plot(x_list, wage_fund_selection, 'y-o', linewidth=3)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.xticks(x_list, ['2020', '2021', '2022'])
    plt.yticks(np.arange(0, 80000000, step=10000000),["0", "10","20", "30", "40", "50", "60", "70"])
    plt.legend(['equipment', 'furniture', 'hr work', 'outer source', 'server maintenance', 'wage fund'])
    plt.xlabel("Год", fontsize=14, fontweight="bold")
    plt.ylabel("Расходы, млн рублей", fontsize=14, fontweight="bold")
    plt.title('СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ТИП ПО ГОДАМ')
    plt.grid()
    plt.show()

def paint_columnar_type_expense(df_type_expense):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = np.arange(6)
    selection_2020 = df_type_expense.loc[df_type_expense["year"]==2020].loc[:, "expense_of_type"]
    selection_2021 = df_type_expense.loc[df_type_expense["year"] == 2021].loc[:, "expense_of_type"]
    selection_2022 = df_type_expense.loc[df_type_expense["year"]==2022].loc[:, "expense_of_type"]
    w = 0.3
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    fig, ax = plt.subplots(figsize=(7, 8))
    ax.bar(x_list - w, selection_2020, width=w)
    ax.bar(x_list, selection_2021, width=w)
    ax.bar(x_list + w, selection_2022, width=w)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.xticks(x_list, ['equipment', 'furniture', 'hr_work', 'outer_source', 'server_maintenance', 'wage_fund'],
               rotation=25)
    plt.yticks(np.arange(0, 75000000, step=10000000), ["0", "10","20", "30", "40", "50", "60", "70"])
    plt.title('СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ТИП ПО ГОДАМ\n(в столбчатом представлении)')
    plt.ylabel("Расходы, млн рублей", fontsize=14, fontweight="bold")
    plt.legend(['2020', '2021', '2022'])
    plt.grid()
    plt.show()

def paint_columnar_type_expense2(df_type_expense):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = np.arange(5)
    df_type_expense = df_type_expense.loc[df_type_expense["expense_type"]!='wage_fund'].loc[:, :]
    selection_2020 = df_type_expense.loc[df_type_expense["year"]==2020].loc[:, "expense_of_type"]
    selection_2021 = df_type_expense.loc[df_type_expense["year"] == 2021].loc[:, "expense_of_type"]
    selection_2022 = df_type_expense.loc[df_type_expense["year"]==2022].loc[:, "expense_of_type"]
    w = 0.3
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    fig, ax = plt.subplots(figsize=(7, 8))
    ax.bar(x_list - w, selection_2020, width=w)
    ax.bar(x_list, selection_2021, width=w)
    ax.bar(x_list + w, selection_2022, width=w)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.xticks(x_list, ['equipment', 'furniture', 'hr_work', 'outer_source', 'server_maintenance'],
               rotation=25)
    plt.yticks(np.arange(0, 6500000, step=500000))
    plt.title('СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ТИП ПО ГОДАМ\n(БЕЗ wage_fund)')
    plt.ylabel("Расходы, млн рублей", fontsize=14, fontweight="bold")
    plt.legend(['2020', '2021', '2022'])
    plt.grid()
    plt.show()

def paint_mean_source_expense(df_source_expense):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = df_source_expense.loc[:, "expense_source"]
    y_list = df_source_expense.loc[:, "mean_expense"]
    y_list = y_list.sort_values()
    colors = ['#768493', '#768493', '#d95f02']
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = plt.barh(x_list, y_list, height=0.8, color=colors)
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    ax.bar_label(bars, padding=-110, color='white',
        fontsize=12, label_type='edge', fmt='%1.0f руб.',
        fontweight='bold')
    ax.spines[['right', 'top', 'bottom']].set_visible(False)
    ax.xaxis.set_visible(False)
    plt.title('СРЕДНЯЯ КВАРТАЛЬНАЯ СУММА РАСХОДОВ НА КАЖДЫЙ ИСТОЧНИК')
    plt.show()

def paint_product_income(df_product_income):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    vals = df_product_income.loc[:, "income_of_product"]
    labels = df_product_income.loc[:, "product"]
    explode = (0, 0.08, 0)
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode,
        wedgeprops={'lw': 1, 'ls': '-', 'edgecolor': "k"})
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.title('СУММА ДОХОДОВ ПО КАЖДОМУ ПРОДУКТУ')
    plt.show()

def paint_company_efficiency(ad_company_efficiency):
    # ОПРЕДЕЛЯЕМ ВЫБОРКИ И КОНСТАНТЫДЛЯ ДИАГРАММЫ
    x_list = ad_company_efficiency.loc[:, "ad_key"]
    y_list = ad_company_efficiency.loc[:, "company_efficiency"]
    # ИНИЦИАЛИЗИРУЕМ ДИАГРАММУ И ОПРЕДЕЛЯЕМ ЕЁ ФУНКЦИИ
    plt.figure(figsize=(7, 7))
    plt.bar(x_list, y_list, linewidth=2.5,edgecolor='r', width=0.5)
    # СТРОИМ ДОПОЛНИТЕЛЬНУЮ ЛИНИЮ И ТЕКСТ К НЕЙ
    plt.axhline(y=0, color='black', ls='-', lw=1.5)
    plt.text(x=5.75, y=0, s='Черта\nокупаемости', ha='center',
        fontsize=8, bbox=dict(facecolor='white', edgecolor='grey', ls='--'))
    # НАСТРАИВАЕМ ВНЕШНИЕ ПАРАМЕТРЫ ДИАГРАММЫ И ВЫВОДИМ ЕЁ
    plt.xticks(rotation=25)
    plt.grid()
    plt.title("ЭФФЕКТИВНОСТЬ РЕКЛАМНЫХ КОМПАНИЙ")
    plt.ylabel("Эффективность, %", fontsize=12, fontweight="bold")
    plt.yticks(np.arange(-100, 500, step=50))
    plt.show()
