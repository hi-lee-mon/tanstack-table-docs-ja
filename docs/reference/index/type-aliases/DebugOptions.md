---
id: DebugOptions
title: DebugOptions
---

```ts
type DebugOptions<TFeatures> = object & DebugKeysFor<CoreFeatures & TFeatures>;
```

定義元: [types/TableOptions.ts:52](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableOptions.ts#L52)

## 型宣言 {#type-declaration}

### debugAll? {#debugall}

```ts
optional debugAll?: boolean;
```

### debugCache? {#debugcache}

```ts
optional debugCache?: boolean;
```

### debugCells? {#debugcells}

```ts
optional debugCells?: boolean;
```

### debugColumns? {#debugcolumns}

```ts
optional debugColumns?: boolean;
```

### debugHeaders? {#debugheaders}

```ts
optional debugHeaders?: boolean;
```

### debugRows? {#debugrows}

```ts
optional debugRows?: boolean;
```

### debugTable? {#debugtable}

```ts
optional debugTable?: boolean;
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
