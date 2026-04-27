from ArrayStack import ArrayStack
from EvalPostFix import evalPostFix

# 연산자 우선순위
def precedunce(op):
    if op == '(' or op == ')' : return 0 # 괄호는 최하위
    elif op == '+' or '-' : return 1 # + -는 중간
    elif op == '*' or '/' : return 2 # * /는 최상위
    else : return -1

def InFixToPostFix(expr) :
    s = ArrayStack(100)
    output = []

    # 입력 토큰 하나씩 처리
    for term in expr:
        if term in '(': # 여는 괄호는 무조건 push
            s.push('(')
        elif term in ')': # 닫는 괄호 나오면
            while not s.isEmpty():
                op = s.pop()
                if op == '(': # 여는 괄호 나올 때까지 pop
                    break
                else :
                    output.append(op)
        elif term in "+-*/" : # 연산자 처리
            while not s.isEmpty(): # 스택 top가 우선순위 높으면 먼저 출력
                op = s.peek()
                if(precedunce(term) <= precedunce(op)):
                    output.append(op)
                    s.pop()
                else : break
            s.push(term) # 현재 연산자 push
        else :
            output.append(term) # 숫자는 바로 output
        
    # 남은 연산자 전부 pop
    while not s.isEmpty():
        output.append(s.pop())

        return output # 결과 반환



# 계산기 테스트 프로그램
if __name__ == "__main__":
    print('중위식을 후위식 표기 변환 프로그램 \n')

    # 중위표기식
    inFix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']

    # 중위 -> 후위 변환
    postFix1 = InFixToPostFix(inFix1)
    result1 = evalPostFix(postFix1)
    
    print(' 중위표기 : ', inFix1)
    print(' 후위표기 : ', postFix1)
    print(' 계산결과 : ', result1) # 7.0

