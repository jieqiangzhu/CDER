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
pd.to_csv('file.csv')
pd.to_excel('file.xlsx',sheet_name='Sheet1')
```

## Selection

## Boolean Indexing 

## Pivotal 
