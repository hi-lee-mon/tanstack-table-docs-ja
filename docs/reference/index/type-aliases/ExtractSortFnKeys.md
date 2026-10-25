---
id: ExtractSortFnKeys
title: ExtractSortFnKeys
---

```ts
type ExtractSortFnKeys<TFeatures> = IsAny<TFeatures> extends true ?
  | keyof SortFns
  | BuiltInSortFn : TFeatures extends object ? Extract<keyof TSortFns, string> : keyof SortFns;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:106](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L106)

機能の組み合わせについて、`columnDef.sortFn` に指定できる文字列の名前を求めます。

features オブジェクトが `sortFns` レジストリを宣言している場合（`tableFeatures({ ..., sortFns })`）は、そのキーだけが有効な名前になります。実際にソート関数が登録されている名前だけを指定できます。
そうでなければ、グローバルに宣言のマージをした `SortFns` インターフェースが使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
