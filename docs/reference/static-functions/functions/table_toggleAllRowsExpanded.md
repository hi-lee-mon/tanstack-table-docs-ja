---
id: table_toggleAllRowsExpanded
title: table_toggleAllRowsExpanded
---

```ts
function table_toggleAllRowsExpanded<TFeatures, TData>(table, expanded?): void;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:92](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L92)

すべての行を展開、または折りたたみます。

`true` を渡すと、「すべて展開」を表す特別な状態を保存します。`false` を渡すと、空のマップを保存します。値を省略すると、すべての行が現在展開されているかどうかをもとに切り替えます。

展開できる行がない場合や、要求された状態が現在の状態とまったく同じ場合は、何もしません（`onExpandedChange` も呼ばれません）。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### expanded? {#expanded}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_toggleAllRowsExpanded(table)
```
