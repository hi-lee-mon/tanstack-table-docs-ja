---
id: filterFns
title: filterFns
---

```ts
const filterFns: object;
```

定義元: [features/column-filtering/filterFns.ts:447](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L447)

組み込みのフィルター関数のレジストリです。

このオブジェクト全体を登録すると、ツリーシェイキングが効かなくなり、組み込みのフィルター関数がすべてバンドルに含まれます。
実際に使う `filterFn_*` 関数を import してそれだけを `filterFns` スロットに登録するか、列オプションの `filterFn` に直接渡すことをおすすめします。

## 型宣言 {#type-declaration}

### ~~arrHas~~ {#arrhas}

```ts
arrHas: CreatedFilterFn<any, any> = filterFn_arrHas;
```

### ~~arrIncludes~~ {#arrincludes}

```ts
arrIncludes: CreatedFilterFn<any, any> = filterFn_arrIncludes;
```

### ~~arrIncludesAll~~ {#arrincludesall}

```ts
arrIncludesAll: CreatedFilterFn<any, any> = filterFn_arrIncludesAll;
```

### ~~arrIncludesSome~~ {#arrincludessome}

```ts
arrIncludesSome: CreatedFilterFn<any, any> = filterFn_arrIncludesSome;
```

### ~~between~~ {#between}

```ts
between: CreatedFilterFn<any, any> = filterFn_between;
```

### ~~betweenInclusive~~ {#betweeninclusive}

```ts
betweenInclusive: CreatedFilterFn<any, any> = filterFn_betweenInclusive;
```

### ~~empty~~ {#empty}

```ts
empty: CreatedFilterFn<any, any> = filterFn_empty;
```

### ~~endsWith~~ {#endswith}

```ts
endsWith: CreatedFilterFn<any, any> = filterFn_endsWith;
```

### ~~equals~~ {#equals}

```ts
equals: CreatedFilterFn<any, any> = filterFn_equals;
```

### ~~equalsString~~ {#equalsstring}

```ts
equalsString: CreatedFilterFn<any, any> = filterFn_equalsString;
```

### ~~equalsStringSensitive~~ {#equalsstringsensitive}

```ts
equalsStringSensitive: CreatedFilterFn<any, any> = filterFn_equalsStringSensitive;
```

### ~~includesString~~ {#includesstring}

```ts
includesString: CreatedFilterFn<any, any> = filterFn_includesString;
```

### ~~includesStringSensitive~~ {#includesstringsensitive}

```ts
includesStringSensitive: CreatedFilterFn<any, any> = filterFn_includesStringSensitive;
```

### ~~inDateRange~~ {#indaterange}

```ts
inDateRange: CreatedFilterFn<any, any> = filterFn_inDateRange;
```

### ~~inNumberRange~~ {#innumberrange}

```ts
inNumberRange: CreatedFilterFn<any, any> = filterFn_inNumberRange;
```

### ~~notEmpty~~ {#notempty}

```ts
notEmpty: CreatedFilterFn<any, any> = filterFn_notEmpty;
```

### ~~startsWith~~ {#startswith}

```ts
startsWith: CreatedFilterFn<any, any> = filterFn_startsWith;
```

### ~~weakEquals~~ {#weakequals}

```ts
weakEquals: CreatedFilterFn<any, any> = filterFn_weakEquals;
```

## 非推奨 {#deprecated}

バンドルを小さくするには、代わりに `filterFn_*` 関数を個別に import してください。このエクスポートは今も動き、v9 でなくなる予定もありません。ただし、組み込みの名前の解決（`filterFn: 'auto'` を含みます）で見つかるのは、自分で登録した関数だけです。
