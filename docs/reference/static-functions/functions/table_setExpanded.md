---
id: table_setExpanded
title: table_setExpanded
---

```ts
function table_setExpanded<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L66)

展開状態のアップデーターを、テーブルの展開の変更ハンドラーに通します。

アップデーターには、`true`、行 ID のマップ、前の展開状態を受け取る関数のいずれかを指定できます。インスタンスの `table.setExpanded` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`ExpandedState`](../../index/type-aliases/ExpandedState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setExpanded(table, (old) => ({ ...old, [rowId]: true }))
```
