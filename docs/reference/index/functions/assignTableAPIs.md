---
id: assignTableAPIs
title: assignTableAPIs
---

```ts
function assignTableAPIs<TFeatures, TData, TDeps, TDepArgs>(
   feature,
   table,
   apis): void;
```

定義元: [utils.ts:542](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L542)

Table API のメソッドをテーブルインスタンスに直接割り当てます。
row / cell / column / header と違い、テーブルは1つしかないため、メソッドを直接割り当てます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TDeps {#tdeps}

`TDeps` *extends* readonly `any`[]

### TDepArgs {#tdepargs}

`TDepArgs`

## パラメーター {#parameters}

### feature {#feature}

keyof `TFeatures` & `string`

### table {#table}

[`Table_Internal`](../interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### apis {#apis}

[`APIObject`](../type-aliases/APIObject.md)\<`TDeps`, [`NoInfer`](../type-aliases/NoInfer.md)\<`TDepArgs`\>\>

## 戻り値 {#returns}

`void`
