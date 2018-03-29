
# monkey
跑Monkey后把日志中的error项转换为Excel表格指导说明:

1、解压xlwt-1.0.0，然后把解压后的文件夹放到python安装文件夹的根目录下面
2、在xlwt-1.0.0文件夹中的setup.py文件路径下，在命令行中输入 python setup.py install
3、把analynsis.py、write_excel.py和导出的monkeyResult文件夹放在同一路径下
4、运行analynsis.py脚本，本地就会生成logresult.xls文件