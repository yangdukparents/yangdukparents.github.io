# 양덕 분교 산책지도 — 7페이지 확장판 (2026-11-13)

학부모 자율 제작 비공식 학교 소개 홈페이지입니다. 학교/교육청의 공식 입장을 대변하지 않습니다.

## 페이지

- index.html — 산책지도, 학교소개, 2개 신규 링크, FAQ 2개
- garden.html — 텃밭과 계절 (기존 3장 사진 보존)
- reading.html — 책과 배움 (기존 3장 사진 보존)
- culture.html — 문화와 놀이 (기존 3장 사진 보존)
- explore.html — 미래 탐구 (기존 3장 사진 보존, 체험학습 링크 추가)
- experience-2026.html — 2026학년도 체험학습 계획
- school-life-2026.html — 2026학년도 방과후, 돌봄, 통학, 입학·전학 안내

모든 HTML 파일과 styles.css, assets/, scripts/, .github/ 폴더를 저장소 최상위에 둡니다.

## GitHub Pages 게시

1. 전체 ZIP의 **압축을 해제**하고 내용물(숨김 .github 포함)을 `yangdukparents/yangdukparents.github.io` 저장소 루트에 업로드합니다.
2. Settings > Pages > Source = GitHub Actions 유지.
3. `.github/workflows/pages.yml`이 실제로 저장되어 있는지 확인합니다.
4. GitHub Actions의 배포가 성공하면 7개 URL을 직접 확인합니다.
5. `scripts/build_site.py`가 configure-pages가 알려준 실제 URL로 sitemap.xml, robots.txt, canonical을 생성합니다.

로컬 시험: `python scripts/build_site.py https://yangdukparents.github.io --output _site_test`

## 정보의 시점

학교의 2026학년도 안내문 내용은 학부모가 전달한 설명에 기반한 것이며, 2027학년도에 그대로 적용된다고 보장하지 않습니다. 실제 운영계획, 신청 및 학구는 학교/교육지원청에 확인하세요.

2027년 양주 통학구역 행정예고: https://www.goedy.kr/goedy/na/ntt/selectNttInfo.do?bbsId=10174&mi=10224&nttSn=1687734
학교 안내(공식 명칭·주소·전화): https://www.goedy.kr/goedy/ssm/scholStts/selectScholSttsList.do?mi=12376

## 보존

기존 PC 및 모바일 메인 배경, 네 분야의 12개 챕터/36개 세부 활동, 12장 사진, 상단 4개 수채화 삽화 및 상세 하단 복귀링크를 유지하였습니다. 신규 사진/급식/API/로그인은 추가하지 않았습니다.
