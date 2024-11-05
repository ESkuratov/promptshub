-----
TEASER PROMT



-----
VARS:

Replace the following shortcodes according to your needs:

* = Required


*[PROJECT_NAME]* = Name of product or features.
*[ROLE]* = A Role that use for create documents.
*[TEAM]* = Team name.
*[DOC_LANGUAGE]* = Language in which you want your story to be written | Example: French

--------
START OF PROMPT:

# Fast research audience

[PROJECT_NAME] = Онлайн ЧДП
[ROLE] = Product owner
[DOC_LANGUAGE] = Russian
[BRD] = BRD_ER_online_20.09.2024

As a [ROLE], create a Product Requirement Document for the project [PROJECT_NAME] using information from the file [BRD] Include the following elements:

## INSTRUCTIONS
1. Write Jobs To Be Done (JTBD) using the format from Example 1, focusing on the needs that the [PROJECT_NAME] project addresses, and prioritize them based on frequency.
2. Organize the list of JTBD into groups similar to Example 2, Example 3, and Example 4.

## Output Format
1. Provide your answers in [DOC_LANGUAGE]
2. Use a clear style and technical language.

## EXAMPLES

### Example 1. JTBD Format
```
Situation: When [describe the situation or context the user is in],
Job: I want to [describe the task or job the user wants to accomplish],
Outcome: So that [describe the desired outcome or benefit the user seeks].
```

### Example 2. Functional JTBD examples
```
Email management software: Imagine you’re overwhelmed with a flood of emails every day. You need a tool to efficiently sort, filter, and manage your inbox to stay organized and ensure you don’t miss important messages.
```

### Example 3. Social JTBD examples
```
Luxury watch: For many customers, a luxury watch is a status and success symbol. Wearing a high-end watch can help someone feel and appear prestigious among peers and colleagues.
```

### Example 4. Emotional JTBD examples
```
Installing a home security system not only protects physical property but also provides a sense of safety and peace of mind.
```