#!/usr/bin/env python
# -*- coding::utf-8 -*-

import sys

def main():

    print('sys.version : %s' %  sys.version)
    print('\n')
    #print('sys.version_info : %s \n' % sys.version_info)
    print('sys.version_info : ', sys.version_info)
    print('\n')
    print('sys.hexversion : hex %x int %d' % (sys.hexversion, sys.hexversion) )
    print('\n')
    print('sys.implementation : %s' %  sys.implementation)
    print('\n')
    print('sys.byteorder : %s' % (sys.byteorder))
    print('\n')
    print('sys.getfilesystemencoding() : %s' % (sys.getfilesystemencoding()))
    print('\n')
    print('sys.maxsize : %d' % (sys.maxsize))
    print('\n')
    print('sys.maxunicode : %d' % (sys.maxunicode))
    print('\n')
    print('sys.thread_info :' ,(sys.thread_info))
    print('\n')
    print('sys.platform : %s' % (sys.platform))
    print('\n')
    print('sys.builtin_module_names : ' , (sys.builtin_module_names))
    print('\n')
    print('sys.abiflags : %s' % (sys.abiflags))
    print('\n')
    print('sys.int_info :' , (sys.int_info))
    print('\n')
    print('sys.float_info :' , (sys.float_info))
    print('\n')
    print('sys.prefix :' , (sys.prefix))
    print('\n')
    print('sys.base_prefix :' , (sys.base_prefix))
    print('\n')
    print('sys.exec_prefix :' , (sys.exec_prefix))
    print('\n')
    print('sys.base_exec_prefix :' , (sys.base_exec_prefix))
    print('\n')
    print('sys.executable :' , (sys.executable))
    print('\n')
    print('sys.getdefaultencoding :' , (sys.getdefaultencoding))
    print('\n')
    print('sys.path :' , (sys.path))
    print('\n')
    print('sys.flags :' , (sys.flags))
    print('\n')
    try:
        10 / 0
    except ZeroDivisionError:
        
        print('warning: 例外処理中に返り値の traceback をローカル変数に代入すると循環参照が発生します。')
        print('sys.exc_info() :' , (sys.exc_info()))
        print('\n')
        
        """
        last_type, last_value, last_traceback
        通常は定義されておらず、捕捉されない例外が発生してインタプリタがエラーメッセージとトレースバックを出力した場合にのみ設定されます。

        """
        #print('sys.last_type :' , (sys.last_type))
        #print('\n')
        #print('sys.last_value :' , (sys.last_value))
        #print('\n')
        #print('sys.last_traceback :' , (sys.last_traceback))
        #print('\n')
    
    obj = {}
    print('sys.getrefcount() :' , (sys.getrefcount(obj)))
    print('\n')
    print('sys.getsizeof() :' , (sys.getsizeof(obj)))
    print('\n')
    print('sys.hash_info :' , (sys.hash_info))
    print('\n')
    print('sys.modules :' , (sys.modules))
    print('\n')
    print('sys.argv :' , (sys.argv))
    print('\n')
    print('sys._xoptions :' , (sys._xoptions))
    print('\n')
    print('sys.stdin :' , (sys.stdin))
    print('\n')
    print('sys.stdout :' , (sys.stdout))
    print('\n')
    print('sys.stderr :' , (sys.stderr))
    print('\n')

if __name__ == '__main__':
    main()
