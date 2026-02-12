# -*- coding: utf-8 -*-
with open('round_08/lecture_08.html', 'r', encoding='utf-8') as f:
    content = f.read()

anchor = r'''R2에서 배운 고유값을 기억하자. 행렬이 양반정치라는 것은 모든 고유값이 0 이상이라는 뜻이다.'''

defbox = r'''<div class="def">
<p class="ni"><strong>Definition 2.3 — 볼록성 판별 조건 (Convexity Conditions)</strong></p>
<div class="eq">\[\text{1차 조건 (First-order):} \quad f(y) \geq f(x) + \nabla f(x)^T(y - x) \quad \forall\, x, y\]</div>
<div class="eq">\[\text{2차 조건 (Second-order):} \quad \nabla^2 f(x) \succeq 0 \quad \forall\, x\]</div>
<p class="ni">1차 조건은 모든 점에서 접선(접평면)이 함수 아래에 있음을 의미하고, 2차 조건은 헤시안 행렬이 양반정치(positive semidefinite)임을 의미한다. 포트폴리오 분산 $w^T\Sigma w$의 헤시안은 $2\Sigma \succeq 0$이므로 항상 볼록하다.</p>
</div>

'''

if anchor in content:
    # Insert before the paragraph
    insert_pos = content.find(anchor)
    # Go back to find the <p> tag
    p_start = content.rfind('<p>', 0, insert_pos)
    content = content[:p_start] + defbox + content[p_start:]
    with open('round_08/lecture_08.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Definition 2.3")
else:
    print("Anchor not found")
