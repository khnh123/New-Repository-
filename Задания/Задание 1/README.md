# Read Me Template

![](https://user-images.githubusercontent.com/48917675/80397153-91aa7600-886a-11ea-97be-60d3e5430aa2.jpg)

> This is a ReadMe template to help save you time and effort.

---
### Installing

1. bestchange_web_scraper - Scrapes the webpaage and returns a dictionary with data
```
201: {'Обменик': 'A-Exchange', 'Статус': 'Работает', 'Резервы': '$71 269', 'Курсов': '373', 'WMBL': '—', 'ACTS': '1', 'PMTS': '2028', 'Негативгые_Отзывы': '0', 'Позитивные_Отзывы': '375', 'ID': '218', 'Отзывы': 'https://www.bestchange.ru/a-exchange-exchanger.html'}, 202: {'Обменик': 'FlyChange', 'Статус': 'Работает', 'Резервы': '$1 476 050', 'Курсов': '22', 'WMBL': '2151', 'ACTS': '—', 'PMTS': '—', 'Негативгые_Отзывы': '0', 'Позитивные_Отзывы': '374', 'ID': '660', 'Отзывы': 'https://www.bestchange.ru/flychange-exchanger.html'}, 203: {'Обменик': 'BTCstaff', 'Статус': 'Работает', 'Резервы': '$27 023', 'Курсов': '380', 'WMBL': '—', 'ACTS': '1', 'PMTS': '171', 'Негативгые_Отзывы': '0', 'Позитивные_Отзывы': '370', 'ID': '805', 'Отзывы': 'https://www.bestchange.ru/btcstaff-exchanger.html'}, 
```
2. 2_db_sqlite - Create, Update SQLite3

Create: 
```
create_table - create database
data_entry - inserts data from .sql file 
create_insert_commands - creates .sql file with "insert" requests
```
INSERT INTO mytable ( `Обменик`, `Статус`, `Резервы`, `Курсов`, `WMBL`, `ACTS`, `PMTS`, `Негативгые_Отзывы`, `Позитивные_Отзывы`, `ID`, `Отзывы` ) VALUES ( 'NetEx24', 'Работает', '$726 378', '216', '—', '—', '1930', '0', '16862', '546', 'https:__www.bestchange.ru_netex24-exchanger.html' );
INSERT INTO mytable ( `Обменик`, `Статус`, `Резервы`, `Курсов`, `WMBL`, `ACTS`, `PMTS`, `Негативгые_Отзывы`, `Позитивные_Отзывы`, `ID`, `Отзывы` ) VALUES ( 'WmExpress', 'Работает', '$105 187', '385', '—', '—', '—', '0', '12402', '528', 'https:__www.bestchange.ru_wmexpress-exchanger.html' );
```
```
Update: 
```
updateSqliteTable - updates database
```
