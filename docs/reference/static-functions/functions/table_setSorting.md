---
id: table_setSorting
title: table_setSorting
---

```ts
function table_setSorting<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L43)

ソートのアップデーターを、テーブルのソートの変更ハンドラーに通します。

アップデーターには、次の `SortingState` 配列か、前のソートの状態を受け取る関数を指定できます。インスタンスの `table.setSorting` と同じ動作です。
状態の持ち主には等価判定で保護されたアップデーターが渡されるので、構造上等しいソートの値なら、持ち主の既存の参照が保たれます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`SortingState`](../../index/type-aliases/SortingState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setSorting(table, (old) => [...old, { id: 'age', desc: true }])
```
