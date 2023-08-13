import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-boiled Free Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🍓Build Your Own Fruit Smoothie🥤🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#add a pick list here so they can pick the fruits they want to include
streamlit.multiselect('Pick Some Fruits:', list(my_fruit_list))

#display the table on the page
streamlit.dataframe(my_fruit_list)




