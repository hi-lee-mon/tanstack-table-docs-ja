---
id: row_toggleExpanded
title: row_toggleExpanded
---

```ts
function row_toggleExpanded<TFeatures, TData>(row, expanded?): void;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:289](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L289)

この行を展開、または折りたたみます。

`expanded` を省略すると、行を切り替えます。現在の状態が「すべて展開」の場合、行ごとの変更を適用する前に、まずその状態を行 ID のマップ（展開できる行の ID だけを含みます）に展開します。

要求された状態が現在の状態と同じ場合や、展開できない行を展開しようとした場合は、何もしません（`onExpandedChange` も呼ばれません）。
古くなった展開済みの ID を片付けられるよう、折りたたみは常に許可されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

### expanded? {#expanded}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
row_toggleExpanded(row)
```
