# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:50:33 2016

@author: pnadolny
"""

#from lxml import html
import requests

page = requests.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
tree = html.fromstring(page.content)

# //*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[3]/table
#<span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.0.0">Nov 18, 2016</span>
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#table = tree.xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[3]/table/tbody')
#table = tree.xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[3]/table/tbody/tr[1]')

#//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[3]/table/tbody/tr[1]
#<tr class="BdT Bdc($lightGray) Ta(end) Fz(s)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0"><td class="Py(10px) Ta(start)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.0"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.0.0">Nov 18, 2016</span></td><td class="Py(10px)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$open"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$open.0">109.72</span></td><td class="Py(10px)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$high"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$high.0">110.54</span></td><td class="Py(10px)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$low"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$low.0">109.66</span></td><td class="Py(10px)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$unadjclose"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$unadjclose.0">110.06</span></td><td class="Py(10px)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$close"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.1:$close.0">110.06</span></td><td class="Py(10px)" data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.$volume"><span data-reactid=".11l4hdy3cxc.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.2.$history-table.1.$0.$volume.0">27,404,300</span></td></tr>
#<div title="buyer-name">Carson Busses</div>

#//div[@title="buyer-name"]/text()
print (page.prettify()[0:1000])

print (page)