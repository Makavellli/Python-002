import pandas as pd
import os

# 获得当前程序执行路径
get_pwd=os.path.dirname(os.path.realpath(__file__))

# 1. SELECT * FROM data;   查询data表中的所有数据

# 加载、读取、打印数据文件
data=os.path.join(get_pwd,'data2.csv')
df_data=pd.read_csv(data)

# 2. SELECT * FROM data LIMIT 10;    查询前10条数据
pre10_data=df_data[0:10]

# 3. SELECT id FROM data;  //id 是 data 表的特定一列  查询data表中列名是id的所有数据

# 为数据增加列名
df_data.columns=['name','id','age']
# 获取列名是id的数据
get_id_data=df_data['id']

# 4. SELECT COUNT(id) FROM data; 获取文件总行数
all_count=len(df_data) ### df_data.shape[0]

# 5. SELECT * FROM data WHERE id<1000 AND age>30; 查询 id小于1000 并且年龄大于30的数据

get_id_data_1=df_data[(df_data['id']<1000)&(df_data['age']>30)]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;  先对order_id字段进行去重操作，后分组并统计数量

group_data1=(df_data.groupby('id')['age'].nunique())

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id; 通过id进行内连接关联查询
#加载user表数据
user_data=os.path.join(get_pwd,'user.csv')
df_user_data=pd.read_csv(user_data)
df_user_data.columns=['user_name','user_id','dept_id']

#加载dept表数据
dept_data=os.path.join(get_pwd,'dept.csv')
df_dept_data=pd.read_csv(dept_data)
df_dept_data.columns=['dept_id','dept_name','dept_code']

#### 增加列头后第一行数据为啥没有了。。。。。

join_data=pd.merge(df_user_data, df_dept_data)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2; 合并两张表

union_data=pd.concat([df_user_data,df_dept_data],ignore_index=True).drop_duplicates()
# print(union_data)

# 9. DELETE FROM table1 WHERE id=10; 删除id等于10的记录
# print(df_data)
df_delete=df_data.drop(df_data[df_data['id']==10].index)
# print(df_delete)
# 10. ALTER TABLE table1 DROP COLUMN column_name; 删除table1的某一列
df_delete_column=df_data.drop(columns=['id'])
# print(df_delete_column)