# TestJDRegisterApi
利用Excel和Python写的一个半自动Web接口测试脚本


### 实现方法

- 语言为Python2.7
- 采用Excel表格来管理测试数据，包括用例、测试数据录入、测试结果呈现，目前暂时只实现了半自动化，还需要部分的手工录入数据
- 测试的对象主要是Web接口，采用Python的Requests来进行接口的调用

### Excel表格样式

![](http://oayp1enl0.bkt.clouddn.com/TestWebApiExcel.jpg)


### 说明

- Excel文件夹中TestCreatExcel.py实现了读取Excel测试数据，写入测试结果，用了Python的xlrd来读取Excel文件，开始时尝试了xlwt来写入数据，但是发现xlwt只能新建文件，新建表格样式，无法在已存在的Excel中写入数据。于是采用xlutils来写入文件，这个库主要实现了xlrd和xlwt之间管道的功能，打开文件利用了xlrd的open_wordbook方法，写入数据后保存。具体代码实现如下

```

from xlrd import open_workbook
from xlutils.copy import copy


rb = open_workbook('TestRegister.xls')
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(4, 4, 'Test')
wb.save('TestRegister.xls')

```

- 为了测试数据的完整性和正确性，每个测试用例跑50次，因为实例代码以京东注册Api为测试项目，为了不对京东服务器造成影响，每次访问url时sleep1秒。
- 多线程采用了Python自带的threadpool，实例代码开启了5个线程
- 测试过程中利用了Python的logging库，记录了线程启动、运行报错等日志信息，代码在log文件夹下，保存的日志文件在TestRegister文件夹下。
- 示例代码只测试了京东用户名检测的Api接口，后台抓包发现接口需要传递regName和pin两个参数，值都为输入的用户名。以此设计了7个测试用例
- 输出的测试结果又三个参数，程序成功运行、Api正确响应、返回正确结果的比。

### 未来需要完善的

- 将TestCreatExcel方法的功能的完善，如测试表格的自动创建、定义样式、用例数据的输入，Excel、日志文件的管理备份，以适用在不同的环境下，而不只限于Web接口测试
- 多线程压力测试方法实现的改善