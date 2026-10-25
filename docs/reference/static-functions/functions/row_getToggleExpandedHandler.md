---
id: row_getToggleExpandedHandler
title: row_getToggleExpandedHandler
---

```ts
function row_getToggleExpandedHandler<TFeatures, TData>(row): () => void;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:428](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L428)

この行の展開状態を切り替える、行の操作部品向けのハンドラーを作成します。

行が展開できない場合、ハンドラーは何もしません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

() => `void`

## 例 {#example}

```ts
const onClick = row_getToggleExpandedHandler(row)
```
