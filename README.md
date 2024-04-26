Only in jdk7-master/: .git
Only in jdk7-master/: build
Only in jdk7-master/: drop
diff -r jdk7-master-origin/hotspot/make/linux/Makefile jdk7-master/hotspot/make/linux/Makefile
238,240c238,240
< ifeq ($(DISABLE_HOTSPOT_OS_VERSION_CHECK)$(EMPTY_IF_NOT_SUPPORTED),)
< 	$(QUIETLY) >&2 echo "*** This OS is not supported:" `uname -a`; exit 1;
< endif
---
> #ifeq ($(DISABLE_HOTSPOT_OS_VERSION_CHECK)$(EMPTY_IF_NOT_SUPPORTED),)
> #	$(QUIETLY) >&2 echo "*** This OS is not supported:" `uname -a`; exit 1;
> #endif
diff -r jdk7-master-origin/hotspot/make/linux/makefiles/gcc.make jdk7-master/hotspot/make/linux/makefiles/gcc.make
89c89
< ARCHFLAG/i486    = -m32 -march=i586
---
> #ARCHFLAG/i486    = -m32 -march=i586
92c92
< ARCHFLAG/sparc   = -m32 -mcpu=v9
---
> #ARCHFLAG/sparc   = -m32 -mcpu=v9
127c127
< WARNINGS_ARE_ERRORS = -Werror
---
> WARNINGS_ARE_ERRORS = -Wno-all
diff -r jdk7-master-origin/hotspot/make/linux/makefiles/sparcWorks.make jdk7-master/hotspot/make/linux/makefiles/sparcWorks.make
36c36
< ARCHFLAG/i486    = -m32
---
> #ARCHFLAG/i486    = -m32
diff -r jdk7-master-origin/hotspot/make/linux/makefiles/vm.make jdk7-master/hotspot/make/linux/makefiles/vm.make
109c109
< LIBS += -lm -ldl -lpthread
---
> LIBS += -lm -ldl -lpthread -lffi
diff -r jdk7-master-origin/hotspot/make/linux/platform_zero.in jdk7-master/hotspot/make/linux/platform_zero.in
17c17
< sysdefs = -DLINUX -D_GNU_SOURCE -DCC_INTERP -DZERO -D@ZERO_ARCHDEF@ -DZERO_LIBARCH=\"@ZERO_LIBARCH@\"
---
> sysdefs = -DLINUX -D_GNU_SOURCE -DCC_INTERP -DZERO -DZERO_LIBARCH=\"@ZERO_LIBARCH@\" -std=c++98
diff -r jdk7-master-origin/hotspot/src/cpu/zero/vm/interpreterRT_zero.hpp jdk7-master/hotspot/src/cpu/zero/vm/interpreterRT_zero.hpp
29a30
> #include <ffi.h>
Only in jdk7-master/hotspot/src/cpu/zero/vm: methodHandles_zero.hpp
diff -r jdk7-master-origin/hotspot/src/os/linux/vm/os_linux.cpp jdk7-master/hotspot/src/os/linux/vm/os_linux.cpp
1867c1867,1869
<     {EM_68K,         EM_68K,     ELFCLASS32, ELFDATA2MSB, (char*)"M68k"}
---
>     {EM_68K,         EM_68K,     ELFCLASS32, ELFDATA2MSB, (char*)"M68k"},
>     {EM_SH,          EM_SH,      ELFCLASS32, ELFDATA2LSB, (char*)"SH"}, /* Support little endian only*/
>     {EM_AARCH64,     EM_AARCH64, ELFCLASS64, ELFDATA2LSB, (char*)"AARCH64"} /* Support little endian only*/
1897a1900,1903
>   #elif  (defined SH)
>     static  Elf32_Half running_arch_code=EM_SH;
>   #elif  (defined AARCH64)
>     static  Elf32_Half running_arch_code=EM_AARCH64;
1902a1909
> 
5248,5254d5254
< #ifndef __NR_fork
< #define __NR_fork IA32_ONLY(2) IA64_ONLY(not defined) AMD64_ONLY(57)
< #endif
< 
< #ifndef __NR_execve
< #define __NR_execve IA32_ONLY(11) IA64_ONLY(1033) AMD64_ONLY(59)
< #endif
5266,5269c5266,5270
<   // On IA64 there's no fork syscall, we have to use fork() and hope for
<   // the best...
<   pid_t pid = NOT_IA64(syscall(__NR_fork);)
<               IA64_ONLY(fork();)
---
> #ifdef SYS_fork
>   pid_t pid = syscall(SYS_fork);
> #else
>   pid_t pid = syscall(SYS_clone, SIGCHLD, 0, 0, 0, 0);
> #endif
5283,5286c5284
<     // IA64 should use normal execve() from glibc to match the glibc fork()
<     // above.
<     NOT_IA64(syscall(__NR_execve, "/bin/sh", argv, environ);)
<     IA64_ONLY(execve("/bin/sh", (char* const*)argv, environ);)
---
>     syscall(SYS_execve, "/bin/sh", argv, environ); 
diff -r jdk7-master-origin/hotspot/src/share/tools/hsdis/Makefile jdk7-master/hotspot/src/share/tools/hsdis/Makefile
73,76c73,76
< CFLAGS/i386	+= -m32
< CFLAGS/sparc	+= -m32
< CFLAGS/sparcv9	+= -m64
< CFLAGS/amd64	+= -m64
---
> #CFLAGS/i386	+= -m32
> #CFLAGS/sparc	+= -m32
> #CFLAGS/sparcv9	+= -m64
> #CFLAGS/amd64	+= -m64
diff -r jdk7-master-origin/hotspot/src/share/vm/code/dependencies.hpp jdk7-master/hotspot/src/share/vm/code/dependencies.hpp
161c161
<     all_types      = ((1<<TYPE_LIMIT)-1) & ((-1)<<FIRST_TYPE),
---
>     all_types      = ((1<<TYPE_LIMIT)-1) & ((~0u)<<FIRST_TYPE),
diff -r jdk7-master-origin/hotspot/src/share/vm/gc_implementation/g1/concurrentMark.cpp jdk7-master/hotspot/src/share/vm/gc_implementation/g1/concurrentMark.cpp
4545c4545
< #define G1PPRL_BYTE_FORMAT            "  "SIZE_FORMAT_W(9)
---
> #define G1PPRL_BYTE_FORMAT            "  " SIZE_FORMAT_W(9)
4551,4554c4551,4554
< #define G1PPRL_SUM_ADDR_FORMAT(tag)    "  "tag":"G1PPRL_ADDR_BASE_FORMAT
< #define G1PPRL_SUM_BYTE_FORMAT(tag)    "  "tag": "SIZE_FORMAT
< #define G1PPRL_SUM_MB_FORMAT(tag)      "  "tag": %1.2f MB"
< #define G1PPRL_SUM_MB_PERC_FORMAT(tag) G1PPRL_SUM_MB_FORMAT(tag)" / %1.2f %%"
---
> #define G1PPRL_SUM_ADDR_FORMAT(tag)    "  " tag ":" G1PPRL_ADDR_BASE_FORMAT
> #define G1PPRL_SUM_BYTE_FORMAT(tag)    "  " tag ": " SIZE_FORMAT
> #define G1PPRL_SUM_MB_FORMAT(tag)      "  " tag ": %1.2f MB"
> #define G1PPRL_SUM_MB_PERC_FORMAT(tag) G1PPRL_SUM_MB_FORMAT(tag) " / %1.2f %%"
diff -r jdk7-master-origin/hotspot/src/share/vm/oops/constantPoolOop.cpp jdk7-master/hotspot/src/share/vm/oops/constantPoolOop.cpp
272c272
<   if (cpool->cache() == NULL)  return false;  // nothing to load yet
---
>   if (cpool->cache() == NULL)  return (methodOop)false;  // nothing to load yet
diff -r jdk7-master-origin/hotspot/src/share/vm/prims/methodHandles.cpp jdk7-master/hotspot/src/share/vm/prims/methodHandles.cpp
228c228
< #ifdef TARGET_ARCH_NYI_6939861
---
> // #ifdef TARGET_ARCH_NYI_6939861
237c237
< #endif //TARGET_ARCH_NYI_6939861
---
> // #endif //TARGET_ARCH_NYI_6939861
diff -r jdk7-master-origin/hotspot/src/share/vm/prims/methodHandles.hpp jdk7-master/hotspot/src/share/vm/prims/methodHandles.hpp
718c718,734
<   static Symbol* convert_to_signature(oop type_str, bool polymorphic, TRAPS);
---
>   static Symbol* convert_to_signature(oop type_str, bool polymorphic, TRAPS);  
>   
>   static void get_ek_bound_mh_info(EntryKind ek, BasicType& arg_type, int& arg_mask, int& arg_slots) {
>     arg_type = ek_bound_mh_arg_type(ek);
>     arg_mask = 0;
>     arg_slots = type2size[arg_type];;
>   }
>   static void get_ek_adapter_opt_swap_rot_info(EntryKind ek, int& swap_bytes, int& rotate) {
>     int swap_slots = ek_adapter_opt_swap_slots(ek);
>     rotate = ek_adapter_opt_swap_mode(ek);
>     swap_bytes = swap_slots * Interpreter::stackElementSize;
>   }
>   static int get_ek_adapter_opt_spread_info(EntryKind ek) {
>     return ek_adapter_opt_spread_count(ek);
>   }
> 
> 
736c752
< #ifdef TARGET_ARCH_NYI_6939861
---
> // #ifdef TARGET_ARCH_NYI_6939861
748,761d763
<   static void get_ek_bound_mh_info(EntryKind ek, BasicType& arg_type, int& arg_mask, int& arg_slots) {
<     arg_type = ek_bound_mh_arg_type(ek);
<     arg_mask = 0;
<     arg_slots = type2size[arg_type];;
<   }
<   static void get_ek_adapter_opt_swap_rot_info(EntryKind ek, int& swap_bytes, int& rotate) {
<     int swap_slots = ek_adapter_opt_swap_slots(ek);
<     rotate = ek_adapter_opt_swap_mode(ek);
<     swap_bytes = swap_slots * Interpreter::stackElementSize;
<   }
<   static int get_ek_adapter_opt_spread_info(EntryKind ek) {
<     return ek_adapter_opt_spread_count(ek);
<   }
< 
774c776
< #endif //TARGET_ARCH_NYI_6939861
---
> // #endif //TARGET_ARCH_NYI_6939861
diff -r jdk7-master-origin/hotspot/src/share/vm/runtime/sharedRuntime.cpp jdk7-master/hotspot/src/share/vm/runtime/sharedRuntime.cpp
84c84
< RuntimeStub*        SharedRuntime::_wrong_method_blob;
---
> /*RuntimeStub*        SharedRuntime::_wrong_method_blob;
94c94,95
< SafepointBlob*      SharedRuntime::_polling_page_return_handler_blob;
---
> SafepointBlob*      SharedRuntime::_polling_page_return_handler_blob;*/
> RicochetBlob*       SharedRuntime::_ricochet_blob;
102c103
< void SharedRuntime::generate_stubs() {
---
> /*void SharedRuntime::generate_stubs() {
118c119
< }
---
> }*/
124c125,126
< #ifndef TARGET_ARCH_NYI_6939861
---
> // fy-change  
> /* #ifndef TARGET_ARCH_NYI_6939861
145c147
< #endif
---
> #endif */
diff -r jdk7-master-origin/hotspot/src/share/vm/utilities/exceptions.cpp jdk7-master/hotspot/src/share/vm/utilities/exceptions.cpp
226a227,241
> void Exceptions::throw_stack_overflow_exception(Thread* THREAD, const char* file, int line) {
>   Handle exception;
>   if (!THREAD->has_pending_exception()) {
>     klassOop k = SystemDictionary::StackOverflowError_klass();
>     oop e = instanceKlass::cast(k)->allocate_instance(CHECK);
>     exception = Handle(THREAD, e);  // fill_in_stack trace does gc
>     assert(instanceKlass::cast(k)->is_initialized(), "need to increase min_stack_allowed calculation");
>   } else {
>     // if prior exception, throw that one instead
>     exception = Handle(THREAD, THREAD->pending_exception());
>   }
>   _throw(THREAD, file, line, exception);
> }
> 
> 
diff -r jdk7-master-origin/hotspot/src/share/vm/utilities/exceptions.hpp jdk7-master/hotspot/src/share/vm/utilities/exceptions.hpp
147a148,150
>  
>  // fy 
>   static void throw_stack_overflow_exception(Thread* thread, const char* file, int line);
Only in jdk7-master/jdk: build
diff -r jdk7-master-origin/jdk/make/common/Subdirs.gmk jdk7-master/jdk/make/common/Subdirs.gmk
80,89c80,89
< define OTHERSUBDIRS-loop
< @$(ECHO) "Begin Processing OTHERSUBDIRS: $(OTHERSUBDIRS)"
< @for i in DUMMY $(OTHERSUBDIRS) ; do \
<   if [ "$$i" != "DUMMY" ] ; then \
<     $(MAKE) -C $$i $@ $(OTHERSUBDIRS_MAKEFLAGS) \
<             FULL_VERSION=$(FULL_VERSION) RELEASE=$(RELEASE) || exit 1; \
<   fi ; \
< done
< @$(ECHO) "Done Processing OTHERSUBDIRS: $(OTHERSUBDIRS)"
< endef
---
> #define OTHERSUBDIRS-loop
> #@$(ECHO) "Begin Processing OTHERSUBDIRS: $(OTHERSUBDIRS)"
> #@for i in DUMMY $(OTHERSUBDIRS) ; do \
> #  if [ "$$i" != "DUMMY" ] ; then \
> #    $(MAKE) -C $$i $@ $(OTHERSUBDIRS_MAKEFLAGS) \
> #            FULL_VERSION=$(FULL_VERSION) RELEASE=$(RELEASE) || exit 1; \
> #  fi ; \
> #done
> #@$(ECHO) "Done Processing OTHERSUBDIRS: $(OTHERSUBDIRS)"
> #endef
diff -r jdk7-master-origin/jdk/make/common/shared/Compiler-gcc.gmk jdk7-master/jdk/make/common/shared/Compiler-gcc.gmk
70c70
<   SHARED_LIBRARY_FLAG = -shared -mimpure-text
---
>   SHARED_LIBRARY_FLAG = -shared
Only in jdk7-master/jdk/make/java/main/java: mapfile-aarch64
diff -r jdk7-master-origin/jdk/src/share/classes/java/util/CurrencyData.properties jdk7-master/jdk/src/share/classes/java/util/CurrencyData.properties
108c108
< AZ=AZM;2005-12-31-20-00-00;AZN
---
> AZ=AZM;2015-12-31-20-00-00;AZN
377c377
< MZ=MZM;2006-06-30-22-00-00;MZN
---
> MZ=MZM;2016-06-30-22-00-00;MZN
439c439
< RO=ROL;2005-06-30-21-00-00;RON
---
> RO=ROL;2015-06-30-21-00-00;RON
529c529
< TR=TRL;2004-12-31-22-00-00;TRY
---
> TR=TRL;2015-12-31-22-00-00;TRY
555c555
< VE=VEB;2008-01-01-04-00-00;VEF
---
> VE=VEB;2018-01-01-04-00-00;VEF
diff -r jdk7-master-origin/jdk/src/share/classes/sun/util/calendar/ZoneInfoFile.java jdk7-master/jdk/src/share/classes/sun/util/calendar/ZoneInfoFile.java
789a790,791
> 	try {
> 	System.out.println("===========================================INTO getZoneAliases=====================================");
790a793
> 	System.out.println("****************buf is*****************"+buf.toString());
827a831,834
> 	} catch (Exception e) {
> 		System.err.println("FY ERROR FIND:"+e.getMessage());
> 		return null;
> 	}
diff -r jdk7-master-origin/jdk/src/share/native/com/sun/java/util/jar/pack/jni.cpp jdk7-master/jdk/src/share/native/com/sun/java/util/jar/pack/jni.cpp
183c183
<     return false;
---
>     return 0;
224c224
<     return false;
---
>     return 0;
diff -r jdk7-master-origin/langtools/make/build.properties jdk7-master/langtools/make/build.properties
71c71
< javac.lint.opts = -Xlint:all,-deprecation -Werror
---
> javac.lint.opts = -Xlint:all,-deprecation
