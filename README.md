# 《양덕 분교 산책지도》 — 네이버·구글 SEO 5페이지 버전

학교나 교육청의 공식 홈페이지가 **아닌**, 학부모 자율 제작·운영 소개 사이트입니다.

## 최종 페이지

- `index.html` — 산책지도 메인
- `garden.html` — 텃밭과 계절 이야기
- `reading.html` — 책과 함께 자라는 배움
- `culture.html` — 문화와 놀이의 시간
- `explore.html` — 미래를 탐구하는 배움

PC·모바일 수채화 이미지는 `assets/`에 따로 저장했습니다. 원래 그림 파일은 다시 그리지 않았습니다.
모든 활동 36개는 별도 JS 없이 위 HTML 안에 들어 있습니다. 메뉴·안내판은 실제 `<a href="garden.html">` 링크입니다.

## GitHub Pages에 게시하는 방법 (권장: Actions 자동 배포)

1. GitHub에서 빈 **Public** 저장소를 만듭니다. 예: `yangdeok-walk`.
2. 이 ZIP을 해제해서 **내용물 전체**를 저장소 최상위(root)에 올립니다. `index.html`, `garden.html`, `assets/`, `.github/`가 모두 저장소 최상위에 있어야 합니다. **ZIP 파일 자체를 올리면 안 됩니다.**
3. GitHub 저장소 → **Settings → Pages → Build and deployment → Source → GitHub Actions**로 선택합니다.
4. **Actions** 탭에서 `Publish Yangdeok Walk (5 pages + SEO)` 실행이 성공했는지 확인합니다. 필요하면 **Run workflow**로 다시 실행합니다.
5. **Settings → Pages**에서 표시되는 실제 공개 사이트 URL로 5개 페이지를 직접 엽니다.
6. 실제 홈페이지에서 `/sitemap.xml`을 열어 5개 URL이 나오고, 각각 실제 사이트 주소를 사용하는지 확인합니다.
7. 네이버 서치어드바이저·Google Search Console에 **실제 공개 URL**을 소유확인 후, `/sitemap.xml`을 제출합니다.

### 왜 GitHub Actions를 사용하나요?

아직 최종 공개 주소가 확정되지 않았기 때문입니다. GitHub Actions는 GitHub Pages가 확정한 사이트 주소(`configure-pages.outputs.base_url`)를 받아 **올바른 절대 URL이 들어간 `sitemap.xml` 및 페이지별 `rel=canonical`을 자동 생성**합니다. 따라서 임의 주소를 파일에 넣을 필요가 없습니다. **배포되기 전 ZIP에는 `sitemap.xml.template`만 있고 유효한 공개 sitemap.xml은 배포 과정에서 생성됩니다.**

GitHub Pages 사이트 주소는 계정 대표 사이트(`https://계정.github.io/`)와 프로젝트 사이트(`https://계정.github.io/저장소명/`)에 따라 다릅니다. 이 프로젝트는 어느 유형에서도 상대경로 링크가 깨지지 않습니다.

### 주의사항

- `robots.txt`는 생성되지만, **프로젝트 하위경로(`/저장소명/robots.txt`)에 있는 파일은 도메인 루트의 robots.txt를 대신하지 못합니다.** 검색로봇은 기본적으로 도메인 루트에 있는 robots.txt를 확인합니다. 다만 사이트의 메뉴·콘텐츠·sitemap.xml은 공개 경로에서 수집 가능합니다.
- Google/Naver의 검색 반영이나 순위를 보장하지는 않습니다. 실제 배포 후 크롤링·색인 상태를 확인하세요.
- 학교 입학/전학 규정·학구·급식 API 등 공식 정보 기능은 포함하지 않았습니다.
- 이전 `#garden` 등의 해시 URL은 새로운 HTML 링크로 바뀝니다. 기존 북마크 링크로 메인에 접속한 사람은 메인 화면을 보게 됩니다. 공개 전에 사이트 주소를 공유하지 않았다면 별도 리다이렉트는 필요하지 않습니다.

## 수동 빌드 (선택)

GitHub Actions가 아니라 로컬에서 최종 사이트를 만들고 싶으면, 실제 주소가 확정된 후 다음 명령을 실행하세요.

```bash
python3 scripts/build_site.py "https://실제-공개-주소/프로젝트-경로" --output _site
```

그러면 `_site/`에 5개 HTML 및 절대 URL을 포함한 `sitemap.xml`이 생성됩니다. 수동 게시할 경우에는 `_site/`의 내용물만 업로드해야 합니다.

## 변경 내역

- 모든 5개 HTML에 고유한 `<title>`, `<meta name="description">`, `<h1>` 포함
- 장별 제목 H2, 각 세부 활동 제목 H3로 구성
- 본문을 정적 HTML로 제공해 JS 실행 없이도 36개 활동 노출
- GitHub 프로젝트 하위 경로에서도 작동하도록 상대 링크 사용
- 비공식 제작 고지 상단·하단 유지
- 디자인·이미지·활동 목록·메뉴 기능 보존
- 공개된 최종 URL로 sitemap/canonical 생성되는 자동 배포 추가

## 학부모 정보·지역 검색 보강

- 메인 페이지에 검색엔진이 읽을 수 있는 학교 소개, 주요 활동, 위치, 입학·전학 공식 정보 확인 방법을 정적 HTML로 추가했습니다.
- 공식 학교명은 **남면초등학교 양덕분교장**이며, 위치는 **경기도 양주시 남면 은남로119번길 373**입니다(동두천양주교육지원청 관내학교 소개 기준).
- 옥정·덕계 등 인근 지역 학부모를 위한 안내이지만 입학·전학 가능 여부를 확정적으로 제시하지 않습니다.
- 공신력 있는 확인 경로로 동두천양주교육지원청 **양주학생배치팀 공고**와 남면초등학교 공식 홈페이지를 링크했습니다.
- 기존 SEO 제목·설명, 네 개 세부 페이지와 36개 활동, PC·모바일 그림, 안내판 클릭 영역은 변경하지 않았습니다.
- 사용자는 사이트 공개 후 학교 관련 안내가 최신인지 주기적으로 검토해야 합니다.
