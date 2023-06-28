
# Dish-based-Restraurant-Recommendation-webApp

Template based django search application that search through the names of dishes and recommend the best match of restaurant offering the same.
The project is developed using Django Framework and SQLite db.

I have made a model to make db.
Installed SQLite in my machine and used it to import the data from Restraurants_small.csv to existing db(in my case dish_dish).

To run this project you have to install django and to visualize the sqlite db either install db browser for sqlite of in visual studio code add extension named SQLite.




## Installation

To install django you can do

```bash
   pip install django
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/chandani7021/Dish-based-Restraurant-Recommendation-webApp.git
```

Go to the project directory

```bash
  cd my-project
```

Install libraries

```bash
   pip install -r requirements.txt
```

To run 

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```




## Screenshots

Here are screenshorts of working of App

search results for momos with Name of Restaurants, its location, The variety of dishes they offer with price.

![search (2)](https://github.com/chandani7021/Dish-based-Restraurant-Recommendation-webApp/assets/69253701/4373ac7f-4c4a-4597-9bf0-3373167e3859)




search results for French Fries with Name of Restaurants, its location, The variety of dishes they offer with price.
![search (1)](https://github.com/chandani7021/Dish-based-Restraurant-Recommendation-webApp/assets/69253701/b5365454-7fac-4659-9f8f-20ac6d345105)

