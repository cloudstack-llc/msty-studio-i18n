#!/bin/bash

# Check if node is available
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is required but not found."
    exit 1
fi

SOURCE_FILE="en_US.json"

if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file $SOURCE_FILE not found in current directory."
    exit 1
fi

echo "------------------------------------------------"
echo "Translation Validator"
echo "Source: $SOURCE_FILE"
echo "------------------------------------------------"
echo "Available translation files:"

# Hardcoded for this run as requested
TARGET_FILE="zh_CN.json"

if [ ! -f "$TARGET_FILE" ]; then
    echo "Error: Target file $TARGET_FILE not found."
    exit 1
fi

echo "------------------------------------------------"
echo "Validating '$TARGET_FILE' against '$SOURCE_FILE'..."

# Use Node.js for robust JSON parsing and deep key comparison
node -e '
const fs = require("fs");

const sourcePath = "'"$SOURCE_FILE"'";
const targetPath = "'"$TARGET_FILE"'";

try {
    const sourceContent = fs.readFileSync(sourcePath, "utf8");
    const targetContent = fs.readFileSync(targetPath, "utf8");

    // Handle empty files
    if (!sourceContent.trim()) throw new Error("Source file is empty");
    if (!targetContent.trim()) throw new Error("Target file is empty");

    const source = JSON.parse(sourceContent);
    const target = JSON.parse(targetContent);

    // Function to recursively get all keys (dot notation)
    function getKeys(obj, prefix = "") {
        let keys = [];
        for (const key in obj) {
            if (obj.hasOwnProperty(key)) {
                const newKey = prefix ? `${prefix}.${key}` : key;
                if (typeof obj[key] === "object" && obj[key] !== null && !Array.isArray(obj[key])) {
                    keys = keys.concat(getKeys(obj[key], newKey));
                } else {
                    keys.push(newKey);
                }
            }
        }
        return keys;
    }

    // Function to check if a key exists in an object (handling nested)
    function hasKey(obj, keyPath) {
        const keys = keyPath.split(".");
        let current = obj;
        for (const key of keys) {
            if (current === undefined || current === null || !Object.prototype.hasOwnProperty.call(current, key)) {
                return false;
            }
            current = current[key];
        }
        return true;
    }

    const sourceKeys = getKeys(source);
    const missingKeys = [];

    sourceKeys.forEach(key => {
        if (!hasKey(target, key)) {
            missingKeys.push(key);
        }
    });

    if (missingKeys.length === 0) {
        console.log("\n✅  SUCCESS: All keys from source are present in the target file.");
    } else {
        console.log(`\n❌  FAILURE: Found ${missingKeys.length} missing keys in ${targetPath}:`);
        console.log("------------------------------------------------");
        // Print first 50 missing keys to avoid spamming if many are missing
        const limit = 50;
        missingKeys.slice(0, limit).forEach(key => console.log(` - ${key}`));
        if (missingKeys.length > limit) {
            console.log(`... and ${missingKeys.length - limit} more.`);
        }
        console.log("------------------------------------------------");
        process.exit(1);
    }

} catch (e) {
    console.error("\n❌  ERROR: " + e.message);
    process.exit(1);
}
'
