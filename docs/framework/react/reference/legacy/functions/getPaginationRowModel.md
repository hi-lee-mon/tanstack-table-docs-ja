---
id: getPaginationRowModel
title: getPaginationRowModel
---

```ts
function getPaginationRowModel<TData>(): RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:79](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L79)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`RowModelFactory`](../type-aliases/RowModelFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックと `createPaginatedRowModel()` を使ってください。

これは、`useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。
ページネーション済み行モデルを有効にする目印として働きます。
