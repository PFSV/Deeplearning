


#perceptron: step function
import numpy as np
import matplotlib.pylab as plt
'''
def step_function(x):
    y = x > 0
    return y.astype(np.int)
'''
x = np.array([-1.0, 1.0, 2.0])
print("x는 ",x)

y = x>0
print("y는 ",y)

#y = y.astype(np.int) / astype() 메서드는 내부 자료형을 바꿔준다.

y = y.astype(np.int)

print("step function graph")

def step_function(x):
    return np.array(x>0, dtype=np.int) 
# array 내부의 인자에 대해, 조건을 수행시키고, 참의 결과에 대해 int 값(1,0)으로 변환

x = np.arange(-5.0, 5.0, 0.1) 
#arange(a,b,c) 시작,끝, 간격으로 numpy 배열 생성 
y = step_function(x) #함수 수행
plt.plot(x,y) #x,y에 대해 그래프 그리기
plt.ylim(-0.1, 1.1) #y축의 범위 지정
plt.show() #plt값(그래프) 수행

