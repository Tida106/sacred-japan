# Sacred Japan - CLAUDE.md

## 進行中タスク（2026-10-25時点・未完了）
- 【進行中】サイトのデザイン変更検討：背景色をもう少し濃いピンクにする案。Artifact（Designキャンバス）でサンプル作成済み → https://claude.ai/artifact/T85DptEdMxn9d6y9Q7Ebk5 。現行--washi(#fdf0f3)に対し案A(#f8d9e0)／案B(#f3c4d1)／案C(#e8a8ba)を比較するカードと、さらにセクションごとに下に行くほど濃くなる5段階グラデーション案（Hero→Footer、#fdf0f3→#e8a8ba）のサンプルを作成。ユーザーがartifact側で表示できず未確認（キャンバスのズレ疑い、再読み込み・fit to screen案内済みだが未解決）。次にやること：artifact再確認→好みの案決定→実サイトのCSS変数（--washi, --washi-dark等）に反映してpush

## PC表示の可読性調整（2026-10-27実施・完了）
- 本文が小さい／狭いとの指摘を受け、PC（幅900px以上）のみ：article p 17.5→19.5px、li 19px、.site-card p 16.5px、main max-width 860→900px。74ページに一括反映（末尾の@media、コミットa8bdd6d）。残り10ページ（トップ・guides/culture/castles/anime/crafts/regional-food/about・shrines2本）も個別CSSで同日反映：ハブ2本は幅1100px＋文字拡大、castles等はdesc文字+1〜2px、shrines2本は記事と同じ設定
- autumn-sanctuaries：カード群（.iconic-block）のみ1200px以上で幅1100px。カード見出しリンクの青下線を修正
- パンくずが<nav>でグローバルのsticky navスタイルを拾いメニューに混入していた不具合を、div[role=navigation]に変更して84ページ修正（コミット66a3770）。今後パンくずに<nav>タグを使わないこと
- 目安：人気サイトの本文は17〜21px。20px超は避ける。まだ読みにくければ本文幅を820px前後に絞る案

## 季節の行事と食べ物ガイド（2026-10-27実施）
- 新規 guides/seasonal-traditions/（春＝花まつり／夏＝夏越の祓・水無月／秋＝月見・七五三／冬＝除夜の鐘・初詣・節分）。事実は Discover Kyoto／Kyoto Travel／Nippon.com／Keihan／Wikipedia で裏取り、ページ末の sources-note に記載。ヒーロー写真は shrine-etiquette の神田明神初詣（CC BY 2.0）を再利用、本文中に唐津くんち写真（CC BY-SA 2.5）
- 反映先：guides/index.html（By Seasonカード＋JSON-LD position 60）、sitemap.xml、index.html（季節カード下のリンク）、festivals/autumn-winter-festivals・summer-festivals の関連カード、OGP（images/og/og-guides-seasonal-traditions.jpg）
- 【未対応】Search Consoleのインデックス登録リクエスト（guides/seasonal-traditions/）、季節ガイド（春・冬）の記事側からの相互リンク追加

## 紅葉・季節コンテンツ作業メモ（2026-10-25実施・完了）
- ホーム季節カード4枚を各ガイドにリンク：春=guides/cherry-blossoms-shrines-temples/（新規）、夏=festivals/summer-festivals/、秋=guides/autumn-sanctuaries/、冬=guides/kyoto-illuminations/。ガイドハブに「By Season」グループ追加
- 祭りページ（festivals/・summer-festivals/）のAI画像を実写真（Wikimedia Commons）に置換、各祭りに公式／紹介サイトへのリンク追加
- guides/autumn-sanctuaries/：冒頭に高台寺の石段（CC0）、聖域5つの前に「The Famous Ones First」節（有名8スポット：清水寺・ライトアップ・日光・厳島・永観堂・東福寺・嵐山天龍寺・高野山、各カードに公式/観光協会リンク、清水寺・東福寺・永観堂・天龍寺の写真）。日光東照宮の写真は紅葉が見つからず無し
- 新規ガイド（検索流入狙い）：guides/tofukuji/（GUIDE 56）、guides/eikando/（57）、guides/tenryuji/（58）。いずれも一人称ガイド視点＋FAQ5問＋公式リンク＋Expedia/Viator、ハブ・JSON-LD・sitemap・OGP・相互リンク反映済み。OGP生成は一時スクリプトで実施（リポジトリ内に常設スクリプト無し）
- guides/nikko-toshogu/ と guides/itsukushima-shrine/ に紅葉の節＋写真を追加（日光=標高順に色づく、いろは坂の渋滞対策／宮島=紅葉谷公園）
- 写真の流れ：ユーザーがCommons/Openverseで探して写真本体＋作者・ライセンスのスクショを送る→1200px幅でjpg/webp生成→figcaptionに作者・ライセンス・via Wikimedia Commons。CC BY-NC-ND等（NC/ND）は使用不可。写真が必要な記事は毎回、検索リンク付きで伝えること
- 料金・開門時間は資料間で食い違うため、記事では「約」「公式で確認」表記
- 【未対応】Search Consoleのインデックス登録リクエスト：tofukuji / eikando / tenryuji / cherry-blossoms-shrines-temples、更新したautumn-sanctuaries・nikko-toshogu・itsukushima-shrine。公式リンクが確認できなかった日光東照宮は未リンク（nikko-kankou.org系の確認待ち）
- 【次の候補】他の紅葉定番（醍醐寺、光明寺など）の単独ガイド、桜記事のOmuro桜写真差し替え、背景色ピンク案の決定

## regional-food 公式リンク作業メモ（2026-10-24〜25実施・完了）
- 18食品カードすべてのGoogle Maps検索リンクを公式観光サイトリンクに差し替え、Amazon「Get at Home」バッジを関連性の高い5品（Edomae Sushi／Takoyaki／Sanuki Udon／Hakata Tonkotsu Ramen／Goya Champuru）に追加（コミット0414c07）。Sapporo Miso Ramenは別途Maruchan Gold Spicy Misoバッジで先行対応済み（コミット893cc7e, 3513b5b）
- 公開後、ユーザーのライブ確認で3件のリンク切れが判明（discover-nagasaki.com全体停止／gotokyo.org 502／edolegacytravel.metro.tokyo.lg.jp メンテナンス中）→ 差し替え（コミット8125bb6）：
  - Nagasaki Champon → https://www.japan.travel/en/ca/cuisine/kyushu/nagasaki/
  - Tsukishima Monjayaki → https://thegate12.com/article/262
  - Edomae Sushi → japan.travel Kanto（関東全般ページで寿司への言及が薄く、ユーザー指摘で再修正）→ gotokyo.orgの寿司特集記事に変更（コミットefb0877）→ gotokyo.orgがサイト全体502で落ちていることが判明し、Time Out Tokyoの江戸前寿司の由来記事に最終差し替え（コミットf181eef、現行）
- 【教訓】gotokyo.orgは本セッション中に複数ページで502が発生（/en/spot/85/、寿司記事）。サイト全体が不安定な可能性が高いため、今後このドメインを新規リンクの候補にする際は特に注意（なるべく避けるか、採用前に必ずライブ確認）
- 現状：3件とも差し替え完了・push済み・タグバランス確認済み。ユーザーには毎回Cloudflareキャッシュパージを依頼済み。追加のリンク切れ報告があれば同じ手順（WebSearch→WebFetchで現役確認→差し替え→タグバランス確認→commit/push）で対応

## サイト基本情報
- サイト名: Sacred Japan（日本の神社・寺院ガイド）
- 公開URL: https://sacred-japan.net
- GitHub: https://github.com/Tida106/sacred-japan
- GitHub Pages運用（index.htmlが唯一のHTMLファイル）
- ターゲット：米国・欧州の英語話者

## 作業ルール
- 作業後は必ずGitHubにpushする
- GitHubアップロード時にindex.html.htmlになりやすいので注意
- index.htmlを編集する際はdivタグの開閉に注意
- レスポンスは簡潔に・日本語で返答する
- サイトはCloudflare経由で配信。画像追加・更新をpushした後はCloudflareダッシュボードでキャッシュパージが必要（このセッションにはAPIトークン無し、ユーザー側で実施）

## アフィリエイト構成
- Viator：PID P00298374（「Book a Tour →」赤ボタン）
- Expedia：camref=1101l5JmFa（「Find Hotels →」紺ボタン）
- AdSense：ca-pub-4224563062633828（審査中）
- Agoda：CID 1963662（審査中・現在カードから削除済み）
- Amazon US（sacredjapan-20）：2026-10-11、Associates USにsacred-japan.netを追加（trance-nexusと同一アカウント内）、新タグ取得。ホームのAmazonセクション9商品を amazon.co.jp→amazon.com、検索語も英訳して差し替え済み。JP版タグ（sacredjapan-22）は不使用に。Rakutenリンク（lucky-sun-shineのID使用）は削除済み。申請後180日以内に適格売上3件が必要（Associates規約）
- KKday：Involve Asia経由で申請予定（2026-10-11〜）。旅行ロジ系（eSIM/JRパス/WiFi）狙い。承認後、guides/japan-travel-planning/ に「Staying Connected」セクションを新設してリンクを埋め込む（money と rail セクションの間）
- VoiceMap（Awin, Merchant ID 99601／Awin Affiliate ID 2869709）：2026-10-16承認済み。音声ガイドアプリ（GPS連動の自己ガイドツアー）、手数料4〜10%。ディープリンクはAwinダッシュボード「Toolbox→Link Builder」から発行（このセッションにはAwin APIアクセス無し）。埋め込み済み4記事：guides/meiji-jingu/「Getting There」セクション、guides/best-shrines-kyoto/ Yasaka Shrineセクション（Gion districtツアー）、guides/sensoji/（Secrets of Sensoji Temple、FAQ直前に設置）、guides/kiyomizu-dera/（Kiyomizu-dera mysteries/legends/ritualsツアー、practical-list直後に設置）。meiji-jingu/best-shrines-kyotoはkey-calloutクラス使用、sensoji/kiyomizu-deraはkey-callout未実装のためインラインstyleで同等の見た目を再現。いずれもCTAボタン「Start the Audio Tour →」形式
- 【2026-10-16完了】VoiceMap：guides/fushimi-inari-taisha/にも埋め込み完了（Fushimi Inari Shrine: An In-Depth Guide）。既存の「Guided Walks」セクション（Viatorガイドツアー紹介）の直後に、セルフペース派向けの代替としてインラインリンクを追加（独立ボックスではなく地の文に自然に差し込む形）。これでVoiceMap埋め込みは計5記事（meiji-jingu／best-shrines-kyoto／sensoji／kiyomizu-dera／fushimi-inari-taisha）。他候補：Kamo River／architecture／tea cultureツアー（kyoto配下）、Shinjuku神社ツアー・Ebisuフードツアー（tokyo配下）は対応記事なし or 弱いため保留

## サイト構成
- スポットカード：24枚（3列×8行）
- Foodセクション：6枚
- Animeセクション：18記事、画像18枚とも設置済み
- 日本地図：images/japan-map.png（再生成済み・チェッカー柄解消）
- ガイド：/guides/temple-stay/, /guides/japan-travel-planning/ 追加済み（2026-10-11）
- カルチャー：/culture/kamidana/ 追加済み（2026-10-11）

## 次にやること
1. AdSense・Agoda承認後に対応
2. KKday：Involve Asiaにsacred-japan.netをプロパティ追加済み（2026-10-11、カテゴリ：Travel/IT & Internet/Hobbies, Arts & Crafts）→審査中（Pending）。承認されたらKKdayに提携申請→承認後リンクをもらって埋め込む
3. Amazon US（sacredjapan-20）：180日以内に適格売上3件必要。承認状況を定期的に確認
4. GA4データ（event_label/event_category カスタムディメンション、2026-10-10登録）が反映され次第、ページ別アフィリエイトクリックを分析
5. GA4データ蓄積後（1〜2ヶ月）にサイト構成見直し

## 完了事項
- Pinterest：/anime/ のkusunoki-tei, noragami, ryomen-sukunaはピン作成済み。fruits-basket/inuyasha/your-nameはlucky-sun-shine.comと重複するため対象外（完了・対応不要）

