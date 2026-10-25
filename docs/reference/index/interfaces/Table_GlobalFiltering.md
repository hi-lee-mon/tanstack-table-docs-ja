---
id: Table_GlobalFiltering
title: Table_GlobalFiltering
---

定義元: [features/global-filtering/globalFilteringFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L69)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getGlobalAutoFilterFn {#getglobalautofilterfn}

```ts
getGlobalAutoFilterFn: () => FilterFn<TFeatures, TData> | undefined;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L76)

現在、この関数は組み込みのフィルター関数 `includesString` を返します。今後のリリースでは、渡されたデータの性質に応じて、より動的なフィルター関数を返すようになるかもしれません。

#### 戻り値 {#returns}

[`FilterFn`](FilterFn.md)\<`TFeatures`, `TData`\> \| `undefined`

***

### getGlobalFilterFn {#getglobalfilterfn}

```ts
getGlobalFilterFn: () => FilterFn<TFeatures, TData> | undefined;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:80](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L80)

グローバルフィルターのフィルター関数を返します（設定によって、利用者が定義したものか自動で決まったもののどちらかです）。

#### 戻り値 {#returns-1}

[`FilterFn`](FilterFn.md)\<`TFeatures`, `TData`\> \| `undefined`

***

### resetGlobalFilter {#resetglobalfilter}

```ts
resetGlobalFilter: (defaultState?) => void;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:86](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L86)

`globalFilter` を `initialState.globalFilter` に戻します。

`true` を渡すと、初期状態を無視して `undefined` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-2}

`void`

***

### setGlobalFilter {#setglobalfilter}

```ts
setGlobalFilter: (updater) => void;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:90](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L90)

次の値かアップデーター関数で、グローバルフィルターの状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

`any`

#### 戻り値 {#returns-3}

`void`
