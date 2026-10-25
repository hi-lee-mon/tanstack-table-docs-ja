---
id: Column_ColumnVisibility
title: Column_ColumnVisibility
---

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L95)

## プロパティ {#properties}

### getCanHide {#getcanhide}

```ts
getCanHide: () => boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L99)

この列を非表示にできるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsVisible {#getisvisible}

```ts
getIsVisible: () => boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L103)

この列が現在表示されているかどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### getToggleVisibilityHandler {#gettogglevisibilityhandler}

```ts
getToggleVisibilityHandler: () => (event) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L107)

この列の表示を切り替える、チェックボックス用のハンドラーを作成します。

#### 戻り値 {#returns-2}

(`event`) => `void`

***

### toggleVisibility {#togglevisibility}

```ts
toggleVisibility: (value?) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:111](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L111)

列の表示を切り替えます。

#### パラメーター {#parameters}

##### value? {#value}

`boolean`

#### 戻り値 {#returns-3}

`void`
