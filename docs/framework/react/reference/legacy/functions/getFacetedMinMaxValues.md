---
id: getFacetedMinMaxValues
title: getFacetedMinMaxValues
---

```ts
function getFacetedMinMaxValues<TData>(): FacetedMinMaxValuesFactory<TData>;
```

定義元: [src/useLegacyTable.ts:127](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L127)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`FacetedMinMaxValuesFactory`](../type-aliases/FacetedMinMaxValuesFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

代わりに、新しい `useTable` フックと `createFacetedMinMaxValues()` を使ってください。

これは、`useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。ファセットの最小値・最大値を有効にする目印として働きます。
