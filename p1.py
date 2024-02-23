import sys
import time
from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 检验日期
def isVaildDate(qdate):
    try:
        qtime = time.strptime(qdate, "%Y%m%d")
        if qtime < time.strptime(beginTime, "%Y%m%d"):
            print("输入日期需要晚于20140101，请重新输入")
            return False
        elif qtime > time.strptime(date.today().isoformat(), "%Y-%m-%d"):
            print("输入日期还没有发生，请重新输入")
            return False
        return True
    except ValueError:
        print("输入日期的格式不合法哦，请重新输入")
        return False


usedDict = {'GBP': '英镑', 'HKD': '港币', 'USD': '美元', 'CHF': '瑞士法郎', 'GSD': '新加坡元', 'SEK': '瑞典克朗',
            'DKK': '丹麦克朗',
            'NOK': '挪威克朗', 'JPY': '日元', 'CAD': '加拿大元', 'AUD': '澳大利亚元', 'EUR': '欧元', 'MOP': '澳门元',
            'PHP': '菲律宾比索',
            'THP': '泰国铢', 'NZD': '新西兰元', 'KRW': '韩元', 'SUR': '卢布', 'MYR': '林吉特', 'TWD': '新台币',
            'ESP': '西班牙比塞塔',
            'ITL': '意大利里拉', 'NLG': '荷盾', 'BEF': '比利时法郎', 'FIM': '芬兰马克', 'IDR': '印尼卢比',
            'BRL': '巴西里亚尔',
            'AED': '阿联酋迪拉姆', 'INR': '印度卢比', 'ZAR': '南非兰特', 'SAR': '沙特里亚尔', 'TRL': '土耳其里拉'}
beginTime = "20140101"


def main():
    try:
        endTime, moneyCode = sys.argv[1:3]
    except ValueError:
        print('输入参数错误，请检查格式')
        return

    if not isVaildDate(endTime):
        return
    if moneyCode not in usedDict:
        print('无效的货币代码，请重新运行')
        return

    # 实例化一款浏览器
    bor = webdriver.Chrome()

    # 对指定的url发起请求
    bor.get('https://www.boc.cn/sourcedb/whpj/')
    sleep(1)

    # 设置起始时间
    beginTimeInput = bor.find_elements(By.CLASS_NAME, "search_ipt")[1]
    beginTimeInput.clear()
    beginTimeInput.send_keys(beginTime)

    # 初始化下拉框
    pjname = bor.find_element(By.NAME, "pjname")
    select = Select(pjname)

    # 设置结束时间
    endTimeInput = bor.find_elements(By.CLASS_NAME, "search_ipt")[2]
    endTimeInput.clear()
    endTimeInput.send_keys(endTime)

    # 选择对应的货币
    select.select_by_value(usedDict[moneyCode])

    # 点击搜索
    bor.find_elements(By.CLASS_NAME, "search_btn")[1].click()

    # 找到对应条目
    tbody = bor.find_elements(By.TAG_NAME, "tbody")[1]
    tr = tbody.find_elements(By.TAG_NAME, "tr")[1]
    td = tr.find_elements(By.TAG_NAME, "td")
    print(td[3].text)

    bor.quit()


main()
