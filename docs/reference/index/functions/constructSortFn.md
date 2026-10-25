---
id: constructSortFn
title: constructSortFn
---

```ts
function constructSortFn<TFeatures, TData>(def): CreatedSortFn<TFeatures, TData>;
```

定義元: [features/row-sorting/sortFns.ts:39](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/sortFns.ts#L39)

値レベルの比較関数と、省略可能な正規化関数 `resolveDataValue` から `SortFn` を組み立てます。

比較関数 `sort` は、2つの行のデータ値を受け取ります。`resolveDataValue` が定義されていれば、どちらもそれを通した値です。
正規化をリゾルバー側に置いておけば、既存のソート関数の派生版を作るときに、比較処理を書き直さずリゾルバーを差し替えるだけで済みます。

定義は戻り値の関数に付いているので、組み込みのソート関数をスプレッドして、異なる部分だけを上書きすれば派生版を作れます。

```ts
const stripDiacritics = (value: string) =>
  value.normalize('NFD').replace(/\p{Diacritic}/gu, '')

const alphanumericIgnoreDiacritics = constructSortFn({
  ...sortFn_alphanumeric,
  resolveDataValue: (value) =>
    stripDiacritics(sortFn_alphanumeric.resolveDataValue!(value)),
})
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md) = `any`

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## パラメーター {#parameters}

### def {#def}

[`SortFnDef`](../interfaces/SortFnDef.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`CreatedSortFn`](../interfaces/CreatedSortFn.md)\<`TFeatures`, `TData`\>
