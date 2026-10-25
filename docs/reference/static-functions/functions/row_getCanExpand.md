---
id: row_getCanExpand
title: row_getCanExpand
---

```ts
function row_getCanExpand<TFeatures, TData>(row): boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:383](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L383)

この行を展開できるかどうかを判定します。

`options.getRowCanExpand` を渡した場合は、そちらが優先されます。そうでなければ、展開が有効で、行がサブ行を持つ場合に展開できます。

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
const canExpand = row_getCanExpand(row)
```
