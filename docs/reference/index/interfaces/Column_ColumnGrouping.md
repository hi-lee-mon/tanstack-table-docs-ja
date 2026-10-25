---
id: Column_ColumnGrouping
title: Column_ColumnGrouping
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:36](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L36)

## プロパティ {#properties}

### getCanGroup {#getcangroup}

```ts
getCanGroup: () => boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L40)

この列が現在グループ化できるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getGroupedIndex {#getgroupedindex}

```ts
getGroupedIndex: () => number;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:44](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L44)

順序付きのグループ化の状態の中で、この列の位置を探します。

#### 戻り値 {#returns-1}

`number`

***

### getIsGrouped {#getisgrouped}

```ts
getIsGrouped: () => boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L48)

この列 ID がグループ化の状態に含まれているかどうかを判定します。

#### 戻り値 {#returns-2}

`boolean`

***

### getToggleGroupingHandler {#gettogglegroupinghandler}

```ts
getToggleGroupingHandler: () => () => void;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:52](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L52)

列のグループ化の状態を切り替える関数を返します。ボタンの `onClick` プロパティに渡すのに便利です。

#### 戻り値 {#returns-3}

() => `void`

***

### toggleGrouping {#togglegrouping}

```ts
toggleGrouping: () => void;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:56](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L56)

列のグループ化の状態を切り替えます。

#### 戻り値 {#returns-4}

`void`
