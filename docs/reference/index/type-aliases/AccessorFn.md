---
id: AccessorFn
title: AccessorFn
---

```ts
type AccessorFn<TData, TValue> = (originalRow, index) => TValue;
```

定義元: [types/ColumnDef.ts:53](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L53)

元の行オブジェクトからセルの値を読み取ります。

位置に応じた、安定した派生値が必要なアクセサーのために、行のインデックスも渡されます。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)

## パラメーター {#parameters}

### originalRow {#originalrow}

`TData`

### index {#index}

`number`

## 戻り値 {#returns}

`TValue`
