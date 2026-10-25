---
id: TableOptions_RowSorting
title: TableOptions_RowSorting
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:216](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L216)

## プロパティ {#properties}

### autoResetSorting? {#autoresetsorting}

```ts
optional autoResetSorting?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:223](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L223)

`data` オプションが変わったときに、ソートを初期状態に戻します。

既定では無効です。`autoResetAll` を明示的に設定した場合は、そちらがこのオプションより優先されます。

***

### enableMultiRemove? {#enablemultiremove}

```ts
optional enableMultiRemove?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:227](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L227)

複数列ソートの切り替えで、列をソートの状態から取り除けるようにします。

***

### enableMultiSort? {#enablemultisort}

```ts
optional enableMultiSort?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:231](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L231)

テーブルの複数列ソートを有効または無効にします。

***

### enableSorting? {#enablesorting}

```ts
optional enableSorting?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:235](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L235)

テーブルのソートを有効または無効にします。

***

### enableSortingRemoval? {#enablesortingremoval}

```ts
optional enableSortingRemoval?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:241](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L241)

テーブルでソートを外せるかどうかを有効または無効にします。
- `true` の場合、ソート順は 'none' -> 'desc' -> 'asc' -> 'none' -> ... の順に切り替わります
- `false` の場合、ソート順は 'none' -> 'desc' -> 'asc' -> 'desc' -> 'asc' -> ... の順に切り替わります

***

### isMultiSortEvent? {#ismultisortevent}

```ts
optional isMultiSortEvent?: (e) => boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:245](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L245)

複数列ソートのイベントを起こすかどうかを判定するカスタム関数を渡します。関数にはソートの切り替えハンドラーのイベントが渡されます。複数列ソートにするべきイベントなら `true` を返してください。

#### パラメーター {#parameters}

##### e {#e}

`unknown`

#### 戻り値 {#returns}

`boolean`

***

### manualSorting? {#manualsorting}

```ts
optional manualSorting?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:249](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L249)

テーブルの手動のソートを有効にします。`true` の場合、テーブルに渡す前にデータを自分でソートしておく必要があります。サーバーサイドでソートする場合に便利です。

***

### maxMultiSortColCount? {#maxmultisortcolcount}

```ts
optional maxMultiSortColCount?: number;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:253](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L253)

複数列ソートできる列の最大数を指定します。

***

### onSortingChange? {#onsortingchange}

```ts
optional onSortingChange?: OnChangeFn<SortingState>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:259](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L259)

ソートの状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.sorting` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。

***

### sortDescFirst? {#sortdescfirst}

```ts
optional sortDescFirst?: boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:263](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L263)

`true` の場合、どのソートも最初の切り替えで降順になります。
