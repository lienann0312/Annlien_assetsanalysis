# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:42:34 2024

@author: Annlien
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 設定支援中文的字型
rcParams['font.sans-serif'] = ['Microsoft JhengHei']
rcParams['axes.unicode_minus'] = False

#讀取Excel
file_path = 'D:\Backup\Downloads\享容資產.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load data categories and amounts
data = excel_data.parse('工作表1')
categories = data.iloc[:, 0]
amounts = data.iloc[:, 1]

# 第一個項目是薪水，其餘是支出
salary = amounts[0]
expenses = amounts[4:].sum()
balance = salary - expenses

#圓餅圖
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(amounts[1:], labels=categories[1:], autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})

#新增標題文字
ax.set_title("每月支出比例圓餅圖", fontsize=16)
plt.text(0, -1.3, f"餘額: ${balance}", ha='center', fontsize=14, color='blue')
plt.show()
