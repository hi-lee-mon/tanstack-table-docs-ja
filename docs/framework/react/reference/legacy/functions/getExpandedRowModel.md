---
id: getExpandedRowModel
title: getExpandedRowModel
---

```ts
function getExpandedRowModel<TData>(): RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:91](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L91)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`RowModelFactory`](../type-aliases/RowModelFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックで `createExpandedRowModel()` を使ってください。

これは `useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。展開済みの行モデルを有効にする目印として働きます。
