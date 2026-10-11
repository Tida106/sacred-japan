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
- Amazon（sacredjapan-22）：JP版（.co.jp）タグ。ホームのAmazonセクション9商品が全部amazon.co.jpで、米欧ターゲットとミスマッチ。要修正: Amazon Associates US（associates.amazon.com）にsacred-japan.netを新規登録→新タグ取得→amazon.co.jp→amazon.comに差し替え。Rakutenリンク（lucky-sun-shineのID使用）は削除済み（2026-10-11）
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
3. Amazon US：Amazon Associates（associates.amazon.com）にsacred-japan.netを新規登録→新タグ取得→ホームの9商品をamazon.co.jp→amazon.comに差し替え（てぃーだ側の作業、審査は数日程度）
4. GA4データ（event_label/event_category カスタムディメンション、2026-10-10登録）が反映され次第、ページ別アフィリエイトクリックを分析
5. GA4データ蓄積後（1〜2ヶ月）にサイト構成見直し

## 完了事項
- Pinterest：/anime/ のkusunoki-tei, noragami, ryomen-sukunaはピン作成済み。fruits-basket/inuyasha/your-nameはlucky-sun-shine.comと重複するため対象外（完了・対応不要）

## 構造改革メモ（2026-10-11実施）
- ホーム＋ハブ8ページ（guides/culture/castles/crafts/anime/regional-food/festivals/about）のモバイルメニューを地域グループ構成に統一、新規ページ全部リンク済み
- 孤立ページ5つ発見・解消：hebikubo-shrine, seimei-shrine, hokakuji, samukawa-shrine, best-castles-japan（hokakujiはsitemapにも無かった）
- best-castles-japanのネスト`<a>`タグバグ（13箇所）修正
- Viatorダミー箱：kotohira-guは削除、hiraizumi/dewa-sanzan/takachihoは広域検索語に差し替え（Tohoku/Yamagata/Miyazaki）
- 個別記事65本のモバイルナビはまだ短縮版バラバラ（優先度低、保留）
