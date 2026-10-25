---
id: Column_ColumnResizing
title: Column_ColumnResizing
---

定義元: [features/column-resizing/columnResizingFeature.types.ts:68](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L68)

## プロパティ {#properties}

### getCanResize {#getcanresize}

```ts
getCanResize: () => boolean;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L72)

この列でリサイズ操作を始められるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsResizing {#getisresizing}

```ts
getIsResizing: () => boolean;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L76)

この列が現在リサイズ中の対象かどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`
