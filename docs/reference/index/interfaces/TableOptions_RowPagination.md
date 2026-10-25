---
id: TableOptions_RowPagination
title: TableOptions_RowPagination
---

定義元: [features/row-pagination/rowPaginationFeature.types.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L18)

## プロパティ {#properties}

### autoResetPageIndex? {#autoresetpageindex}

```ts
optional autoResetPageIndex?: boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L22)

`true` にすると、`data` の更新、フィルターの変更、グループ化の変更など、ページの内容を変える状態が変わったときに、ページネーションが最初のページに戻ります。

***

### manualPagination? {#manualpagination}

```ts
optional manualPagination?: boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L26)

手動のページネーションを有効にします。このオプションを `true` にすると、テーブルは `getPaginatedRowModel()` で行を自動でページ分割せず、テーブルに渡す前に行を自分でページ分割しておくことを前提にします。
サーバーサイドでページネーションと集計をする場合に便利です。

***

### onPaginationChange? {#onpaginationchange}

```ts
optional onPaginationChange?: OnChangeFn<PaginationState>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L32)

ページネーションの状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.pagination` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。

***

### pageCount? {#pagecount}

```ts
optional pageCount?: number;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:36](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L36)

ページネーションを手動で制御する場合、総ページ数がわかっていれば、`pageCount` としてテーブルに渡せます（`rowCount` を渡せば `pageCount` は計算されます）。ページ数がわからない場合は `-1` にできます。

***

### rowCount? {#rowcount}

```ts
optional rowCount?: number;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L40)

ページネーションを手動で制御する場合、総行数がわかっていれば、`rowCount` としてテーブルに渡せます。`pageCount` は、この値と `pageSize` から計算できます。
