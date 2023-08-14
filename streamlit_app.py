import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  #take the json version of the respnse and normalize it.
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error('Please select a fruit to get information')
  else:
    back_from_fucntion = get_fruityvice_data(fruit_choice)
    #output it on the screen as a table
    streamlit.dataframe(back_from_function)          
except URLError as e:
  streamlit.error()

streamlit.header('The Fruit Load List Contains')
def get_fruit_load_list():
  with my_connection.cursor() as my_cur:
       my_cur.execute('select * from fruit_load_list')
       return my_cur.fetchall()
if streamlit.button('Get Fruit Load List'):
  my_connection = snowflake.connector.connect(**streamlit.secrets['snowflake'])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)

#allow end user to add fruit from fruitlist
def insert_row_snowflake(new_fruit):
  with my_connection.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values('from streamlit')")
       return 'Thanks for adding' + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
   my_connection = snowflake.connector.connect(**streamlit.secrets['snowflake'])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)

