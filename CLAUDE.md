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
- サイトはCloudflare経由で配信。画像追加・更新をpushした後はCloudflareダッシュボードでキャッシュパージが必要（このセッションにはAPIトークン無し、ユーザー側で実施）

## アフィリエイト構成
- Viator：PID P00298374（「Book a Tour →」赤ボタン）
- Expedia：camref=1101l5JmFa（「Find Hotels →」紺ボタン）
- AdSense：ca-pub-4224563062633828（審査中）
- Agoda：CID 1963662（審査中・現在カードから削除済み）
- Amazon US（sacredjapan-20）：2026-10-11、Associates USにsacred-japan.netを追加（trance-nexusと同一アカウント内）、新タグ取得。ホームのAmazonセクション9商品を amazon.co.jp→amazon.com、検索語も英訳して差し替え済み。JP版タグ（sacredjapan-22）は不使用に。Rakutenリンク（lucky-sun-shineのID使用）は削除済み。申請後180日以内に適格売上3件が必要（Associates規約）
- KKday：Involve Asia経由で申請予定（2026-10-11〜）。旅行ロジ系（eSIM/JRパス/WiFi）狙い。承認後、guides/japan-travel-planning/ に「Staying Connected」セクションを新設してリンクを埋め込む（money と rail セクションの間）
- VoiceMap（Awin, Merchant ID 99601／Awin Affiliate ID 2869709）：2026-10-16承認済み。音声ガイドアプリ（GPS連動の自己ガイドツアー）、手数料4〜10%。ディープリンクはAwinダッシュボード「Toolbox→Link Builder」から発行（このセッションにはAwin APIアクセス無し）。埋め込み済み4記事：guides/meiji-jingu/「Getting There」セクション、guides/best-shrines-kyoto/ Yasaka Shrineセクション（Gion districtツアー）、guides/sensoji/（Secrets of Sensoji Temple、FAQ直前に設置）、guides/kiyomizu-dera/（Kiyomizu-dera mysteries/legends/ritualsツアー、practical-list直後に設置）。meiji-jingu/best-shrines-kyotoはkey-calloutクラス使用、sensoji/kiyomizu-deraはkey-callout未実装のためインラインstyleで同等の見た目を再現。いずれもCTAボタン「Start the Audio Tour →」形式
- VoiceMap：fushimi-inari-taisha用ツアー（Fushimi Inari Shrine: An In-Depth Guide, voicemap.me/tour/kyoto/fushimi-inari-shrine-an-in-depth-guide/map）は確認済みだが2026-10-16時点でディープリンク未発行・未埋め込み（次回ユーザーからリンクもらい次第対応）。他候補：Kamo River／architecture／tea cultureツアー（kyoto配下）、Shinjuku神社ツアー・Ebisuフードツアー（tokyo配下）は対応記事なし or 弱いため保留

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
