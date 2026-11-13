# 양덕 분교 산책지도 — GitHub Pages 전체 업로드 패키지

이 ZIP은 **yangdukparents.github.io** 저장소에 바로 올리는 전체 파일입니다. 학부모 자율 제작 비공식 소개 홈페이지이며, PC/모바일 디자인과 기존 5개 HTML 페이지를 유지합니다.

## 이번 패키지에 포함한 최신 수정

- 메인 안내: 위치 문구에서 옥정·덕계 관련 안내 제거
- 메인 안내: "통학구역, 선택적 공동통학구역 및 전학 절차는 학교로 문의해 주세요"와 네이버 지도 검색 링크
- 4개 상세 페이지: 사진 아래 "작은 학교의 한 장면" 캡션 모두 제거
- 텃밭과 계절 이야기: 텃밭 활동/전통 음식 만들기/가을 걷이 한마당 각 챕터에 사용자가 제공한 사진 1장씩 추가
- 사진은 사본 WebP로 보관하고 파일명 및 대체텍스트를 활동 주제에 맞게 작성
- 36개 활동과 기존 PC/모바일 수채화 이미지, 안내판·메뉴 링크는 보존
- 웹사이트 배포를 위한 `.github/workflows/pages.yml` 파일과 자동 sitemap/canonical 생성 스크립트 포함

## 업로드 — 중요한 순서

1. ZIP 파일을 **압축 해제**합니다.
2. 압축 해제 후 첫 화면에 `index.html`, `garden.html`, `styles.css`, `assets`, `scripts`, `.github`가 바로 있어야 합니다. 상위 폴더가 하나 더 있으면 그 안으로 들어가 **내용물 전체**를 선택하세요.
3. GitHub 저장소 `https://github.com/yangdukparents/yangdukparents.github.io` → Code → Add file → Upload files.
4. 파일과 폴더 전체를 업로드하고, 아래 `Commit changes`를 누릅니다. 커밋 대상은 반드시 **main**입니다.
5. GitHub의 Code 파일 목록에 `.github/workflows/pages.yml`이 보이는지 확인하세요. 숨김 폴더 `.github`가 안 보이면 아래의 수동 복구 방법을 사용합니다.
6. Settings → Pages → Build and deployment → Source = **GitHub Actions**를 유지하세요.
7. Actions 탭에 **Publish Yangdeok Walk (5 pages + SEO)** 실행 기록이 새로 생기는지 확인하세요. 초록색 체크가 되면 배포가 완료된 것입니다.
8. `https://yangdukparents.github.io/`와 `https://yangdukparents.github.io/garden.html`를 새로고침하고 사진 3장 및 문구 수정이 적용됐는지 확인하세요.

### `.github`가 웹 업로드 중 누락될 때 (중요)

1. GitHub 저장소 → Code → Add file → **Create new file**을 선택합니다.
2. 파일 이름 칸에 `.github/workflows/pages.yml`을 그대로 입력합니다. GitHub가 폴더 경로를 자동으로 만들어 줍니다.
3. 압축 해제한 패키지의 `.github/workflows/pages.yml` 파일을 메모장으로 열고, **내용 전체**를 복사해 GitHub 새 파일의 편집창에 붙여넣습니다.
4. **Commit changes**를 누릅니다. 이제 Actions 탭에 사용자 지정 워크플로가 표시됩니다.

이미 `.github/workflows/pages.yml`이 있는 경우에는 이 수동 단계가 필요 없습니다.

## 주요 파일 구조

```text
index.html
garden.html
reading.html
culture.html
explore.html
styles.css
assets/
  school-map.webp
  mobile-school-scene.webp
  garden.webp
  ...
  yangdeok-school-garden-activity.webp
  yangdeok-traditional-food-making-activity.webp
  yangdeok-autumn-harvest-festival-activity.webp
scripts/build_site.py
.github/workflows/pages.yml
.nojekyll
robots.txt
sitemap.xml.template
README.md
```

`README.md`, `robots.txt`, `sitemap.xml.template`은 개발·검색 최적화용으로 포함합니다. 실제 사이트에 게시할 `sitemap.xml`, 각 페이지 canonical 및 `robots.txt`는 GitHub Actions 빌드 과정에서 실제 사이트 주소를 사용해 자동 생성합니다.

**주의:** GitHub에서 Public 저장소를 사용하는 동안 학생 이미지와 콘텐츠가 공개됩니다. 필요한 공개 동의 및 이용 권한을 확인하세요.
