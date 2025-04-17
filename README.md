
# LangChain Summary API
📄  
뉴스 기사나 일반 문서를 입력받아 핵심 내용을 3줄로 요약해주는 FastAPI + LangChain 기반의 요약기입니다
멀티체인 기능을 활용하여 요약 결과 외에도 감정 분석 카테고리 분류 등 다양한 분석 결과를 함께 사용가능합니다



---

## 🧠 기능 설명

- 사용 기술: FastAPI, LangChain, OpenAI GPT, Docker
- **기사 요약 (Summary)**: 기사의 핵심적인 내용을 3줄로 요약합니다
- **감정 분석 (Sentiment Analysis)**: 기사의 감정을 긍정적, 부정적 또는 중립적 평가합니다
- **주제 분류 (Category Classification)**: 기사의 주제를 정치, 경제, 사회 등으로 분류합니다

---

## 🚀 실행 방법

### 1. 환경 변수 설정

루트에 `.env` 파일 생성 후 아래 내용 추가:

---

## 📘 Summary API

### ✅ Endpoint

`POST /summary`

뉴스 기사 또는 일반 문서를 입력하면 핵심 내용을 요약한 결과를 반환합니다 멀티체인 기능을 활용하여 감정 분석 카테고리 분류 등 다양한 분석을 동시에 사용 가능 합니다

---

### 📝 Request Body

| 필드명  | 타입   | 설명                          |
| ------- | ------ | ----------------------------- |
| article | string | 요약 대상 뉴스 기사 전체 내용 |

#### 📌 예시

```json
{
  "article": "삼성전자는 2025년 1분기 실적 발표를 통해 연결 기준 매출 76조 원, 영업이익 6조 4천억 원을 기록했다고 16일 밝혔다. 이는 전년 동기 대비 각각 12%, 57% 증가한 수치로, 주요 사업 부문에서의 회복세와 글로벌 수요 증가가 영향을 미친 것으로 분석된다. 특히 반도체 부문은 고부가가치 메모리 수요가 살아나며 전체 실적 개선을 주도했다. DDR5, HBM3 등 차세대 제품의 공급 확대와 함께, AI 연산에 최적화된 솔루션 개발도 실적 견인에 일조했다.\n\n스마트폰을 포함한 MX(Mobile eXperience) 부문 역시 프리미엄 모델의 판매 호조에 힘입어 견조한 실적을 이어갔다. 갤럭시 S24 시리즈는 출시 한 달 만에 글로벌 판매량 1천만 대를 돌파하며 AI 기능을 강조한 전략이 시장에서 긍정적인 반응을 얻었다는 평가다.\n\n디스플레이 부문은 OLED 수요 증가와 중국 시장 내 점유율 확대가 주요 성과로 꼽힌다. 특히 폴더블 디스플레이의 기술 완성도가 높아지면서 주요 스마트폰 제조사의 채택이 증가한 것이 주효했다.\n\n삼성전자는 향후 전략에 대해 \"AI 반도체, 차세대 메모리, 시스템 반도체 등 핵심 기술 분야에 대한 선제적 투자와 글로벌 협력을 확대해 나갈 것\"이라며 \"친환경 경영과 지속 가능한 공급망 강화도 병행할 계획\"이라고 밝혔다. 또, R&D 예산도 전년 대비 15% 이상 확대 편성하여 기술 리더십 확보에 총력을 기울일 방침이다.\n\n한편, 업계 전문가들은 삼성전자의 이번 실적에 대해 \"전반적인 시장 회복과 함께 기술 중심 전략이 본격적으로 성과를 내기 시작한 시기\"라며 \"2025년 하반기 이후 AI 반도체와 서버 메모리 수요 본격화에 따른 추가 성장 가능성이 높다\"고 전망했다."
}
```

---

### ✅ Response Body

| 필드명  | 타입   | 설명                          |
| ------- | ------ | ----------------------------- |
| summary | string | 요약된 기사 내용 반환         |
| sentiment | string | 기사의 감정 분석 결과           |
| category  | string | 기사에 대한 카테고리 분류 결과 |

#### 📌 예시

```json
{
  "summary": "삼성전자는 2025년 1분기에 연결 기준 매출 76조 원, 영업이익 6조 4천억 원을 기록하여 전년 대비 각각 12%, 57% 증가한 실적을 발표했다. 반도체와 스마트폰 부문의 호조 판매로 실적을 견인했으며, OLED 수요와 폴더블 디스플레이 기술 완성도 향상으로 디스플레이 부문도 성과를 거뒀다. 삼성전자는 향후 AI 반도체, 차세대 메모리, 시스템 반도체 등 핵심 기술 분야에 대한 투자와 글로벌 협력을 강화할 계획이다.",
  "sentiment": "이 기사는 긍정적인 감정을 전달한다. 삼성전자의 실적이 크게 증가했고, 기술 중심의 전략이 긍정적인 평가를 받았다.",
  "category": "경제 (기업 실적 발표)"
}
```

---

### 🌟 멀티체인 기능

멀티체인 기능을 사용하면, 하나의 입력에 대해 여러 분석을 동시에 처리할 수 있습니다. 예를 들어, 기사의 요약, 감정 분석, 카테고리 분류 등을 동시에 수행하여 더 많은 정보를 제공할 수 있습니다.

#### 멀티체인 기능 예시

1. **기사 요약**: 기사의 핵심적인 내용 3줄로 요약
2. **감정 분석**: 기사의 감정이 긍정적인지, 부정적인지, 또는 중립적인지를 평가
3. **주제 분류**: 기사의 주제를 '경제', '정치', '사회' 등으로 분류

이러한 멀티체인 기능은 기사의 다양한 측면을 동시에 파악할 수 있어 매우 유용합니다.

---

### 추가적인 사용법 및 확장 기능

- **다양한 입력 형식**: 이 API는 뉴스 기사뿐만 아니라 일반 문서도 요약할 수 있습니다
- **자동 요약 기능**: 기사를 입력하면 실시간으로 요약된 내용을 반환하는 방식으로 쉽게 사용할 수 있습니다
- **에러 처리**: 잘못된 입력이나 예상치 못한 오류가 발생한 경우 적절한 오류 메시지를 반환합니다

### 🔒 인증 및 보안

현재 API는 인증 없이 공개되어 있으며, 보안 인증 기능을 추가할 수 있습니다. 향후 업데이트에서 인증을 추가할 수 있습니다.

### 🚀 향후 계획

- **지원 언어 확장**: 다른 언어로도 요약이 가능하도록 멀티언어 모델을 지원할 계획입니다
- **자세한 메타데이터**: 요약된 기사 외에도 메타데이터(예: 기사 제목, 날짜 등)를 반환하도록 API를 확장할 수 있습니다
- **추가적인 분석 기능**: 뉴스 기사의 주제 분류, 감정 분석 등 추가적인 분석 기능을 도입할 수 있습니다

