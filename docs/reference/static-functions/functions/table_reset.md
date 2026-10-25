---
id: table_reset
title: table_reset
---

```ts
function table_reset<TFeatures, TData>(table): void;
```

定義元: [core/table/coreTablesFeature.utils.ts:102](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.utils.ts#L102)

テーブルの内部の基底アトムをすべて `table.initialState` に戻し、そのあと、登録された機能のリセット用フックを通して一時的なインスタンスデータを消します。

内部で持つ状態スライスを、1回のリアクティビティのバッチでリセットします。スライスを外部が持っている可能性がある場合は、機能ごとのリセット API を使ってください。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_reset(table)
```
