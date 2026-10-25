---
id: constructFilterFn
title: constructFilterFn
---

```ts
function constructFilterFn<TFeatures, TData>(def): CreatedFilterFn<TFeatures, TData>;
```

定義元: [features/column-filtering/filterFns.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L41)

値レベルの比較関数と、省略可能なリゾルバーから `FilterFn` を組み立てます。

比較関数 `filter` は、行のデータ値（`resolveDataValue` が定義されていれば、それを通した値）と、フィルター値（テーブルが `resolveFilterValue` を通した値）を受け取ります。
正規化をリゾルバー側に置いておけば、既存のフィルター関数の派生版を作るときに、比較処理を書き直さずリゾルバーを差し替えるだけで済みます。

定義は戻り値の関数に付いているので、組み込みのフィルター関数をスプレッドして、異なる部分だけを上書きすれば派生版を作れます。

```ts
const normalize = (value: unknown) =>
  String(value ?? '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '')

const includesStringIgnoreDiacritics = constructFilterFn({
  ...filterFn_includesString,
  resolveFilterValue: normalize,
  resolveDataValue: normalize,
})
```

注意: テーブルは、行を判定する前に、フィルターごとに `resolveFilterValue` を1回だけ適用します。
テーブルを介さずにフィルター関数を直接呼ぶ場合は、自分で適用してください: `fn(row, columnId, fn.resolveFilterValue?.(value) ?? value)`。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md) = `any`

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## パラメーター {#parameters}

### def {#def}

[`FilterFnDef`](../interfaces/FilterFnDef.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`CreatedFilterFn`](../interfaces/CreatedFilterFn.md)\<`TFeatures`, `TData`\>
