---
id: table_getFooterGroups
title: table_getFooterGroups
---

```ts
function table_getFooterGroups<TFeatures, TData>(table): HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/coreHeadersFeature.utils.ts:108](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.utils.ts#L108)

現在のヘッダーグループを逆順にして、フッターグループを作ります。

フッターの描画では、同じヘッダーオブジェクトとグループの構造を使いますが、末端の階層からルートに向かって描画します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`HeaderGroup`](../../index/interfaces/HeaderGroup.md)\<`TFeatures`, `TData`\>[]

## 例 {#example}

```ts
const footerGroups = table_getFooterGroups(table)
```
