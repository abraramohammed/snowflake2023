import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-boiled Free Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🍓Build Your Own Fruit Smoothie🥤🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add a pick list here so they can pick the fruits they want to include
fruits_selected = streamlit.multiselect('Pick Some Fruits:', list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(my_fruit_list)

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What frui would you like information about?','kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen

#take the json version of the respnse and normalize it.
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it on the screen as a table
streamlit.dataframe(fruityvice_normalized)



