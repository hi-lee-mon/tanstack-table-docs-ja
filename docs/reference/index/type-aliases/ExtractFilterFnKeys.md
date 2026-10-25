---
id: ExtractFilterFnKeys
title: ExtractFilterFnKeys
---

```ts
type ExtractFilterFnKeys<TFeatures> = IsAny<TFeatures> extends true ?
  | keyof FilterFns
  | BuiltInFilterFn : TFeatures extends object ? Extract<keyof TFilterFns, string> : keyof FilterFns;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:165](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L165)

機能の組み合わせについて、`columnDef.filterFn` と `options.globalFilterFn` に指定できる文字列の名前を求めます。

features オブジェクトが `filterFns` レジストリを宣言している場合（`tableFeatures({ ..., filterFns })`）は、そのキーだけが有効な名前になります。実際にフィルター関数が登録されている名前だけを指定できます。
そうでなければ、グローバルに宣言のマージをした `FilterFns` インターフェースが使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
