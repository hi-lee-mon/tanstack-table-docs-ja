---
id: Column_ColumnPinning
title: Column_ColumnPinning
---

定義元: [features/column-pinning/columnPinningFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L60)

## プロパティ {#properties}

### getCanPin {#getcanpin}

```ts
getCanPin: () => boolean;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:64](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L64)

この列か、その末端の列のいずれかを固定できるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsPinned {#getispinned}

```ts
getIsPinned: () => ColumnPinningPosition;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:68](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L68)

列の論理的な固定位置を読み取ります: `'start'`、`'end'`、`false` のいずれかです。

#### 戻り値 {#returns-1}

[`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)

***

### getPinnedIndex {#getpinnedindex}

```ts
getPinnedIndex: () => number;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L72)

固定領域の中で、この列のインデックスを探します。

#### 戻り値 {#returns-2}

`number`

***

### pin {#pin}

```ts
pin: (position) => void;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:77](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L77)

この列の末端の列を論理的な先頭または末尾に固定します。`false` を渡すと固定を解除します。

#### パラメーター {#parameters}

##### position {#position}

[`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)

#### 戻り値 {#returns-3}

`void`
