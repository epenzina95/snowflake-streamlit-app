import streamlit
import pandas

streamlit.title("My parents' new healthy dinner")

streamlit.header("Breakfast menu")
streamlit.text("Omega 3 and blueberry oatmeal")
streamlit.text("Kale, Spinach & Rocket Smoothie")
streamlit.text("Hard-boiled three-ranged egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
