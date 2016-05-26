"""
＃筆者註：
因為是入門的練習題，所以在輸入時比較沒有考慮到太多的條件，如整數的範圍、浮點數、邊長為負、輸入字串而非數字等等。
而程式的寫法每個人都不一樣，只要能把握「可執行》邏輯正確》寫得漂亮」的目標即可！

<h3>＠老師想要快速打分數，想設計一個快速分級的程式，條件如下：</h3>
1/每張考卷都是0~100分，不能打錯！
2/80分以上分類為「優秀」，60分以上為「普通」，不到60分為「再加油」！
＃測試點：37 / 67 / 87 / 102 / -69
"""

score = input('Enter Score!')
score = int (score)
if score >=0 and score >=100 : 
    if score >=80 :
        print ('優秀')
    elif score &gt;=60 :
        print ('普通')
    else :
        print ('再加油')
else :
    print ('請輸入0~100')

"""＠設計一個程式
輸入：兩個數字
輸出：相加的結果
＃測試點： 1,3 / 209,22 / -90,63
"""

a = input('Enter first number')
a = int(a)
b = input('Enter second number')
b = int(b)
print (a+b)


"""＠有一個方程式 f(x) = ax^2 + bx +c
輸入：係數a,b,c，
輸出：此方程式解的可能？
＃測試點：2,1,-10 / 1,4,4 / 1,1,5
"""

print('ax^2 + bx + c')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
D = b**2 - 4*a*c
if D&gt;0 :
    print ('有相異根')
elif D == 0 :
    print ('重根')
elif D&lt;0 :
    print ('無實根')


"""＠設計一個程式
輸入：三個邊長 （由小到大）
輸出：此三邊是否可以為成三角形
＃測試點：3,3,7 / 3,4,5
"""
a = int (input('第一個邊= '))
b = int (input('第二個邊= '))
c = int (input('第三個邊= '))
if a+b > c :
    print ('三角形存在')
else :
    print ('三角形不存在')

"""＠有一家餐廳的服務生，想知道這個月應該得到的工資，工資的算法如下：
1.來上班的日子，都可以領到全天的薪水
2.每個月工作超過20天，超過的每一天薪水是1.5倍
輸入：「一般日薪」、「當月工作天數」
輸出：當月服務生總共可以領多少錢？
＃測試點：1000,30 / 1500,15
"""

salary = int (input('Enter daily salary'))
day = int (input('Enter work day'))
if day > 20 : 
    print (salary * 1.5 * (day-20) + salary * 20)
else :
    print ( salary * day)


"""＠請設計出一個程式
輸入：「西元年份」
輸出：判斷是「閏年」或「平年」
閏年規則：
1西元年分除以400可整除，為閏年。
2西元年分除以4可整除但除以100不可整除，為閏年。
3西元年分除以4不可整除，為平年。
4西元年分除以100可整除但除以400不可整除，為平年
＃測試點： 2000 / 2004 / 2010 / 1700 / 1999
"""

year = int (input('Enter year'))
if (year%4 ==0 and year%100 != 0) or year%400==0 :
    print ('閏年')
else:
    print ('平年')
