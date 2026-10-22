---
id: FacetedMinMaxValuesFactory
title: FacetedMinMaxValuesFactory
---

```ts
type FacetedMinMaxValuesFactory<TData> = (table, columnId) => () => undefined | [number, number];
```

定義元: [src/useLegacyTable.ts:192](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L192)

v8 API のファセット最小値・最大値ファクトリー関数の型です。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## パラメーター {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

() => `undefined` \| \[`number`, `number`\]
