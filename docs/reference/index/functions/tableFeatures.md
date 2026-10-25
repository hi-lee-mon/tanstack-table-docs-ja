---
id: tableFeatures
title: tableFeatures
---

```ts
function tableFeatures<TFeatures>(features): TFeatures;
```

定義元: [helpers/tableFeatures.ts:46](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableFeatures.ts#L46)

テーブルインスタンスに import して適用する機能を定義するためのヘルパー関数です。
このユーティリティを使うと、import する機能の型が正しく推論されやすくなります。
**注意:** このユーティリティは、コンポーネントの外で静的に使うことをおすすめします。

このオブジェクトには、機能モジュールのほかに、テーブルへ静的に組み込むものがすべて入ります:

- 行モデルのファクトリー（`sortedRowModel`、`filteredRowModel` など）
- 行モデル関数のレジストリ（`sortFns`、`filterFns`、`aggregationFns`）。
  ここに登録したキーが、`sortFn`、`filterFn`、`globalFilterFn`、`aggregationFn` に指定できる文字列になり、型も完全に推論されます
- テーブルごとの meta の型を宣言するための型専用スロット `tableMeta` / `columnMeta`。
  グローバルな宣言のマージを使わずに済みます。値は実体がなく（実行時には無視され、取り除かれます）、使われるのは型だけです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

## パラメーター {#parameters}

### features {#features}

`TFeatures` & [`ValidateFeatureSlots`](../type-aliases/ValidateFeatureSlots.md)\<`TFeatures`\>

## 戻り値 {#returns}

`TFeatures`

## 例 {#example}

```
import {
  columnFilteringFeature,
  createFilteredRowModel,
  createSortedRowModel,
  filterFn_includesString,
  rowSortingFeature,
  sortFn_alphanumeric,
  sortFn_text,
  tableFeatures,
} from '@tanstack/react-table'
const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  filterFns: { includesString: filterFn_includesString, myCustomFilterFn },
  sortFns: { alphanumeric: sortFn_alphanumeric, text: sortFn_text },
  tableMeta: {} as { updateData: (rowIndex: number, columnId: string, value: unknown) => void },
  columnMeta: {} as { align?: 'left' | 'right' },
});
const table = useTable({ features, columns, data });
```
