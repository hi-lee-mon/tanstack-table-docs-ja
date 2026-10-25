---
id: TableOptions_RowExpanding
title: TableOptions_RowExpanding
---

定義元: [features/row-expanding/rowExpandingFeature.types.ts:36](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L36)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### autoResetExpanded? {#autoresetexpanded}

```ts
optional autoResetExpanded?: boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L43)

ページの内容を変えるテーブルの状態が変わったときに、展開状態を自動でリセットするようにします。

***

### enableExpanding? {#enableexpanding}

```ts
optional enableExpanding?: boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L47)

サブ行を持つ行を展開できるようにします。

***

### getIsRowExpanded? {#getisrowexpanded}

```ts
optional getIsRowExpanded?: (row) => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:51](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L51)

指定すると、行が現在展開されているかどうかを判定する既定の動作を上書きできます。

#### パラメーター {#parameters}

##### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

`boolean`

***

### getRowCanExpand? {#getrowcanexpand}

```ts
optional getRowCanExpand?: (row) => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L55)

指定すると、行を展開できるかどうかを判定する既定の動作を上書きできます。

#### パラメーター {#parameters-1}

##### row {#row-1}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-1}

`boolean`

***

### manualExpanding? {#manualexpanding}

```ts
optional manualExpanding?: boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L59)

手動の行の展開を有効にします。`true` にすると、行の展開に `getExpandedRowModel` は使われず、展開は自分のデータモデルで行うことになります。サーバーサイドで展開する場合に便利です。

***

### onExpandedChange? {#onexpandedchange}

```ts
optional onExpandedChange?: OnChangeFn<ExpandedState>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:65](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L65)

展開状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.expanded` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。

***

### paginateExpandedRows? {#paginateexpandedrows}

```ts
optional paginateExpandedRows?: boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L69)

`true` の場合、展開された行もテーブルの他の行と一緒にページ分割されます（つまり、展開された行が複数のページにまたがることがあります）。
`false` の場合、展開された行はページネーションの対象になりません（つまり、展開された行は常に親と同じページに描画されます）。この場合、設定したページサイズより多くの行が描画されることになります。
