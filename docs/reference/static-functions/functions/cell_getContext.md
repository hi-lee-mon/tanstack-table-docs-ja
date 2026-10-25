---
id: cell_getContext
title: cell_getContext
---

```ts
function cell_getContext<TFeatures, TData, TValue>(cell): object;
```

定義元: [core/cells/coreCellsFeature.utils.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.utils.ts#L54)

列の `cell` テンプレートに渡す描画コンテキストを作ります。

返されるオブジェクトには、テーブル・行・列・セルへの安定した参照と、描画関数のために結び付けた `getValue` と `renderValue` のヘルパーが含まれます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`object`

### cell {#cell-1}

```ts
cell: Cell<TFeatures, TData, TValue>;
```

### column {#column}

```ts
column: Column<TFeatures, TData, TValue> = cell.column;
```

### getValue {#getvalue}

```ts
getValue: () => NoInfer<TValue>;
```

#### 戻り値 {#returns-1}

[`NoInfer`](../../index/type-aliases/NoInfer.md)\<`TValue`\>

### renderValue {#rendervalue}

```ts
renderValue: () => NoInfer<TValue | null>;
```

#### 戻り値 {#returns-2}

[`NoInfer`](../../index/type-aliases/NoInfer.md)\<`TValue` \| `null`\>

### row {#row}

```ts
row: Row<TFeatures, TData> = cell.row;
```

### table {#table}

```ts
table: Table_Internal<TFeatures, TData> = cell.table;
```

## 例 {#example}

```ts
const context = cell_getContext(cell)
```
