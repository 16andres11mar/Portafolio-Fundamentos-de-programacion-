## Break
```python
j=0
for i in range (10):
    j+=2
    print ("i;",i,"j:",j)
    if j==10:
        break
```

## Break y continue
```python
j =  0
for i in range(10):
    j += 2
    print('i:', i, 'j:', j)
    if j >=2 and j<=18:
        continue
    print('el valor de j:', j)
```

## Break
```python
contador = 0
for i in range(10):
    for j in range(10):
        contador += 1
        print('i:', i, 'j:', j)
        if contador > 50:
            break
print('Contador:', contador)
```
