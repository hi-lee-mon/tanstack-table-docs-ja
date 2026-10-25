---
id: createPaginatedRowModel
title: createPaginatedRowModel
---

```ts
function createPaginatedRowModel<TFeatures, TData>(): (table) => () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/createPaginatedRowModel.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/createPaginatedRowModel.ts#L15)

メモ化されたページ分割済み行モデルのファクトリーを作成します。

ファクトリーは関係するテーブルの状態のアトムとオプションを読み取り、テーブルの行モデルのパイプラインで使う行モデル関数を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`) => () => [`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
