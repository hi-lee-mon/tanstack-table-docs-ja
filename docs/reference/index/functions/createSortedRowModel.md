---
id: createSortedRowModel
title: createSortedRowModel
---

```ts
function createSortedRowModel<TFeatures, TData>(): (table) => () => RowModel<TFeatures, TData>;
```

定義元: [features/row-sorting/createSortedRowModel.ts:28](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/createSortedRowModel.ts#L28)

メモ化されたソート済み行モデルのファクトリーを作成します。

ファクトリーは関係するテーブルの状態のアトムとオプションを読み取り、テーブルの行モデルのパイプラインで使う行モデル関数を返します。

使うソート関数は、`features` オプションの `sortFns` スロットに登録します:
`tableFeatures({ rowSortingFeature, sortedRowModel: createSortedRowModel(), sortFns: { alphanumeric: sortFn_alphanumeric } })`。
`sortFn_*` 関数を個別に import すれば、使わない組み込み関数はバンドルに含まれません。列オプションの `sortFn` に直接渡すソート関数は、登録する必要がありません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## 戻り値 {#returns}

(`table`) => () => [`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
