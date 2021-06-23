# 파이썬 Better Way

## 복잡한 식을 쓰는 대신 도우미 함수를 작성하라.
* URL의 질의 문자열을 구문 분석
```python
from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0초록=',
                      keep_blank_values=True)

print(repr(my_values))

# 일부는 파라미터가 여러 값이 들어 있고, 일부 파라미터는 값이 하나만 들어있거나, 이름은 있지만 값이 없는 경우가 있다.
print(my_values.get('빨강'))
print(my_values.get('파랑'))
print(my_values.get('초록'))

# 파라미터가 없거나 비어있을 경우 0을 default로 표현하여보자.
# 이식은 읽기 어려운데다 원하는 모든 기능을 제공하지도 못한다.
# 코드를 짧게 유지하면 멋지지만, 우겨 넣기위해 노력할 만큼 가치는 없다.
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0
print(f'빨강:{red!r}')
print(f'초록:{green!r}')
print(f'투명도:{opacity!r}')

# 이 코드가 조금 더 낫다.
red_str = my_values.get('빨강', [''])
red = int(red_str[0]) if red_str else 0

# 도우미 함수를 작성해 호출하면 훨씬 명확하다.
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

```
* 복잡한 식을 도우미 함수로 옮겨라. 특히 같은 로직을 반복해 사용할 때는 도우미 함수를 꼭 사용하라.
* 불(boolean) 연산자 or 나 and를 식에 사용하는 것보다 if/else 식을 쓰는 편이 가독성이 좋다.

## 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라
* 파이썬에서는 값으로 이뤄진 불변(immutable) 순서쌍을 만들어낼 수 있는 tuple 내장 타입이 있다.
* 튜플에 있는 값은 숫자 인덱스를 사용해 접근할 수 있다.
```python
item = ('호박엿', '식혜')
first = item[0]
second = item[1]
print(first, '&', second)
```
* 파이썬 언패킹을 이용해 튜플에 인덱스 대신 변수로 접근할 수 있다.
```python
item = ('호박엿', '식혜')
first, second = item
print(first, '&', second)

# 언패킹은 튜플 인덱스를 사용하는 것보다 시각적인 잡음이 적다.
favorite_snacks = {
    '짧쪼름한 과자': ('프레즐', 100),
    '달콤한 과자': ('쿠키', 100),
    '채소': ('당근', 100),
}
((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()


# enumerate를 사용해 언패킹 사용
snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name}은 {calories} 칼로리 입니다.')

```

## range 보다는 enumerate를 사용하라
```python
flavor_list = ['바닐라', '초콜릿', '파칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛이에요')

# range 사용
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')


# enumerate 사용(enumerate 지연계산 제네레이터로 감싼다.)
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')
```

## 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용하라
```python
names = ['Cecilia', '남궁민수', '트럼프']
longest_name = None
max_count = 0

# 리스트 컴프리헨션을 사용하면 새로운 list를 파생시키기 쉽다.
counts = [len(n) for n in names]

# 두 리스트를 동시에 이터레이션할 경우 names 소스 리스트의 길이를 사용해 이터레이션 할 수 있다.
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)
```
* 문제는 이 루프가 시각적으로 잡음이 많다는 것이다. 인덱스를 사용해 names와 counts의 원소를 찾는 과정이 코드를 읽기 어렵게 만든다.
* 이러한 코드를 더 깔끔하게 만들 수 있도록 파이썬은 zip이라는 내장함수를 제공한다.
```python

names = ['Cecilia', '남궁민수', '트럼프']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

# zip은 자신이 감싼 이터레이터 원소를 하나씩 소비한다. 
# 따라서 메모리를 다 소모해서 프로그램이 중단되는 위험 없이 아주 긴 입력도 처리 할 수 있다. 
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

# zip을 사용할 때 주의할 점은 두 리스트의 길이가 동일해야 한다는 것이다.
# 리스트가 동일하지 않을 경우 itertools 내장 모듈에 있는 zip_longest를 사용하는 것을 고려하라
import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

```

# 슬라이싱 보다는 나머지를 모두 잡아내는 언패킹을 사용하라
* 기본 언패킹의 한계점은 언패킹할 시퀀스의 길이를 미리 알고 있어야 한다는 것이다.
```python
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest = car_ages_descending

# 슬라이싱 사용
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]

# 별표 식 언패킹
oldest, second_oldest, *others = car_ages_descending
```
* 별표 식이 포함된 언패킹 대입을 처리하려면 필수인 부분이 적어도 하나는 있어야 한다.
* 별표 식은 항상 list의 인스턴스가 된다.
* 리스트를 서로 겹치지 않게 여러 조각으로 나눌 경우, 슬라이싱과 인덱싱을 사용하기 보다는 나머지를 모두 잡아내는 언패킹을 사용해야 실수할 여지가 훨식 줄어든다.


