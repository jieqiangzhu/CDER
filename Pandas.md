# Pandas

## I/O
### Import

```Python
pd.read_csv('file.csv',header=None, nrow=5)  # import from csv files
pd.read_table(filename)  #从限定分隔符的文本文件导入数据
pd.read_excel('file.xlsx','sheet1',header = None)  # import from excel files
pd.read_sql(query, connection_object)  #从SQL表/库导入数据
pd.read_json(json_string)  #从JSON格式的字符串导入数据
pd.read_html(url)  #解析URL、字符串或者HTML文件，抽取其中的tables表格
pd.read_clipboard()  #从你的粘贴板获取内容，并传给read_table()
pd.DataFrame(dict)  #import form dict，Key is the column name，Value is the data

```


### Output

```Python
df.to_csv(filename)  #导出数据到CSV文件
pd.to_excel('file.xlsx',sheet_name='Sheet1')  #导出数据到Excel文件
df.to_sql(table_name, connection_object)  #导出数据到SQL表
df.to_json(filename)  #以Json格式导出数据到文本文件
```

## Selection
```Python
df[col]  #根据列名，并以Series的形式返回列
df[[col1, col2]]  #以DataFrame形式返回多列
s.iloc[0]  #按位置选取数据
s.loc['index_one']  #按索引选取数据
df.iloc[0,:]  #返回第一行
df.iloc[0,0]  #返回第一列的第一个元素
```
## Boolean Indexing 

## Pivotal 
