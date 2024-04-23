( cd  ./jdk/make && \
  make sanity all docs images JDK_TOPDIR=/opt/src/jdk7-master/jdk JDK_MAKE_SHARED_DIR=/opt/src/jdk7-master/jdk/make/common/shared EXTERNALSANITYCONTROL=true SOURCE_LANGUAGE_VERSION=7 TARGET_CLASS_VERSION=7 MILESTONE=internal BUILD_NUMBER=b00 JDK_BUILD_NUMBER=b00 FULL_VERSION=1.7.0-internal-root_2024_04_23_17_35-b00 PREVIOUS_JDK_VERSION=1.6.0 JDK_VERSION=1.7.0 JDK_MKTG_VERSION=7 JDK_MAJOR_VERSION=1 JDK_MINOR_VERSION=7 JDK_MICRO_VERSION=0 PREVIOUS_MAJOR_VERSION=1 PREVIOUS_MINOR_VERSION=6 PREVIOUS_MICRO_VERSION=0 ARCH_DATA_MODEL=32 COOKED_BUILD_NUMBER=0 ALT_OUTPUTDIR=/opt/src/jdk7-master/build/linux-aarch64 ALT_LANGTOOLS_DIST=/opt/src/jdk7-master/build/linux-aarch64/langtools/dist ALT_CORBA_DIST=/opt/src/jdk7-master/build/linux-aarch64/corba/dist ALT_JAXP_DIST=/opt/src/jdk7-master/build/linux-aarch64/jaxp/dist ALT_JAXWS_DIST=/opt/src/jdk7-master/build/linux-aarch64/jaxws/dist ALT_HOTSPOT_IMPORT_PATH=/opt/src/jdk7-master/build/linux-aarch64/hotspot/import BUILD_HOTSPOT=true ; )
