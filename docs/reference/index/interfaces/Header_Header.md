---
id: Header_Header
title: Header_Header
---

定義元: [core/headers/coreHeadersFeature.types.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L114)

## 継承元 {#extends}

- [`Header_CoreProperties`](Header_CoreProperties.md)\<`TFeatures`, `TData`, `TValue`\>

## 継承先 {#extended-by}

- [`Header_Core`](Header_Core.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### colSpan {#colspan}

```ts
colSpan: number;
```

定義元: [core/headers/coreHeadersFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L59)

ヘッダーの col-span です。

#### 継承元のメンバー {#inherited-from}

[`Header_CoreProperties`](Header_CoreProperties.md).[`colSpan`](Header_CoreProperties.md#colspan)

***

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [core/headers/coreHeadersFeature.types.ts:63](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L63)

ヘッダーに対応する列オブジェクトです。

#### 継承元のメンバー {#inherited-from-1}

[`Header_CoreProperties`](Header_CoreProperties.md).[`column`](Header_CoreProperties.md#column)

***

### depth {#depth}

```ts
depth: number;
```

定義元: [core/headers/coreHeadersFeature.types.ts:67](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L67)

ヘッダーの深さです（0始まり）。

#### 継承元のメンバー {#inherited-from-2}

[`Header_CoreProperties`](Header_CoreProperties.md).[`depth`](Header_CoreProperties.md#depth)

***

### getContext {#getcontext}

```ts
getContext: () => HeaderContext<TFeatures, TData, TValue>;
```

定義元: [core/headers/coreHeadersFeature.types.ts:122](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L122)

ヘッダー、フッター、フィルターのような、列を基にしたコンポーネントのための描画コンテキスト（props）を返します。

#### 戻り値 {#returns}

[`HeaderContext`](HeaderContext.md)\<`TFeatures`, `TData`, `TValue`\>

***

### getLeafHeaders {#getleafheaders}

```ts
getLeafHeaders: () => Header<TFeatures, TData, TValue>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:126](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L126)

このヘッダーの下に階層的に入れ子になった、末端のヘッダーを返します。

#### 戻り値 {#returns-1}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>[]

***

### headerGroup {#headergroup}

```ts
headerGroup: HeaderGroup<TFeatures, TData> | null;
```

定義元: [core/headers/coreHeadersFeature.types.ts:71](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L71)

ヘッダーに対応するヘッダーグループのオブジェクトです。

#### 継承元のメンバー {#inherited-from-3}

[`Header_CoreProperties`](Header_CoreProperties.md).[`headerGroup`](Header_CoreProperties.md#headergroup)

***

### id {#id}

```ts
id: string;
```

定義元: [core/headers/coreHeadersFeature.types.ts:75](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L75)

ヘッダーの一意な識別子です。

#### 継承元のメンバー {#inherited-from-4}

[`Header_CoreProperties`](Header_CoreProperties.md).[`id`](Header_CoreProperties.md#id)

***

### index {#index}

```ts
index: number;
```

定義元: [core/headers/coreHeadersFeature.types.ts:79](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L79)

ヘッダーグループ内での、ヘッダーのインデックスです。

#### 継承元のメンバー {#inherited-from-5}

[`Header_CoreProperties`](Header_CoreProperties.md).[`index`](Header_CoreProperties.md#index)

***

### isPlaceholder {#isplaceholder}

```ts
isPlaceholder: boolean;
```

定義元: [core/headers/coreHeadersFeature.types.ts:87](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L87)

ヘッダーがプレースホルダーのヘッダーかどうかを示す真偽値です。
プレースホルダーのヘッダーは、階層の浅い末端の列で、本来のヘッダーより上の行を埋めます。これにより、どのヘッダーグループの行も、表示中のすべての列を含みます。空のセルとして描画するか、`header.rowSpan` を使って、連なったプレースホルダーを縦に結合した1つのヘッダーセルにまとめてください。

#### 継承元のメンバー {#inherited-from-6}

[`Header_CoreProperties`](Header_CoreProperties.md).[`isPlaceholder`](Header_CoreProperties.md#isplaceholder)

***

### placeholderId? {#placeholderid}

```ts
optional placeholderId?: string;
```

定義元: [core/headers/coreHeadersFeature.types.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L91)

ヘッダーがプレースホルダーのヘッダーの場合、テーブル内の他のどのヘッダーとも重ならない一意なヘッダー ID になります。

#### 継承元のメンバー {#inherited-from-7}

[`Header_CoreProperties`](Header_CoreProperties.md).[`placeholderId`](Header_CoreProperties.md#placeholderid)

***

### rowSpan {#rowspan}

```ts
rowSpan: number;
```

定義元: [core/headers/coreHeadersFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L103)

ヘッダーセルを縦に結合するときに、このヘッダーが結合するヘッダーグループの行数です。
いちばん深い末端の列より浅い末端の列では、本来のヘッダーの上にプレースホルダーのヘッダーが連なります。連なりのいちばん上にあるプレースホルダーは連なり全体の行数を返し、それが覆うヘッダー（最下行にある本来の末端のヘッダーを含みます）はすべて 0 を返します。
縦に結合するには、rowSpan が 0 のヘッダーを描画せず、それ以外のヘッダーを `rowSpan` 属性とその列のヘッダーの内容で描画します。プレースホルダーであっても同じです。列ツリーの深さがそろっている場合、ヘッダーは常に 1 を返します。

#### 継承元のメンバー {#inherited-from-8}

[`Header_CoreProperties`](Header_CoreProperties.md).[`rowSpan`](Header_CoreProperties.md#rowspan)

***

### subHeaders {#subheaders}

```ts
subHeaders: Header<TFeatures, TData, TValue>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L107)

ヘッダーの階層上のサブヘッダー（子ヘッダー）です。対応する列が末端の列なら空です。

#### 継承元のメンバー {#inherited-from-9}

[`Header_CoreProperties`](Header_CoreProperties.md).[`subHeaders`](Header_CoreProperties.md#subheaders)

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/headers/coreHeadersFeature.types.ts:111](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L111)

親のテーブルインスタンスへの参照です。

#### 継承元のメンバー {#inherited-from-10}

[`Header_CoreProperties`](Header_CoreProperties.md).[`table`](Header_CoreProperties.md#table)