# 컴프리헨션 내부에 제어 하위 식을 세개 이상 사용하지 말라
* 컴프리헨션은 루프를 여러 수준으로 내포하도록 허용한다.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

# 리스트의 중첩 수가 많을 경우 컴프리헨션이 너무 길어져서 여러줄로 나눠 써야 한다.
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
]

flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]

# 3단계 리스트 컴프리헨션보다 이 코드의 루프가 더 명확해 보인다.
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
```
* 컴프리헨션에 들어가는 하위식이 세 개 이상 되지 않게 제한하라는 규칙을 지켜라
* 조건문 두개, 루프 두개, 혹은 조건문 한 개와 루프 한 개를 사용할 수 있다는 것
* 컴프리헨션이 이보다 더 복잡해지면 일반 if와 for 문을 사용하고 도우미 함수를 작성하라

## 리스트를 반환하기보다는 제네레이터를 사용하라
* 시퀀스를 결과로 만들어 내는 함수를 만들 때 가장 간단한 선택은 원소들이 모인 리스트를 반환하는 것이다.
```python
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

# 간단한 예시 입력에 대해서는 이 코드는 잘 동작한다.
address = '컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관'
result = index_words(address)

```
* 이 코드의 첫번째 문제점은 코드에 잡음이 많고 핵심을 알아보기 어렵다는 것
* 이 코드는 새로운 결과를 찾을 때마다 append 메서드를 호출한다. 메서드 호출이 너무 덩어리가 크기 때문에(result.append) 리스트에 추가될 값(index + 1)의 중요성을 희석한다.
* 함수 본문 전체에는 130여개의 글자(공백 제외)가 들어가는데, 그중 75개의 글자 내외만 중요한 일을 한다.
* 이 함수를 개선하는 방법은 제너레이터를 사용하는 것이다.
```python
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.'            
it = index_words_iter(address)
print(next(it))
print(next(it))
```
* index_words 의 두번째 단점은 반환하기 전에 리스트에 모든 결과를 다 저장해야 한다는 것이다. 이로 인해 입력이 매우 크면 프로그램이 메모리를 소진해서 중단될 수 있다.
```python
# 파일에서 한 번에 한 줄씩 읽어 한 단어씩 출력하는 제네레이터를 정의하는 코드
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
```

## 이터레이터나 제너레이터를 다룰 때는 itertools 를 사용하라
```python
import itertools

# chain : 여러 이터레이터를 하나의 순차적인 이터레이터로 합치고 싶을 때 chain을 사용
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

# repeat : 한 값을 계속 반복해 내놓고 싶을 때 사용
it = itertools.repeat('hello', 3)
print(list(it))

# cycle : 어떤 이터레이터가 내놓은 원소들을 계속 반복하고 싶을 때
it = itertools.cycle([1, 2])
result = [next(it) for _ in range (10)]
print(result)

# tee : 한 이터레이터를 병렬적으로 두 번째 인자로 지정된 개수의 이터레이터로 만들고 싶을 때 사용
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))


# zip_longest
keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print('zip:        ', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest:', longest)


# islice : 이터레이터를 복사하지 않고 슬라이싱하고 싶을때
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print('First five: ', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds:', list(middle_odds))


# takewhile : 이터레이터에서 주어진 술어가 False를 반환하는 첫 원소가 나타날때까지 원소를 돌려준다.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))


# dropwhile : takewhile의 반대
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))


# filterfalse : filter 내장 함수 반대
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0

filter_result = filter(evens, values)
print('Filter:      ', list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print('Filter false:', list(filter_false_result))


# accumulate : 누적된 결과 리턴
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('Sum:   ', list(sum_reduce))

def sum_modulo_20(first, second):
    output = first + second
    return output % 20

modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print('Modulo:', list(modulo_reduce))


# product : 하나 이상의 이터레이터에 들어 있는 아이템들의 데카르트 곱을 반환
single = itertools.product([1, 2], repeat=2)
print('Single:  ', list(single))

multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple))


# permutations : 이터레이터가 내놓은 원소들로부터 만들어낸 길이 N인 순열 리턴
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))


# combinations : 이터레이터가 내놓은 원소들로부터 만들어낸 길이 N 조합 반환
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))


# combinations_with_replacement : combinations와 같지만 중복 허용
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))
```