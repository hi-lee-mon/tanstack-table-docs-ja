---
id: table_getIsAllColumnsVisible
title: table_getIsAllColumnsVisible
---

```ts
function table_getIsAllColumnsVisible<TFeatures, TData>(table): boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:340](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L340)

すべての末端の列が現在表示されているかどうかを判定します。

表示の状態にエントリーがなければ既定値は `true` なので、非表示にできない列は自然に表示されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const allVisible = table_getIsAllColumnsVisible(table)
```
