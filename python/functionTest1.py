def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
    
def Hello1(name):
    print('Hello, ' + name)
    
def Hello2(name):
    return'Hello, '*3 + name

def Hello3(num, name):
    return'Hello, '*num + name

#hello() # finction call
#Hello1('陳亮妤')
#print(Hello2("陳亮妤"))
#print(Hello3(5, "陳亮妤"))  __name__ == "__main__"
  
if __name__ == '__main__'
hello()
Hello1('陳亮妤')
print(Hello2("陳亮妤"))
print(Hello3(5, "陳亮妤"))


