import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('Brakfast Menu')

streamlit.text('🥗 Omega-3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hardboiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# let's put a pick list 
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index) )
#display the table on the page..
streamlit.dataframe(my_fruit_list)
