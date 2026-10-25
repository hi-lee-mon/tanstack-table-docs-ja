---
id: Row_RowExpanding
title: Row_RowExpanding
---

定義元: [features/row-expanding/rowExpandingFeature.types.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L13)

## プロパティ {#properties}

### getCanExpand {#getcanexpand}

```ts
getCanExpand: () => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:17](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L17)

この行を展開できるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsAllParentsExpanded {#getisallparentsexpanded}

```ts
getIsAllParentsExpanded: () => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L21)

この行の祖先がすべて展開されているかどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### getIsExpanded {#getisexpanded}

```ts
getIsExpanded: () => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L25)

この行が現在展開されているかどうかを判定します。

#### 戻り値 {#returns-2}

`boolean`

***

### getToggleExpandedHandler {#gettoggleexpandedhandler}

```ts
getToggleExpandedHandler: () => () => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L29)

この行の展開状態を切り替えるハンドラーを作成します。

#### 戻り値 {#returns-3}

() => `void`

***

### toggleExpanded {#toggleexpanded}

```ts
toggleExpanded: (expanded?) => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L33)

この行の展開状態を切り替えます（`expanded` を渡した場合はその値に設定します）。

#### パラメーター {#parameters}

##### expanded? {#expanded}

`boolean`

#### 戻り値 {#returns-4}

`void`
