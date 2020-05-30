# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.8
# ---

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('PS') 
import matplotlib.pyplot as plt
import time
import datetime
import filterbyip as fbi
import Cdf
import Pmf

quic = pd.read_csv('./data/pi-1/strace/quic_strace.csv',',')
tcp = pd.read_csv('./data/pi-1/strace/tcp_strace.csv',',')

quic.head()

quic.tail()

tcp.head()

tcp.tail()

sum_row = {col: quic[col].sum() for col in ['%time','seconds','calls']}
print(sum_row)

sum_row = {col: tcp[col].sum() for col in ['%time','seconds','calls']}
print(sum_row)
