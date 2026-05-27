# Harmony editor core
This is the core editor component of Harmony, our terminal based code editor. Now extracted and in minimal form for use in other projects. This consists of a legacy, simple editor core, and a new object oriented version to theoretially allow multiple instances of the editor to run simultaneously

# How do I?
The Harmony editor core comes with basic functionality, it can open files, write to them, and that's about it. any further functionality should be added to the extensions file, and we advise rewriting the printfilecore function as an extension as it is very basic. So if you do rewrite the printfilecore function, change all references to printfilecore to extensions.yourprintfile, and check the box at the top that should say:

`#Modified? []`

You'll notice the extensions file already contains a commands function, this is because we needed a way to process the `:q` command, so you can actually close the editor. But other than that, we have added absolutely nothing, not even a menu.