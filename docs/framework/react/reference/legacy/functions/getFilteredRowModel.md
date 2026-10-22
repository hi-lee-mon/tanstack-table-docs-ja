---
id: getFilteredRowModel
title: getFilteredRowModel
---

```ts
function getFilteredRowModel<TData>(): RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:55](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L55)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`RowModelFactory`](../type-aliases/RowModelFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックで、`features` の `filteredRowModel` スロットに `createFilteredRowModel()` を指定してください。

これは `useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。フィルタリング済みの行モデルを有効にする目印として働きます。
