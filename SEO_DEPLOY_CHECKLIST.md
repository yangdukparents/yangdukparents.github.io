# 양덕 분교 산책지도 — 배포와 SEO 체크리스트 (2026-11-13)

## 배포 방식 유지
- 현재 GitHub Pages 설정은 변경할 필요 없습니다. 기본 branch 배포(`main`/root)와 기존 사용자 지정 `.github/workflows/pages.yml` 어느 방식에서도 정적 SEO 파일이 제공됩니다.
- 완성된 `sitemap.xml`, `robots.txt`, 각 HTML의 절대 canonical을 저장소 루트에 넣었습니다.
- 사용자 지정 Actions가 실행되면 `scripts/build_site.py`가 canonical을 **중복하지 않고** 갱신하며, 동적 사이트맵과 robots를 재생성합니다.
- 현재 공개 주소: https://yangdukparents.github.io/

## 업로드 전후 확인
1. ZIP 압축을 해제하고 내용물 전체(`.github` 포함)를 저장소 최상위에 업로드/Commit합니다.
2. GitHub Actions에서 배포 완료를 확인한 뒤 https://yangdukparents.github.io/sitemap.xml 및 /robots.txt 를 브라우저에서 열어봅니다.
3. 사이트맵이 XML 문서로 열리고 7개 URL이 있는지 확인합니다.
4. 메인과 상세 페이지에서 브라우저 페이지 소스 보기를 통해 `<link rel="canonical" ...>`과 `og:` 메타태그를 확인합니다.
5. 이미지 https://yangdukparents.github.io/assets/yangdeok-social-preview.jpg 가 공개되는지 확인합니다.
6. 아래 검증 스크립트를 인터넷 연결 환경에서 실행할 수 있습니다: `python scripts/check_live_seo.py`.

## Google Search Console (URL-prefix 속성)
1. https://search.google.com/search-console 에서 URL 접두어 속성 `https://yangdukparents.github.io/`를 추가합니다.
2. 소유권 확인은 HTML 태그 또는 HTML 파일 업로드를 이용합니다. 서비스가 발급한 고유 토큰을 정확히 넣어야 하므로 패키지에는 임의 토큰을 넣지 않았습니다.
3. HTML 태그 방식이라면 `index.html`의 `<head>`에 `google-site-verification` 메타태그를 복사해 추가한 다음 Commit합니다.
4. HTML 파일 방식을 선택하면 Google이 제공한 파일을 **이름·내용 수정 없이** 저장소 루트에 추가합니다. 사용자 지정 Actions에서도 자동으로 복사됩니다.
5. 소유확인 뒤 'Sitemaps'에 `sitemap.xml`을 제출하고 URL 검사에서 7개 URL 색인을 검사합니다.

## 네이버 서치어드바이저
1. https://searchadvisor.naver.com/ 에서 `https://yangdukparents.github.io` 를 등록합니다.
2. HTML 태그 방식이면 메인 `index.html`의 `<head>`에 실제 발급받은 `naver-site-verification` 태그를 추가합니다.
3. HTML 파일 방식이면 네이버에서 받은 검증 HTML 파일을 저장소 루트에 그대로 업로드합니다. 사용자 지정 Actions에서도 자동으로 복사됩니다.
4. 소유확인 뒤 '요청 → 사이트맵 제출'에 `https://yangdukparents.github.io/sitemap.xml`을 제출하고 URL 검사/웹페이지 수집을 이용합니다.

## GitHub 저장소의 Website
- https://github.com/yangdukparents/yangdukparents.github.io → About 영역의 톱니바퀴 → Website에 `https://yangdukparents.github.io/` 입력 → Save changes.

## 7개 색인 대상 URL
- https://yangdukparents.github.io/
- https://yangdukparents.github.io/garden.html
- https://yangdukparents.github.io/reading.html
- https://yangdukparents.github.io/culture.html
- https://yangdukparents.github.io/explore.html
- https://yangdukparents.github.io/experience-2026.html
- https://yangdukparents.github.io/school-life-2026.html

## 주의
- HTML/서치어드바이저의 소유 확인은 고유 토큰이 발급되고 실제 공개 사이트에 반영되어야 완료됩니다. 이 파일만 올렸다고 자동 인증되는 것은 아닙니다.
- 카카오톡 공유 썸네일은 메타태그 반영 뒤에도 캐시로 인해 이전 이미지가 보일 수 있습니다.
- 학부모 자율 제작 비공식 사이트 고지, 2026학년도 정보 출처 및 학년도 구분, 학부모 제작 팜플렛·사진 등의 사용 권한 확인이 필요합니다.
