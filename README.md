# smart-novel-insert-novel2elasticsearch-lambda
elasticsearchへの小説データ挿入

## 設定
| 項目 | 値 |
| ---- | ---- |
| ランタイム | Python 3.8 |
| メモリ | 256 MB |
| タイムアウト | 5 s |
| layer | testlayer |
| VPC |  smartnovel-vpc-dev |

## 環境変数
| 変数名 | 値 |
| ---- | ---- |
| ES_HOST | vpc-smartnovel-es-dev-j74tj7mufmh6cmogkjcudm6uq4.ap-northeast-1.es.amazonaws.com |
| ES_INDEX | smart-novel |
| ES_REGION | ap-northeast-1 |