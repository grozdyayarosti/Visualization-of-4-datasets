import pandas as pd

def get_click_amount_for_ad_types(advertisement_list, advertisement_info):
    # СОЕДИНЯЕМ ТАБЛИЦЫ
    df_join = pd.merge(advertisement_list, advertisement_info, left_on="Ad_key", right_on="ad_key", how="right")
    # df_join = df_join.loc[:, ["Ad_type", "event_type"]]

    # ОСТАВЛЯЕМ В СТРОКАХ С СОБЫТИЯМИ ТОЛЬКО СОБЫТИЯ С КЛИКОМ
    df_only_click = df_join.loc[df_join["event_type"] == 'click']

    # ГРУППИРУЕМ ПО ТИПАМ РЕКЛАМЫ И ПОДСЧИТЫВАЕМ ЗАПИСИ У КАЖДОГО ТИПА РЕКЛАМЫ(ВСЕ ЗАПИСИ С КЛИКАМИ)
    df_click_for_ad_types = df_only_click.groupby('Ad_type', as_index=False).aggregate({'event_type': 'count'})
    df_click_for_ad_types = df_click_for_ad_types.rename(columns={'event_type': 'ad_type_click_amount'})

    return df_click_for_ad_types

def get_show_amount_for_ad_types(advertisement_list, advertisement_info):
    # СОЕДИНЯЕМ ТАБЛИЦЫ
    df_join = pd.merge(advertisement_list, advertisement_info, left_on="Ad_key", right_on="ad_key", how="right")
    # df_join = df_join.loc[:, ["Ad_type", "event_type"]]
    print(df_join)
    # ОСТАВЛЯЕМ В СТРОКАХ С СОБЫТИЯМИ ТОЛЬКО СОБЫТИЯ С ПРОГСМОТРАМИ
    df_only_show = df_join.loc[df_join["event_type"] == 'show']

    # ГРУППИРУЕМ ПО ТИПАМ РЕКЛАМЫ И ПОДСЧИТЫВАЕМ ЗАПИСИ У КАЖДОГО ТИПА РЕКЛАМЫ(ВСЕ ЗАПИСИ С ПРОСМОТРАМИ)
    df_show_for_ad_types = df_only_show.groupby('Ad_type', as_index=False).aggregate({'event_type': 'count'})
    df_show_for_ad_types = df_show_for_ad_types.rename(columns={'event_type': 'ad_type_show_amount'})

    return df_show_for_ad_types

def get_clickability(df_click_amount_for_ad_types, df_show_amount_for_ad_types):
    # СОЕДИНЯЕМ ТАБЛИЦЫ
    df_cliclability = (pd.merge(df_click_amount_for_ad_types, df_show_amount_for_ad_types, on="Ad_type", how="inner"))

    # И СОЗДАЁМ СТОЛБЕЦ - CTR - показатель кликабельности рекламной компании(100% * кол-во кликов/показы)
    df_cliclability.loc[:, "clickability"] = (
        100*(df_cliclability.loc[:, "ad_type_click_amount"]) / df_cliclability.loc[:, "ad_type_show_amount"])
    df_cliclability = df_cliclability.loc[:, ["Ad_type", "clickability"]]

    return df_cliclability

def get_cpm(advertisement_list, advertisement_info):
    # ОСТАВЛЯЕМ ТОЛЬКО СТРОКИ С ПРОСМОТРАМИ
    df_only_show = advertisement_info.loc[advertisement_info["event_type"] == 'show']

    # ВЫЧИСЛЯЕМ КОЛИЧЕСТВО ПРОСМОТРОВ В КАЖДОЙ РЕКЛАМНОЙ КОМПАНИИ
    df_show_for_ad_key = df_only_show.groupby('ad_key').aggregate({'event_type': 'count'})
    df_show_for_ad_key = df_show_for_ad_key.rename(columns={'event_type': 'show_count'})

    # ТЕПЕРЬ СОПОСТАВЛЯЕМ КОМПАНИЮ, ЕЁ ПРОСМОТРЫ, ЕЁ СТОИМОСТЬ
    df_cpm = pd.merge(df_show_for_ad_key, advertisement_list, left_on="ad_key", right_on="Ad_key", how="left")

    # И СОЗДАЁМ СТОЛБЕЦ - CPM (1000*(СТОИМОСТЬ КОМПАНИИ) / КОЛ-ВО ПРОСМОТРОВ)
    df_cpm.loc[:, "cpm"] = round(
        1000*(df_cpm.loc[:, "Ad_price"]) / df_cpm.loc[:, "show_count"], 0)
    df_cpm = df_cpm.loc[:, ["Ad_key", "cpm"]]

    return df_cpm

