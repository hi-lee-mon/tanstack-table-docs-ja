---
id: ColumnDef_RowSorting
title: ColumnDef_RowSorting
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:118](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L118)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableMultiSort? {#enablemultisort}

```ts
optional enableMultiSort?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:125](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L125)

この列の複数列ソートを有効または無効にします。

***

### enableSorting? {#enablesorting}

```ts
optional enableSorting?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:129](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L129)

この列のソートを有効または無効にします。

***

### invertSorting? {#invertsorting}

```ts
optional invertSorting?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:133](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L133)

この列のソート順を反転させます。順位（1位、2位、3位）やゴルフのスコアのように、数が小さいほど良いという逆向きの尺度を持つ値に便利です。

***

### sortDescFirst? {#sortdescfirst}

```ts
optional sortDescFirst?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:137](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L137)

`true` にすると、この列でソートを切り替えたときに降順から始まります。

***

### sortFn? {#sortfn}

```ts
optional sortFn?: SortFnOption<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:143](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L143)

この列で使うソート関数です。
- 組み込みのソート関数を指す `string`
- カスタムのソート関数

***

### sortUndefined? {#sortundefined}

```ts
optional sortUndefined?: false | 1 | -1 | "first" | "last";
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:157](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L157)

この列をソートするときの undefined の値の優先度です。
- `false`
  - undefined の値は、特別な扱いをせず他の値と同じようにソート関数へ渡されます。扱いはソート関数に任されます
- `-1`
  - undefined の値を高い優先度（昇順）でソートします（昇順なら undefined はリストの先頭に来ます）
- `1`
  - undefined の値を低い優先度（降順）でソートします（昇順なら undefined はリストの末尾に来ます）
- `'first'`
  - ソートの向きに関係なく、undefined の値をリストの先頭に置きます
- `'last'`
  - ソートの向きに関係なく、undefined の値をリストの末尾に置きます
