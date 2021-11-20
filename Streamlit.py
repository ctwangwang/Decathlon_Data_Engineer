#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:01:45 2021

@author: wangkaiyuan
"""
#Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('data/Decathlon_Data_Engineer.sqlite')
#conn = sqlite3.connect('data/transaction_detail.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


store_dim = ['store_id,', 'store_name,', 'store_lat_coordinate,', 'store_lon_coordinates']
transaction_detail = ['transaction_id_hash,', 'sgtin_hash,', 'type_detail,', 'transaction_date']
store_features = ['Store Name,', 'Average Distance,', 'Number of Sport,', 'Top 1 Accessible Sport,', 'Top 2 Accessible Sport,', 'Top 3 Accessible Sport']




def main():
	st.title("SQLPlayground")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.expander("Table Info"):
				table_info = {'store_dim':store_dim,'transaction_detail':transaction_detail,'store_features':store_features}
				st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
		st.subheader("About")





if __name__ == '__main__':
	main()