def get_expense_of_type(project_costs):
    # ГРУППИРУЕМ РАСХОДЫ КАЖДОГО ТИПА ПО ТИПУ И ГОДУ И СУММИРУЕМ РАСХОДЫ НА КАЖД ГОД
    df_expense = project_costs
    df_expense = df_expense.groupby(['expense_type', 'year'], as_index=False).aggregate({'expense_sum': 'sum'})
    df_type_expense = df_expense.rename(columns={'expense_sum': 'expense_of_type'})
    return df_type_expense


def get_expense_of_source(project_costs):
    # ГРУППИРУЕМ РАСХОДЫ КАЖДОГО ИСТОЧНИКА ПО ИСТОЧНИКУ И КВАРТАЛУ И ВЫЧИСЛЯЕМ СНАЧАЛА СУММУ РАСХОДОВ ПО КАЖД КВАРТАЛУ
    df_expense = project_costs
    df_expense = df_expense.groupby(['expense_source', 'quarter'], as_index=False).aggregate({'expense_sum': 'sum'})

    # ТЕПЕРЬ ГРУППИРУЕМ РАСХОДЫ КАЖДОГО ИСТОЧНИКА ПО ИСТОЧНИКУ И ВЫЧИСЛЯЕМ СРЕДНИЕ РАСХОДЫ ПО КВАРТАЛАМ
    df_mean_expense = df_expense.groupby('expense_source', as_index=False).aggregate({'expense_sum': 'mean'})
    df_mean_expense = df_mean_expense.rename(columns={'expense_sum': 'mean_expense'})

    return df_mean_expense


def get_product_income(subscription_sales):
    # ГРУППИРУЕМ ДОХОДЫ КАЖДОГО ПРОДУКТА ПО ПРОДУКТАМ И СУММИРУЕМ ДОХОДЫ ДЛЯ КАЖД ПРОДУКТА
    df_income = subscription_sales
    df_income = df_income.groupby('product', as_index=False).aggregate({'money': 'sum'})
    df_product_income = df_income.rename(columns={'money': 'income_of_product'})
    return df_product_income


def get_ad_company_efficiency(subscription_sales, advertisement_list):
    # ГРУППИРУЕМ ДОХОДЫ КАЖДОЙ РЕКЛ КОМПАНИИ ПО КОМПАНИИ И СУММИРУЕМ ДОХОДЫ ДЛЯ КАЖД КОМПАНИИ
    df_company_income = subscription_sales
    df_company_income = df_company_income.groupby('ad_key', as_index=False).aggregate({'money': 'sum'})
    df_company_income = df_company_income.rename(columns={'money': 'income'})

    # ТЕПЕРЬ СОПОСТАВЛЯЕМ КОМПАНИЮ, ЕЁ ДОХОД, ЕЁ СТОИМОСТЬ
    df_efficiency = pd.merge(df_company_income, advertisement_list, left_on="ad_key", right_on="Ad_key", how="left")
    # df_efficiency = df_efficiency.loc[:, ["ad_key", "income", "Ad_price"]]

    # И СОЗДАЁМ СТОЛБЕЦ - ЭФФЕКТИВНОСТЬ (100*(ДОХОД КОМПАНИИ - СТОИМОСТЬ КОМПАНИИ) / СТОИМОСТЬ КОМПАНИИ)
    df_efficiency.loc[:, "company_efficiency"] = (
        100*(df_efficiency.loc[:, "income"] - df_efficiency.loc[:, "Ad_price"]) / df_efficiency.loc[:, "Ad_price"])
    df_efficiency = df_efficiency.loc[:, ["ad_key", "company_efficiency"]]

    return df_efficiency