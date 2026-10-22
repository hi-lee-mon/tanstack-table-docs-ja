---
id: LegacyTableOptions
title: LegacyTableOptions
---

```ts
type LegacyTableOptions<TData> = Omit<TableOptions<LegacyFeatures, TData>, "features"> & LegacyRowModelOptions<TData>;
```

定義元: [src/useLegacyTable.ts:279](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L279)

useLegacyTable で使う、v8 スタイルのレガシーなテーブルオプションです。

この型は `features` を除外し、代わりに v8 スタイルの
`get*RowModel` 関数のオプションを受け取ります。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 非推奨 {#deprecated}

これは v8 から移行するための互換レイヤーです。代わりに、`features` オプションを明示的に指定して `useTable` を使ってください。
