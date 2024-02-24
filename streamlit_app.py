import streamlit
import pandas
import requests

import snowflake.connector
from urllib.error import URLError


streamlit.title("My parents' new healthy dinner")

streamlit.header("Breakfast menu")
streamlit.text("Omega 3 and blueberry oatmeal")
streamlit.text("Kale, Spinach & Rocket Smoothie")
streamlit.text("Hard-boiled three-ranged egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  return pandas.json_normalize(fruityvice_response.json())

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fuit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  streamlit.error()

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

if streamlit.button('Get Fruit Load List'):
  streamlit.header("The fuir load list contains:")
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

streamlit.stop()
fruit_add = streamlit.text_input('What fuit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', fruit_add)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
