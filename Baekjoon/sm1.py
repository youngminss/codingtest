소마 스토리 앤 파이터 M
코더랜드의 인기 게임 소마 스토리 앤 파이터 M에는 많은 단독 스킬과 연계 스킬이 존재하며 사용자들은 스킬을 다양하게 조합하여 사용할 수 있다.

여기서 단독 스킬이란 다른 스킬에 영향을 받지 않고 단독적으로 사용할 수 있는 스킬을 의미하며
연계 스킬은 단독 스킬과 달리 단독적으로 사용이 불가하여 사전에 다른 스킬을 사용한 후 사용할 수 있는 스킬을 의미한다.

예를 들어 마법사 직업의 스킬로는 근접 공격, 염력, 불 뿜기, 물 뿌리기, 회복으로 구성되어 있고 아래의 연계 구조를 가진다고 가정한다.

근접 공격 후 염력 또는 불 뿜기를 사용할 수 있다. 이때 근접 공격은 염력 또는 불 뿜기의 선행 스킬이며 염력 또는 불 뿜기 스킬은 근접 공격의 후행 스킬이라고 한다.
염력 후 회복 또는 물 뿌리기를 사용할 수 있다. 이때 염력은 회복 또는 물 뿌리기의 선행 스킬이며 회복 또는 물 뿌리기 스킬은 염력의 후행 스킬이라고 한다.
근접 공격과 같이 특정 연계 구조가 제시되어 있지 않다면 단독 스킬로 규정하고 각 스킬은 아래의 표와 같이 구분된다.

스킬 명	구분
근접 공격	단독 스킬
염력	연계 스킬
불 뿜기	연계 스킬
물 뿌리기	연계 스킬
회복	연계 스킬
위의 내용을 토대로 마법사 직업은 총 3가지의 스킬 구성이 가능하다.

근접 공격 → 염력 → 회복
근접 공격 → 염력 → 물 뿌리기
근접 공격 → 불 뿜기
단, 연계 스킬들은 아래의 조건을 가지고 있다.

근접 공격 → 염력 이후 회복이나 물 뿌리기와 같이 스킬 사용 이후 연계되는 스킬이 있다면 중간에 스킬을 중단할 수 없다.
염력 스킬과 같은 연계 스킬의 경우 단독으로 사용할 수 없다.
단독 스킬 하나로만 구성된 경우는 스킬 구성에서 제외한다.
하나의 스킬은 여러 개의 후행 스킬을 가질 수 있지만 (1:NN) 여러 개의 선행 스킬을 가질 수는 없다. (1:1)
스킬이 무한으로 연계되는 상황은 없다고 가정한다.
소마가 구성할 수 있는 연계 스킬 구성을 모두 출력하시오.

입력
첫 번째 줄에는 KK 개의 스킬을 공백을 구분자로 입력받는다. 이때 스킬은 각 스킬을 나타내는 영문자로 이뤄진 문자열로 입력되며 대소문자를 구분한다. (a 스킬 ≠ A 스킬)

(1 < K ≦ 100)
(1<K≦100)
두 번째 줄에는 연계 스킬의 개수 정수 NN을 입력받는다.
(1 ≦ N < K)
(1≦N<K)
세 번째 줄부터 N+2N+2번째 줄까지 xx와 yy를 공백을 구분자로 연계 스킬의 관계를 입력받는다. (xx 스킬 이후 yy 스킬을 사용할 수 있다는 의미이며 반대로 사용은 불가능하다.)

출력
소마가 구성할 수 있는 연계 스킬 구성을 공백을 구분자로 모두 출력한다.
출력의 순서는 입력된 순서대로 출력한다.
입력 예시
h g f w r
4
h g
h f
g r
g w
출력 예시
h g r 
h g w 
h f 