import pandas as pd
# print(pd.__version__)

# data = {
#     'Name' : ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
#     'Age' : [28, 24, 35, 32, 45],
#     'City' : ['New York', 'Paris', 'Berlin', 'London', 'Tokyo'],
#     'Salary' : [50000, 65000, 75000, 85000, 600000]
# }

# df = pd.DataFrame(data)
# print(df)

# # 기본 속성
# print("크기(행, 열) : ", df.shape)
# print("열 이름 : ", df.columns)
# print("행 인덱스 : ", df.index)
# print("데이터 타입 : ", df.dtypes)

# # 데이터 확인
# print("처음 2행\n : ", df.head(2))
# print("마지막 2행\n : ", df.tail(2))
# print("기본 통계량\n : ", df.describe())

# # 데이터 접근
# print("'Age' 열 : \n", df['Age'])
# print("여러 열 선택 : \n", df[['Name', 'Salary']])
# print("첫 3행 : \n", df.iloc[0:3])
# print("조건부 선택 : \n", df[df['Age'] > 30])

# # 데이터 수정
# df['Age'] = df['Age'] + 1
# print("모든 나이에 1 추가 : \n", df)
# df['Country'] = ['USA', 'France', 'Germany', 'UK', 'Japn']
# print("새 열 추가 : \n", df)
# df.loc[5] = ['Charlie', 29, 'Sydney', 70000, 'Australia']
# print("새 행 추가 : \n", df)
# df.drop('Country', axis=1, inplace=True)
# df.drop(5, axis=0, inplace=True)
# print("열 삭제 : \n", df)
# print("행 삭제 : \n", df)

# 데이터 선택(Selecting)과 필터링(Filtering)

# # 샘플 DataFrame 생성 
# df = pd.DataFrame({
#     'Name' : ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
#     'Age' : [28, 24, 35, 32, 45],
#     'City' : ['New York', 'Paris', 'Berlin', 'London', 'Tokyo'],
#     'Salary' : [50000, 65000, 75000, 85000, 600000],
#     'Department' : ['IT', 'HR', 'IT', 'Finance', 'Maketing']
# })

# print("단일 열 선택 (Series 반환) : ")
# print(df['Name'])

# # 여러 열 선택
# print("\n여러 열 선택 (DataFrame 반환) : ")
# print(df[['Name', 'Salary']])

# # 행 선택(위치 기반)
# print("\n처음 3행 선택 : ")
# print(df.iloc[0:3])

# # 행 선택(레이블 기반)
# print("\n인덱스 1, 3, 4 행 선택 : ")
# print(df.loc[1, 3, 4])

# # 특정 행과 열 동시 선택
# print("\n첫 2행의 'Name'과 'Age' 열 : ")
# print(df.loc[0:1, ['Name', 'Age']])

# # 조건부 필터링
# print("\n30세 이상인 직원 : ")
# print(df[df['Age'] >= 30])

# # 다중 조건 필터링
# print("\nIT 부서의 30세 이상 직원 : ")
# print(df[(df['Age'] >= 30) & (df['Department'] == 'IT')])

# # 값 존재 여부 필터링
# print("\n도쿄나 런던에 사는 직원 : ")
# print(df[(df['City'] >= 30) & (df['Tokyo', 'London'])])

# ------------------------ #

# 데이터 프레임 GroupBy
# df = pd.DataFrame({
#     'Department' : ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT'],
#     'Employee' : ['Alice', 'bob', 'Charlie', 'David', 'Eve', 'Frank'],
#     'Salary' : [75000, 65000, 85000, 90000, 60000, 78000],
#     'Age' : [28, 35, 32, 45, 30, 29],
#     'Year' : [2021, 2022, 2021, 2022, 2021, 2022]
# })

# # 기본 groups 연산
# dept_groups = df.groupby('Department')
# print("부서별 평균 급여 : ")
# print(dept_groups['Salary'].mean())

