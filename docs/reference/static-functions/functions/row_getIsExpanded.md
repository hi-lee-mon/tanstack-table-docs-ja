---
id: row_getIsExpanded
title: row_getIsExpanded
---

```ts
function row_getIsExpanded<TFeatures, TData>(row): boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:348](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L348)

この行が展開されているかどうかを判定します。

`options.getIsRowExpanded` で、状態から導き出す動作を上書きできます。そうでなければ、展開状態が `true` か、この行 ID を含む場合に展開されているとみなします。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const expanded = row_getIsExpanded(row)
```
