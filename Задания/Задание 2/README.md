# Read Me

![Screenshot_1](https://user-images.githubusercontent.com/48917675/81112680-e3d74100-8ed3-11ea-854b-675da3414e97.jpg)

---
### Run

Задание 2
1. takes user's input

//2. Adds data to DataFrame

//3. Appends Dataframe to .csv file

2. finds name of the exchanger in the database
3. extracts link
4. Opens webpage
5. Opens review form
6. Fills in the review form
7. Presses submit
---

### Functions, Files

Задание_2.py:
- is_valid_email(email) -  check if email is valid
- user_input() - Takes User Input, returns list 
- listToDict(list1) - converts list to dict, coloms are predefined 

//add_to_df() - Add row (user input) to Dataframe 
//append_to_csv - append user input to .csv file
//return_data_as_html_table() 

_3_db_sqlite.py:
- create_connection(db_file) 
- extract_link(exchanger_name, table, cur) - returns link from the database
- get_table_names(cur) - get the name of the table

//print_all
//get_colomns(cur, table) - returns list of colomns


executeJS_on_webpage.py:
- post_review(payload, url) - automatically fills out the review form

---

## User Input
```
ID обменника в системе blockchain: 324qt2323
Имя : Name
email: email
Enter Valid email: email@gmail.com
текст отзыва: Review
номер обмена: 34t234
(1 - положительный, 2 -нейтральный, 3 - отрецательный)
тип отзыва: 2
```
## JS Commands
![form input 2](https://user-images.githubusercontent.com/48917675/81111861-97d7cc80-8ed2-11ea-9680-d3ef8b0597bf.jpg)
![form input](https://user-images.githubusercontent.com/48917675/81111872-9b6b5380-8ed2-11ea-8be0-d2eac1052afb.jpg)

## .CSV file
![adfgvd](https://user-images.githubusercontent.com/48917675/80627132-49bf5680-8a04-11ea-87d9-31ccff4bdab0.jpg)


## Visualize Data as html
def return_data_as_html_table() - function

df_style.css - file for styling
![adf](https://user-images.githubusercontent.com/48917675/80627428-bb97a000-8a04-11ea-8012-7b703c0b2050.jpg)



