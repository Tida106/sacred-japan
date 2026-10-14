# Sacred Japan - CLAUDE.md

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

## アフィリエイト構成
- Viator：PID P00298374（「Book a Tour →」赤ボタン）
- Expedia：camref=1101l5JmFa（「Find Hotels →」紺ボタン）
- AdSense：ca-pub-4224563062633828（審査中）
- Agoda：CID 1963662（審査中・現在カードから削除済み）
- Amazon US（sacredjapan-20）：2026-10-11、Associates USにsacred-japan.netを追加（trance-nexusと同一アカウント内）、新タグ取得。ホームのAmazonセクション9商品を amazon.co.jp→amazon.com、検索語も英訳して差し替え済み。JP版タグ（sacredjapan-22）は不使用に。Rakutenリンク（lucky-sun-shineのID使用）は削除済み。申請後180日以内に適格売上3件が必要（Associates規約）
- KKday：Involve Asia経由で申請予定（2026-10-11〜）。旅行ロジ系（eSIM/JRパス/WiFi）狙い。承認後、guides/japan-travel-planning/ に「Staying Connected」セクションを新設してリンクを埋め込む（money と rail セクションの間）

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
- 完了21記事（コミット順）：fushimi-inari-taisha（社殿／狐像）、kiyomizu-dera（本堂舞台／音羽の滝）、meiji-jingu（大鳥居／森の小川）、izumo-taisha（本殿屋根／しめ縄）、kasuga-taisha（拝殿／吊り灯籠）、best-shrines-kyoto（平安神宮大鳥居／八坂神社楼門）、todaiji（大仏殿／大仏）、nikko-toshogu（陽明門／三猿彫刻）、tsurugaoka-hachimangu（本殿／大鳥居）、ryoanji（石庭／方丈畳間）、byodoin（鳳凰堂全景／鳳凰像）、zenko-ji（本堂／仁王門）、atsuta-shrine（森の鳥居／摂社）、hakone-shrine（湖の大鳥居／神事）、enryakuji（根本中堂／横川）、kumano-kodo（参道階段／大鳥居／大社本殿の3枚構成）、mount-koya（奥の院／根本大塔）、naritasan-shinshoji（大本堂／三重塔）、kawasaki-daishi（大本堂／仲見世通り）、omiya-hikawa-jinja（楼門／参道鳥居／舞殿の3枚構成）、suwa-taisha（下社秋宮神楽殿／下社春宮鳥居）
- 残り：guides/culture配下の画像ゼロ記事が約28本残存。次に優先度の高い記事から同じ手法で継続予定
- ユーザー指示（2026-10-14）：進行確認（「続ける？」）は不要、次の記事を直接出す運用に変更
- 副産物：guides/meiji-jinguが約833語と他記事（2000語超）の半分以下で、FAQセクションも無いことが判明。後日の拡充対象として記録（画像追加作業とは別タスク）

## SEOメモ（2026-10-11実施）
- hokakujiのみ`<meta name="robots" content="noindex, follow">`になっておりGoogle非インデックス状態だった（全46ガイド中唯一）。`"index, follow"`に修正（コミットf7562c0）。sitemap.xmlには元々掲載済みだったので別途修正不要
- FAQPage構造化データ（JSON-LD）：guides/culture/shrines配下でFAQセクションを持つ45ページ中44ページは既に実装済み（過去セッションで対応済みと判明）。未実装だったhokakujiのみ追加（4問、コミットae26eec）
- OGP画像：50ページ（guides/culture/anime/shrines配下）が汎用ogp.pngのみに依存していた。サイトのデザイントークン（washi/beni/sumi等）を使ったブランド付きタイトルカード画像を自動生成するPythonスクリプト（PIL/Pillow）を作成し、該当50ページ全部に個別画像を設置（images/og/og-<section>-<slug>.jpg、コミットdf8f766）。既に実写真を使っていた15ページ（best-castles-japan, dazaifu-tenmangu, ise-grand-shrine, itsukushima-shrine, kinkakuji, kotohira-gu, meiji-jingu, nikko-toshogu, sensoji, sumiyoshi-taisha, kamidana, demon-slayer, noragami, ryomen-sukuna, your-name）は対象外（変更なし）
- OG画像生成スクリプトはh1のタイトル抽出で`<em>`タグ直後の句読点（: , . ; ! ?）前に余計なスペースが入るバグがあったが修正済み（正規表現で除去）
