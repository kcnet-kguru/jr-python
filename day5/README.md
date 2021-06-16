## 해쉬 테이블 (Hash Table)

### 1. 해쉬 구조
* Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
  - Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
  - 파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄
  - 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
  - <font color='#BF360C'>단, 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨</font>


### 2. 알아둘 용어
* 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
* 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
* 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
* 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
* 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
* 저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음
<img src="https://www.fun-coding.org/00_Images/hash.png" width=400 />
 

### 3. 시간 복잡도
- 일반적인 경우(Collision이 없는 경우)는 O(1)
- 최악의 경우(Collision이 모두 발생하는 경우)는 O(n)

> 해쉬 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에, 시간 복잡도는 O(1) 이라고 말할 수 있음 

## 트리

### 1. 트리 (Tree) 구조
- 트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
- 실제로 어디에 많이 사용되나? 
  - 트리 중 이진 트리 (Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

### 2. 알아둘 용어
- Node: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
- Root Node: 트리 맨 위에 있는 노드
- Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
- Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
- Child Node: 어떤 노드의 상위 레벨에 연결된 노드
- Leaf Node (Terminal Node): Child Node가 하나도 없는 노드
- Sibling (Brother Node): 동일한 Parent Node를 가진 노드
- Depth: 트리에서 Node가 가질 수 있는 최대 Level
<img src="http://www.fun-coding.org/00_Images/tree.png" width="600" />

### 3. 이진 트리와 이진 탐색 트리 (Binary Search Tree)
- 이진 트리: 노드의 최대 Branch가 2인 트리
- 이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
  - 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음!
  
<img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-insertion-animation.gif" />

(출처: https://www.mathwarehouse.com/programming/gifs/binary-search-tree.php#binary-search-tree-insertion-node)

### 4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
- 주요 용도: 데이터 검색(탐색) 
- 장점: 탐색 속도를 개선할 수 있음

> 단점은 이진 탐색 트리 알고리즘 이해 후에 살펴보기로 함

### 이진트리와 정렬된 배열간의 탐색 비교
<img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-sorted-array-animation.gif" />

(출처: https://www.mathwarehouse.com/programming/gifs/binary-search-tree.php#binary-search-tree-insertion-node)

### 5. 이진 탐색 트리의 시간 복잡도와 단점
#### 5.1. 시간 복잡도 (탐색시)
  - depth (트리의 높이) 를 h라고 표기한다면, O(h)
  - n개의 노드를 가진다면, $h = log_2{n} $ 에 가까우므로, 시간 복잡도는 $ O(log{n}) $ 
     - 참고: 빅오 표기법에서 $log{n}$ 에서의 log의 밑은 10이 아니라, 2입니다.
       - 한번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미. 즉 50%의 실행시간을 단축시킬 수 있다는 것을 의미함
<img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-sorted-array-animation.gif" />

(출처: https://www.mathwarehouse.com/programming/gifs/binary-search-tree.php#binary-search-tree-insertion-node)

#### 5.2. 이진 탐색 트리 단점
  - 평균 시간 복잡도는 $ O(log{n}) $ 이지만, 
    - 이는 트리가 균형잡혀 있을 때의 평균 시간복잡도이며,
  - 다음 예와 같이 구성되어 있을 경우, 최악의 경우는 링크드 리스트등과 동일한 성능을 보여줌 ( $O(n)$ )
<img src="http://www.fun-coding.org/00_Images/worstcase_bst.png" width="300" />
    
## 힙

### 1. 힙 (Heap) 이란?
- 힙: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
  - 완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

<img src="https://www.fun-coding.org/00_Images/completebinarytree.png" width=300>

- 힙을 사용하는 이유
  - 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n) 이 걸림
  - 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면, $ O(log n) $ 이 걸림
  - 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

### 2. 힙 (Heap) 구조
- 힙은 최대값을 구하기 위한 구조 (최대 힙, Max Heap) 와, 최소값을 구하기 위한 구조 (최소 힙, Min Heap) 로 분류할 수 있음
- 힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조임
  1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
     - 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
  2. 완전 이진 트리 형태를 가짐

### 힙과 이진 탐색 트리의 공통점과 차이점
- 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
- 차이점: 
  - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
  - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
  - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
    - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
- 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨  
<img src="https://www.fun-coding.org/00_Images/completebinarytree_bst.png" width="800" />
  
### 3. 힙 (Heap) 동작
- 데이터를 힙 구조에 삽입, 삭제하는 과정을 그림을 통해 선명하게 이해하기

### 힙에 데이터 삽입하기 - 기본 동작 
- 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입
<img src="https://www.fun-coding.org/00_Images/heap_ordinary.png">

### 힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap 의 예)
- 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
- 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함 (swap)
<img src="https://www.fun-coding.org/00_Images/heap_insert.png">

### 힙의 데이터 삭제하기 (Max Heap 의 예)
- 보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
  - 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
- 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드 (일반적으로 가장 마지막에 추가한 노드) 를 root 노드로 이동
- root 노드의 값이 child node 보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)

<img src="https://www.fun-coding.org/00_Images/heap_remove.png">

### 4. 힙 구현
### 힙과 배열
- 일반적으로 힙 구현시 배열 자료구조를 활용함
- 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀더 수월함
  - 부모 노드 인덱스 번호 (parent node's index) = 자식 노드 인덱스 번호 (child node's index) // 2
  - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2
  - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2 + 1
<img src="https://www.fun-coding.org/00_Images/heap_array.png" width=400>
    

### 5. 힙 (Heap) 시간 복잡도
  - depth (트리의 높이) 를 h라고 표기한다면,
  - n개의 노드를 가지는 heap 에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 $h = log_2{n} $ 에 가까우므로, 시간 복잡도는 $ O(log{n}) $ 
     - 참고: 빅오 표기법에서 $log{n}$ 에서의 log의 밑은 10이 아니라, 2입니다.
     - 한번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미. 즉 50%의 실행시간을 단축시킬 수 있다는 것을 의미함