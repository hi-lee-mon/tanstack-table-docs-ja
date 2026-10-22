---
id: legacyCreateColumnHelper
title: legacyCreateColumnHelper
---

```ts
function legacyCreateColumnHelper<TData>(): ColumnHelper<LegacyFeatures, TData>;
```

定義元: [src/useLegacyTable.ts:360](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L360)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

`ColumnHelper`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

## 非推奨 {#deprecated}

代わりに、useTable とあわせて `createColumnHelper<TFeatures, TData>()` を使ってください。

useLegacyTable で使うための、LegacyFeatures があらかじめ結び付けられた列ヘルパーです。
必要なのは TData だけで、TFeatures を指定する必要はありません。
