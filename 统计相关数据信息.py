import pandas as pd
id_date = 31
all = open('汇总.csv',mode='w',encoding='utf-8')
all.write('driver_id' + ',' + 'order_num' + ',' + 'id_date' + ',' + '平均订单长度'+'详情'+'\n')
while id_date <= 31:
    driver = open('E:/滴滴数据处理程序/单个司机数据文件/10-'+str(id_date)+'/大于25的司机id10-'+str(id_date)+'.txt',mode='r')
    for driver_id in driver:
        driver_id = driver_id.rstrip('\n')
        with open('E:/滴滴数据处理程序/单个司机数据文件/10-'+str(id_date)+'/司机' + driver_id + '.csv', mode='r', encoding='utf-8') as driver_jilu:
            y = pd.read_csv(driver_jilu)
            len_of_order = []
            order_len = 0
            order_id = y.values[0][1]
            for i in range(1,len(y)):
                if order_id == y.values[i][1]:
                    order_len += 1
                else:
                    len_of_order.append({order_id: order_len})
                    order_id = y.values[i][1]
                    order_len = 0
            print('司机' + str(driver_id) + ':')
            print(len_of_order)

            all.write(driver_id + ',' + str(len(len_of_order)) + ',' + str(id_date) + ',' + str(len(y)/len(len_of_order))+','+str(len_of_order)+'\n')
    id_date += 1
all.close()