---
id: ExtractColumnMeta
title: ExtractColumnMeta
---

```ts
type ExtractColumnMeta<TFeatures, TData, TValue> = IsAny<TFeatures> extends true ? ColumnMeta<TFeatures, TData, TValue> : TFeatures extends object ? TMeta : ColumnMeta<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:36](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L36)

機能の組み合わせについて、`columnDef.meta` の型を求めます。

features オブジェクトが型専用スロット `columnMeta` を宣言している場合（`tableFeatures({ ..., columnMeta: {} as MyColumnMeta })`）は、その型が使われます。
そうでなければ、グローバルに宣言のマージをした `ColumnMeta` インターフェースが使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
