from ArrayStack import ArrayStack

# 후위표기식 계산 함수
def evalPostFix(expr):
    s = ArrayStack(100)
    for token in expr: # 입력된 (숫자/연산자)을 순서대로 처리
        if token in "+-*/": # 연산자면 계산
            val2 = s.pop() # 2번쨰 값
            val1 = s.pop() # 1번째 값
            # 연산 수행 후 결과를 다시 push
            if(token=='+'): s.push(val1+val2)
            if(token=='-'): s.push(val1-val2)
            if(token=='*'): s.push(val1*val2)
            if(token=='/'): s.push(val1/val2)
        else:
            s.push(float(token)) # 숫자면 float으로 변환해서 넣음
    return s.pop() # 최종 결과 꺼내서 반환

expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+'];
print(expr1, '==>', evalPostFix(expr1)) # 7.0