# # 다중 열 기준 그룹화
# year_dept_groups = df.groupby(['Year', 'Department'])
# print("\n연도별, 부서별 평균 급여 : ")
# print(year_dept_groups['Salary'].mean())

# # describe()는 각 그룹별로 기본 통계량(개수, 평균, 표준편차, 최소값, 25%, 50%, 75%, 최대값)을 제공함
# print("\n부서별 급여 통계 요약 : ")
# print(dept_groups['Salary'].describe())

# # agg 메소드로 다양한 집계 함수 적용
# print("\n여러 집계 함수 적용: ")
# print(dept_groups['Salary'].agg(['count', 'mean', 'sum', 'std', 'min', 'max']))
# # egg와 describe 차이점
# # - egg : 사용자가 원하는 집계 함수들을 직접 선택하여 적용
# # - describe : 미리 정의된 통계 요약 정보를 제공 ('count', 'mean', 'sum', 'std', 'min', 'max')

# # 열마다 다른 집계 함수 적용
# print("\n열별 다른 집계 함수 : ")
# print(dept_groups.agg({
#     'Salary': ['mean', 'max'],
#     'Age': ['mean', 'max', 'max']
# }))

# # transform 메소드 : 그룹 통계를 원본 데이터 크기로 변환
# # transform()은 그룹별 집계 결과를 원본 DataFramer과 같은 크기로 확장하여 반환
# df['Dept_Avg_Salary'] = dept_groups['Salary'].transform('mean')
# print("\n각 직원의 급여와 부서 평균 급여 : ")
# print(df[['Employee', 'Department', 'Salary', 'Dept_Avg_Salary']])

# # filter 메소드 : 그룹 조건에 따라 필터링
# high_salary_depts = dept_groups.filter(lambda x: x['Salary'].mean() > 70000)
# print(high_salary_depts)

# # get_group 메소드 : 특정 그룹 선택
# print("\nIT 부서 직원 : ")
# print(dept_groups.get_group('IT'))

# # ------------------------ #

# # 데이터 프레임 GroupBy 고급

# # 1. 시간 기반 그룹화(월별, 분기별, 연도별)
# df['Date'] = pd.date_range(start='2022-01-01', periods=len(df), freq='M')
# print("\n월별 평균 급여 : ")
# print(df.groupby(df['Date'].dt.month)['Salary'].mean())

# print("\n분기별 평균 급여 : ")
# print(df.groupby(df['Date'].dt.quarter)['Salary'].mean())

# # 2. 연속 변수의 범주화 후 그룹화(구간별 그룹)
# df['Age_Group'] = pd.cut(df['Age'], bins=[20, 30, 40, 50], labels=['20대', '30대', '40대'])
# print("\n연령대별 평균 급여 : ")
# print(df.groupby('Age_Group')['Salary'].mean())

# # 3. 크기 기반 분위수로 그룹화
# df['Salary_Quantile'] = pd.qcut(df['Salary'], q=3, labels=['Low', 'Medium', 'High'])
# print("\n급여 부위수별 평균 나이: ")
# print(df.groupby('Salary_Quantile')['Age'].mean())

# # 4. 사용자 정의 함수로 그룹화
# # apply() 메소드와 사용자 정의 함수를 결합하여 복잡한 그룹과 기준을 만들 수 있음
# def seperience_level(age):
#     # 나이를 기준으로 경력 수준을 분류하는 함수
#     if age < 30:
#         return 'Junior'
#     elif age < 40:
#         return 'Mid-level'
#     else:
#         return 'Senior'
    
# df['Experience'] = df['Age'].apply(seperience_level)
# print("\n경력 수준별 평균 급여 : ")
# print(df.groupby('Experience')['Salary'].mean())

# # # ------------------------ #

# # # 데이터 프레임 정렬 메서드
# df = pd.DataFrame({
#     'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
#     'Score' : [85, 92, 96, 88, 73],
#     'Attendance' : [95, 80, 90, 75, 85, 92]
# })