## ホームページ改善メモ（2026-10-12実施）
- ヒーロー画像にCSSのみでインパクト追加（動画・新規画像・AI生成は不使用、LCP維持のため）：Ken Burns風ズーム、斜め光のシマー、桜の花びらが「ひらひら」舞い落ちるアニメーション（外側divで落下、内側divで独立した左右スウェイ＋回転を重ねることで、直線的な「羽根」ではなく本物の花びららしい不規則な動きを実現）。prefers-reduced-motionで無効化対応済み
- 地図（images/japan-map.png, .webp）をチープなクローム調3Dレンダーから刷新：実際の都道府県GeoJSON境界データ＋geopandas/matplotlibで、サイトのブランドカラー（beni/kin等）に地方ごと正確に着色したフラットなベクター地図に変更。列島を-16度回転＋トリミングして横長構図に最適化、離島の小片はノイズとして除去、日英バイリンガルラベル＋ソフトシャドウを追加。washi背景との馴染みを確認済み（コミット86a22f6）
- 【対応済み】Templesボタンの色を薄いグレーブルー(#8e9eab)→抹茶グリーン(#4a5e3a)に変更。Shrinesの赤との重み不揃い解消、かつHokkaidoの水色(#5bacd4)との印象被りも解消（コミットa3f1461, fe4893c）
- 【対応済み】地図（images/japan-map.png/.webp）の地方色を、独自配色からフィルターボタンの実際の色（Kanto #e8928a／Kansai #8b5fa8／Chubu #c9a84c／Chugoku #6a9e6a／Shikoku #a393c8／Kyushu #e07840／Tohoku #3a9e7e／Hokkaido #5bacd4）に完全一致させ、地図とボタンの対応関係を明確化（コミットfe4893c）

## 構造改革メモ（2026-10-11実施）
- ホーム＋ハブ8ページ（guides/culture/castles/crafts/anime/regional-food/festivals/about）のモバイルメニューを地域グループ構成に統一、新規ページ全部リンク済み
- 孤立ページ5つ発見・解消：hebikubo-shrine, seimei-shrine, hokakuji, samukawa-shrine, best-castles-japan（hokakujiはsitemapにも無かった）
- best-castles-japanのネスト`<a>`タグバグ（13箇所）修正
- Viatorダミー箱：kotohira-guは削除、hiraizumi/dewa-sanzan/takachihoは広域検索語に差し替え（Tohoku/Yamagata/Miyazaki）
- 【2026-10-11 完了】個別記事65本の短縮版バラバラだったモバイルナビを、ハブページと同じ地域グループ構成の完全版に統一（div/ul/li/a balance=0確認済み、コミットac2490f）
- 【2026-10-11 完了】anime配下の内部リンクも機械チェック。fruits-basket/inuyasha/kusunoki-tei/spirited-awayはanimeハブ以外からリンクされておらず、対応するguide記事（nikko-toshogu/fushimi-inari-taisha・best-time-fushimi-inari/atsuta-shrine/kotohira-gu）側は既にアニメ記事へリンクしていたが逆方向が無かった（片方向リンク）。該当5ガイドの関連記事セクションに相互リンクを追加（コミットd3b0027）
- 【2026-10-11 完了】noragami・your-nameの未解消だった内部リンク問題を、新規ガイド記事2本の執筆で解消：guides/yushima-tenmangu/（湯島天満宮、458年創建の力の神→1355年に菅原道真の祟り神テンジンへ乗っ取られた経緯、受験シーズンの絵馬壁、梅まつり、神田明神との組み合わせ）とguides/suwa-taisha/（諏訪大社、四社中三社に本殿が無い構造、建御名方の敗走神話、御柱祭）。事実はWeb検索で裏取り済み。サイトの一人称guide視点＋FAQ4問＋締め＋関連ガイド（anime記事への相互リンク含む）の型に完全準拠。ハブページのKanto／Chubu&Tokaiグループ・JSON-LD ItemList（position 50-51）・モバイルナビ・sitemap.xml・OGP画像すべてに反映済み（コミットae179a6）
- 【2026-10-11 完了】OGP画像バッチ生成（コミットdf8f766）で一部ページ（20本）のog:image:width/heightが旧ogp.pngの寸法（1424×752）のまま更新されていなかったバグを発見・修正。正しい1200×630に統一（コミットae179a6）

## コンテンツ品質メモ（2026-10-11実施）
- 問題：Gemini DeepResearchで集めた素材をそのまま貼るだけで、サイトの語り口（一人称「As a licensed guide」＋神話/伝説フック）に変換していなかった記事が存在（原因はDeepResearch自体ではなく変換工程の欠落）
- 該当4本（katsuragawa, kongoin, ryuonji, hashikuraji）は冒頭＋本文の地の文を書き直し済み。事実・出典・リンク・構造はそのまま、div balance=0確認済み
- 今後、DeepResearch素材から記事を作る際は「素材収集→一人称・ストーリーフックへの変換」を必須工程にする
- GA4で上記4本の表示回数を確認したところ過去28日間すべて0。原因は文章の硬さ以前の問題で、guides/index.html（ハブページ）にカードが無く、autumn-sanctuaries記事以外から一切リンクされていない「孤立ページ」状態だった（構造改革メモの孤立ページ発見時に見逃していた分）
- katsuragawa, kongoin, ryuonji をハブページのKansaiグループに追加。hashikurajiとkotohira-gu（同じく未掲載だった）用に新規「Shikoku 四国」地域グループを新設して追加。JSON-LD ItemListにposition 44〜48を追加。div balance=0確認済み（2026-10-11, コミットd3b4b95）
- 全ページ対象に内部リンク数を機械チェックし、guides/omamori/（culture/omamori-guide/からしかリンクされていなかった）も発見・ハブに追加（position 49, コミット8b5e5d2）。これでチェック範囲内（guides/shrines/culture配下）の孤立・弱リンクページは解消済み
- 【2026-10-11 完了】全65記事（anime 8本、culture 9本、guides 46本、shrines 2本）を本文全文で通読し語り口を精査（開幕段落だけの高速スクリーニングではなく、全文を実際に読んだ）。結果：5本目の問題記事としてguides/hokakuji/を発見（他の4本と同じ「素材貼り付けのまま」状態で、かつ他記事の1/3程度の文字数、一人称なし、FAQなし、締めの一文なし）。一人称guide視点＋FAQ＋締めに書き換え済み（事実は元記事にあったもののみ使用、新規の住所・創建年等は創作せず）。div balance=0確認済み（コミットa390118）
- 他に見つかった「硬い」記事はゼロ。確認した別タイプの語り口（いずれも問題ではなく意図されたバリエーション）：kyoto-illuminations/meiji-jingu/nikko-toshogu/shikoku-pilgrimage/todaiji＝「学術的スリラー」調、samukawa-shrine/hebikubo-shrine/seimei-shrine＝絵文字・箇条書き多用の「情報密度重視リスト」調。これらはhedge文体ではなく独自のフックを持つため書き換え対象外と判断
- 今後、新規記事を素材から作る際は必ず「一人称guide視点＋フック＋FAQ＋締めの一文」を含める。文字数が他記事の半分未満になりそうな場合は特に要注意（hokakujiはこれが見逃しの主因だった）

## 実写真追加メモ（2026-10-13実施）
- 記事に画像が無いと「殺風景」との指摘を受け、guides/culture配下67記事を機械チェックしたところ49記事が画像ゼロと判明。全部は非現実的なので、検索されやすい有名どころ6本から着手
- 手法：Wikimedia Commonsの検索URLを渡してユーザー側で候補を探してもらい、良さそうな写真の位置を指定→ライセンス（CC BY/BY-SA/CC0等）と作者名をスクショで確認→本体を送ってもらう→1400px/1050px幅にリサイズ・トリミング（4:3）してjpg/webp両方生成→ヒーロー画像（記事冒頭、max-height:420px、object-fit:cover）＋本文中1枚（関連セクション末、max-width:420px）の計2枚構成で設置、全てfigcaptionに作者名・ライセンスリンク・Wikimedia Commonsのクレジット表記を記載
- 完了26記事（コミット順）：fushimi-inari-taisha（社殿／狐像）、kiyomizu-dera（本堂舞台／音羽の滝）、meiji-jingu（大鳥居／森の小川）、izumo-taisha（本殿屋根／しめ縄）、kasuga-taisha（拝殿／吊り灯籠）、best-shrines-kyoto（平安神宮大鳥居／八坂神社楼門）、todaiji（大仏殿／大仏）、nikko-toshogu（陽明門／三猿彫刻）、tsurugaoka-hachimangu（本殿／大鳥居）、ryoanji（石庭／方丈畳間）、byodoin（鳳凰堂全景／鳳凰像）、zenko-ji（本堂／仁王門）、atsuta-shrine（森の鳥居／摂社）、hakone-shrine（湖の大鳥居／神事）、enryakuji（根本中堂／横川）、kumano-kodo（参道階段／大鳥居／大社本殿の3枚構成）、mount-koya（奥の院／根本大塔）、naritasan-shinshoji（大本堂／三重塔）、kawasaki-daishi（大本堂／仲見世通り）、omiya-hikawa-jinja（楼門／参道鳥居／舞殿の3枚構成）、suwa-taisha（下社秋宮神楽殿／下社春宮鳥居）、yushima-tenmangu（本殿／絵馬の壁／梅と女坂の3枚構成）、samukawa-shrine（拝殿／三の鳥居と神池橋）、hebikubo-shrine（表参道鳥居／弁財天近くの鳥居。shrines/配下）、seimei-shrine（鳥居の五芒星／晴明井。shrines/配下）、dewa-sanzan（羽黒山五重塔／月山稜線）、hiraizumi（中尊寺本堂前雪景色／地蔵堂脇雪景色。金色堂は堂内撮影禁止のため建物自体ではなく境内風景を採用）、takachiho（高千穂峡ボート／真名井の滝）、kyoto-illuminations（清水寺青レーザー／高台寺水鏡／高台寺竹林の3枚構成）、nara-day-trip（鹿の群れ／春日大社の石灯籠と鹿）、best-castles-japan（姫路城／松本城／熊本城／二条城の4城4枚構成に拡張完了）、temple-stay（高野山・金剛三昧院の精進料理膳／高野山・蓮花定院の門）、koyasan-temple-stay（奥の院・御廟橋／奥の院の墓石群と鳥居）、hashikuraji（ロープウェイからの桜景色／中門）、japan-travel-planning（新幹線ホーム／東京市街地を走る新幹線）、shikoku-pilgrimage（本山寺の弘法大師像／白装束のお遍路さん）、omamori（清水寺のお守り2点／三十三間堂のお守り）、shrine-etiquette（神田明神の初詣／弓弦羽神社の鈴緒）、what-is-shinto（北海道・森の神社／壹岐宮の鳥居）、goshuin-guide（平等院での揮毫／西国三十三所の納経帳）、sacred-animals（伏見稲荷の狐像／奈良の鹿／田端八幡神社の狛犬の3枚構成。烏〈八咫烏・熊野〉はCommonsに写真なしで対応見送り）、omamori-guide（授与所の様子／お守り各種の陳列）、three-sacred-treasures（伊勢神宮内宮の鳥居／神楽殿。神器自体は非公開のため舞台となる神社で代替）、shrine-vs-temple（平安神宮の大鳥居／本国寺の仁王門。鳥居vs山門の見分け方セクションに対応）、why-did-you-come-to-japan（千本鳥居トンネル／参拝者のいる千本鳥居。番組自体の写真は使用不可のため「自分の旅へ」セクションの鳥居ステップに対応させた）
- スキップ：hokakuji（記事は奈良県の廃墟寺が題材だが、Wikimedia検索は同名の山梨県甲州市の現役寺院がヒットしてしまい無関係。奈良版で再検索しても無名すぎてCommonsに写真なし→対応見送り）、katsuragawa（滋賀・葛川息障明王院、Commonsに写真なし→対応見送り）、ryuonji（Commonsに写真なし→対応見送り）、kongoin（舞鶴・金剛院。「Kongoin」単独検索は1件のみで無関係の可能性、「Kongoin Maizuru」は0件、日本語「金剛院 舞鶴」は広すぎて護衛艦「こんごう」やコスプレ写真が混入し本物の金剛院か確証が持てず→対応見送り）
- guides配下は実写真追加対象がこれで全て完了。2026-10-15、guides/culture/shrines配下の画像ゼロ記事はこれで全て完了（対応見送りの4本を除く）
- 【2026-10-15 第2弾・完了】文字数の割に写真が少ない記事（2200語超で写真2枚以下、または1800語超で写真1枚）を機械チェックし、3枚目／2枚目を追加する作業。対象20記事すべて完了。
  - 3枚目追加完了（13記事）：shrine-vs-temple（浅草寺の大香炉）、goshuin-guide（八坂神社南楼門）、best-shrines-kyoto（上賀茂神社の立砂）、best-time-fushimi-inari（混雑時の正面鳥居）、omamori-guide（お焚き上げの焚き火）、shrine-etiquette（手水舎の柄杓）、what-is-shinto（祓串を振る神職）、byodoin（宇治上神社の拝殿）、koyasan-temple-stay（壇上伽藍・根本大塔）、hakone-shrine（杉並木の参道）、tsurugaoka-hachimangu（実朝暗殺の石段）、dewa-sanzan（三神合祭殿）、enryakuji（東塔の堂宇）
  - 2枚目追加完了（7記事）：kotohira-gu（表参道の石段）、dazaifu-tenmangu（神牛像）、kinkakuji（屋根上の鳳凰）、sensoji（仲見世通り）、ise-grand-shrine（内宮・宇治橋）、itsukushima-shrine（干潮時の大鳥居）、sumiyoshi-taisha（反橋）
- ユーザー指示（2026-10-14）：進行確認（「続ける？」）は不要、次の記事を直接出す運用に変更
- 【2026-10-15 完了】副産物として判明していたguides/meiji-jingu（約833語・FAQ無し）を拡充。新規セクション4つ（Who Is Enshrined／Burned in 1945, Rebuilt in 1958／Reading the Approach：夫婦楠・酒樽とワイン樽・大鳥居／Inner Garden and Kiyomasa's Well）を追加し約1950語に。FAQ6問＋FAQPage JSON-LD、closing-blockも新設。事実はWeb検索で裏取り済み（thegate12.com, gltjp.com）、新規写真追加は無し（既存2枚を再利用）。TOC更新・div等タグbalance=0確認済み（コミットbedea59）

## SEOメモ（2026-10-11実施）
- hokakujiのみ`<meta name="robots" content="noindex, follow">`になっておりGoogle非インデックス状態だった（全46ガイド中唯一）。`"index, follow"`に修正（コミットf7562c0）。sitemap.xmlには元々掲載済みだったので別途修正不要
- FAQPage構造化データ（JSON-LD）：guides/culture/shrines配下でFAQセクションを持つ45ページ中44ページは既に実装済み（過去セッションで対応済みと判明）。未実装だったhokakujiのみ追加（4問、コミットae26eec）
- OGP画像：50ページ（guides/culture/anime/shrines配下）が汎用ogp.pngのみに依存していた。サイトのデザイントークン（washi/beni/sumi等）を使ったブランド付きタイトルカード画像を自動生成するPythonスクリプト（PIL/Pillow）を作成し、該当50ページ全部に個別画像を設置（images/og/og-<section>-<slug>.jpg、コミットdf8f766）。既に実写真を使っていた15ページ（best-castles-japan, dazaifu-tenmangu, ise-grand-shrine, itsukushima-shrine, kinkakuji, kotohira-gu, meiji-jingu, nikko-toshogu, sensoji, sumiyoshi-taisha, kamidana, demon-slayer, noragami, ryomen-sukuna, your-name）は対象外（変更なし）
- OG画像生成スクリプトはh1のタイトル抽出で`<em>`タグ直後の句読点（: , . ; ! ?）前に余計なスペースが入るバグがあったが修正済み（正規表現で除去）

## 宿坊ガイド写真追加（2026-10-31）
- guides/temple-stay/ に実写真7枚を追加（高野山の宿坊：無量光院の客室・夕食、成就院の客室2＋布団、奥之院の灯籠参道、座禅堂＝CC0・場所不明のため「illustrative」表記）。Search Console表示が上がってきたため。全て作者・ライセンス（CC BY 2.0 / BY-SA 3.0 / CC0）をfigcaptionに記載

## カード見出しの表記変更（2026-10-31）
- regional-food／crafts／castles のカード見出しを、英語を上（大きく）・日本語を下（小さく・enshu色）に変更（海外読者向け）。HTMLの順序をname-en→name-jpに入れ替え、CSSでサイズ調整（コミット済み）
- 同じ変更をホーム（.spot-card 24枚）とanime（.anime-card 18枚）にも適用済み（ホームのhover「↗」は英語名側に移動）。festivals系ページは該当クラスなし

## アニメ記事リライト（2026-11-01実施）
- 背景：アニメ記事が「論文調」で読者の動機（あの場面はどこ？）に答えていなかったため、8本すべてを新しい型で書き直し（noragami→your-name/demon-slayer/spirited-away/inuyasha/fruits-basket/ryomen-sukuna/kusunoki-tei）
- 型：冒頭は場面や設定のフック（一人称ガイド）→「場面→実在の場所→行き方」の対応表（確度も併記：公式／広く言われる／ファン説）→体験セクション→場所別Expedia/Viator枠→FAQ4問（FAQPage JSON-LD）→締めの一文
- ルール：公式に確認できない対応は断言しない（ファンの聖地マップ由来と明記）。誤情報だった「神田明神がノラガミの場面」の記述は湯島天満宮ガイドとホームのカードも修正済み
- 判明：アニメハブ（anime/index.html）はGoogleマップリンクの18カード（別作品）で、8記事はホームのカードからしかリンクされていなかった。ハブ上部に「In-Depth Pilgrimage Guides」8カードを追加（2026-11-01）
- 【未対応】Search Consoleの再インデックス登録（8記事）

## アニメ聖地ガイド新規3本（2026-11-01実施）
- 新規：anime/lucky-star/（鷲宮神社）、anime/anohana/（秩父）、anime/love-live/（神田明神）。リライト版と同じ型、写真なし（OGPはPILで簡易カード生成）。ハブ「In-Depth」カードとsitemap反映済み（コミットc11d27f）
- 事実はWikipedia／kanko-map／ANN／FUN! JAPANで裏取り。最寄り駅の徒歩時間や料金は古い記事由来のため「要確認」表記
- 【未対応】写真追加（3本とも）、Search Consoleインデックス登録、
- 追加2本（同日）：anime/girls-und-panzer/（大洗磯前神社・大洗町）、anime/hyouka/（高山・日吉神社）。JNTO／watabi／rawjpn／Ibaraki観光で裏取り、写真なし。【未対応】写真追加、インデックス登録（lucky-star／anohana／love-live／anime/＋この2本。2026-11-01は上限到達のため翌日）

## 工芸ハブ再構成と工芸ガイド追加（2026-11-01実施）
- 方針：外部の公式サイトに頼る構成から、自前記事へ誘導する構成へ。工芸ハブ（/crafts/）は3ヶ月で最もクリックが多い工芸ページ（CTR 2.1%）。記事が出来た工芸カードは、画像リンク・「Read the full guide」ボタンを自前記事へ、公式サイトは小さい下線リンクに降格。記事が無いカードは従来のまま
- 対象：nambu-tekki／edo-kiriko／arita-ware＋新規 bizen-ware／wajima-nuri。ハブ最上部に「Try a Craft Yourself」（金継ぎ・陶芸・藍染め・江戸切子・和紙・茶道のViator検索リンク6枚＋kintsugi記事カード）。【要確認】Viator検索結果が0件のカードが無いか
- 新規ガイド3本：guides/kintsugi/（Wikipedia）、guides/bizen-ware/（岡山県公式観光）、guides/wajima-nuri/（Wikipedia＋KOGEI Standardの2024年報告）。edo-kirikoのページ構成を流用、写真なし。輪島の被災・宿泊状況は2024年秋時点の記事のため「要確認」表記
- 【2026-11-01 写真追加済み】kintsugi・bizen-ware（東博の皿＋箱根美術館の鉢、Daderot CC0）・wajima-nuri（赤い飯椀、yuuki CC BY-SA 4.0）。ヒーロー＝ベルリン民族学博物館の金継ぎ茶碗（Daderot, CC0）、本文＝Ruthann Hurwitzの青い鉢（CC BY-SA 4.0）。
- 【未対応】3本の写真追加、インデックス登録、残り13工芸の記事化（優先：Mashiko、Awa Aizome、Nishijin、Kaga Yuzen、Hagi、Shigaraki）
- 今後の工芸記事の作り方：edo-kiriko型（冒頭フック→what→選び方/見どころ→訪問→FAQ→結び）、体験Viator枠、ハブカードを自前記事リンクに切替
- 背景（Search Console 3ヶ月）：アニメ系クエリが上位、/anime/が2位、ホームは表示19,515でCTR0.4%。ホームに「Start here」3入口、/anime/はタイトル・H1をキーワード化し詳細13記事を最上部に移動

## 城の単独ガイド（2026-11-01開始）
- 城ハブ（/castles/）最上部に詳細ガイドカードを配置（READ FIRST）。新しい城ガイドはここにカードを足す
- 新規：guides/himeji-castle/（公式歴史ページ／Wikipedia／japan-guide／Japan Timesで裏取り。2026年3月から非居住者2,500円・市民1,000円。お菊井戸は「伝説」として記述）。ヒーローはbest-castles-japanと同じBernard Gagnon写真（CC BY-SA 3.0）を再利用。ハブ・JSON-LD(position 69)・sitemap・OGP反映済み
- 作り方：scratchpadのcraft.py（edo-kiriko複製）＋castle_run.py。本文中の内部リンクにはclass="inline-link"を付けること（付けないと青リンクになる）
- 本文写真5枚追加済み（外観Gorgo PD／回廊Drivephotographer CC0／火縄銃pdeaudney CC BY 2.0／天守内部Zairon CC BY 4.0／お菊井戸Drivephotographer CC0）
- 【未対応】インデックス登録（guides/himeji-castle/、/castles/）。次の候補：松本城、熊本城、犬山城、彦根城、二条城（京都）
- 新規：guides/matsumoto-castle/（Wikipedia／GLTJP／Go Nagano／Nagano Tabiで裏取り。料金はGLTJPの電子券1,200円・紙1,300円を「最近のガイド」として記載、公式確認を促す表記）。ヒーローはbest-castles-japanと同じManishprabhune写真（CC BY 4.0）。ハブ・JSON-LD(position 70)・sitemap・OGP・城ハブ上部カード反映済み。【2026-11-01 写真追加済み】鎧レプリカ(lumoplank CC0)／天守内部・月見櫓内部(z tanuki CC BY 3.0)／月見櫓の窓(KimonBerlin CC BY-SA 2.0)／雪(Beggerly CC BY 2.0)／雪囲い(Japanexperterna CC BY-SA 3.0)／アルプスと天守(tsuruta yosuke CC BY 2.0)。Fg2のPD写真は青枠注釈入りのため未使用。【未対応】インデックス登録。次の候補：熊本城、犬山城、彦根城、二条城
- 新規：guides/kumamoto-castle/（GLTJP／Wikipedia／熊本城復旧見学ルート公式／Nippon.comで裏取り。料金800円・9:00-17:00・12/29休はGLTJP引用で「公式確認」表記。復旧完了目標2052年。ヒーローはbest-castles-japanと同じ663highland写真 CC BY-SA 3.0）。ハブ・JSON-LD(position 71)・sitemap・OGP・城ハブ上部カード反映済み。城3本のヒーロー上ラベルの「伝統工芸」残りを「城」に修正。【未対応】本文写真追加、インデックス登録。次の候補：犬山城、彦根城、二条城
- 熊本城：2026-07-28にM7.1の地震（震源は宇城市付近、最大震度7＝宇城市・氷川町）があり、石垣40か所崩落・11か所に構造被害（天守の床のひびを含む）、16日間閉鎖→8/13再開（The Star／The Art Newspaper／GIGAZINE）。ガイドに「July 2026: Shaken Again」節を追加、タイトルを「Walls, Two Earthquakes and Visiting Today」に変更（OGP再生成、ハブ・JSON-LD反映）。FAQ・復旧目標（2052年は再延期の可能性）も更新。【注意】guides/best-castles-japan/ の熊本城節は2026年地震未反映の可能性。
- 熊本城 本文写真6枚追加済み（663highland×2 CC BY-SA 3.0／Nagoya Taro CC BY-SA 3.0／Fraxinus2 CC BY-SA 4.0／そらみみ CC BY-SA 3.0／Katorisi 2026崩落の石垣 CC BY-SA 4.0）。663highlandの「人々が歩く石垣」はヒーローと同一のため未使用。【未対応】インデックス登録。次の候補：犬山城、彦根城、二条城

- 新規：guides/inuyama-castle/（GLTJP／japan-guide／FUN! JAPANで裏取り。創建年は1537年説と他説があり「one of the oldest」表記、料金1,000円（浦楽園セット2,000円）・9:00-17:00・12/29-31休は「公式確認」表記。ナルセ家が2004年まで所有）。ハブ・JSON-LD(position 72)・sitemap・OGP・城ハブ上部カード反映済み。写真なし（既存のimages/castle-inuyama.jpgは出典不明のため未使用）。【未対応】ヒーロー＋本文写真追加、インデックス登録。次の候補：彦根城、二条城
\n
- 犬山城 写真7枚追加済み（ヒーロー：桜の天守 Tomio344456 CC BY-SA 4.0／犬山橋からの遠景 Alpsdake CC BY-SA 3.0／梁 Hyppolyte de Saint-Rambert CC BY 4.0／上段の間 村国左近 CC BY-SA 4.0／木曽川と城 KKPCW CC BY-SA 4.0／犬山祭の山車2枚 Bariston CC BY-SA 4.0）。【未対応】インデックス登録。次の候補：彦根城、二条城
- 新規：guides/hikone-castle/（japan-guide／Wikipedia／彦根市観光で裏取り。天守は大津城から移築、明治の取り壊しを天皇の要請で免れた説、玄宮園、ひこにゃん。料金1,000円（博物館込み1,500円）・8:30-17:00はjapan-guide引用で「公式確認」表記）。ハブ・JSON-LD(position 73)・sitemap・OGP・城ハブ上部カード反映済み。写真なし。【未対応】ヒーロー＋本文写真追加、インデックス登録。次の候補：二条城
- 彦根城 写真8枚追加済み（ヒーロー：紅葉の天守 Martin Falbisoner CC BY-SA 4.0／石畳の道 Mti CC BY-SA 3.0／天秤櫓・太鼓門櫓・西の丸三重櫓 z tanuki CC BY 3.0／ひこにゃん Hyppolyte de Saint-Rambert CC BY-SA 4.0／夢京橋キャッスルロード Sakaori CC BY 3.0／堀の桜 Luka Peternel CC BY-SA 4.0）。【未対応】インデックス登録。次の候補：二条城

## アニメ記事：写真4枚化と聖地巡礼寄りの書き直し（2026-11-02開始）
- 方針：全13アニメ記事を写真4枚に（リール化のため）。現状：anohana 3／love-live 1／他11本は2枚。ユーザーが写真＋ライセンスのスクショを送るので、入れられるだけ入れる。誤った場所の写真（例：山梨・笛吹の定林寺は秩父のAnohanaとは別寺）は使わない
- 書き直し：理論寄りの節を縮め、「Pilgrimage Plan」のkey-calloutで行き方・時間・料金・開放日を明記。済み：ryomen-sukuna（千光寺：タクシー約20〜30分、宝物館500円、冬季休、宿儺堂は開放日要確認）、spirited-away（道後：市電15〜20分、商店街約250m、Kami no Yu／Tama no Yu、開館時間は要確認、神道形而上学ボックスを縮約）。【未対応】fruits-basket（日光の歩き方）、kusunoki-tei、inuyasha、demon-slayer、noragami の巡礼プラン化
- 2026-11-02 anohana：秩父神社の節（#chichibu-shrine）を新設し写真7枚追加（鳥居 yamai36 CC BY 3.0／赤門・本殿隅の龍 Carbonium CC BY 3.0／拝殿 NY066 CC BY-SA 3.0／つなぎの龍・北辰の梟・元気三猿 tak1701d CC BY-SA 3.0）。写真ごとの解説あり（出典：jinjajourney、japan-guide）。Anohanaは計10枚。リールは4枚に絞って使う。写真が多い記事は写真ごとに説明文を書く方針（ユーザー指示）
- 2026-11-02 love-live：神田明神の写真6枚＋解説を追加（随神門と銅の鳥居 Kakidai CC BY-SA 3.0／随神門の彫刻2枚・ハート形おみくじ台 Hyppolyte de Saint-Rambert CC BY-SA 4.0／祭務所と神楽殿の夕景 Simo Räsänen CC BY-SA 4.0／手水舎の龍 江戸村のとくぞう CC BY-SA 4.0）。Love Liveは計7枚。noragamiにも鳥居と手水舎の龍を再利用（計4枚）。パス注意：神社マナー記事は /culture/shrine-etiquette/（/guides/ではない）
- 2026-11-02 love-live：階段2枚（Junya Ogura CC BY-SA 2.0／Simo Räsänen CC BY-SA 4.0）＋神田祭2枚（Jose Fernando CC BY-SA 2.0／江戸村のとくぞう CC BY-SA 4.0）を追加。Love Liveは計11枚
- 2026-11-02 lucky-star：鷲宮神社の写真6枚＋解説を追加（旧大鳥居2012・参道・社殿側面・屋根 Peter Schlömer CC BY-SA 3.0／新鳥居2023 Lukini CC BY-SA 4.0／絵馬の壁 Nao Iizuka CC BY 2.0）。Lucky Starは計8枚。旧鳥居の写真は「2018年に倒壊し交換」の記述と対応させて新旧比較で見せている
- 2026-11-02 girls-und-panzer：大洗磯前神社の写真7枚＋解説を追加（神磯の鳥居・波 Saigen Jiro PD／正面鳥居・境内・本殿 Saigen Jiro PD／階段・随神門 Σ64 CC BY 3.0／絵馬 KΛΝΛΤΛ CC BY-SA 3.0）。計9枚。随神門の掲示は「月次祭 1日・15日 10時」と読み取れるが「要確認」表記
- 2026-11-02 hyouka：写真9枚＋解説を追加。新節#yatai（高山祭の屋台：神楽台 Gagnon CC BY-SA 3.0／屋台2枚 Chme82 CC BY-SA 4.0／屋台会館2枚 Daderot CC0）、古い町並み（雪の通り2枚 Raita Futo CC BY 2.0／パノラマ2枚 z tanuki CC BY 3.0）。計11枚。日吉神社の祭礼日を「4/14・15（春）、10/9・10（秋・桜山八幡宮）」に修正（旧記述の4/3は削除）。屋台2枚の撮影日は30 Apr 2017表記のみで祭礼日とは断定せず
- 2026-11-02 noragami：新節#yushima-visit（湯島天満宮）に写真6枚＋解説（銅鳥居と露店 江戸村のとくぞう CC BY-SA 4.0／拝殿 Carbonium CC BY 3.0・Ph0kin PD／回廊 KimonBerlin CC BY-SA 2.0／絵馬 Vellut CC BY 2.0／臥牛 Daderot CC0）。noragamiは計10枚
- 2026-11-02 noragami：梅・夕景（Pbdragonwang CC BY-SA 4.0×2／Manish Prabhune CC BY 4.0）と新節#suehiro（末廣神社 Higa4 CC0×3）を追加。計16枚。夜の湯島天満宮の写真は作者が不明（ライセンス画面が切れていた）ため未使用。末廣神社の写真1枚（狛犬）はライセンス画面なしで未使用
- 2026-11-02 your-name：須賀神社の写真4枚＋解説を追加（階段を見上げ・鳥居・拝殿 Higa4 CC0／階段を見下ろし Yuet Man Lee CC BY-SA 4.0）。計6枚。飛騨古川の写真は未追加
- 2026-11-02 your-name：飛騨古川の写真3枚＋解説（駅舎・駅名標 そらみみ CC BY-SA 4.0／起し太鼓展示の建物 Asturio Cantabrio CC BY-SA 4.0）。計9枚。瀬戸川・白壁土蔵の写真は未追加
- 2026-11-02 your-name：瀬戸川と白壁土蔵（Asturio Cantabrio CC BY-SA 4.0）を追加。計10枚
- 2026-11-02 demon-slayer：浅草の雷門の写真3枚＋解説を追加（正面 Daderot PD／仲見世から提灯 MIKI Yoshihito CC BY 2.0／軒と金龍山の扁額 Another Believer CC BY-SA 4.0）。計5枚。雷門は1865年焼失→1960年再建のため大正期の浅草には無かった旨を記載
- 2026-11-02 demon-slayer：竈門神社（太宰府）の写真3枚＋解説を追加（拝殿2枚・式部稲荷の鳥居 いずれもそらみみ CC BY-SA 4.0）。計8枚。拝殿2枚の撮影時刻はスクショ上2枚（15:27/15:31）だが写真との対応不明のため時刻は記載せず
- 2026-11-02 spirited-away：道後温泉本館の夜のバルコニー写真1枚を追加（Takuya Matsuyama CC BY 3.0、2015年）。計3枚。色付きの窓は特別ライトアップの可能性があるため「日によって異なる」と記載
- 2026-11-02 spirited-away：道後温泉の写真5枚＋解説を追加（商店街 Raita Futo CC BY 2.0／本館正面 Wei-Te Wong CC BY-SA 2.0／飛鳥乃湯泉の畳の広間・浴室・椿の湯 松山市役所 CC BY 4.0）。新h3「The Two Other Public Baths」。計8枚。本館正面は2017年（改修前）のため「現在と異なる可能性」と記載
- 2026-11-02 fruits-basket：日光東照宮の写真4枚＋解説を追加（雀の彫刻 pastaitaken CC BY 3.0／神厩舎 Fg2 PD／神厩舎の彫刻列 Joli Rumi CC BY-SA 4.0／三猿 foooomio CC BY 2.0）。新h3「Also at Nikko: The Sacred Stable and Its Monkeys」。計6枚。【要確認】雀の写真はCommonsの説明が「Tombe de Humayun」と不一致のファイルのスクショと対応させた（320px・小さい）。違えば削除
- 2026-11-02 kusunoki-tei：鳳来寺の写真5枚＋解説を追加（石段入口・892段目と医王院・鐘楼2枚・紅葉の本堂 いずれもAlpsdake CC0）。新h3「Up the Stone Stairs」（#lore直前）。計7枚。仁王門の写真はヒーローと同一ショットのため未使用。傘杉の写真は未入手
- 2026-11-02 kusunoki-tei：傘杉の写真2枚＋解説を追加（根元・見上げ Alpsdake CC0、Commons説明：樹齢800年以上・樹高約60m・幹回り約7.5m）。石段入口の直後に配置。計9枚
- 2026-11-02 inuyasha：葛葉稲荷神社の写真4枚＋解説を追加（入口の鳥居 阪神強いな CC BY-SA 3.0／拝殿・狐の碑・姿見の井戸 KENPEI CC BY-SA 3.0）。#kuzunoha節の末尾。計6枚。入口の写真は2007年撮影のため「変わっている可能性」と記載。【未対応】伏見稲荷の写真追加
- 2026-11-02 inuyasha：伏見稲荷の狐像の写真6枚＋解説を追加（跳ぶ狐2枚 Oren Rozen／Alice.liv CC BY-SA 4.0、鍵の狐 Dumphasizer CC BY-SA 2.0、巻物の狐 Hyppolyte de Saint-Rambert CC BY-SA 4.0、苔の狐 Jakub Hałun CC BY 4.0、陶器の狐と小鳥居 Immanuel Giel CC BY-SA 4.0）。計12枚。【要確認】苔の狐と巻物の狐の作者対応は縦横比が同じため撮影地点・ファイルサイズから推定。鍵の狐と陶器の狐はCommons説明に場所の明記なし
- 2026-11-02 inuyasha：千本鳥居の写真3枚＋解説を追加（Balon Greyjoy CC0／DXR CC BY-SA 4.0／Kakidai CC BY-SA 4.0）。計15枚。【未対応】Ryomen Sukuna（千光寺・高山）の写真
- 2026-11-02 ryomen-sukuna：千光寺本堂（Tomio344456 CC BY-SA 4.0）、円空作 両面宿儺像1685（Toyotsu CC BY-SA 4.0・阿倍野ハルカス円空展、千光寺の像とは限らない旨を記載）、宿儺像（Ryōmen-sukunal CC BY-SA 4.0・撮影地不明）の3枚＋解説を追加。計5枚。Pilgrimage Planの直前に配置。全13記事の写真追加はこれで一巡
- 2026-11-02 ryomen-sukuna：渋谷事変の節（#shibuya）を新設。場面→実在の場所の対応表（渋谷駅B5F/B4F・ヒカリエB3F・マークシティ通路・スクランブル交差点・明治神宮前・青山霊園）、巡礼プラン、Expedia/Viator枠、FAQ1問（JSON-LD含む）、TOC追加。出典FUN! JAPAN／Tabimania Japan。ナナミンの最期の場所は資料が食い違うため記載せず。【未対応】渋谷の写真追加（ユーザー指示）。タイトル・meta・ハブのカード文言の渋谷反映は未実施
- 2026-11-02 ryomen-sukuna：渋谷スクランブル交差点の写真1枚＋解説（Syced CC0、ハロウィン2023、警備・バリケードは通常ない旨を記載）。【未対応】明日の神話／渋谷駅構内／ヒカリエの写真、タイトル・冒頭への渋谷反映、アニメハブのカード文言
- 2026-11-02 ryomen-sukuna：渋谷の夜景写真1枚（David Kernan CC BY 4.0、渋谷ストリームから）追加。計7枚。昼のヒカリエ/マークシティ外観は世界観に合わないため不採用（ユーザー判断）。【未対応】明日の神話／駅構内の写真、タイトル・冒頭・アニメハブへの渋谷反映
- 2026-11-02 ryomen-sukuna：タイトル／meta／H1／冒頭／スナップショットに渋谷を反映（「Jujutsu Kaisen Locations: Shibuya Incident Map and Senko-ji」）、アニメハブのカード文言も更新。【未対応】明日の神話／駅構内の写真、再インデックス登録
- 2026-11-02 PHOTO-CREDITS.csv を新設（全ページのfigcaptionから 画像・ライセンス・作者・Commonsリンクを一覧化）。写真追加後は再生成すること。スクリプトは本ファイルの手順参照（figure/figcaptionを正規表現で抽出）
- 2026-11-02 新規：guides/nijo-castle/（japan-guide／Wikipedia／熊日（二条城の二重価格化報道）で裏取り。1603年家康→1626年家光、二の丸御殿（国宝6棟）、うぐいす張りの音の仕組み（釘と金具の摩擦、侵入者用とは断定せず）、1867年慶喜の大政奉還、1939年京都市に寄贈・1940年公開、1994年世界遺産、本丸御殿は2024年9月再公開・要予約＋1,000円。料金800円＋二の丸500円=1,300円、2026年10月1日報道で2027年度中に二重価格（市民1,000円／市民以外2,000円）の計画＝確定ではない旨を記載。ヒーローはbest-castles-japanと同じ京都束の唐門写真（CC BY-SA 4.0）。ハブ・JSON-LD(position 74)・sitemap・OGP・城ハブ上部カード反映済み）。【未対応】本文写真（二の丸御殿・庭園・紅葉・桜など）、インデックス登録（guides/nijo-castle/、/castles/、/guides/）
- 2026-11-02 nijo-castle：本文写真3枚＋解説を追加（二の丸御殿の破風 Nacaru CC BY-SA 4.0／台所の活け花と箏 Reggaeman CC BY-SA 3.0・2009年4月／二の丸庭園の池 Reggaeman CC BY-SA 3.0・同）。破風は「車寄せ」とは断定せず屋根の破風として記載。活け花は台所での撮影（Commons説明）で、館内撮影ルールは場所・行事で異なる旨を記載。PHOTO-CREDITS.csv追記済み。【未対応】本丸御殿・紅葉・桜の写真、インデックス登録
- 2026-11-02 nijo-castle：庭園写真2枚追加（夏の池 そらみみ CC BY-SA 4.0・2015年9月／苔と紅葉 Guilhem Vellut CC BY 2.0・Commons日付2014年3月）。苔と紅葉の写真は3月撮影のため『11月の色の目安ではない』と本文に明記。計5枚（ヒーロー除く）。【未対応】本丸御殿・桜・梅・本物の11月紅葉の写真、インデックス登録
- 2026-11-02 nijo-castle：本物の紅葉写真を追加（Maechan0360 CC BY-SA 3.0・Commons日付2008-12-01、GFDL併記だがBY-SA 3.0を採用）。苔の写真の直後。計6枚。【未対応】本丸御殿・桜・梅の写真、インデックス登録
- 2026-11-02 nijo-castle：堀と石垣（#history末）・桜の木々（紅葉の直後）の写真2枚を追加（KimonBerlin CC BY-SA 2.0・2011-04-08）。2枚の撮影時刻/座標はスクショ上2通りだが作者・ライセンス・日付は同一のため、写真との対応は不確かでもクレジットは正確。計8枚。【未対応】本丸御殿・梅の写真、インデックス登録
- 2026-11-02 nijo-castle：本丸御殿の写真1枚追加（DXR CC BY-SA 3.0・2013-08-11、Commons説明『本丸御殿の建物の一つ』）。#honmaru第1段落の直後。計9枚。2013年撮影のため2024年再公開後の状態と異なる可能性を明記。玄関の唐破風写真は未入手。【未対応】インデックス登録
- 2026-11-02 nijo-castle：二の丸御殿の室内写真1枚追加（Zairon CC BY-SA 4.0・2018-04-11、金地の松の壁画・格天井）。活け花の直後。計10枚。館内は通常撮影禁止で、写真は特別な状況の可能性がある旨を本文に明記。【未対応】梅・玄関の写真、インデックス登録
- 2026-11-02 新規：guides/matsue-castle/（Visit Matsue公式（城・城下エリア）／Nippon.com／松江市（祈祷札・国宝指定の経緯PDF）で裏取り。1611年完成（堀尾吉晴・5年）、現存12天守で山陰唯一、国宝5城の一つ、千鳥城、地階の井戸24m、1950年に国宝資格を失い2012/5/21に松江神社で祈祷札2枚再発見→2015/7/8国宝指定。料金は公式サイト1,200円だが古い資料は670〜680円で食い違うため「公式確認」表記。堀川遊覧（公式2,000円・約40分／Nippon.com約50分）、塩見縄手、パス情報。人柱伝説は裏取りできず不掲載）。ハブ・JSON-LD(position 75)・sitemap・OGP・城ハブ上部カード反映済み。写真なし（ヒーロー無し）。【未対応】ヒーロー＋本文写真追加（天守外観・井戸・堀川遊覧・塩見縄手・小泉八雲旧居・桜など）、インデックス登録（guides/matsue-castle/、/castles/、/guides/）。城の残り：弘前・丸岡・備中松山・丸亀・松山・宇和島・高知
- 2026-11-02 matsue-castle：写真8枚＋解説を追加（ヒーロー：夏の天守 663highland CC BY-SA 3.0・2008-07／雪の天守 Suicasmo CC BY-SA 4.0・2017-01／堀川の船・小泉八雲記念館の門・旧居の縁側 663highland CC BY-SA 3.0・2008-07／塩見縄手 663highland・2015-03／八雲旧居の庭 Reggaeman CC BY-SA 3.0・2006-09／和室 irisgazer Public Domain Mark・2019-01、Commons説明は『at Matsue City』のみのため『illustrative・建物は不明』と表記）。1枚目と3枚目のスクショ（663highland 2008-07-20）と船／夏の天守の対応は不確かだが作者・ライセンス・日付は同一。PHOTO-CREDITS.csv追記済み。【未対応】井戸・天守内部・桜の写真、インデックス登録
- 2026-11-02 matsue-castle：写真7枚＋解説を追加（桜前の天守と提灯 Peter Broster CC BY 2.0・2007-03＝#keep末／天守からの眺め・鎧の展示ケース 江戸村のとくぞう CC BY-SA 4.0・2015-09／天守内部 Mister99 CC BY-SA 3.0・2011-06／兜の展示列 Mti CC BY-SA 3.0・2013-12／角の兜・鹿角状の前立ての兜 G41rn8 CC BY-SA 4.0・2016-10）。#insideに新h3「Armor and Helmets」。兜の札「六十二間総覆輪兜」は『私の読み』として要確認表記、卍の注記あり、持ち主は不明のため断定せず。眺め/鎧（とくぞう）とG41rn8の2枚の対応はスクショ上不確かだがクレジット同一。計15枚（ヒーロー含む）。【未対応】井戸の写真、インデックス登録
- 2026-11-02 新規：guides/hirosaki-castle/（GLTJP／Wikipedia／弘前市（石垣修理・天守曳戻しページ、2026-10-28更新）／弘前公園公式（内部見学休止）／Web東奥／Japan Worldで裏取り。1603計画→1611完成、1627落雷焼失、1810三層再建、東北唯一の現存天守。2015年に約70m曳家（市ページ77.6m）、石垣積み直し2021-2024年末（2,185石）、2026-07-01曳戻し1次移動開始、着座は当初2026年11月→市の最新で2027年3月中に天守台へ・2027年秋に固定。天守内部は2025-11-24から令和14年度（FY2032）まで休止、外観は2028年秋頃まで見られその後は保護囲い（市）。遅延理由は報道で土台の傷みとされるが市ページに明記なしと記載。料金320/100円・4/1-11/23 9-17時（GLTJP）、植物園込みかは資料間で食い違い。桜約2,600本・約50種、まつり4/23-5/5頃・花筏はピーク後2-3日（Japan World）。Kikko門の矢傷はGLTJP1ソースのみと明記。ヒーロー・本文写真なし）。ハブ・JSON-LD(position 76)・sitemap・OGP・城ハブ上部カード反映済み。【未対応】写真追加（曳家中の天守・下乗橋・花筏・桜・追手門・石垣など）、インデックス登録、曳戻し完了後（2027年春）に記事更新。城の残り：丸岡・備中松山・丸亀・松山・宇和島・高知
- 2026-11-02 matsue-castle：ハーン旧居の看板写真1枚＋解説を追加（kajikawa CC BY 3.0・2014-09、Panoramio由来）。看板は2014年で大人300円・4-9月8:30-18:30・10-3月8:30-17:00・定休なしだが、Visit Matsue現行は400円のため『古い』と明記。計16枚（ヒーロー含む）
- 2026-11-02 hirosaki-castle：写真10枚＋解説を追加（ヒーロー：仮台座の天守 掬茶 CC BY-SA 4.0・2022-05／曳家前の天守2枚 Si-take CC BY-SA 3.0・2007-05（GFDL併記）、Kojin PD・2010-05／追手門と桜 掬茶・2025-04／南内門の雪夜 掬茶・2020-02／秋の夜景 Feri88 CC BY 3.0・2010-11（塔の名は不明で未特定）／夜桜の橋 mko294 CC BY 4.0・2021-04／堀の並木・花筏・松と桜の反射 掬茶・2026-04）。スクショと写真の対応は送信順の逆順で確定。雪灯籠の行事名はCommonsに無いため断定せず。PHOTO-CREDITS.csv追記済み。【未対応】インデックス登録、曳戻し完了後（2027年春）に記事更新
- 2026-11-02 新規：guides/matsuyama-castle/（GLTJP／Nippon.com／Wikipedia／ANA／公式パンフレットで裏取り。1602年加藤嘉明、1784年落雷で天守焼失、現天守は1854年再建（Nippon.comは1852年）、現存12天守、重要文化財21棟、登り石垣（彦根と松山のみ）、野原櫓。料金520円・ロープウェイ/リフト往復520円はGLTJP等引用で「公式確認」表記、定休日は未確認のため明記せず）。ハブ・JSON-LD(position 77)・sitemap・OGP・城ハブ上部カード反映済み。写真なし。【未対応】ヒーロー＋本文写真追加、インデックス登録（guides/matsuyama-castle/、/castles/、/guides/）。城の残り：備中松山・丸岡・丸亀・宇和島・高知
- 2026-11-02 matsuyama-castle：写真12枚＋解説を追加（全てZairon CC BY 4.0・2023-10-21。ヒーロー＝天守上層／広場と天守／下から見上げ／隅の低角度／天守内の廊下2枚／鎧4領（加藤嘉明・松平定行・定長・定直と伝わる）／伊予四季図屏風（遠藤広実）／眺望）。鎧4枚はスクショの寸法で対応確定。スクショ11枚に対し写真12枚で1枚だけスクショ未確認（作者・撮影日同一のため同一作者と判断、違えば削除）。PHOTO-CREDITS.csv追記済み。【未使用】Jyo81の写真（櫓2棟と十間廊下、2011-03、GFDL/CC BY 3.0）：スクショにAuthor欄が写っておらず保留。Author欄入りのスクショが来たら追加。備中松山城用にReggaeman 2006-04-08 大手門跡の石垣（CC BY-SA 3.0／GFDL）の写真を scratchpad/bitchu/otemon-walls.jpg に保管済み
- 2026-11-02 matsuyama-castle：リフトの写真1枚追加（lienyuan lee CC BY 3.0・2014-10-18、Commonsタイトルは『Ropeway』だが一人乗りのためリフトと判断し本文で注記）。計13枚
- 2026-11-02 matsuyama-castle：眺望の写真1枚追加（Suicasmo CC BY-SA 4.0・2017-01-23、屋根の鯱と市街・遠くの海）。計14枚
- 2026-11-03 matsuyama-castle：「12天守で最も高い」の記述（161m）が誤り（備中松山城は430m）だったため削除し、「GLTJPはhonmaruを約161mとする」に修正（本文・オープニング・FAQ・JSON-LD）。他ページに同種の記述が無いかは未確認
- 2026-11-03 新規：guides/bitchu-matsuyama-castle/（公式サイトの歴史・ガイド／Nippon.com／GLTJP／japan-guideで裏取り。1240年秋庭重信の砦、1574備中兵乱・三村元親、小堀政次・遠州、水谷勝宗の1681-83大修築で天守・二重櫓・本丸南御門、1694年赤穂浅野家→大石内蔵助が約1年管理、1873廃城令、信濃友春の調査・1939-40昭和大修理（学生が約2万枚の瓦を運ぶ）、1941重文、1997/2003修復、標高430m・12天守で唯一の山城。水谷勝宗/勝隆の功績はNippon.comと公式で食い違うため併記。料金500円・200円、4-9月9-17:30/10-3月9-16:30、12/29-1/3休、ふいご峠駐車場から徒歩約20分、シャトルバスの区間・料金は資料間で食い違うため「公式確認」表記。猫のさんじゅーろうは2018年記事のみで現状未確認と明記。写真：大手門跡の石垣1枚（Reggaeman CC BY-SA 3.0・2006-04-08）、ヒーローなし。ハブ・JSON-LD(position 78)・sitemap・OGP・城ハブ上部カード反映済み。城ハブの既存Bitchuカード（castle-bitchu-matsuyama）は外部リンクのまま）。【未対応】写真追加（天守・雲海・城下・猫・石段）、インデックス登録。城の残り：丸岡・丸亀・宇和島・高知
- 2026-11-03 bitchu-matsuyama-castle：写真7枚（ヒーロー雲海 Jogungagon CC BY-SA 4.0・2021-11-19／城下 Jogungagon CC BY-SA 4.0・2022-05-07 雲海展望台から／猫さんじゅーろう あかしょうぴん CC BY 4.0・2025-08-03／天守 Reggaeman PD（作者が公有化）・2006-04-08／天守と二重櫓・本丸 Reggaeman CC BY-SA 3.0・同／大手門跡の石垣は既設）。Reggaemanの3枚はスクショの説明文と写真内容の消去法で対応。猫の節は2025-08の写真で更新。PHOTO-CREDITS.csv追記済み。城の残り：丸亀・丸岡・宇和島・高知
- 2026-11-03 新規：guides/marugame-castle/（GLTJP／japan-guide／Wikipedia／Nippon.com／KSBニュース2023・2024で裏取り。築城開始は1587年説(Wikipedia)と1597年説(Nippon.com/japan-guide)、現天守1660年、高さ約15m・三重、重文。石垣「60m」はGLTJPの堀から天守までの全体、単独の高石垣は20m超(Nippon.com/Wikipedia)と区別して記載。2018年7月豪雨で三の丸・帯曲輪の石垣が崩落、根石の発見で31m、回収石11,746個(2024)、復旧完了は2027年度末→2028年3月→2031年3月と報道で後ろ倒し＝要確認。料金400円・9:00-16:30(最終16:00)はGLTJP/japan-guide引用で「公式確認」、徒歩10分(GLTJP)/15分(japan-guide)。写真なし）。ハブ・JSON-LD(position 79)・sitemap・OGP・城ハブ上部カード反映済み。【未対応】ヒーロー＋本文写真追加、インデックス登録。城の残り：丸岡・宇和島・高知
- 2026-11-03 marugame-castle：写真11枚＋解説を追加（ヒーロー：北面の天守 Naokijp CC BY-SA 4.0・2019-05-03／本丸から南西面 Naokijp・同／松の中の天守 Motokoka CC BY-SA 4.0・2010-09-24／天守からの眺め Suicasmo CC BY-SA 4.0・2017-01-21／城山の石垣 Toto-tarou CC BY-SA 3.0・2008-07／大手一の門 Toto-tarou・2005-04（640x480、低解像度）／門3枚 Motokoka・2010-09-24（Commons説明は「Gates of Marugame Castle」のみのため門の名前は断定せず）／門と堀 Tōjichi CC BY-SA 4.0・2021-04-06／堀と石垣と天守 Reggaeman CC BY-SA 3.0・2009-04-29）。Naokijpの北面写真が2回送られてきたため重複は1枚に。写真とスクショの対応は縦横比・説明文・サムネイルで確認、Motokokaの門3枚は撮影時刻とのひも付けが不確かだが作者・ライセンス・日付は同一。本文の「石垣の段数」は写真で複数段と確認できたため「several tiers」に修正。PHOTO-CREDITS.csv追記済み。【未対応】インデックス登録、崩落した石垣の写真（2018年豪雨後）
- 2026-11-03 marugame-castle：天守内部の写真2枚＋解説を追加（梁と天井・上階の床と火気厳禁の札 いずれもMotokoka CC BY-SA 4.0・2010-09-24、Commons説明「Interior of Marugame Castle」）。スクショ3枚（うち16:14:40が重複）に対し写真2枚、時刻との対応は不確かだが作者・ライセンス・日付は同一。階は不明のため断定せず。計13枚。
- 2026-11-03 新規：guides/maruoka-castle/（Wikipedia／GLTJP／japan-guide／Nippon.com／Fun! Japan／Markus Sesko（本多重次の手紙）／切手解説で裏取り。築城1576年（柴田勝豊）は伝承、天守は寛永期（Nippon.com）・2019年調査で柱が1626年以降（Wikipedia）・japan-guideは1600年代初頭＝時期は併記。石瓦は約6,000枚・約120t（Nippon.com/GLTJP、Wikipediaは60or120t）、階段最大67度（GLTJP）、1948福井地震で倒壊→1955再建、約70%部材再利用。お静の人柱伝説はWikipediaのみのため「伝説」と明記。手紙は訳が資料間で異なる（お仙を痩せさすな／泣かすな）、お仙＝仙千代＝成重（Sesko）→1613丸岡藩主（Wikipedia）。料金450/150円・8:30-17:00（最終16:30）・無休はGLTJP/japan-guide引用で「公式確認」。写真なし）。ハブ・JSON-LD(position 80)・sitemap・OGP・城ハブ上部カード反映済み。城ハブの既存Maruokaカード（castle-maruoka、外部リンク）はそのまま。【未対応】ヒーロー＋本文写真追加（石瓦・天守・急な階段・桜・堀・石垣）、インデックス登録。城の残り：宇和島・高知
- 2026-11-03 maruoka-castle：写真6枚＋解説を追加（ヒーロー：松の中の天守 baku13 CC BY-SA 2.1 JP・2010-05-29／下から見た天守 baggio4ever CC BY 3.0・2013-05-05（Panoramio由来）／石段下からの天守・天守内部 baku13・同日／急な階段とロープ 藤谷良秀 CC BY-SA 4.0・2017-02-12／桜と天守 アラツク CC BY-SA 4.0・2012-04-15）。baku13はGFDL併記だがCC BY-SA 2.1 JPを採用、アラツクは複数ライセンスから4.0を選択。写真とスクショの対応は日付・内容・縦横比で確認（baku13は3枚、baggio4everは1920x1080の1枚と推定）。石瓦そのものは写真で判別できないため本文で「出典に依拠」と明記。計6枚。【未対応】石瓦のアップ・お静の墓・堀の写真、インデックス登録
- 2026-11-03 maruoka-castle：お静慰霊碑の写真1枚＋解説を追加（藤谷良秀 CC BY-SA 4.0・2017-02-12、Commons説明「丸岡城内にあるお静の慰霊碑」）。中央の小さい石は何か不明のため墓とは断定せず。伝説の段落の直後。計7枚。
- 2026-11-03 新規：guides/uwajima-castle/（Nippon.com／GLTJP／Zooming Japan／ANA／Jeepeで裏取り。築城は藤堂高虎、開始は1601年説（Nippon.com/GLTJP）と1595-96〜1601年（Zooming/ANA）で併記。富田信高→1615年伊達秀宗入城、宗利が1661年から約11年かけ大改修（GLTJP）、望楼型天守を層塔型に建替え（Nippon.com）、天守は1666年頃・櫓門は1671年（Zooming）。3層3階・約15.8m（Zooming）、各階に装飾性の高い破風と懸魚＝太平の世の象徴（Nippon.com）、唐破風と千鳥破風（Jeepe）、現存12天守・重文（GLTJP/ANA）、1934年指定（Zooming）。伊達家紋「向かい合う二羽の鳥」はZooming単独のため要確認表記。山の標高は80m（GLTJP/ANA）と73m（Jeepe）で併記。料金200円・65歳以上160円・現金のみ、天守9-17時（3-10月）/9-16時（11-2月）は資料間で月の区切りが異なるため「公式確認」、駅から入口徒歩約15分・天守まで約35分（GLTJP/Jeepe）、入口から天守15-20分（Jeepe）。城山の博物館は名称・由来が資料間で食い違うため「free local-history museum」とのみ記載。写真なし）。ハブ・JSON-LD(position 81)・sitemap・OGP・城ハブ上部カード反映済み。【未対応】ヒーロー＋本文写真追加（天守・唐破風・登城路・上り立ち門・石垣）、インデックス登録。城の残り：高知
- 2026-11-03 uwajima-castle：写真12枚＋解説を追加（ヒーロー：Suicasmo CC BY-SA 4.0・2017-06／正面 Vickerman625 PD・2006-08／市街 Reggaeman CC BY-SA 3.0・2009-07／桜2枚 Yamaguchi Yoshiaki CC BY-SA 2.0・2008-03、PekePON CC BY-SA 3.0・2009-03／本丸石垣・上り立ち門（街側）Saigen Jiro CC0・2020-12／一の門跡・三の門跡・雷門跡・上り立ち門・桑折家長屋門 Reggaeman CC BY-SA 3.0・2009-07）。写真とスクショの対応は縦横比・説明文・看板で確認（上り立ち門のSaigen/Reggaeman取り違えと長屋門の特定は推定）。Vickerman625のPDはTemplate:PD-userへリンク。PHOTO-CREDITS.csv追記済み。【未対応】インデックス登録。城の残り：高知
- 2026-11-03 新規：guides/kochi-castle/（GLTJP／Japan Visitor／Japan Experience／Wikipedia（wikiwand経由）で裏取り。1601-1611山内一豊、1727火災→1729-53再建、天守1749、追手門の年代は資料間で食い違い（1801／火災を免れた／最古）で併記、天守の階数は4重6階／5階で併記、忍び返しの位置も資料間で相違。料金420円（GLTJP）と400円（他）併記、9-17時・12/26-1/1休。写真なし）。ハブ・JSON-LD(position 82)・sitemap・OGP・城ハブ上部カード反映済み。城ハブの既存Kochiカード（外部リンク）はそのまま。【未対応】ヒーロー＋本文写真追加（天守・本丸御殿・追手門・詰門・日曜市・桜・山内一豊像・板垣退助像）、インデックス登録。城ガイドは一巡完了（残り：なし）
- 2026-11-03 kochi-castle：写真13枚＋解説を追加（ヒーロー：石段と天守 663highland CC BY-SA 3.0・2008-02／天守下からバルコニー・詰門 Reggaeman CC BY-SA 3.0・2006-07／三の丸から天守・追手門 京浜にけ CC BY-SA 3.0・2010-08／天守低角度 ノボホショコロトソ CC BY 4.0・2024-12／天守からの市街 Suicasmo CC BY-SA 4.0・2017-01／パノラマ・模型・石段 z tanuki CC BY 3.0・2016-05／門内側 Higa4 CC0・2025-03／山内一豊像 baggio4ever CC BY 3.0・2013-02／日曜市 NevinThompson CC BY-SA 4.0・2014-03）。写真とスクショの対応は縦横比・撮影日・季節・内容で推定（特に模型=z tanuki、門内側=Higa4）。【保留（ライセンス/作者不明）】作者欄なしの2048x1536（本丸御殿入口と天守・平成19年看板）、京浜にけ「三の丸石垣」（ライセンス下部が未確認）、板垣退助像（写真側ライセンス未確認）。PHOTO-CREDITS.csv追記済み。【未対応】インデックス登録
- 2026-11-03 kochi-castle：保留していた2枚を追加（三の丸の石垣と楕円の石 京浜にけ CC BY-SA 3.0・2010-08-31／板垣退助像 z tanuki CC BY 3.0・2016-05-05、像の作者は本山白雲＝PD）。計15枚。PHOTO-CREDITS.csv追記済み
- 2026-11-03 kochi-castle：保留最後の1枚を追加（本丸御殿前の建物と天守 Taisyo CC BY-SA 3.0・2007-05-20、Commons説明『天守閣』のため御殿のどの部分かは断定せず。#palace末）。計16枚、保留ゼロ。PHOTO-CREDITS.csv追記済み
- 2026-11-03 best-castles-japan：熊本城節に2026-07の地震（M7.1・石垣約40か所・16日閉鎖→8/13再開）を追記しkumamoto-castleへリンク、dateModified更新。【確認済み】他の城ガイドに誤った『最も高い』記述なし（備中松山は430mで正）
- 2026-11-03 新規：guides/osaka-castle/（GLTJP／Japan-guide／大阪観光局／Wikipedia（ミラー）で裏取り。現存天守ではないが検索需要の大きい城として追加。1583秀吉着工・1585天守・1615落城・1620〜秀忠再建（天守は1628-30＝Wikipedia、1626＝GLTJPで併記）・1665落雷・1931コンクリート天守（市民寄付）・1995-97改修。天守5層8階・55m（大阪観光局）。石垣は1620s・花崗岩・モルタルなし・家紋刻印（Wikipedia）、豊臣期の石垣は徳川が埋め1950年代に再発見・2025年に豊臣石垣館が開館し入場券に含む（Japan-guideのみ＝要確認と明記）。重要文化財13件。西の丸庭園の料金（300/350円 vs 200円）・桜の本数（約600 vs 約300）は食い違うため併記。料金1,200円・9-18時（最終17:30）・12/28-1/1休。写真なし）。ハブ・JSON-LD(position 83)・sitemap・OGP・城ハブ上部カード反映済み。【未対応】ヒーロー＋本文写真追加（天守・桜・石垣・大手門・堀・西の丸庭園・豊臣石垣館）、インデックス登録。次の候補：名古屋城、江戸城（皇居東御苑）、岡山城、広島城
- 2026-11-03 osaka-castle：写真15枚＋解説を追加（ヒーロー：石垣と堀の天守 Otto Domes CC BY-SA 4.0・2018-05／南面 DXR CC BY-SA 4.0・2019-04／展望デッキと金の虎 dconvertini CC BY-SA 2.0・2019-05／夕景 Manish Prabhune CC BY-SA 4.0・2011-07（色が強調されている旨を明記）／内堀と屋形船 Joli Rumi CC BY-SA 4.0・2025-11／桜門・大手門 Zairon CC BY-SA 4.0・2018-04／大手門と千貫櫓 inoue-hiro CC BY-SA 3.0・2007-07（GFDL併記）／堀と隅櫓 Francisco Anzola CC BY 3.0・2015-10／全景 Saigen Jiro CC0・2017-05／池と庭園 Nacaru CC BY-SA 4.0・2024-02／芝生 663highland CC BY-SA 3.0・2009-09／極楽橋 Sakai Yayoi CC0・2026-08／桜と天守 Tom Purves CC BY 2.0・2006-04／夜桜イルミ Mc681 CC BY-SA 4.0・2015-04）。写真とスクショは縦横比・ピクセル寸法・内容で対応（芝生=663highland、橋=Sakai Yayoiは消去法）。Nacaruの庭は西の丸庭園とは断定せず。千貫櫓は資料で未確認のため注記。【未対応】インデックス登録。PHOTO-CREDITS.csv追記済み
- 2026-11-03 【名古屋城ガイド：2026-11-03 作成済み→下の記録参照】次の作業はosaka.py（scratchpad）を複製してnagoya.pyを作り、ハブ(guides/index.html position 84)・城ハブ上部カード・sitemap・OGP(名古屋城)・CLAUDE.mdメモ・各種チェック・push。調査メモ（出典：Wikipedia／名古屋城公式英語ページ／GLTJP item 20335／japan-guide e3300／watabi／japantravel）：
  - 1609-11家康が築城決定→1610-01着工（20大名の天下普請、加藤清正・福島正則・前田利光ら。石垣に刻印、清正石が最大）→天守1612-12完成、本丸御殿1615-02完成、二の丸御殿1617。普請奉行は中井正清（Wikipedia）
  - 金鯱：雄(北)2.621m・1,272kg・金44.69kg／雌(南)2.579m・1,215kg・金43.39kg（公式/Wikipedia）。1730・1827・1846に改鋳、1871に政府へ。1945-05-14空襲で焼失、1959に再建。2005に万博後に屋根へ戻る。Wikipediaは年表記に和暦の不整合があるため、年は1945焼失/1959再建のみ使用
  - 1893宮内省移管（名古屋離宮）→1930-12市へ下賜。1930に24棟が国宝指定→1945空襲で天守・本丸御殿など焼失。1952特別史跡。現天守は鉄骨鉄筋コンクリートで1959-10-03再公開
  - 本丸御殿：2009-2018復元（約10年・約150億円・30室超・書院造）、2018-06全面公開。撮影可（フラッシュ・三脚不可）
  - 天守は2018-05-07から閉鎖（耐震・老朽化）。木造復元は完成目標FY2032（GLTJP）だが、japan-guide等は2032年以降・確定スケジュールなしと表記＝併記して「要確認」。公式は天守「閉鎖中」のみ
  - 現存隅櫓3棟（西南・東南・西北。通常非公開）、東北隅櫓は戦災で焼失。二の丸庭園は国名勝（1953、2018拡大）
  - 料金：大人1,000円（2026-10-01から。以前500円、watabi/GLTJP/japan-guide一致）、中学生以下無料。9:00-16:30（御殿は16:00まで）、12/29-1/1休（GLTJP）。公式の料金ページは未確認＝「公式確認」表記
  - アクセス：地下鉄名城線「名古屋城」駅7番出口から徒歩約5分（2023-01-04に市役所駅から改称）。メーグルは月曜運休・1回210円/1日500円
  - 桜：約1,000本・10品種（GLTJP）、桜まつり3月下旬〜4月下旬。watabi：天守に登りたいなら大阪城を勧める
  - 写真が必要：天守外観と金鯱、本丸御殿、桜、堀と隅櫓

- 2026-11-03 新規：guides/nagoya-castle/（上記調査メモをもとに _tools/castle/nagoya.py で生成。タイトル「Nagoya Castle Guide: Golden Shachi, a Rebuilt Palace and a Keep That Is Closed」。天守は2018-05から閉鎖中を冒頭で明示、木造復元はFY2032目標（GLTJP）／2032年以降で未確定（japan-guide）を併記。本丸御殿2009-2018・約150億円・30室超・撮影可（フラッシュ・三脚不可）。金鯱の寸法と金量は公式／Wikipedia。料金1,000円（2026-10-01〜、旧500円）はGLTJP／japan-guide／watabi一致だが公式の料金ページ未確認＝「公式確認」表記。隅櫓は「通常非公開」と記載（見学可否は未確認）。FAQ5問。ハブ・JSON-LD(position 84)・sitemap・OGP・城ハブ上部カード反映済み、タグ均衡・JSON-LD・390px幅OK）。写真なし（ヒーロー無し）。【未対応】ヒーロー＋本文写真追加（天守外観と金鯱、本丸御殿、桜、堀と隅櫓）、インデックス登録（guides/nagoya-castle/、/castles/、/guides/）。次の城候補：江戸城（皇居東御苑）→岡山城→広島城

- 2026-11-03 nagoya-castle：写真4枚＋解説を追加（ヒーロー：天守と金鯱 Noodle snacks CC BY-SA 3.0・2008-08-09（3×3の合成）／下から見た天守 Syced CC0・2025-03-23／空撮パノラマ BobTanGo CC BY 4.0・2024-12-17／桜と天守 Hiroaki Kaneko CC BY-SA 3.0・2016-03-31（Panoramio由来、画像に「H. Kaneko」の透かし文字あり）。写真とスクショは寸法・日付・季節（下から見た天守＝裸木なので3月のSyced）で対応。（追記・同日）空だった2枚は再送で解決：本丸御殿の車寄せ風の建物 Mauricio V. Genta CC BY-SA 4.0・2023-08-27（6000×8000の縦長＝先に空だった黒画像と同寸）／天守の近景と金鯱2つ Syced CC0（stitched、Commonsの日付は仮の1970-01-01のため日付は載せない。6430×4351＝先に空だった白画像と同寸）を追加、計6枚。写真とスクショの対応は寸法による消去法。Commonsは建物名を明記していないため『entrance porchに見える』と記載。堀と隅櫓の写真は未入手。PHOTO-CREDITS.csv追記済み。【未対応】インデックス登録

## 【引き継ぎ】城ガイド量産の手順と運用ルール（2026-11-03・新チャット用）
### ユーザーとのやり取りの決まり
- 返答は丁寧な日本語・簡潔・結論先・温かいトーン・結びの言葉なし。推奨は1案に絞る
- 更新のたびに：①公開URL（クリック可）②Cloudflareキャッシュパージのお願い③Search Consoleインデックス登録のお願い（フルURLで、新規は各言語版も）。pushは毎回
- 写真が必要な記事は毎回、必要な写真と検索リンクを伝える。リンクは https://commons.wikimedia.org/w/index.php?search=TERM&title=Special:MediaSearch&type=image 形式（画像検索モード）、検索語は広め、クリック可のリンク（コードブロックにしない）
- 写真：ユーザーが写真本体＋作者・ライセンスのスクショを送る。作者・ライセンスが確認できない写真は使わず保留→Author欄/ライセンス欄のスクショを依頼。NC/ND不可。送られた写真は入れられるだけ入れ、全写真に解説段落を書く
- スクショだけ届いて写真本体が無い時は、読み取れたライセンスを一覧にして写真本体を依頼（責められた訳ではない）
- 料金・開館時間・年は資料間で食い違えば併記し「公式確認」。単一ソースは明記
- SNS：リール投稿時は「投稿直後にコメントを」と促す。コメント文はFB・Threads（フルURL）とInstagram（URLなし＝プロフィールのリンクへ）を別々に。リールは3〜4項目、1ページ約3.5秒、音楽なし
- コミット末尾に必ず付ける：
  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01EpyvmJaAWoN52Wmz9c73wc
### 写真追加の手順
- 写真⇔スクショの対応はピクセル寸法・縦横比・説明文・撮影日・消去法で行う
- 幅1200px（拡大しない）でjpg(q84)＋webp(q80)を guides/SLUG/images/ に保存
- figure：横長 max-width 760px／縦長 420px／ヒーローは `<main>` 直後の `<figure style="margin:0 0 48px;">`（eager、max-height 420px、object-fit cover）。figcaption＝作者・ライセンスリンク・「via Wikimedia Commons (resized)」＋解説の`<p>`
- PHOTO-CREDITS.csv（CRLF、列：page,image,license,license_url,commons_link,caption）に追記、CLAUDE.mdに記録
- GFDL併記はCC BY-SA側を採用
### 新規城ガイドのチェックリスト
1. 既存城ページ（osaka-castle）の head/tail を流用するビルダースクリプトで main を書き換え（_tools/castle/osaka.py を複製してnagoya.pyに。scratchpadが消えていたら osaka-castle/index.html から直接複製でも可）。本文内部リンクは class="inline-link"。パンくずに<nav>を使わない
2. guides/index.html：前の城カードの後ろにカード＋JSON-LD ItemList（次は position 84）
3. castles/index.html：上部カードを前の城の後ろに追加
4. sitemap.xml（lastmod当日）
5. OGP 1200×630：images/og/og-guides-matsue-castle.jpg をコピー→矩形[40,150,1170,380]を(252,240,242)で塗り、タイトル2行をDejaVuSerif-Bold 48pt (66,170)/(66,238)（2行目の幅<1090）、漢字をNotoSerifCJK-Bold.ttc 28pt (66,332)
6. CLAUDE.mdに記録
7. チェック：div/figure/picture/p/a/ul/li/details/section/h2のタグ均衡、JSON-LDのparse、スマホ390px幅の横はみ出し（Playwright、`390 []`なら問題なし。_tools/castle/shot_os.py）
8. commit→push
- ローカル確認：`cd /home/claude/sacred-japan && nohup python3 -m http.server 8765 &`（よく落ちる。再起動する。`pkill -f http.server`は使わない）
- WebFetchは許可リスト外で失敗しやすい。検索結果に出たURLか、japan-guide／watabi／japantravel等を使う。gltjpやWikipediaミラーは失敗することあり
### 名古屋城ガイドの方針
- 天守は2018-05から閉鎖中（本丸御殿と敷地は見学可）を冒頭で明示。木造復元の時期は「FY2032目標／2032年以降で未確定」を併記
- 追加で調べたい点：隅櫓の見学可否、公式の料金・時間ページ（nagoyajo.city.nagoya.jp/en/information/）
### 未対応バックログ（主なもの）
- インデックス登録（城：osaka／kochi／best-castles-japan／castles／guides、他は上記各メモの【未対応】参照）
- 写真待ち：丸亀（崩落石垣・桜）、丸岡（石瓦・堀）、備中松山（天守内部・石段）、高知（桜・本丸御殿）、二条城（梅・玄関）、松江（井戸）、松山城Jyo81（Author欄待ち）、名古屋城（作成後）
- アニメ記事の巡礼プラン化：fruits-basket／kusunoki-tei／inuyasha／demon-slayer／noragami。アニメ記事のリール
- 工芸記事の残り13（Mashiko、Awa Aizome、Nishijin、Kaga Yuzen、Hagi、Shigaraki優先）、/crafts/のViator 0件カード確認
- 弘前城は曳戻し完了後（2027年春）に更新。背景ピンク案の決定
- 次の城候補：名古屋城→江戸城（皇居東御苑）→岡山城→広島城
- 2026-11-03 nagoya-castle：写真6枚＋解説を追加（本丸御殿内部・縦 Mauricio V. Genta CC BY-SA 4.0・2023-08-27／金一色の間・海の絵の間 Kiyotaka Katsuragi CC BY-SA 4.0・2015（2枚と題名「対面所 次之間」2015-06-01／「表書院 二之間」2015-04-06の対応は不確かなため部屋名は載せず）／展示室「対面所」2枚 Gryffindor PD・2011-02-15（2011年の展示で再建御殿ではない旨を記載。4:3の1枚は同日の同一展示と推定）／二の丸茶亭の金の茶釜 Gryffindor CC BY-SA 4.0・2017-11-23（金曜10-16時の呈茶は2017年の記述＝要確認と明記））。#palace末に5枚、#grounds末に茶釜。計12枚。PHOTO-CREDITS.csv追記済み。【未対応】堀と隅櫓の写真、インデックス登録
- 2026-11-03 nagoya-castle：堀と桜の写真1枚＋解説を追加（Alpsdake CC BY-SA 4.0・2015-03-31、桜の解説の後・茶釜の前）。左奥の白い建物は不明のため隅櫓とは断定せず。計13枚。【未対応】隅櫓の写真、インデックス登録
- 2026-11-03 新規：guides/edo-castle/（GLTJP item 18846／japan-guide e3018／Wikipedia／国交省 多言語表記DB（天守台 H30-00468・松の大廊下跡 H30-00472）／Jeepeで裏取り。タイトル「Edo Castle Guide: A Missing Keep, Free Ruins and the East Gardens Today」。1457太田道灌→1590家康→1603将軍→1593-1636普請、天守1638完成（japan-guide）・5層約51m（Wikipedia）・1657明暦の大火で焼失、家綱が天守台を再建（1658）、叔父の進言で天守は再建せず（DB。保科正之とは明記なし）。天守台寸法は資料差（Wikipedia 41×45m高11m／DB 42×46m高10m）で併記。松の大廊下（約55m×4m）1701刃傷→1702討ち入り。現存：富士見櫓等（Wikipedia）／東御苑に天守台・三つの番所・富士見櫓（GLTJP）。東御苑は無料・入園票・大手門/平川門/北桔橋門。開園時間はGLTJP＝japan-guide（3/1-4/14・9月9-17、4/15-8月9-18、10月9-16:30、11-2月9-16、最終30分前）とJeepeで差があるため併記＝公式確認、休園は月・金と12/28-1/3（祝日の扱いは資料間で差）。FAQ6問。写真なし。ハブ・JSON-LD(position 85)・sitemap・OGP・城ハブ上部カード反映済み）。【未対応】ヒーロー＋本文写真（天守台・大手門・富士見櫓・百人番所・二の丸庭園・松の大廊下跡の碑・桜）、インデックス登録（guides/edo-castle/、/castles/、/guides/）。次の城候補：岡山城→広島城
- 2026-11-03 edo-castle：写真8枚＋解説を追加（ヒーロー：三層櫓 Another Believer CC BY-SA 4.0・2019-11-29（Commons題名は「Tokyo, 2019」のみ）／櫓を下から Fg2 PD・2005-12-24／百人番所 Celuici CC BY-SA 3.0・2017-05-20／池の庭パノラマ Don Ramey Logan CC BY-SA 4.0（アップロード2022-05-22、色は強調されている旨を記載）／夏の池 Guilhem Vellut CC BY 2.0・2013-08-14／松の道 Vellut・2013-11-26／門と橋の空撮 WPPilot CC BY-SA 3.0（アップロード2020-11-20）／門と橋と高層ビル Don Ramey Logan CC BY-SA 4.0（アップロード2022-09-03））。写真とスクショは縦横比・寸法・内容で対応。【要確認】WPPilotの写真はAuthor欄が写っておらず、「own work」のアップロード者名で表記。門の名前・櫓の名前はCommonsに明記がないため断定せず。スクショのみで写真が無かったChris 73・Otemon（Author不明）は未使用。PHOTO-CREDITS.csv追記済み。【未対応】天守台・桜の写真、インデックス登録
- 2026-11-03 新規：guides/okayama-castle/（GLTJP item 20347／Wikipedia／Jeepe（岡山1日コース）で裏取り。タイトル「Okayama Castle Guide: The Black Crow Castle, a 1966 Rebuild and Korakuen Next Door」。ナワ氏1346-69→1570宇喜多直家→1597秀家が天守完成（GLTJP:約8年・秀吉の指導）→関ヶ原・八丈島流罪→小早川秀秋→池田氏1602-1869（後楽園）→1869兵部省・外堀埋立1873-82。烏城：黒漆の下見板（GLTJP）、金瓦・金烏城（GLTJP）と、関ヶ原前は金瓦で現在は屋根の一部・鯱のみ金（Wikipedia、1996年に鯱を金箔）で併記し「金は約束しない」と記載。1945-06-29空襲で焼失（国宝だった）→1964-66コンクリート再建。現存：月見櫓（江戸期・本丸で唯一・外観2階で実は3階）・西手櫓（1603-15頃）＝重文（GLTJP）。料金500円・14歳未満無料（GLTJP）／小中学生無料（Jeepe）、後楽園セット800円（Jeepe）、9:00-17:30（最終17:00）・12/29-31休、後楽園500円（65歳以上200円）・3/20-9/30 7:30-18:00・10/1-3/19 8:00-17:00（Jeepe）、月見橋で接続（Jeepe）、路面電車東山線→城下駅徒歩約10分（総15分）。百名城スタンプはGLTJPの口コミ由来と明記。所要時間は資料に無く「私の見積り」と明記。ハブ・JSON-LD(position 86)・sitemap・OGP・城ハブ上部カード反映済み、タグ均衡・JSON-LD・390px幅OK）。写真なし。【未対応】ヒーロー＋本文写真（天守・月見櫓・西手櫓・石垣・月見橋・後楽園・夜のライトアップ）、インデックス登録（guides/okayama-castle/、/castles/、/guides/）。次の城候補：広島城
- 2026-11-03 okayama-castle：写真14枚＋解説を追加（ヒーロー：正面 663highland CC BY-SA 3.0・2008-01-31／金鯱 663highland（同作者・同ライセンスで2枚は入れ替わりの可能性）／春 Reggaeman CC BY-SA 3.0・2005-04-16／秋 Kimon Berlin CC BY-SA 2.0・Commons題名「Okayama Castle from Korakuen」、日付はアップロード日のみ／堀 Lynn0927 CC BY-SA 4.0・2015-12-13／夕景 Zairon CC BY 4.0・2023-10-20／天守からの眺め・鎧3領・刀・駕籠 Zairon CC BY 4.0／廊下門 Zairon（Commons題名「Corridor Gate」、原構か再建か不明）／石垣の門 Daderot CC0・2011-12-08）。鎧は花房正成と読めるが札が読みにくく「要確認」、他の鎧・駕籠・刀の持ち主は断定せず。写真とスクショは縦横比・内容で対応。PHOTO-CREDITS.csv追記済み。【未対応】石垣と堀の近景・後楽園・月見橋・夜のライトアップの写真、インデックス登録（guides/okayama-castle/、/castles/、/guides/）。次の城候補：広島城
- 2026-11-03 okayama-castle：写真5枚＋解説を追加（現存櫓 663highland CC BY-SA 3.0・Commons履歴の日付2008-02-14＝アップロード日、どちらの櫓かは説明が切れており断定せず／灯幻郷ライトアップ 恭パパ CC BY-SA 4.0・2015-08-14／後楽園（沢の池畔・春）Fjkelfeimvvn CC BY 3.0・2010-05-09（GFDL併記、CC BY 3.0を採用）／後楽園（秋）Zairon CC BY 4.0・2023-10-20／月見橋 George N CC BY 2.0・2016-08-18（Flickr G.A.I.N）。写真とスクショは縦横比で対応。計19枚（ヒーロー含む）。PHOTO-CREDITS.csv追記済み。【未対応】石垣と堀の近景の写真、インデックス登録
- 2026-11-03 okayama-castle：天守から北を望む写真1枚＋解説を追加（Mikel Lizarralde CC BY-SA 2.0・2008-08-04、金鯱越しに堀と後楽園、鯱左のビルは岡山プラザホテル＝Commons説明）。眺めの写真の直後。計20枚。PHOTO-CREDITS.csv追記済み。【未対応】石垣と堀の近景の写真、インデックス登録
- 2026-11-03 新規：guides/hiroshima-castle/（Wikipedia／GLTJP item 20344／国交省 多言語表記DB（001560954.pdf）／Japan Experienceで裏取り。タイトル「Hiroshima Castle Guide: The Carp Castle, the 1945 Blast and a 1958 Keep」。毛利輝元の築城、開始年は1588（GLTJP）／1589（MLIT・Wikipedia）／1590（Japan Experience）で併記・完成1599、福島正則1600-1619→浅野長晟（12代・MLIT）、1894-95日清戦争で大本営（Wikipedia）、1931国宝（Wikipedia・MLIT）、1945-08-06の原爆で倒壊（MLITは「下部の柱が壊れ残りが崩れた可能性」、Wikipediaは2010年の証拠で同説＝「現時点の最有力説」と記載）、1958再建（天守はコンクリート＝Wikipedia/MLIT、最上階木造＋下層RC＝GLTJPで併記）、5層26.6m＋石垣12.4m（Wikipedia）・約40m（GLTJP）。館内の階別展示（GLTJP）。二の丸は無料、1989-1994復元・表門1991（GLTJP）／門と櫓3棟1994（Wikipedia）で併記、多聞櫓68m。三重の堀のうち内堀のみ現存、広島護国神社は内堀内（Wikipedia）。被爆樹木はユーカリ約740m・柳・柊で距離とも資料間で差（Wikipedia／GLTJP／MLIT：3本か4本）、戦後初のラジオ放送に使われたコンクリート壕（Wikipedia・Japan Experience）。88の櫓・石垣31,781個・刻印214はGLTJP単独＝要確認と明記。料金370円（GLTJP）／360円（Japan Experience）、天守3-11月9-18時（最終17:30）・12-2月9-17時（最終16:30）・12/29-31休、二の丸4-9月9-17:30・10-3月9-16:30・12/29-1/2休（GLTJP）。電車1・2・6系統→紙屋町東/西から徒歩約15分、駅から徒歩約25分（GLTJP）。原爆は平和記念公園が主役で城は「older layer」として扱う方針。写真なし。ハブ・JSON-LD(position 87)・sitemap・OGP・城ハブ上部カード反映済み、タグ均衡・JSON-LD・390px幅OK）。【未対応】ヒーロー＋本文写真追加（天守・堀と石垣・二の丸の櫓と門・被爆樹木・護国神社・桜）、インデックス登録（guides/hiroshima-castle/、/castles/、/guides/）。次の城候補：萩城跡、津山城、福山城、鳥取城（要相談）
- 2026-11-03 hiroshima-castle：写真9枚＋解説を追加（ヒーロー：堀と石垣 Marion & Christoph Aistleitner CC0・2014-02-04／紅葉の正面 Yoshio Kohara CC BY 3.0・2014-11-28（Panoramio由来）／入口の屋根付き通路・縦長 DXR CC BY-SA 4.0（アップロード2019-05-05／撮影2019-04-17）／市街の眺め Jakubhal CC BY 4.0（アップロード2025-10-20、Author欄が写っておらずアップロード者名で表記、撮影地点は未確認のため断定せず）／青空の堀 ノボホショコロトソ CC BY 4.0・2025-08-30／曇りの堀 melveny CC BY-SA 4.0・2013-08-24／夜の堀 Hiroaki Kaneko CC BY-SA 3.0・2015-11-25（透かしあり）／夜の枝越し ADS-Slayer CC BY-SA 3.0・コメント上2009-01-20）。写真とスクショは縦横比・寸法で対応。PHOTO-CREDITS.csv追記済み。【未対応】堀と石垣の近景・二の丸の櫓と門・被爆樹木・護国神社・桜の写真、インデックス登録（guides/hiroshima-castle/、/castles/、/guides/）
- 2026-11-03 hiroshima-castle：写真7枚＋解説を追加（正門と橋 Jakub Hałun CC BY 4.0・2024-08-17（Quality image）＝#grounds／新h3「Hiroshima Gokoku Shrine」に6枚：鳥居と拝殿 そらみみ CC BY-SA 4.0・2017-03-11／鳥居（おみくじ屋台・トラック）・手水舎・拝殿前の参拝者と作業員・昇鯉の像 Hyppolyte de Saint-Rambert CC BY 4.0・2024-01-11／夏の拝殿 Madhav Sharma CC BY-SA 4.0・2016-06-23）。Hyppolyteの4枚はスクショのサムネイルと寸法で対応。鳥居の柱の刻字（平成二年…御大典記念）は読み取りに自信がないため「appears to」表記、両鳥居が同一かは断定せず。送られてきた金鯱の写真（Mikel Lizarralde）は岡山城の既掲載写真のため不使用。PHOTO-CREDITS.csv追記済み。広島城は計16枚。【未対応】二の丸の櫓・被爆樹木・桜の写真、インデックス登録
- 2026-11-03 hiroshima-castle：桜の写真1枚＋解説を追加（Mark Bucayan CC BY 3.0・2 April 2013、500px由来、堀と対岸の桜並木、画像右下に透かしあり）。#stayの桜の段落の直後。広島城は計17枚。PHOTO-CREDITS.csv追記済み。【未対応】二の丸の櫓・被爆樹木の写真、インデックス登録
- 2026-11-03 新規：guides/hagi-castle/（GLTJP item 16147／Japan-guide e6152／Wikipedia／萩市公式英語ページ2本（190010・100049）／国交省 多言語表記DB H30-01054／Fun Japan 10581で裏取り。タイトル「Hagi Castle Ruins Guide: The Castle Its Own Lords Tore Down, Now a Park and World Heritage Site」。毛利は関ヶ原後に広島から萩へ（Wikipedia：戦わず約3分の2を没収／市・MLIT：1603移転・1604築城）、竣工1608・五層天守はWikipedia単独、1863山口移転（砲撃の恐れ）もWikipedia単独＝要確認と明記、1874天守解体（命令の主体は資料で差：Wikipedia・Fun Japan＝政府、市の1ページ＝政府、市の別ページ・MLIT＝旧藩主が撤去に協力→併記）、跡地は売却され公園に。現存：石垣・堀・天守台・志都岐山神社（1878）・花江茶亭（1889移築／三の丸から＝資料差）・VR展示。二の丸の櫓12棟・門は石垣のみ（Fun Japan）、Wikipediaは外門と隅櫓が後に復元＝食い違うため「現地確認」。指月山は徒歩約20分（Japan-guide）、詰丸跡の現状は不明と記載。2015年世界遺産（萩城下町の一部）、国史跡は1951（市・MLIT）、Wikipediaは年が不整合。桜は約600本（GLTJP・Fun Japan）／500本超（市）、ミドリヨシノは県天然記念物。料金220円（GLTJP・Japan-guide・市）／210円（Fun Japan）、4-10月8:00-18:30・3月8:30-18:00・11-2月8:30-16:30・無休（Japan-guide・市）、阿川毛利家長屋門との共通券（GLTJP）。まるバス東回り／西回りは資料で食い違うため「要確認」。所要約2時間は私の見積りと明記。FAQ5問。ハブ・JSON-LD(position 88)・sitemap・OGP・城ハブ上部カード反映済み、タグ均衡・JSON-LD・390px幅OK）。写真なし。【未対応】ヒーロー＋本文写真追加（石垣と堀・天守台・志都岐山神社・花江茶亭・桜・ライトアップ・指月山・旧益田家ではなくAsa Mori residence）、インデックス登録（guides/hagi-castle/、/castles/、/guides/）。次の城候補：津山城、福山城、鳥取城
- 2026-11-04 hagi-castle：極楽橋と本丸門跡の写真1枚＋解説を追加（そらみみ CC BY-SA 4.0・2017-05-04、Commons説明「萩城の極楽橋と本丸門跡」、#see末）。左の標柱「史跡 萩城趾」、右は志都岐山神社と読めるが「appears to」表記、2017年の写真で現状と異なる可能性を明記。Commonsリンクは作者のライセンスURLで代用（ファイル名がスクショで途切れていたため）。ヒーロー未設置。PHOTO-CREDITS.csv追記済み。【未対応】残り5枚（内堀と極楽橋・指月山・天守台・石橋・社殿）の写真本体待ち、インデックス登録
- 2026-11-04 新規：guides/tsuyama-castle/（GLTJP 12541／Nippon.com（桜百選）／Jeepe／Wikipedia（ミラー）で裏取り。タイトル「Tsuyama Castle Guide: Stone Walls, a Rebuilt Turret and 1,000 Cherry Trees」。森忠政（蘭丸の弟＝GLTJP）、着工1603・完成1616・77櫓・五重天守（Wikipedia）／GLTJPは1604完成・13年で食い違い→Wikipedia採用と明記、80超の建物（GLTJP）。四層目の屋根を外して五重扱いを避けた話はWikipedia単独＝要確認と明記。1873財務省管理→1874-75天守・櫓取り壊し（Wikipedia）。石垣の高さはGLTJP約10m／Nippon.com 45mで食い違い→断定せず。備中櫓は2004-05復元（Wikipedia）／2004（Nippon.com）、畳の間あり。桜約1,000本（全資料一致）、見頃4月上旬、まつり約2週間・7:30-22:00。料金310円（GLTJP・Jeepeハイライト）／300円（Nippon.com・Jeepe FAQ）、中学生以下無料、開園8:40-19:00／-17:00（季節の区切りは4月〜9月（GLTJP）／5月〜9月（Jeepe））、12/29-31休、津山駅から徒歩約10分、岡山から約1時間10分、駐車約600円。国史跡1963はWikipedia単独のため不掲載。FAQ5問。ハブ・JSON-LD(position 89)・sitemap・OGP・城ハブ上部カード反映済み）。写真なし。【未対応】ヒーロー＋本文写真（石垣・備中櫓・桜・夜桜ライトアップ・天守台・鶴山館・城下町）、インデックス登録（guides/tsuyama-castle/、/castles/、/guides/）。
- 2026-11-04 修正：guides/hagi-castle/ と hiroshima-castle/ の下部固定CTA（Expedia・Viator）の行き先が高知（Kochi）のままだったのを萩／広島に修正。今後、kochi-castleを雛形にする際は固定CTAの destination%3D と viator.com/search/ の置換を忘れないこと（tsuyama.pyは対応済み）。
- 2026-11-04 方針：城は「検索需要の高い人気城」に絞って約10城で区切る（津山城は人気が低めだが公開済みのため残す・写真依頼は今後しない）。残り優先順：金沢城→首里城→竹田城跡→小田原城→会津若松城→五稜郭→仙台城→和歌山城→高遠城址→島原城
- 2026-11-04 新規：guides/kanazawa-castle/（GLTJP 12566／Visit Kanazawa／Kanazawa Station（kanazawastation.com）／Japan Experienceで裏取り。タイトル「Kanazawa Castle Guide: Lead-Tile Turrets, a 1788 Gate and the Park Next to Kenrokuen」。1546尾山御坊→1580佐久間盛政→1583前田利家入城、1602天守焼失・再建なし、1759大火、1881焼失（Kanazawa Station）、1631・1808はGLTJPの口コミのみ＝未確認と明記、1602の雷はGLTJP口コミ単独＝原因は未確認。石川門1788（原構）、三十間長屋の年代は1858（Visit Kanazawa）と原構（Japan Experience）で食い違い→年は断定せず。1999-2001に菱櫓・五十間長屋・橋爪門続櫓を復元、河北門2010、鼠多門2020はGLTJP単独＝要確認、玉泉院丸庭園は1634着手・2015復元、ライトアップは日没〜21時（GLTJP）／土曜・指定日（Visit Kanazawa）で食い違い。公園無料・毎日開園（3/1-10/15 7-18時、10/16-2月 8-17時）、櫓群は320/100円（Visit Kanazawa・Kanazawa Station）／300円（Japan Experience）、9-16:30（最終16:00）、バス約18分・220円／200円、徒歩20-25分、駐車場なし。国史跡2008（Visit Kanazawa）。兼六園は道路向かい。FAQ5問。ハブ・JSON-LD(position 90)・sitemap・OGP・城ハブ上部カード反映済み）。写真なし。【未対応】ヒーロー＋本文写真（石川門・菱櫓と五十間長屋・河北門・橋爪門続櫓・玉泉院丸庭園・石垣・桜・夜のライトアップ）、インデックス登録（guides/kanazawa-castle/、/castles/、/guides/）
- 2026-11-04 hagi-castle：写真6枚＋解説を追加（ヒーロー：指月山と堀・石垣・史跡萩城趾の標柱 Kuru man（トトト補正）CC BY 2.0・2010-09-22／天守台 Reggaeman CC BY-SA 3.0・2006-10-19（610×404のまま拡大せず、max-width610px）＝#see第1段落の後／志都岐山神社の参道の鳥居 そらみみ CC BY-SA 4.0・2017-05-04（銘板・明治二十三年六月の刻字・「縣社」標柱は「reads as」表記）／紅白幕と家紋幕の社殿 そらみみ・アップロード2017-07-29（Commonsの説明が確認できず建物は断定せず、毛利家の紋は「looks like…believe」）／苔むす石橋とアヤメ池 そらみみ・アップロード2017-07-28（説明・日付なしのため場所を断定せず）＝#see第2段落の後／内堀と極楽橋 そらみみ・2017-05-04＝極楽橋写真の後）。【保留】石段と社殿の写真（そらみみ想定・スクショなし。参道の鳥居と同じ6枚目のスクショ「志都岐山神社の参道」にどちらが対応か不明のため、鳥居を採用し石段を保留）。写真とスクショは縦横比・寸法・内容で対応。PHOTO-CREDITS.csv追記済み。萩城は計7枚。【未対応】石段の写真（スクショ待ち）、桜・花江茶亭・ライトアップ・天守台近景の写真、インデックス登録（guides/hagi-castle/、/castles/、/guides/）
- 2026-11-04 kanazawa-castle：写真8枚＋解説を追加（ヒーロー：堀と桜の櫓 Zairon CC BY-SA 4.0・2019-04-09、Commons題名「Higashi Yagura of Kanazawa Castle & Cherry Blossom」／#gate末：石川橋の通り Kagaland（Wikivoyage由来）CC BY-SA 1.0・2001-10-04（1280×960）、第一門（Vortor）・石川門 Zairon 2019-04-09／#rebuilt：長い白い建物の遠景・近景（Commonsは「Higashi Yagura」）Zairon、菱櫓の出窓 Andrea Schaffer CC BY 2.0・2009-07-27、内部 Zairon）。写真とスクショは縦横比・寸法・撮影時刻で対応（Andrea Schafferのスクショは重複して2枚）。Commons名「Higashi Yagura」は本文の櫓名リストと未照合のため「ラベルに従う・例示」と明記、梅鉢紋・コスモスは『見える』表記。PHOTO-CREDITS.csv追記済み。【未対応】河北門・橋爪門続櫓・玉泉院丸庭園・石垣・夜景の写真、インデックス登録（guides/kanazawa-castle/、/castles/、/guides/）
- 2026-11-04 kanazawa-castle：写真8枚＋解説を追加（河北門の一の門・二の門 そらみみ CC BY-SA 4.0・2015-01-20（二の門の看板『9:00〜16:30・無料』は2015年表記＝要確認と明記）／橋爪門 Benh LIEU SONG CC BY-SA 2.0・2018-10-19／桜3枚 Zairon CC BY-SA 4.0・2019-04-09（石川門付近に見えるがCommonsは城名のみ＝断定せず）／玉泉院丸庭園 あばさー（作者がPD公開）・2016-09-09／石垣2段 Asanagi CC0・2006-09-29）。写真本体16枚中8枚は前回掲載済みの重複で未使用。対応は縦横比（石垣は縦長、橋爪門16:9、河北門2枚は署名看板の有無で二の門／一の門を判別）。PHOTO-CREDITS.csv追記済み。金沢城は計16枚。【未対応】夜のライトアップの写真、インデックス登録（guides/kanazawa-castle/、/castles/、/guides/）
- 2026-11-04 kanazawa-castle：夜の門と橋の写真1枚＋解説を追加（くろふね CC BY 4.0・2022-11-05 18:55、Commons題名『夜の金沢城』のみ。鼠多門に見えるが私の読み＝断定せず）。橋爪門の写真の直後。計17枚。PHOTO-CREDITS.csv追記済み。【写真本体待ち（スクショ受領済み）】くろふね 2022-11-05 20:00:58／19:19:46／19:14:50（CC BY 4.0・1600×1067）、先従隗始 鼠多門と鼠多門橋 2020-08-19（CC0・4608×3456）、Okochuke 玉泉院丸庭園 2015-08-15 23:07:10／23:10:58（CC BY-SA 3.0・2048×1536）。【未対応】インデックス登録
- 2026-11-04 新規：guides/shuri-castle/（oki-park.jp 首里城公園チケットページ／Travel Watch 2133105／Wikipedia／K005 Powerspot／Japan Ode／Sumimasen Guideで裏取り。タイトル「Shuri Castle Guide: Ryukyu's Red Palace, the Rebuilt Main Hall and Timed Tickets」。正殿は2026-11-23一般公開予定（11/22竣工式・全園休園）、時間指定予約制（30分枠・Webket・1回9枚まで・追加料金なし）、有料区域1,000円（旧400円）・高校760・小中370・未就学無料。2019-10-31火災（原因は資料で未解決のため不記載）、正殿工事2022-11着工・外装2025-07完成。台湾産木材・与那国砂岩の龍柱・北殿南殿の鉄骨はWikipedia単独＝要確認と明記。営業時間はJapan Ode単独＝公式確認。ゆいレール首里駅から徒歩約15分（K005/Japan Ode）／守礼門…約20分（公式ページ、守里館まで）で併記。FAQ6問。ハブ・JSON-LD(position 91)・sitemap・OGP・城ハブ上部カード反映済み、タグ均衡・JSON-LD・390px幅OK）。写真なし。【未対応】ヒーロー＋本文写真（守礼門、正殿外観、歓会門・瑞泉門・広福門、園比屋武御嶽石門、石垣、京の内、桜）、インデックス登録（guides/shuri-castle/、/castles/、/guides/）。次の城：竹田城跡→小田原城→会津若松城→五稜郭→仙台城→和歌山城→高遠城址→島原城
- 2026-11-04 shuri-castle：写真10枚＋解説を追加（ヒーロー：守礼門 Suicasmo CC BY-SA 4.0・2015-02-11／守礼門の扁額 Hiroki Ogawa CC BY 3.0・Panoramio 2016-04／守礼門の夕景 Kennagata CC BY-SA 4.0・2019-04-27（火災前）／歓会門（Commons題名「Gates of Shuri Castle」、看板から歓会門と判断）Suicasmo／瑞泉門・久慶門 Zairon CC BY 4.0・2023-10-26／木曳門 663highland CC BY-SA 3.0・2011-07（GFDL・CC BY 2.5併記、BY-SA 3.0採用）／御庭と奉神門 そらみみ CC BY-SA 4.0・2015-03（火災前）／正殿の玉座 CEphoto, Uwe Aranas CC BY-SA 3.0・2016-01（火災前と明記）／奉神門 CEphoto・2016-01）。ミニチュア（東武ワールドスクウェア）は実物でないため不使用。写真とスクショは寸法・縦横比・内容で対応。瑞泉門の再建時期・久慶門の見学情報は未確認と明記。PHOTO-CREDITS.csv追記済み。【未対応】正殿の新外観（2025-26）・園比屋武御嶽石門・京の内・桜の写真、インデックス登録
- 2026-11-04 shuri-castle：写真5枚＋解説を追加（園比屋武御嶽石門 663highland CC BY-SA 3.0・Commons履歴2011-06（GFDL・CC BY 2.5併記、BY-SA 3.0採用）／石門と世界遺産の銘板 xiquinhosilva（Xiquinho Silva）CC BY 2.0・2018-08-05（透かしあり）／瑞泉門前の城壁とソテツ・広福門前の城壁と右掖門・城壁と那覇市街 そらみみ CC BY-SA 4.0・2015-03-15）。右掖門の読みは断定せずCommonsの日本語キャプションを引用。写真とスクショは縦横比・内容で対応。首里城は計15枚（ヒーロー含む）。PHOTO-CREDITS.csv追記済み。【未対応】正殿の新外観（2025-26）・京の内・桜の写真、インデックス登録
- 2026-11-04 shuri-castle：正殿（火災前）の写真1枚＋解説を追加（CEphoto, Uwe Aranas CC BY-SA 3.0・2016-01-05、Commons説明「Palace building of Shuri Castle」、正殿と私の読み＝「I take it to be」表記）。#fire第1段落の直後（玉座の前）。計16枚。PHOTO-CREDITS.csv追記済み。【未対応】正殿の新外観（2025-26）・京の内・桜の写真、インデックス登録
- 2026-11-04 新規：guides/takeda-castle-ruins/（japan-guide e3592／GLTJP 19012／thegate12 spot/572で裏取り。Wikipediaはallowlist外で未取得。タイトル「Takeda Castle Ruins Guide: Japan's Machu Picchu, the Cloud Sea and the Winter Closure」。築城は1411（japan-guide）／1443〜13年（thegate12）で食い違い→「15世紀」とだけ記載。1590赤松広秀の石垣完成はthegate12単独＝明記。1600関ヶ原後に廃城、1970-80年代に整備（japan-guide）。標高353.7m（GLTJP）。雲海はjapan-guide=10-11月・日の出6:00-6:30・約3日に1回、thegate12=9-11月、GLTJP=秋〜初冬で併記。立雲峡は環境協力金300円・公共交通なし（japan-guide）。料金500円・中学生以下無料・現金のみ。開園時間は3資料で差があり併記＝公式確認。休園1/4〜2月末（3資料一致、thegate12は'lat February'と誤記）。駅から徒歩40分（30分説あり）、天空バス300円・約20分＋徒歩20分、タクシー約2,000円（japan-guide）。FAQ6問。ハブ・JSON-LD(position 92)・sitemap・OGP・城ハブ上部カード反映済み）。写真なし。【未対応】ヒーロー＋本文写真（石垣と雲海、立雲峡からの眺め、天守台、紅葉、雪）、インデックス登録（guides/takeda-castle-ruins/、/castles/、/guides/）。次の城：小田原城→会津若松城→五稜郭→仙台城→和歌山城→高遠城址→島原城
- 2026-11-04 takeda-castle-ruins：写真14枚＋解説を追加（ヒーロー：日の出の雲海 bullets95 CC BY-SA 2.0・2010-12-05／#history末：史跡竹田城跡の標柱 Baku13 CC BY-SA 3.0・2013-05-07／#walls：南二の丸（天守台から）ブレイズマン PD・2009-04-15、同 Baku13・2013-05-07、石垣の間の道 Brakeet CC0・2011-05-05 15:47、天守台（南千畳から・三の丸から）ブレイズマン PD、対岸からの遠景 Brakeet CC0・16:10／#clouds：霧と紅葉 Norio NAKAYAMA CC BY-SA 2.0・2011-11-16（Commons題名が立雲峡）、雪と雲海 Hiroaki Kaneko CC BY-SA 3.0・2011-12-24／新節#spring（春の桜）：Totti CC BY-SA 4.0・2019-04-13 ×3、Drivephotographer CC0・2022-04-17（開花前）。写真とスクショは縦横比・寸法・内容で対応（Totti 3枚のスクショは時刻とのひも付けが不確かだが作者・ライセンス・日付は同一）。ブレイズマンの説明文（日本語）は翻訳して引用。Nakayamaのバナー画像（立雲峡の切り抜き）は同一ショットの切り抜きのため不使用。ヒーローの日の出写真は撮影地点がCommonsに無く断定せず。桜の本数・見頃は資料なしのため記載せず。PHOTO-CREDITS.csv追記済み。【未対応】インデックス登録（guides/takeda-castle-ruins/、/castles/、/guides/）
- 2026-11-04 新規：guides/odawara-castle/（japan-guide e5222／Jeepe／小田原市英語ページ（2016更新・古い）で裏取り。タイトル「Odawara Castle Guide: The Hojo Stronghold, a 1960 Keep and the Ninja Museum」。大森氏の砦→1500頃北条早雲（Jeepe）、後北条5代約100年、1590秀吉に敗北、1703地震で倒壊・再建、1870天守取り壊し・売却、1960コンクリート再建（japan-guide）。江戸期の大久保・稲葉氏はJeepe単独＝明記。料金：天守510円・忍者館310円・武家博物館200円（japan-guide）、セット610円は資料間で内容差（japan-guide=天守+両館、Jeepe=天守+武家博物館）、市の旧ページは500円。9-17時（最終16:30）、天守は12月第2水・12/31-1/1休。東口から徒歩約10分。桜は3月下旬〜4月上旬、約300本（Jeepe単独）。甲冑体験500円はJeepe単独。FAQ7問。ハブ・JSON-LD(position 93)・sitemap・OGP・城ハブ上部カード反映済み）。写真なし。【未対応】ヒーロー＋本文写真（天守・堀と城門・桜・忍者館・武家博物館）、インデックス登録（guides/odawara-castle/、/castles/、/guides/）。次の城：会津若松城→五稜郭→仙台城→和歌山城→高遠城址→島原城
- 2026-11-04 odawara-castle：写真12枚＋解説を追加（ヒーロー：晴天の天守 663highland CC BY-SA 3.0・2016-12-23（GFDL併記、BY-SA採用）／#keep：夕景 Agustin Rafael Reyes CC BY 2.0・2010-08-07（色が強調されている旨を明記）、南東からの天守 Ymblanter CC BY-SA 4.0・2018-04-14（東側ファイルとの対応は不確か）、常盤木門 KENPEI CC BY-SA 4.0・2015-06-07（japan-guideの「Tokiwaki」＝武家博物館の建物）／#grounds：銅門 KENPEI・2015-06-07、銅門（1997年復元＝Commons説明）Kicho-66 CC BY-SA 3.0・2008-02-01（1280px、GFDL併記）、銅門と堀・標識（2018年表記7:00-21:00・ライトアップ日没〜22時＝要確認）Ymblanter、馬出門 Ymblanter・2018-04-14、入口の門 Alvinz CC0・2018-07-13（門名は断定せず）、住吉橋 妖精書士 CC0・2020-03-17（コーンの理由は不明と記載）／桜：Σ64 CC BY 3.0・2018-04-01（GFDL併記）、桜と海の眺め 江戸村のとくぞう CC BY-SA 4.0・2009-04-04（天守からとは断定せず））。写真とスクショは縦横比・寸法・内容で対応。PHOTO-CREDITS.csv追記済み。【写真本体待ち（スクショ受領済み）】Akonnchiroll 天守2024-02-14（CC BY 4.0・3099×2214）、Suicasmo 城門2021-12-01（CC BY-SA 4.0・5184×3456）、Ymblanter 東から見た天守2018-04-14 04:29（CC BY-SA 4.0・3648×2736）。【未対応】インデックス登録（guides/odawara-castle/、/castles/、/guides/）
- 2026-11-04 odawara-castle：写真3枚＋解説を追加（東から見た天守 Ymblanter CC BY-SA 4.0・2018-04-14／冬の天守と松 Akonnchiroll CC BY 4.0・2024-02-14／堀端の門（Commons題名「Odawara Castle Gate」、門名は断定せず）Suicasmo CC BY-SA 4.0・2021-12-01）。小田原城は計15枚。kanazawa-castle：夜の写真3枚を追加（ピンクの石垣と櫓／門と橋を横から／月と櫓 いずれもくろふね CC BY 4.0・2022-11-05。建物名は私の読みと明記、スクショ時刻との対応は不確か）。正面の門と橋の写真は既掲載と同一ショットのため不使用。金沢城は計20枚。PHOTO-CREDITS.csv追記済み。【写真本体待ち（金沢）】先従隗始 鼠多門 2020-08-19 CC0・Okochuke 玉泉院丸庭園 2015-08-15 ×2 CC BY-SA 3.0。【未対応】インデックス登録（小田原・金沢ほか）
- 2026-11-04 kanazawa-castle：玉泉院丸庭園の夜景2枚を追加（Okochuke CC BY-SA 3.0・2015-08-15、紫と琥珀のライトアップ。スクショ時刻との対応は不確か）。金沢城は計22枚。【保留】昼の庭園（2576×1932・作者/ライセンス不明）→スクショ待ち。【写真本体待ち】鼠多門 先従隗始 CC0 2020-08-19
- 2026-11-04 kanazawa-castle：鼠多門と橋の夜（先従隗始 CC0・2020-08-19、寸法とスクショの対応は4:3で推定）と玉泉院丸庭園の池（Benh LIEU SONG CC BY-SA 2.0・2018-10-19 10:28）を追加。昼の庭園（作者/ライセンス不明）は未使用のままで確定。金沢城は計24枚。同作者の10:26パノラマ（9187×3047）は写真本体なしで未使用。写真待ち：なし
