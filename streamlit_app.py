import streamlit
import pandas
import requests
import snowflake.connector


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


fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'] )
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page..
streamlit.dataframe(fruits_to_show)
#========frutivice code..
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
# take the json version of the of the response and normalise it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json())
# Displays data as a table
streamlit.dataframe(fruityvice_normalized)

# snowflake part
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains::")
streamlit.text(my_data_row)
