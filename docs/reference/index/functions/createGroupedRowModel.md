---
id: createGroupedRowModel
title: createGroupedRowModel
---

```ts
function createGroupedRowModel<TFeatures, TData>(): (table) => () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/createGroupedRowModel.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/createGroupedRowModel.ts#L26)

メモ化されたグループ化済み行モデルのファクトリーを作成します。

ファクトリーは関係するテーブルの状態のアトムとオプションを読み取り、テーブルの行モデルのパイプラインで使う行モデル関数を返します。

rowAggregationFeature も登録されている場合、グループ化された行は、グループ以外の値の計算にその共有の実行器を使います。集計がなくてもグループ化は使えます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`) => () => [`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
