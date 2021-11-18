#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:35:58 2021

@author: wangkaiyuan
"""

create table txn_analysis(
transaction_id_hash varchar(max),
sgtin_hash varchar(max),
type_detail varchar(max),
transaction_date datetime,
store_id integer);

copy txn_analysis from 's3://ctwangwang2/transaction_detail.csv' access_key_id 'AKIARTKBCKW62KDKJGSC' secret_access_key '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' delimiter ',' IGNOREHEADER 1 TIMEFORMAT 'auto';


select store_id, avg(avg_days) as avg_store_fluidity from 
(
select store_id, sgtin_hash, ROUND(DATEDIFF(day,min(transaction_date), max(transaction_date)) * 1.0/count(*),2) as avg_days,DATEDIFF(day,min(transaction_date), max(transaction_date)) as date_diff, count(*) as num_record from txn_analysis group by store_id, sgtin_hash
) as table_store_prod group by store_id order by store_id;