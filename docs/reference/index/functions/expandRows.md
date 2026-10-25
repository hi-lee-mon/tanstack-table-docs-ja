---
id: expandRows
title: expandRows
---

```ts
function expandRows<TFeatures, TData>(rowModel): RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/createExpandedRowModel.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/createExpandedRowModel.ts#L62)

現在の展開状態に従って行モデルを展開します。

展開されたサブ行は、元の行の階層を保ったまま、平坦化された行の並びに挿入されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## パラメーター {#parameters}

### rowModel {#rowmodel}

[`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
