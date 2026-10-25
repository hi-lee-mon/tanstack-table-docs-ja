---
id: TableOptions_GlobalFiltering
title: TableOptions_GlobalFiltering
---

定義元: [features/global-filtering/globalFilteringFeature.types.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L35)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableGlobalFilter? {#enableglobalfilter}

```ts
optional enableGlobalFilter?: boolean;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L42)

許可している列を対象に、グローバルフィルタリングを有効にします。

***

### getColumnCanGlobalFilter? {#getcolumncanglobalfilter}

```ts
optional getColumnCanGlobalFilter?: <TFeatures, TData, TValue>(column) => boolean;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L47)

指定すると、この関数が列を引数にして呼ばれます。その列をグローバルフィルタリングに使うかどうかを `true` か `false` で返してください。
列に `string` や `number` 以外のデータ（`undefined` など）が入りうる場合に便利です。

#### 型パラメーター {#type-parameters-1}

##### TFeatures {#tfeatures-1}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-1}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters}

##### column {#column}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns}

`boolean`

***

### globalFilterFn? {#globalfilterfn}

```ts
optional globalFilterFn?: FilterFnOption<TFeatures, TData>;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L60)

グローバルフィルタリングに使うフィルター関数です。
- 組み込みのフィルター関数を指す `string`
- `tableOptions.filterFns` オプションで渡したカスタムのフィルター関数を指す `string`
- カスタムのフィルター関数

***

### onGlobalFilterChange? {#onglobalfilterchange}

```ts
optional onGlobalFilterChange?: OnChangeFn<any>;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L66)

グローバルフィルターの状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.globalFilter` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
