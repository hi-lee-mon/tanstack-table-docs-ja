---
id: getInitialTableState
title: getInitialTableState
---

```ts
function getInitialTableState<TFeatures>(features, initialState?): TableState<TFeatures>;
```

定義元: [core/table/constructTable.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/constructTable.ts#L18)

登録された機能と利用者が指定した初期状態から、テーブルの初期状態を組み立てます。

各機能が既定の状態を提供し、そのあとで利用者が指定した `initialState` の値がマージされます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

## パラメーター {#parameters}

### features {#features}

`TFeatures`

### initialState? {#initialstate}

  \| `Partial`\<[`TableState`](../type-aliases/TableState.md)\<`TFeatures`\>\>
  \| `undefined`

## 戻り値 {#returns}

[`TableState`](../type-aliases/TableState.md)\<`TFeatures`\>
