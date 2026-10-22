---
id: RowModelFactory
title: RowModelFactory
---

```ts
type RowModelFactory<TData> = (table) => () => RowModel<LegacyFeatures, TData>;
```

定義元: [src/useLegacyTable.ts:177](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L177)

v8 API の行モデルファクトリー関数の型です。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## パラメーター {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

## 戻り値 {#returns}

() => `RowModel`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>
