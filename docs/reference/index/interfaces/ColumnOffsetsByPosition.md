---
id: ColumnOffsetsByPosition
title: ColumnOffsetsByPosition
---

定義元: [features/column-sizing/columnSizingFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L23)

## プロパティ {#properties}

### all {#all}

```ts
all: ColumnOffsets;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L27)

固定領域を考えずに、表示中のすべての末端の列で計算したオフセットです。

***

### center {#center}

```ts
center: ColumnOffsets;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L31)

中央（固定されていない）領域内でのオフセットです。

***

### end {#end}

```ts
end: ColumnOffsets;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L45)

論理的な末尾の固定領域内でのオフセットです。

LTR の言語やレイアウトでは、末尾はふつう右にあたります。RTL の言語やレイアウトでは、末尾はふつう左にあたります。

***

### start {#start}

```ts
start: ColumnOffsets;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L38)

論理的な先頭の固定領域内でのオフセットです。

LTR の言語やレイアウトでは、先頭はふつう左にあたります。RTL の言語やレイアウトでは、先頭はふつう右にあたります。
