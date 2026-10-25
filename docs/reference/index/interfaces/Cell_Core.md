---
id: Cell_Core
title: Cell_Core
---

定義元: [types/Cell.ts:9](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Cell.ts#L9)

## 継承元 {#extends}

- [`Cell_Cell`](Cell_Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [core/cells/coreCellsFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L29)

セルに対応する Column オブジェクトです。

#### 継承元のメンバー {#inherited-from}

[`Cell_Cell`](Cell_Cell.md).[`column`](Cell_Cell.md#column)

***

### getContext {#getcontext}

```ts
getContext: () => CellContext<TFeatures, TData, TValue>;
```

定義元: [core/cells/coreCellsFeature.types.ts:52](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L52)

セルや集計済みセルのような、セルを基にしたコンポーネントのための描画コンテキスト（props）を返します。この props をフレームワークの `flexRender` ユーティリティに渡すと、好きなテンプレートで描画できます:

#### 戻り値 {#returns}

[`CellContext`](CellContext.md)\<`TFeatures`, `TData`, `TValue`\>

#### 継承元のメンバー {#inherited-from-1}

[`Cell_Cell`](Cell_Cell.md).[`getContext`](Cell_Cell.md#getcontext)

***

### getValue {#getvalue}

```ts
getValue: Getter<TValue>;
```

定義元: [core/cells/coreCellsFeature.types.ts:56](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L56)

セルの値を返します。値は、対応する列のアクセサーのキーまたはアクセサー関数で取り出されます。

#### 継承元のメンバー {#inherited-from-2}

[`Cell_Cell`](Cell_Cell.md).[`getValue`](Cell_Cell.md#getvalue)

***

### id {#id}

```ts
id: string;
```

定義元: [core/cells/coreCellsFeature.types.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L33)

テーブル全体で一意なセルの ID です。

#### 継承元のメンバー {#inherited-from-3}

[`Cell_Cell`](Cell_Cell.md).[`id`](Cell_Cell.md#id)

***

### renderValue {#rendervalue}

```ts
renderValue: Getter<TValue | null>;
```

定義元: [core/cells/coreCellsFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L60)

`getValue` と同じようにセルの値を描画しますが、値が見つからない場合は `renderFallbackValue` を返します。

#### 継承元のメンバー {#inherited-from-4}

[`Cell_Cell`](Cell_Cell.md).[`renderValue`](Cell_Cell.md#rendervalue)

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

定義元: [core/cells/coreCellsFeature.types.ts:37](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L37)

セルに対応する Row オブジェクトです。

#### 継承元のメンバー {#inherited-from-5}

[`Cell_Cell`](Cell_Cell.md).[`row`](Cell_Cell.md#row)

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/cells/coreCellsFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L41)

親のテーブルインスタンスへの参照です。

#### 継承元のメンバー {#inherited-from-6}

[`Cell_Cell`](Cell_Cell.md).[`table`](Cell_Cell.md#table)
