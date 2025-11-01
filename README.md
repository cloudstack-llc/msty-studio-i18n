# Msty Internationalization (i18n)

Welcome to the **Msty Internationalization Repository**! This repository enables the global community to contribute translations for the Msty app, making it accessible to users around the world. 🌍

## Repository Structure

The root of this repository contains an `i18n` directory, which includes the following:

- **`locales` directory**: This is where all language files are stored. Each language has its own JSON file (e.g., `en_US.json`, `es_ES.json`).

### Example Structure
```
i18n/
└── locales/
    ├── en_US.json   // English strings (maintained by the Msty team)
    ├── es_ES.json   // Spanish strings (community contribution)
    ├── fr_FR.json   // French strings (community contribution)
    └── ...          // Add other language files here
```

## Contributing Translations

### 1. Locate `en_US.json`
The `en_US.json` file is the primary source of truth for all text in Msty. It is maintained by the Msty development team.

### 2. Copy and Translate
1. Copy the `en_US.json` file and save it with the appropriate language code (e.g., `de_DE.json` for German, `zh_CN.json` for Simplified Chinese).
2. Translate the strings in the new file while maintaining the same structure as `en_US.json`.

### 3. Submit Your Translation
Once your translation is complete:
1. Fork this repository.
2. Add your new language file under `i18n/locales/`.
3. Create a pull request for review.


## Guidelines for Translations

- **Preserve JSON Structure**: The structure of your translated file must exactly match `en_US.json`.
- **Maintain Accuracy**: Ensure translations are as accurate and contextually relevant as possible.
- **Use UTF-8 Encoding**: JSON files should use UTF-8 encoding to support all characters.

## Nuxt i18n and Vue i18n

Msty leverages [Nuxt i18n](https://i18n.nuxtjs.org/) and [Vue i18n](https://vue-i18n.intlify.dev/) for internationalization. While users don't need to know these specifics to contribute, the links are provided for reference.

## Ownership and Usage

Please note that Msty is not open source. By contributing to this repository, you agree that your translations will be used by the Msty team to enhance the app for global users.

---

Thank you for contributing to the Msty internationalization effort! Your help ensures that Msty can reach and support users worldwide. 🌟

> **Disclaimer**  
> The following German translation (`i18n/locales/de_DE.json`) was provided on an unpaid, volunteer basis. While every effort has been made to ensure accuracy and relevance, the contributor cannot guarantee that the file is error‑free or fully context‑appropriate. The contributor disclaims all liability for any mistakes, issues, or damages arising from the use of this translation. 👻
