---
id: Column_ColumnSizing
title: Column_ColumnSizing
---

定義元: [features/column-sizing/columnSizingFeature.types.ts:112](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L112)

## プロパティ {#properties}

### getAfter {#getafter}

```ts
getAfter: (position?) => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:119](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L119)

この列の末尾の端から、その領域の末尾までのオフセットを測ります。

固定領域を渡すと、その論理的な領域内で測ります。値は、この列より後ろにある表示中の末端の列の幅の合計です。

#### パラメーター {#parameters}

##### position? {#position}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns}

`number`

***

### getSize {#getsize}

```ts
getSize: () => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:123](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L123)

状態と最小値・最大値の制約を反映した、列の現在の幅を求めます。

#### 戻り値 {#returns-1}

`number`

***

### getStart {#getstart}

```ts
getStart: (position?) => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L131)

この列が属する領域の先頭から、この列の先頭の端までのオフセットを測ります。

固定領域を渡すと、その論理的な領域内で測ります。値は、この列より前にある表示中の末端の列の幅の合計です。

#### パラメーター {#parameters-1}

##### position? {#position-1}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns-2}

`number`

***

### resetSize {#resetsize}

```ts
resetSize: () => void;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:135](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L135)

列を初期の幅に戻します。

#### 戻り値 {#returns-3}

`void`
