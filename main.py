from file_functions import parse_CSV
from graphic_functions import paint_activity_of_types, paint_activity_of_types, paint_type_expense, \
    paint_mean_source_expense, \
    paint_product_income, paint_company_efficiency, paint_click_show_compare, paint_clickability, paint_cpm, \
    paint_columnar_type_expense, paint_columnar_type_expense2
from main_functions import get_click_amount_for_ad_types, get_expense_of_type, \
    get_expense_of_source, get_product_income, get_ad_company_efficiency, get_show_amount_for_ad_types, \
    get_clickability, get_cpm

# КОНВЕРТИРУЕМ ВСЕ ДАТАСЕТЫ В ДАТАФРЕЙМЫ
advertisement_info, advertisement_list, project_costs, subscription_sales \
    = parse_CSV()


# ПОУЛЧАЕМ КОЛИЧЕСТВО КЛИКОВ ДЛЯ КАЖД ТИПА РЕКЛАМЫ
df_click_amount_for_ad_types = (
    get_click_amount_for_ad_types(advertisement_list, advertisement_info))
print(f'\nКОЛИЧЕСТВО КЛИКОВ ДЛЯ КАЖД ТИПА РЕКЛАМЫ\n{df_click_amount_for_ad_types}',
      end='\n\n')
# ПОУЛЧАЕМ КОЛИЧЕСТВО ПРОСМОТРОВ ДЛЯ КАЖД ТИПА РЕКЛАМЫ
df_show_amount_for_ad_types = (
    get_show_amount_for_ad_types(advertisement_list, advertisement_info))
print(f'КОЛИЧЕСТВО ПРОСМОТРОВ ДЛЯ КАЖД ТИПА РЕКЛАМЫ\n{df_show_amount_for_ad_types}',
      end='\n\n')
# РИСУЕМ СТОЛБЧАТУЮ ДИГРАММУ ДЛЯ ПЕРВЫХ ДВУХ РЕЗУЛЬТАТОВ
paint_click_show_compare(df_click_amount_for_ad_types, df_show_amount_for_ad_types)
# РИСУЕМ КРУГОВУЮ ДИГРАММУ ДЛЯ ПЕРВЫХ ДВУХ РЕЗУЛЬТАТОВ
paint_activity_of_types(df_click_amount_for_ad_types, df_show_amount_for_ad_types)


# ПОУЛЧАЕМ КЛИКАБЕЛЬНОСТЬ ДЛЯ КАЖД РЕКЛАМНОЙ КОМПАНИИ
df_clickability = (
    get_clickability(df_click_amount_for_ad_types, df_show_amount_for_ad_types))
print(f'КЛИКАБЕЛЬНОСТЬ ДЛЯ КАЖД РЕКЛАМНОЙ КОМПАНИИ\n{df_clickability}',
      end='\n\n')
# РИСУЕМ ДИГРАММУ КЛИКАБЕЛЬНОСТИ
paint_clickability(df_clickability)


# ПОУЛЧАЕМ CPM ДЛЯ КАЖД РЕКЛАМНОЙ КОМПАНИИ
df_cpm = get_cpm(advertisement_list, advertisement_info)
print(f'CPM ДЛЯ КАЖД РЕКЛАМНОЙ КОМПАНИИ\n{df_cpm}',
      end='\n\n')
# РИСУЕМ ДИГРАММУ ДЛЯ CPM
paint_cpm(df_cpm)


# ПОЛУЧАЕМ СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ТИП РАСХОДОВ ПО ГОДАМ
df_type_expense = get_expense_of_type(project_costs)
print(f'СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ТИП РАСХОДОВ ПО ГОДАМ\n{df_type_expense}',
      end='\n\n')
# РИСУЕМ ГРАФИК РАСХОДОВ ПО ГОДАМ
paint_type_expense(df_type_expense)
# РИСУЕМ СТОЛБЧАТУЮ ДИАГРАММУ РАСХОДОВ ПО ГОДАМ
paint_columnar_type_expense(df_type_expense)
# РИСУЕМ СТОЛБЧАТУЮ ДИАГРАММУ РАСХОДОВ ПО ГОДАМ БЕЗ wage_fund
paint_columnar_type_expense2(df_type_expense)


# ПОЛУЧАЕМ СРЕДНЮЮ СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ИСТОЧНИК ЗА КВАРТАЛ
df_source_expense = get_expense_of_source(project_costs)
print(f'СРЕДНЮЮ СТОИМОСТЬ РАСХОДОВ НА КАЖДЫЙ ИСТОЧНИК ЗА КВАРТАЛ\n{df_source_expense}',
      end='\n\n')
# РИСУЕМ ГРАФИК ДЛЯ СР СТОИМОСТИ РАСХОДОВ ЗА КВАРТАЛ
paint_mean_source_expense(df_source_expense)


# ПОЛУЧАЕМ СУММУ ДОХОДОВ ПО КАЖДОМУ ПРОДУКТУ
df_product_income = get_product_income(subscription_sales)
print(f'СУММА ДОХОДОВ ПО КАЖДОМУ ПРОДУКТУ\n{df_product_income}',
      end='\n\n')
# РИСУЕМ ГРАФИК СУММЫ ДОХОДОВ
paint_product_income(df_product_income)


# ПОЛУЧАЕМ ЭФФЕКТИВНОСТЬ РЕКЛАМНОЙ КОМПАНИИ
ad_company_efficiency = (
    get_ad_company_efficiency(subscription_sales, advertisement_list))
print(f'ЭФФЕКТИВНОСТЬ РЕКЛАМНЫХ КОМПАНИЙ\n{ad_company_efficiency}',
      end='\n\n')
# РИСУЕМ ГРАФИК ДЛЯ ЭФФЕКТИВНОСТЬ РЕКЛ КОМПАНИИ
paint_company_efficiency(ad_company_efficiency)
