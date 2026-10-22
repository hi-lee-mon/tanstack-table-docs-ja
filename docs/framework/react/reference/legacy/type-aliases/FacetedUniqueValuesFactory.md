---
id: FacetedUniqueValuesFactory
title: FacetedUniqueValuesFactory
---

```ts
type FacetedUniqueValuesFactory<TData> = (table, columnId) => () => Map<any, number>;
```

定義元: [src/useLegacyTable.ts:200](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L200)

v8 API のファセットの一意な値を作るファクトリー関数の型です。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## パラメーター {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

() => `Map`\<`any`, `number`\>
