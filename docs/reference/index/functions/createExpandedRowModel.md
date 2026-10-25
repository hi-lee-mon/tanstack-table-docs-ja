---
id: createExpandedRowModel
title: createExpandedRowModel
---

```ts
function createExpandedRowModel<TFeatures, TData>(): (table) => () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/createExpandedRowModel.ts:14](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/createExpandedRowModel.ts#L14)

メモ化された展開済み行モデルのファクトリーを作成します。

ファクトリーは関係するテーブルの状態のアトムとオプションを読み取り、テーブルの行モデルのパイプラインで使う行モデル関数を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`) => () => [`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
