---
id: LegacyReactTable
title: LegacyReactTable
---

```ts
type LegacyReactTable<TData> = ReactTable<LegacyFeatures, TData, TableState<LegacyFeatures>> & object;
```

定義元: [src/useLegacyTable.ts:290](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L290)

v8 スタイルの `getState()` メソッドを含む、レガシーなテーブルインスタンスの型です。

## 型宣言 {#type-declaration}

### ~~getState~~ {#getstate}

```ts
getState: () => TableState<LegacyFeatures>;
```

現在のテーブルの状態を返します。

#### 戻り値 {#returns}

`TableState`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md)\>

#### 非推奨 {#deprecated}

v9 では、`table.state` で状態に直接アクセスするか、状態全体が必要なら `table.state` を使ってください。

### ~~setState~~ {#setstate}

```ts
setState: (state) => void;
```

現在のテーブルの状態を設定します。

#### パラメーター {#parameters}

##### state {#state}

`TableState`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md)\>

#### 戻り値 {#returns-1}

`void`

#### 非推奨 {#deprecated-1}

v9 では、`table.baseAtoms` で状態に直接アクセスしてください。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 非推奨 {#deprecated-2}

代わりに、状態を明示的に選択する形で `useTable` を使ってください。
