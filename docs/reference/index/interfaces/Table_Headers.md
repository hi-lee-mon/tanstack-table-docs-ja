---
id: Table_Headers
title: Table_Headers
---

定義元: [core/headers/coreHeadersFeature.types.ts:8](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L8)

## 継承先 {#extended-by}

- [`Table_Core`](Table_Core.md)
- [`Table_Internal`](Table_Internal.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getFlatHeaders {#getflatheaders}

```ts
getFlatHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L25)

すべてのヘッダーグループにあるヘッダーを、すべて平坦化します。親のヘッダーとプレースホルダーのヘッダーも含みます。

#### 戻り値 {#returns}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getFooterGroups {#getfootergroups}

```ts
getFooterGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L20)

現在のヘッダーグループの順を逆にして、フッターグループを作ります。

#### 戻り値 {#returns-1}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getHeaderGroups {#getheadergroups}

```ts
getHeaderGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L16)

現在の列ツリー、表示の状態、固定の状態から、表示するヘッダーグループを作ります。

#### 戻り値 {#returns-2}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getLeafHeaders {#getleafheaders}

```ts
getLeafHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L29)

末端のヘッダーだけを集めます。親のヘッダー（グループヘッダー）は含みません。

#### 戻り値 {#returns-3}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]
