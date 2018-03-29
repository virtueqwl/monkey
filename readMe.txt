操作步骤：
1 配置好环境变量;
2 Whitelist.txt 里面放入需要测试的应用apk包名；
3 双击monkey.py 可进行monkey测试；
4 测试完成，手机连上电脑adb，运行PullLog.py 导出monkey日志及报错信息；
5 运行analynsis.py ，生成 excel 的结果文档

备注：设置monkey测试时长通过设置monkey的点击时间，monkeyAll.sh里面的 -v -v -v  后面的数字，时长对应的次数如下：

0.5h=25000  2h=100000  6h= 300000  
12h=600000  24h=1200000  72h=3600000

跑Monkey后把日志中的error项转换为Excel表格指导说明:

1、解压xlwt-1.0.0，然后把解压后的文件夹放到python安装文件夹的根目录下面
2、在xlwt-1.0.0文件夹中的setup.py文件路径下，在命令行中输入 python setup.py install
3、把analynsis.py、write_excel.py和导出的monkeyResult文件夹放在同一路径下
4、运行analynsis.py脚本，本地就会生成logresult.xls文件
