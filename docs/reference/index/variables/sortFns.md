---
id: sortFns
title: sortFns
---

```ts
const sortFns: object;
```

定義元: [features/row-sorting/sortFns.ts:361](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/sortFns.ts#L361)

組み込みのソート関数のレジストリです。

このオブジェクト全体を登録すると、ツリーシェイキングが効かなくなり、組み込みのソート関数がすべてバンドルに含まれます。
実際に使う `sortFn_*` 関数を import してそれだけを `sortFns` スロットに登録するか、列オプションの `sortFn` に直接渡すことをおすすめします。

## 型宣言 {#type-declaration}

### ~~alphanumeric~~ {#alphanumeric}

```ts
alphanumeric: CreatedSortFn<any, any> = sortFn_alphanumeric;
```

### ~~alphanumericCaseSensitive~~ {#alphanumericcasesensitive}

```ts
alphanumericCaseSensitive: CreatedSortFn<any, any> = sortFn_alphanumericCaseSensitive;
```

### ~~basic~~ {#basic}

```ts
basic: CreatedSortFn<any, any> = sortFn_basic;
```

### ~~datetime~~ {#datetime}

```ts
datetime: CreatedSortFn<any, any> = sortFn_datetime;
```

### ~~text~~ {#text}

```ts
text: CreatedSortFn<any, any> = sortFn_text;
```

### ~~textCaseSensitive~~ {#textcasesensitive}

```ts
textCaseSensitive: CreatedSortFn<any, any> = sortFn_textCaseSensitive;
```

## 非推奨 {#deprecated}

バンドルを小さくするには、代わりに `sortFn_*` 関数を個別に import してください。このエクスポートは今も動き、v9 でなくなる予定もありません。ただし、組み込みの名前の解決（`sortFn: 'auto'` を含みます）で見つかるのは、自分で登録した関数だけです。
