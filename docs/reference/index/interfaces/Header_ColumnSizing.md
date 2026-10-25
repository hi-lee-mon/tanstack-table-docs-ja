---
id: Header_ColumnSizing
title: Header_ColumnSizing
---

定義元: [features/column-sizing/columnSizingFeature.types.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L138)

## プロパティ {#properties}

### getSize {#getsize}

```ts
getSize: () => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:142](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L142)

末端の列から、このヘッダーの描画時の幅を計算します。

#### 戻り値 {#returns}

`number`

***

### getStart {#getstart}

```ts
getStart: (position?) => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L146)

ヘッダーの、行方向の軸（ふつうのテーブルでは多くの場合 x 軸）に沿ったオフセットを返します。実質的には、前にあるすべてのヘッダーのオフセットの合計です。

#### パラメーター {#parameters}

##### position? {#position}

[`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)

#### 戻り値 {#returns-1}

`number`
