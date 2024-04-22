
<h2>Please visit my wiki link for full list of questions</h2>
<h3>https://github.com/mission-peace/interview/wiki</h3>

<h2> Like my facebook page for latest updates on my youtube channel</h2>
<h3>https://www.facebook.com/tusharroy25</h3>

<h2> Contribution </h2>
Please contribute to this repository to help it make better. Any change like new question, code improvement, doc improvement etc. is very welcome. Just send me a pull request and I will review the request and approve it if it looks good. 

<h2> How to use this repository </h2>

<h3> Softwares to install </h3>
* Install JDK8 https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html
* Install Git https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* Install either Intellij https://www.jetbrains.com/idea/download/
* If you like eclipse instead of intellij install eclipse https://eclipse.org/downloads/

<h3> Set up your desktop </h3>
* Pull the git repository. Go to command line and type git clone https://github.com/mission-peace/interview.git
* Go to root directory of checked out project.
* Run ./gradlew idea to generate idea related classes
* Fire up intellij. Go to Open. Go to git repo folder and open interview.ipr . On file menu go to project structure. Update language level support to 8
* If you use eclipse, do ./gradlew eclipse . This will generate eclipse related files. Go to eclipse and open up folder containing this repo.
* Go to any program and run that program
* Go to any test and run the junit test.
* Run ./gradlew build to create classes, run tests and create jar.


conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/

conda config --set show_channel_urls yes   # 设置搜索时显示通道地址

/*
 * Copyright (c) 2011, 2013, Oracle and/or its affiliates. All rights reserved.
 * Copyright (c) 2011, 2016, Red Hat, Inc.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 *
 */
#ifndef CPU_ZERO_VM_METHODHANDLES_ZERO_HPP
#define CPU_ZERO_VM_METHODHANDLES_ZERO_HPP
// Adapters
static unsigned int adapter_code_size() {
  return sizeof(ZeroEntry) * (Interpreter::method_handle_invoke_LAST - Interpreter::method_handle_invoke_FIRST + 1);
}
private:
  static oop popFromStack(TRAPS);
  static void invoke_target(methodOop method, TRAPS);
  static int method_handle_entry_invokeBasic(methodOop method, intptr_t UNUSED, TRAPS);
  static int method_handle_entry_linkToStaticOrSpecial(methodOop method, intptr_t UNUSED, TRAPS);
  static int method_handle_entry_linkToVirtual(methodOop method, intptr_t UNUSED, TRAPS);
  static int method_handle_entry_linkToInterface(methodOop method, intptr_t UNUSED, TRAPS);
  static int method_handle_entry_invalid(methodOop method, intptr_t UNUSED, TRAPS);
#endif // CPU_ZERO_VM_METHODHANDLES_ZERO_HPP

