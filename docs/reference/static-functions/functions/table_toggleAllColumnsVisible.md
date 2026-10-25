---
id: table_toggleAllColumnsVisible
title: table_toggleAllColumnsVisible
---

```ts
function table_toggleAllColumnsVisible<TFeatures, TData>(table, value?): void;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:313](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L313)

非表示にできる末端の列を、すべて表示または非表示にします。

すべての列を非表示に切り替えても、非表示にできない列は表示されたままです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### value? {#value}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_toggleAllColumnsVisible(table)
```
