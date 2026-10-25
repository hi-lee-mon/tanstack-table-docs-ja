---
id: createFilteredRowModel
title: createFilteredRowModel
---

```ts
function createFilteredRowModel<TFeatures, TData>(): (table) => () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/createFilteredRowModel.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/createFilteredRowModel.ts#L32)

メモ化されたフィルター済み行モデルのファクトリーを作成します。

ファクトリーは関係するテーブルの状態のアトムとオプションを読み取り、テーブルの行モデルのパイプラインで使う行モデル関数を返します。

使うフィルター関数は、`features` オプションの `filterFns` スロットに登録します:
`tableFeatures({ columnFilteringFeature, filteredRowModel: createFilteredRowModel(), filterFns: { includesString: filterFn_includesString } })`。
`filterFn_*` 関数を個別に import すれば、使わない組み込み関数はバンドルに含まれません。列オプションの `filterFn` に直接渡すフィルター関数は、登録する必要がありません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`) => () => [`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
