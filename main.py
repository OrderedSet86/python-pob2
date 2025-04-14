import os
import sys
from pathlib import Path

import lupa.lua51 as lupa


def main():
    print(f'Using {lupa.LuaRuntime().lua_implementation}')

    lua = lupa.LuaRuntime(unpack_returned_tuples=True)

    with open('src/HeadlessWrapper.lua', 'r') as f:
        launch_src = f.read()

    os.chdir('runtime/lua')

    for lib_path in Path().rglob('*.lua'):
        lib_import_name = f'{lib_path.parent}/{lib_path.stem}'
        print(f'Injecting lib dep {lib_import_name}')
        lua.require(lib_import_name)

    lua.execute(launch_src)
    

if __name__ == '__main__':
    main()
