---
id: FacetedRowModelFactory
title: FacetedRowModelFactory
---

```ts
type FacetedRowModelFactory<TData> = (table, columnId) => () => RowModel<LegacyFeatures, TData>;
```

定義元: [src/useLegacyTable.ts:184](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L184)

v8 API のファセット行モデルファクトリー関数の型です。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## パラメーター {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

() => `RowModel`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>
