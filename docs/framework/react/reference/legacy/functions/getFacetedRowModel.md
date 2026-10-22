---
id: getFacetedRowModel
title: getFacetedRowModel
---

```ts
function getFacetedRowModel<TData>(): FacetedRowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:115](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L115)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`FacetedRowModelFactory`](../type-aliases/FacetedRowModelFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックと `createFacetedRowModel()` を使ってください。

これは `useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。
ファセット行モデルを有効にする目印として働きます。
