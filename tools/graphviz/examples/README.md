```bash
alias crdot 'dot -Tpng -o \!\!:1.png \!\!:1.dot && gthumb \!\!:1.png &'
```

## Commands to run from inside ipython interpreter

```ìpython
!pyreverse attributes -p attributes
!dot -Tpng -o attributes.png classes_attributes.dot
!cmd.exe /C start attributes.png
```
