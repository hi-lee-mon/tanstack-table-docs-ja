---
id: table_autoResetExpanded
title: table_autoResetExpanded
---

```ts
function table_autoResetExpanded<TFeatures, TData>(table): void;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L38)

行の構造が変わったあとに、展開状態のリセットを予約します。

リセットは、`autoResetAll`、`autoResetExpanded`、またはクライアントサイドでの展開の既定の動作が許可する場合に実行されます。手動の展開では、リセットのオプションで明示的に有効にしない限り実行されません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_autoResetExpanded(table)
```
