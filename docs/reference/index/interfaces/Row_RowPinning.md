---
id: Row_RowPinning
title: Row_RowPinning
---

定義元: [features/row-pinning/rowPinningFeature.types.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L42)

## プロパティ {#properties}

### getCanPin {#getcanpin}

```ts
getCanPin: () => boolean;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:46](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L46)

この行を固定できるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsPinned {#getispinned}

```ts
getIsPinned: () => RowPinningPosition;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:50](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L50)

行の固定位置を返します（`'top'`、`'bottom'`、`false` のいずれか）。

#### 戻り値 {#returns-1}

[`RowPinningPosition`](../type-aliases/RowPinningPosition.md)

***

### getPinnedIndex {#getpinnedindex}

```ts
getPinnedIndex: () => number;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L54)

固定された行グループの中での、行の固定位置のインデックス（数値）を返します。

#### 戻り値 {#returns-2}

`number`

***

### pin {#pin}

```ts
pin: (position, includeLeafRows?, includeParentRows?) => void;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L58)

行を `'top'` または `'bottom'` に固定します。`false` を渡すと固定を解除し、中央に戻します。

#### パラメーター {#parameters}

##### position {#position}

[`RowPinningPosition`](../type-aliases/RowPinningPosition.md)

##### includeLeafRows? {#includeleafrows}

`boolean`

##### includeParentRows? {#includeparentrows}

`boolean`

#### 戻り値 {#returns-3}

`void`
