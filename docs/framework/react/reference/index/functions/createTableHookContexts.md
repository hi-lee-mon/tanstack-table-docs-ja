---
id: createTableHookContexts
title: createTableHookContexts
---

```ts
function createTableHookContexts<TFeatures, TData>(): TableHookContexts<TFeatures, TData>;
```

定義元: [src/createTableHookContexts.tsx:83](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L83)

[createTableHook](createTableHook.md) に渡せる、スコープを限定したテーブル・セル・ヘッダーのコンテキスト（と、それぞれに対応するコンテキストのフック）を新しく1組作ります。TanStack Form の `createFormHookContexts` にならった API です。

通常、これを使う必要は**ありません**。`createTableHook` はデフォルトで、`AppTable`・`AppCell`・`AppHeader` の各プロバイダーを、モジュールスコープで共有されるコンテキストに結び付けます。そのコンテキストは、`createTableHook` が返す `useTableContext`・`useCellContext`・`useHeaderContext` フックで読み取れます。`createTableHookContexts` を使うのは、*分離された*コンテキストが必要なときです。たとえば、テーブルの中に別のテーブルを入れ子にすると、そのままでは利用側が誤った（最も近い）プロバイダーを読み取ってしまう場合があります。

型安全性についての注意: ここで返されるフックの型は `TFeatures` だけをもとにしています。`createTableHook` で登録するコンポーネントのマップ（`tableComponents`・`cellComponents`・`headerComponents`）はあとから定義されるため、これらのフックはそれを**知りません**。最も詳しい型（`App*` コンポーネントと登録したコンポーネントが付いた型）がほしい場合は、`createTableHook` の呼び出しが返す `use*Context` フックを使ってください。ここで作るフックは、`createTableHook` の結果をインポートしない、またはできないモジュールからコンテキストを読み取るための抜け道（escape hatch）です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData` = `RowData`

## 戻り値 {#returns}

[`TableHookContexts`](../interfaces/TableHookContexts.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```tsx
// scoped-table-context.ts
export const {
  tableContext,
  cellContext,
  headerContext,
  useTableContext,
  useCellContext,
  useHeaderContext,
} = createTableHookContexts<typeof features>()

// table.ts
export const { useAppTable } = createTableHook({
  features,
  tableContext, // <- pass the scoped contexts so the providers use them
  cellContext,
  headerContext,
  tableComponents: { PaginationControls },
})
```
