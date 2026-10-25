---
id: Table_Rows
title: Table_Rows
---

定義元: [core/rows/coreRowsFeature.types.ts:130](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L130)

## 継承先 {#extended-by}

- [`Table_Core`](Table_Core.md)
- [`Table_Internal`](Table_Internal.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getMaxSubRowDepth {#getmaxsubrowdepth}

```ts
getMaxSubRowDepth: () => number;
```

定義元: [core/rows/coreRowsFeature.types.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L138)

コア行モデルで、構造上いちばん深い行の深さを返します。
ルートの行は深さ `0`、直下のサブ行は深さ `1` で、以降も同様です。

#### 戻り値 {#returns}

`number`

***

### getRow {#getrow}

```ts
getRow: (id, searchAll?) => Row<TFeatures, TData>;
```

定義元: [core/rows/coreRowsFeature.types.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L153)

指定した ID の行を返します。

#### パラメーター {#parameters}

##### id {#id}

`string`

##### searchAll? {#searchall}

`boolean`

#### 戻り値 {#returns-1}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

***

### getRowId {#getrowid}

```ts
getRowId: (_, index, parent?) => string;
```

定義元: [core/rows/coreRowsFeature.types.ts:149](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L149)

指定した行の行 ID を返します。

#### パラメーター {#parameters-1}

##### \_ {#_}

`TData`

##### index {#index}

`number`

##### parent? {#parent}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-2}

`string`

***

### getRowsInDisplayOrder {#getrowsindisplayorder}

```ts
getRowsInDisplayOrder: () => Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L145)

現在の表示順で行を返し、各行に表示インデックスを割り当てます。展開された行がページネーションを素通りする場合は、展開された子孫もこの順に含まれます。
これは `row.getDisplayIndex()` が使う、メモ化された元データです。

#### 戻り値 {#returns-3}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]
