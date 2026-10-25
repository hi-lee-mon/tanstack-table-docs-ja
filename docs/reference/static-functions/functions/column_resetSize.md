---
id: column_resetSize
title: column_resetSize
---

```ts
function column_resetSize<TFeatures, TData, TValue>(column): void;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:235](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L235)

この列の、確定した幅の上書きを取り除きます。

リセットしたあとは、列の幅は再び `columnDef.size` か組み込みの既定値から決まります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
column_resetSize(column)
```
