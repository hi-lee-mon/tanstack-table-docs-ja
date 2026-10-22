---
id: getFacetedUniqueValues
title: getFacetedUniqueValues
---

```ts
function getFacetedUniqueValues<TData>(): FacetedUniqueValuesFactory<TData>;
```

定義元: [src/useLegacyTable.ts:139](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L139)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`FacetedUniqueValuesFactory`](../type-aliases/FacetedUniqueValuesFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックと `createFacetedUniqueValues()` を使ってください。

これは `useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。
ファセットの一意な値（faceted unique values）を有効にする目印として働きます。
