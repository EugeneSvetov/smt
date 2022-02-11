# # кол-во повторяющихся строк (по имени столбца)
# select column_name, count(column_name)
#   from table
# group by column_name
# having count (column_name) > 1;
#
# # показать индексы схемы бд
# select TABLE_NAME, count(*)
#   from all_indexes
# where owner = 'OWNER_NAME' or table_owner = 'TABLE_OWNER'
# group by TABLE_NAME
# order by TABLE_NAME;
#
# # показать самые затратные запросы
# select
#      st.TEXT AS QueryName,
#      wt.execution_count AS ExecutionCount,
#      wt.total_worker_time/1000000 AS TotalCpuTimeInSeconds,
#      wt.total_worker_time/wt.execution_count/1000 AS AverageCpuTimeInMs],
#      qp.query_plan,
#      DB_NAME(st.dbid) AS [Database Name]
# from
#     (select top 10
#           qs.execution_count,
#           qs.total_worker_time
#             from sys.dm_exec_query_stats qs
#      order by qs.total_worker_time desc) wt
#
# cross apply sys.dm_exec_sql_text(plan_handle) st
# cross apply sys.dm_exec_query_plan(plan_handle) qp
# order by wt.total_worker_time desc;
#
# # мониторинг юзания индекса
# ALTER INDEX INDEX_NAME MONITORING USAGE;
# select *
# from
#   v$object_usage view
#
# # count(1) > count(*)
# select
#   count(1) from big_table;
#
# # when > if-then-else
# select column1, column2,
#        case when price >= 100 then '1'
#             when price between 90 and 99 then '2'
#             else 'Other case' end price_type
# from table
#
# # OTB
# with CTE_NAME as (
#   select name
#     from table
#   where condition1 < 1000 and ...
# )
#
# select *
#   from other_table
# where name in (SELECT name from CTE_NAME)