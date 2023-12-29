# # print(advertisement_list)
# # print(advertisement_info.iloc[1, 0])
# # print(advertisement_info.columns)
#
# a = pd.DataFrame({"Ad_type": ['email','social','contextual', 'email', 'contextual', 'contextual'],
#               "Ad_key": ['new_subs','black_friday', 'summer_sale', 'current_clients', 'about_market', 'about_storage'],
#               "Ad_price": ['100','300','10', '400', '1000', '700']})
#
#
# b = pd.DataFrame({"ad_key": ['summer_sale','new_subs','summer_sale', 'current_clients', 'about_market', 'about_market',
#                              'about_market', 'black_friday', 'about_storage', 'summer_sale', 'summer_sale'],
#               "event_type": ['show','show','show', 'click', 'buy', 'buy', 'show', 'click', 'buy', 'click', 'click']})
#
# # d = df_join.loc[:, ["ad_key", "Ad_type", "event_type"]]
#
# def get_click_price_for_ad_types(advertisement_list, advertisement_info):
#     # ОСТАВЛЯЕМ ТОЛЬКО СТРОКИ С КЛИКАМИ
#     df_only_click = advertisement_info.loc[advertisement_info["event_type"] == 'click']
#
#     # ВЫЧИСЛЯЕМ КОЛИЧЕСТВО КЛИКОВ В КАЖДОЙ РЕКЛАМНОЙ КОМПАНИИ
#     df_click_for_ad_key = df_only_click.groupby('ad_key').aggregate({'event_type': 'count'})
#     df_click_for_ad_key = df_click_for_ad_key.rename(columns={'event_type': 'click_count'})
#
#     # СОЕДИНЯЕМ ТАБЛИЦУ КОЛИЧЕСТВА КЛИКОВ И ТАБЛИЦУ ЦЕНЫ РЕКЛАМНЫХ КОМПАНИЙ
#     df_price = advertisement_list
#     df_join = pd.merge(df_click_for_ad_key, df_price, left_on="ad_key", right_on="Ad_key", how="right")
#     # df_join = df_join.loc[:, ["Ad_type", "Ad_key", "click_count", "Ad_price"]]
#
#     # ВЫЧИСЛЯЕМ НОВЫЙ СТОЛБЕЦ С ЦЕНОЙ КЛИКА В КАЖДОЙ РЕКЛАМНОЙ КОМПАНИИ(ПОЛУЧАЕМ ТАБЛИЦУ СО ВСЕМИ ЦЕНАМИ)
#     df_full_price = df_join
#     df_full_price.loc[:, 'Ad_key_price'] = df_price.loc[:, 'Ad_price'] / df_full_price.loc[:, 'click_count']
#     # df_full_price = df_full_price.loc[:, ["Ad_type", 'Ad_key_price']]
#     # df_full_price = df_full_price.fillna(0) # заменяем значения NaN на 0, чтобы не портили вычисления
#
#     # ТЕПЕРЬ ОСТАЛОСЬ ВЫЧИСЛИТЬ ЦЕНУ НА КАЖДЫЙ ТИП РЕКЛАМЫ(ПРОСУММИРУЕМ ЦЕНЫ ВНУТРИ КАЖДОГО ТИПА РЕКЛАМЫ)
#     df_price_click_for_ad_types = df_full_price.groupby('Ad_type', as_index=False).aggregate({'Ad_key_price': 'sum'})
#     df_price_click_for_ad_types = df_price_click_for_ad_types.rename(columns={'Ad_key_price': 'ad_type_price'})
#
#     return df_price_click_for_ad_types
#
# ar_2020 = df_type_expense.loc[df_type_expense["year"]==2020].loc[:, "expense_of_type"]
# ar_2021 = df_type_expense.loc[df_type_expense["year"] == 2021].loc[:, "expense_of_type"]
# ar_2022 = df_type_expense.loc[df_type_expense["year"]==2022].loc[:, "expense_of_type"]