# # 점수 기준 상위 3명
# print("점수 기준 상위 3명 : ")
# print(df.nlargest(3, 'Score'))

# # 출석률 기준 하위 2명
# print("\n출석률 기준 하위 2명 : ")
# print(df.nsmallest(2, 'Attendance'))

# # 여러 열 기준 정렬(다중 기준)
# print("\n점수와 출석률 모두 높은 상위 3명 : ")
# print(df.nlargest(3, ['Score', 'Attendance']))

# # sort_values 메소드
# print("\n점수 기준 내림차순 정렬 : ")
# print(df.sort_values('Score', ascending=False))

# print("\n여러 열 기준 정렬 (점수, 내림차순, 출석률 오름차순) : ")
# print(df.sort_values(['Score', 'Attendance'], ascending=[False, True]))

# # 상관관계 및 공분산
# print("\n점수와 출석률의 상관관계 : ")
# print(df[df['Score', 'Attendance']].corr)
# print("\n점수와 출석률의 공분산 : ")
# print(df[df['Score', 'Attendance']].cov)

# # 데이터 병합
# # 샘플 데이터 : 고객 정보
# customers = pd.DataFrame({
#     'customer_id' : [1, 2, 3, 4, 5],
#     'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'email' : ['alice@example.com', 'bob@example.com', 'charlie@example.com',
#                'david@example.com', 'eve@example.com']
# })

# # 샘플 데이터 : 주문 정보
# orders = pd.DataFrame({
#     'orders_id' : [101, 102, 103, 104, 105],
#     'customer_id' : [1, 2, 3, 6, 7],
#     'product' : ['Laptop', 'Phone', 'Tablet', 'Monitoer', 'Keyboard'],
#     'amount' : [1200, 800, 450, 300, 80]
# })

# print("고객 정보 : ")
# print(customers)
# print("\n주문 정보 : ")
# print(orders)

# # 내부 조인(Inner Join) : 양쪽 모두에 있는 데이터만
# inner_join = pd.merge(customers, orders, on='customer_id')
# print("\n내부 조인(고객 + 주문) : ")
# print(inner_join)

# # 왼쪽 조인(Left Join) : 왼쪽 데이터 프레임의 모든 행 포함
# left_join = pd.merge(customers, orders, on='customer_id', how='left')
# print("\n왼쪽 조인(모든 고객, 주문 없으면 NaN) : ")
# print(left_join)

# # 오른쪽 조인(Right Join) : 오른쪽 데이터 프레임의 모든 행 포함
# right_join = pd.merge(customers, orders, on='customer_id', how='right')
# print("\n오른쪽 조인(모든 고객, 주문 없으면 NaN) : ")
# print(right_join)

# # 외부 조인(Outer Join) : 양쪽 데이터 프레임의 모든 행 포함
# outer_join = pd.merge(customers, orders, on='customer_id', how='outer')
# print("\n외부 조인(모든 고객 및 주문) : ")
# print(outer_join)

# ------------------------ #

# 데이터 연결
# 데이터프레임 2개 생성
df1 = pd.DataFrame({
    'A' : ['A0', 'A1', 'A2'],
    'B' : ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'A' : ['A3', 'A4', 'A5'],
    'B' : ['B3', 'B4', 'B5']
})

print("DataFrame 1 : ")
print(df1)
print("\nDataFrame 2 : ")
print(df2)

# 세로 방향으로 연결(행 추가)
result_rows = pd.concat([df1, df2])
print("\n세로 연결(행 추가) : ")

# 가로 방향으로 연결(열 추가)
df3 = pd.DataFrame({
    'C' : ['C0', 'C1', 'C2'],
    'D' : ['D0', 'D1', 'D2']
})

result_cols = pd.concat([df1, df3], axis=1)
print("\n가로 연결(열 추가) : ")
print(result_cols)