make[2]: Entering directory '/opt/src/jdk7-master/jdk/make'
linux aarch64 1.7.0-internal build started: 24-04-23 17:35
Begin Processing SUBDIRS: tools java javax sun com    org sunw jpda mkdemo mksample launchers
make[3]: Entering directory '/opt/src/jdk7-master/jdk/make/tools'
Begin Processing SUBDIRS: addjsum buildmetaindex commentchecker compile_font_config compile_properties dir_diff dtdbuilder generate_break_iterator GenerateCharacter generatecurrencydata hasher_classes jarreorder jarsplit javazic jdwpgen makeclasslist strip_properties spp CharsetMapping generate_nimbus
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/addjsum'
=========================================================
BUILDTOOL:                addjsum
PACKAGE:                  build.tools.addjsum
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.addjsum.AddJsum
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/addjsum.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/addjsum'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/buildmetaindex'
=========================================================
BUILDTOOL:                buildmetaindex
PACKAGE:                  build.tools.buildmetaindex
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.buildmetaindex.BuildMetaIndex
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/buildmetaindex.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/buildmetaindex'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/commentchecker'
=========================================================
BUILDTOOL:                commentchecker
PACKAGE:                  build.tools.commentchecker
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.commentchecker.CommentChecker
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/commentchecker.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/commentchecker'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/compile_font_config'
=========================================================
BUILDTOOL:                compilefontconfig
PACKAGE:                  build.tools.compilefontconfig
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.compilefontconfig.CompileFontConfig
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/compilefontconfig.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/compile_font_config'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/compile_properties'
=========================================================
BUILDTOOL:                compileproperties
PACKAGE:                  build.tools.compileproperties
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.compileproperties.CompileProperties
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/compileproperties.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/compile_properties'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/dir_diff'
=========================================================
BUILDTOOL:                dirdiff
PACKAGE:                  build.tools.dirdiff
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.dirdiff.DirDiff
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/dirdiff.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/dir_diff'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/dtdbuilder'
=========================================================
BUILDTOOL:                dtdbuilder
PACKAGE:                  build.tools.dtdbuilder
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.dtdbuilder.DTDBuilder
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/dtdbuilder.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/dtdbuilder'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/generate_break_iterator'
=========================================================
BUILDTOOL:                generatebreakiteratordata
PACKAGE:                  build.tools.generatebreakiteratordata
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.generatebreakiteratordata.GenerateBreakIteratorData
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/generatebreakiteratordata.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/generate_break_iterator'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/GenerateCharacter'
=========================================================
BUILDTOOL:                generatecharacter
PACKAGE:                  build.tools.generatecharacter
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.generatecharacter.GenerateCharacter
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/generatecharacter.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/GenerateCharacter'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/generatecurrencydata'
=========================================================
BUILDTOOL:                generatecurrencydata
PACKAGE:                  build.tools.generatecurrencydata
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.generatecurrencydata.GenerateCurrencyData
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/generatecurrencydata.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/generatecurrencydata'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/hasher_classes'
=========================================================
BUILDTOOL:                hasher
PACKAGE:                  build.tools.hasher
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.hasher.Hasher
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/hasher.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/hasher_classes'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/jarreorder'
=========================================================
BUILDTOOL:                jarreorder
PACKAGE:                  build.tools.jarreorder
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.jarreorder.JarReorder
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/jarreorder.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/jarreorder'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/jarsplit'
=========================================================
BUILDTOOL:                jarsplit
PACKAGE:                  build.tools.jarsplit
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.jarsplit.JarSplit
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/jarsplit.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/jarsplit'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/javazic'
=========================================================
BUILDTOOL:                javazic
PACKAGE:                  build.tools.javazic
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.javazic.Main
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/javazic.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/javazic'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/jdwpgen'
=========================================================
BUILDTOOL:                jdwpgen
PACKAGE:                  build.tools.jdwpgen
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.jdwpgen.Main
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/jdwpgen.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/jdwpgen'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/makeclasslist'
=========================================================
BUILDTOOL:                makeclasslist
PACKAGE:                  build.tools.makeclasslist
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.makeclasslist.MakeClasslist
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/makeclasslist.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/makeclasslist'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/strip_properties'
=========================================================
BUILDTOOL:                stripproperties
PACKAGE:                  build.tools.stripproperties
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.stripproperties.StripProperties
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/stripproperties.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/strip_properties'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/spp'
=========================================================
BUILDTOOL:                spp
PACKAGE:                  build.tools.spp
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.spp.Spp
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/spp.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/spp'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/CharsetMapping'
=========================================================
BUILDTOOL:                charsetmapping
PACKAGE:                  build.tools.charsetmapping
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.charsetmapping.Main
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/charsetmapping.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/CharsetMapping'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/tools/generate_nimbus'
=========================================================
BUILDTOOL:                generatenimbus
PACKAGE:                  build.tools.generatenimbus
BUILDTOOL_SOURCE_ROOT:    ../../tools/src
BUILTTOOL_MAINCLASS:      build.tools.generatenimbus.Generator
BUILDTOOL_JAR_FILE:       /opt/src/jdk7-master/build/linux-aarch64/btjars/generatenimbus.jar
=========================================================
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools/generate_nimbus'
Done Processing SUBDIRS: addjsum buildmetaindex commentchecker compile_font_config compile_properties dir_diff dtdbuilder generate_break_iterator GenerateCharacter generatecurrencydata hasher_classes jarreorder jarsplit javazic jdwpgen makeclasslist strip_properties spp CharsetMapping generate_nimbus
make[3]: Leaving directory '/opt/src/jdk7-master/jdk/make/tools'
make[3]: Entering directory '/opt/src/jdk7-master/jdk/make/java'
Begin Processing SUBDIRS: version jvm redist verify fdlibm java sun_nio jli main zip security math util text net nio jar jexec awt applet beans  management npt java_crw_demo java_hprof_demo logging instrument invoke sql rmi
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/java/version'
make[4]: Nothing to be done for 'all'.
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/java/version'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/java/jvm'
make[4]: Nothing to be done for 'all'.
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/java/jvm'
make[4]: Entering directory '/opt/src/jdk7-master/jdk/make/java/redist'
Begin Processing SUBDIRS:  fonts    sajdi
make[5]: Entering directory '/opt/src/jdk7-master/jdk/make/java/redist/fonts'
make[5]: Nothing to be done for 'all'.
make[5]: Leaving directory '/opt/src/jdk7-master/jdk/make/java/redist/fonts'
make[5]: Entering directory '/opt/src/jdk7-master/jdk/make/java/redist/sajdi'
make[5]: Nothing to be done for 'all'.
make[5]: Leaving directory '/opt/src/jdk7-master/jdk/make/java/redist/sajdi'
Done Processing SUBDIRS:  fonts    sajdi
make[4]: *** No rule to make target '/opt/src/jdk7-master/build/linux-aarch64/hotspot/import/jre/lib/aarch64/server/libjvm.so', needed by '/opt/src/jdk7-master/build/linux-aarch64/lib/aarch64/server/libjvm.so'.  Stop.
make[4]: Leaving directory '/opt/src/jdk7-master/jdk/make/java/redist'
make[3]: *** [Makefile:63: all] Error 1
make[3]: Leaving directory '/opt/src/jdk7-master/jdk/make/java'
make[2]: *** [Makefile:247: all] Error 1
make[2]: Leaving directory '/opt/src/jdk7-master/jdk/make'
make[1]: *** [make/jdk-rules.gmk:79: jdk-build] Error 2
make[1]: Leaving directory '/opt/src/jdk7-master'
make: *** [Makefile:244: build_product_image] Error 2
