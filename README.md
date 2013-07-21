# CSScomb for Sublime Text 2 & 3

## About

Tool for sorting CSS properties in specific order.

* Sorting CSS properties. The order of properties in the help of professionals
* Setting the order of CSS properties. Use the order to which you are accustomed to
* Parsing CSS in the tags ```<style>```, ```style="..."``` attribute. CSScomb find a CSS-code to other languages and will sort it
* Formatting style sheets does not change. Work as a singleline and multiline CSS
* Separation of CSS properties for the group. Separate groups of empty string if you want
* Full support CSS2/CSS2.1/CSS3/CSS4 ;) CSScomb ready for the advanced CSS-code

The algorithm of CSScomb simulates web-technologists actions upon working with
CSS-code to the limit. Usually to re-order code you move lines over each other
considering comments in the code, multilines records of property values, hacks
and everything that could be found in the real file. CSScomb reproduces these
actions for you. This means that the parser "thinks" as a person editing the
text, not as a blind robot parsing CSS.

For more info, online demo and tests see [http://csscomb.com](http://csscomb.com)


## The Requirements

CSScomb is written in pure PHP, without any external libraries or dependencies.
See details at [wiki](https://github.com/csscomb/CSScomb/wiki/Requirements).


## Plugin usage

Select code and press <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>c</kbd>  
  
Tip: Combine expand selection by indentation <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>j</kbd> with <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>c</kbd> to quickly  
select all rules for current css selector and sort them with csscomb.

## Custom sort order

Plugin allows to use your own sort order.  
  
To customize it do following:  
1. Open default sort order:  `Preferences` → `Package Settings` → `CSScomb` → `Sort Order – Default`  
2. Copy whole file content.  
3. Open user-defined sort order:  `Preferences` → `Package Settings` → `CSScomb` → `Sort Order – User`  
4. Paste in this file.  
5. Change order how you want.
6. Set `custom_sort_order` value to `true`

## Issues & bugs

[CSScomb tracker](https://github.com/csscomb/CSSComb/issues)


## Authors

CSScomb core: [miripiruni](https://github.com/miripiruni), [tonyganch](https://github.com/tonyganch)

Sublime plugin: [i-akhmadullin](https://github.com/i-akhmadullin)
