import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents New Healthy Dinner')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('Brakfast Menu')

streamlit.text('🥗 Omega-3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hardboiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast nnnnn')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# let's put a pick list 


fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'] )
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page..
streamlit.dataframe(fruits_to_show)
#========frutivice code..
#==== create a repeatable code block
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  
  return fruityvice_normalized
  

#=====
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit you like information about?')
  if not fruit_choice or fruit_choice == '':
    streamlit.error("Please select a fruit to get information..")
  else:
    #streamlit.write('User entered',fruit_choice)
    back_from_function = get_fruityvice_data(fruit_choice)
    # streamlit.text(fruityvice_response.json())
    # Displays data as a table
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()


# =====SNOWFLAKE PART part
streamlit.header("View Our Fruit List - Add Your Favourates!")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()

# add a button to load a list 
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  

# add a button to add a fruit 
def insert_row_snow_flake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit  + "')")
    my_cnx.close()
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input("What fruit you would like to add?" )

if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snow_flake(add_my_fruit)
  streamlit.text(back_from_function) 
streamlit.stop()    

streamlit.write('Thanks for adding:', add_my_fruit)
# this code will not work ..
my_cur.execute("insert into fruit_load_list values ('frmo streamlit')")




