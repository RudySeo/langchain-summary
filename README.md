# LangChain Summary API

📄 자연어 기사 텍스트를 3줄로 요약해주는 FastAPI + LangChain 기반 요약기

---

## 🧠 기능 설명

- 사용 기술: FastAPI, LangChain, OpenAI GPT, Docker
- 기사 내용을 POST로 전달하면 요약 결과 반환

---

## 🚀 실행 방법

### 1. 환경 변수 설정
루트에 `.env` 파일 생성 후 아래 내용 추가:



---

## 📘 Summary API

### ✅ Endpoint

`POST /summary`

뉴스 기사 또는 일반 문서를 입력하면, 핵심 내용을 요약한 결과를 반환합니다.

---

### 📝 Request Body

| 필드명   | 타입    | 설명                  |
|--------|--------|---------------------|
| article | string | 요약 대상 뉴스 기사 전체 내용 |

#### 📌 예시

```json
{
  "article": "삼성전자는 2025년 1분기 실적 발표를 통해 연결 기준 매출 76조 원, 영업이익 6조 4천억 원을 기록했다고 16일 밝혔다. 이는 전년 동기 대비 각각 12%, 57% 증가한 수치로, 주요 사업 부문에서의 회복세와 글로벌 수요 증가가 영향을 미친 것으로 분석된다. 특히 반도체 부문은 고부가가치 메모리 수요가 살아나며 전체 실적 개선을 주도했다. DDR5, HBM3 등 차세대 제품의 공급 확대와 함께, AI 연산에 최적화된 솔루션 개발도 실적 견인에 일조했다.\n\n스마트폰을 포함한 MX(Mobile eXperience) 부문 역시 프리미엄 모델의 판매 호조에 힘입어 견조한 실적을 이어갔다. 갤럭시 S24 시리즈는 출시 한 달 만에 글로벌 판매량 1천만 대를 돌파하며 AI 기능을 강조한 전략이 시장에서 긍정적인 반응을 얻었다는 평가다.\n\n디스플레이 부문은 OLED 수요 증가와 중국 시장 내 점유율 확대가 주요 성과로 꼽힌다. 특히 폴더블 디스플레이의 기술 완성도가 높아지면서 주요 스마트폰 제조사의 채택이 증가한 것이 주효했다.\n\n삼성전자는 향후 전략에 대해 \"AI 반도체, 차세대 메모리, 시스템 반도체 등 핵심 기술 분야에 대한 선제적 투자와 글로벌 협력을 확대해 나갈 것\"이라며 \"친환경 경영과 지속 가능한 공급망 강화도 병행할 계획\"이라고 밝혔다. 또, R&D 예산도 전년 대비 15% 이상 확대 편성하여 기술 리더십 확보에 총력을 기울일 방침이다.\n\n한편, 업계 전문가들은 삼성전자의 이번 실적에 대해 \"전반적인 시장 회복과 함께 기술 중심 전략이 본격적으로 성과를 내기 시작한 시기\"라며 \"2025년 하반기 이후 AI 반도체와 서버 메모리 수요 본격화에 따른 추가 성장 가능성이 높다\"고 전망했다."
}
```

---

### ✅ Response Body

| 필드명   | 타입    | 설명               |
|--------|--------|------------------|
| summary | string | 요약된 기사 내용 반환 |

#### 📌 예시

```json
{
  "summary": "삼성전자는 2025년 1분기에 연결 기준 매출 76조 원, 영업이익 6조 4천억 원을 기록하여 전년 대비 각각 12%, 57% 증가한 실적을 발표했다. 반도체와 스마트폰 부문의 호조 판매로 실적을 견인했으며, OLED 수요와 폴더블 디스플레이 기술 완성도 향상으로 디스플레이 부문도 성과를 거뒀다.\n\n삼성전자는 향후 AI 반도체, 차세대 메모리, 시스템 반도체 등 핵심 기술 분야에 대한 투자와 글로벌 협력을 강화할 계획이며, R&D 예산도 15% 이상 확대하여 기술 리더십을 확보할 방침이다. 업계 전문가들은 이번 실적을 통해 기술 중심 전략이 본격적으로 성과를 내기 시작한 것으로 평가하고, AI 반도체와 서버 메모리 수요 증가로 추가 성장 가능성이 높다고 전망했다."
}
```





---

