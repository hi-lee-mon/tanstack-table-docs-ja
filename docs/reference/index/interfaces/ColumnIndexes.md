---
id: ColumnIndexes
title: ColumnIndexes
---

定義元: [features/column-ordering/columnOrderingFeature.types.ts:8](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L8)

## プロパティ {#properties}

### all {#all}

```ts
all: Record<string, number>;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:12](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L12)

表示中の各末端の列 ID を、表示中の全列の並びにおけるインデックスに対応付けます。

***

### center {#center}

```ts
center: Record<string, number>;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L16)

固定されていない表示中の各末端の列 ID を、中央領域内でのインデックスに対応付けます。

***

### end {#end}

```ts
end: Record<string, number>;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L24)

末尾に固定された表示中の各末端の列 ID を、末尾領域内でのインデックスに対応付けます。

***

### start {#start}

```ts
start: Record<string, number>;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L20)

先頭に固定された表示中の各末端の列 ID を、先頭領域内でのインデックスに対応付けます。
