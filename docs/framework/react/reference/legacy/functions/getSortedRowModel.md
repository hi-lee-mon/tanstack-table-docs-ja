---
id: getSortedRowModel
title: getSortedRowModel
---

```ts
function getSortedRowModel<TData>(): RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:67](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L67)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`RowModelFactory`](../type-aliases/RowModelFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックで `sortedRowModel` 機能スロットに `createSortedRowModel()` を指定してください。

これは `useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。
ソート済み行モデルを有効にする目印として働きます。
