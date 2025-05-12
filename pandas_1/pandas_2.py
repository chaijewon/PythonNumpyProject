import numpy as np
import pandas as pd

# GROUP BY
# COUNT => deptno
"""
  SELECT deptno,COUNT(*) FROM emp
  GROUP BY deptno
"""
emp_df=pd.read_csv('c:/pydata/EMP.csv')
print(emp_df.groupby('DEPTNO')['SAL'].mean())
print(emp_df.groupby('DEPTNO')['SAL'].sum())
print(emp_df.groupby('DEPTNO')['SAL'].max())
print(emp_df.groupby('DEPTNO')['SAL'].min())

print(emp_df.groupby('DEPTNO')['SAL'].agg(['mean','max','sum','min']))
# JOIN
