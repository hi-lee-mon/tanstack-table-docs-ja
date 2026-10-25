---
id: ValidateFeatureSlots
title: ValidateFeatureSlots
---

```ts
type ValidateFeatureSlots<TFeatures> = IsAny<TFeatures> extends true ? object : { [K in keyof TFeatures as K extends keyof FeatureSlotPrereqs ? K : never]: K extends keyof FeatureSlotPrereqs ? [Extract<FeatureSlotPrereqs[K], keyof TFeatures>] extends [never] ? `Error: '${K & string}' requires '${FeatureSlotPrereqs[K] & string}' to be included in this table's features.` : TFeatures[K] : never };
```

定義元: [types/TableFeatures.ts:161](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L161)

features オブジェクトの行モデルと関数レジストリのスロットそれぞれに、前提となる機能がそろっているかを検証します。

前提の機能が足りないスロットは、型がエラーメッセージのリテラルに置き換えられます。そのため、問題のプロパティは型チェックで失敗し、追加すべき機能の名前がメッセージに出ます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
