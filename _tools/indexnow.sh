#!/bin/sh
# tells bing + yandex + seznam + naver every url changed (reads the sitemap)
# run after a deploy: sh _tools/indexnow.sh
KEY=4c72ed452b9c33086ba6e0c2561eaf52
URLS=$(grep -o '<loc>[^<]*' sitemap.xml | sed 's/<loc>//' | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
curl -s -o /dev/null -w "indexnow %{http_code}\n" -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"arnaudleroy.com\",\"key\":\"$KEY\",\"keyLocation\":\"https://arnaudleroy.com/$KEY.txt\",\"urlList\":$URLS}"
