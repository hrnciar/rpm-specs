%global _eclipsedir %{_prefix}/lib/eclipse

%global _build_id_links alldebug

%bcond_with bootstrap

# Change following to 0 to default to no remote support when building
# for the first time in a buildroot -- this is needed to build:
#  * eclipse-remote
# which all make circular dependencies on cdt
%if %{without bootstrap}
%global _enable_remote_support 1
%else
%global _enable_remote_support 0
%endif

Epoch: 2

%global eclipse_base            %{_datadir}/eclipse
%global cdt_snapshot            org.eclipse.cdt-CDT_9_11_1

%global _cdtstandalonedir       %{_prefix}/lib/cdt-stand-alone-debugger

# we don't want to either provide or require anything from the stand-alone debugger install dir
%global __provides_exclude_from ^%{_cdtstandalonedir}/.*$
%global __requires_exclude_from ^%{_cdtstandalonedir}/.*$

%ifarch s390x x86_64 aarch64 ppc64le
    %global eclipse_arch %{_arch}
%endif

# Desktop file information
%global app_name %{?app_name_prefix}%{!?app_name_prefix:Eclipse} C/C++ Debugger
%global app_exec %{?app_exec_prefix} cdtdebug

# Glassfish EE APIs that moved to jakarta namespace
%if 0%{?fedora} >= 33
%global _jakarta_activation jakarta.activation-api
%global _jakarta_annotations jakarta.annotation-api
%global _jakarta_el jakarta.el-api
%global _jakarta_servlet jakarta.servlet-api
%global _jakarta_jaxb jakarta.xml.bind-api
%global _jakarta_jsp_api javax.servlet.jsp-api
%global _jakarta_jsp org.glassfish.web.jakarta.servlet.jsp
%else
%global _jakarta_activation jakarta.activation-api
%global _jakarta_annotations javax.annotation-api
%global _jakarta_el javax.el-api
%global _jakarta_servlet javax.servlet-api
%global _jakarta_jaxb jaxb-api
%global _jakarta_jsp_api javax.servlet.jsp
%global _jakarta_jsp org.glassfish.web.javax.servlet.jsp
%endif

Summary:        Eclipse C/C++ Development Tools (CDT) plugin
Name:           eclipse-cdt
Version:        9.11.1
Release:        10%{?dist}
License:        EPL-2.0 and CPL
URL:            https://www.eclipse.org/cdt

Source0: https://git.eclipse.org/c/cdt/org.eclipse.cdt.git/snapshot/%{cdt_snapshot}.tar.xz

Source3: eclipse-cdt.desktop

# man-page for /usr/bin/cdtdebug
Source4: cdtdebug.man

# Following fixes cdtdebug.sh script to get proper platform filesystem plugin
Patch1: eclipse-cdt-cdtdebug.patch

# Following fixes Standalone Debugger config.ini file to use bundle symbolic names
Patch2: eclipse-cdt-config-ini.patch

# Following fixes Standalone Debugger README file to refer to /usr/bin/cdtdebug
Patch3: eclipse-cdt-cdtdebug-readme.patch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires: java-11-openjdk-devel
BuildRequires: make
BuildRequires: rsync
BuildRequires: gcc-c++
BuildRequires: tycho
BuildRequires: tycho-extras
BuildRequires: desktop-file-utils
BuildRequires: google-gson
%if 0%{?fedora} >= 33
BuildRequires: jaxb-api
BuildRequires: jaxb-impl
%else
BuildRequires: glassfish-jaxb-api
BuildRequires: glassfish-jaxb-runtime
%endif
BuildRequires: eclipse-egit
BuildRequires: eclipse-license2
BuildRequires: eclipse-platform
BuildRequires: eclipse-pde
BuildRequires: exec-maven-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: freemarker
%if %{_enable_remote_support}
BuildRequires: eclipse-remote >= 2.1.0
%endif

Requires:      gdb make gcc-c++
%if %{_enable_remote_support}
Requires:      autoconf automake libtool
Requires:      eclipse-remote >= 2.1.0
%endif

# Added in F31
Obsoletes:     %{name}-tests < 2:9.7.0-4
Obsoletes:     %{name}-parsers < 2:9.7.0-4
# Added in F32
Obsoletes:     %{name}-docker < 2:9.11.0-6

# Added in F32 - this package absorbed launchbar
Obsoletes: eclipse-launchbar < 1:2.5.0-2
Provides:  eclipse-launchbar = %{epoch}:%{version}-%{release}

Recommends:    eclipse-linuxtools-libhover
Recommends:    eclipse-cdt-llvm
Recommends:    eclipse-cdt-qt

%description
Eclipse features and plugins that are useful for C and C++ development.

%package native
Summary:        Eclipse C/C++ Development Tools (CDT) Natives
Requires:       eclipse-platform

%description native
Architecture specific parts of CDT.

%package llvm
Summary:        Eclipse C/C++ Development Tools (CDT) LLVM
Requires:       %{name} = %{epoch}:%{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       clang
Requires:       lldb
%endif

%description llvm
Optional llvm parsers for the CDT.

%package terminal
Summary:        Eclipse Terminal Plug-in
# Added in F32 - this package absorbed tm-terminal
Obsoletes: eclipse-tm-terminal < 4.5.200-2
Provides:  eclipse-tm-terminal = %{epoch}:%{version}-%{release}
Obsoletes: eclipse-tm-terminal-connectors < 4.5.200-2
Provides:  eclipse-tm-terminal-connectors = %{epoch}:%{version}-%{release}
Obsoletes: eclipse-tm-terminal-rse < 4.5.200-2
Provides:  eclipse-tm-terminal-rse = %{epoch}:%{version}-%{release}

%description terminal
An integrated Eclipse View for the local command prompt (console) or
remote hosts (SSH, Telnet, Serial).

%if %{_enable_remote_support}

%if 0%{?fedora}
%package arduino
Summary:        Arduino C++ Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description arduino
Extensions to support Arduino C++ projects in Eclipse.
%endif

%package qt
Summary:        QT C++ Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
#for new qt project to work out of the box
Requires:       pkgconfig(Qt5)
Requires:       pkgconfig(Qt5Qml)
Requires:       pkgconfig(Qt5Quick)
%endif

%description qt
Extensions to support Qt projects and objects in the indexer.

%endif

%package sdk
Summary:        Eclipse C/C++ Development Tools (CDT) SDK plugin
Requires:       %{name} = %{epoch}:%{version}-%{release}
# Added in F32 - this package absorbed tm-terminal
Obsoletes: eclipse-tm-terminal-sdk < 4.5.200-2
Provides:  eclipse-tm-terminal-sdk = %{epoch}:%{version}-%{release}

%description sdk
Source for Eclipse CDT for use within Eclipse.

%prep
%setup -q -n %{cdt_snapshot}

# get desktop info
mkdir desktop
cp %{SOURCE3} desktop

# handle man page
mkdir man
cp %{SOURCE4} man

%patch1 -p0
%patch2 -p1
%patch3 -p1

# Fix tycho target environment
TYCHO_ENV="<environment><os>linux</os><ws>gtk</ws><arch>%{eclipse_arch}</arch></environment>"
%pom_xpath_set "pom:configuration/pom:environments" "$TYCHO_ENV" . core/org.eclipse.cdt.core.linux debug/org.eclipse.cdt.debug.application.product

# Add secondary arch support if we are building there
%ifarch s390x aarch64
sed -i -e 's/linux.x86_64"/linux.%{eclipse_arch}"/g' pom.xml
pushd core
sed -i -e 's/linux.x86_64 /linux.%{eclipse_arch} /g' org.eclipse.cdt.core.native/plugin.properties
sed -i -e 's/\\(x86_64\\)/(%{eclipse_arch})/g' org.eclipse.cdt.core.native/plugin.properties
cp -r org.eclipse.cdt.core.linux.x86_64 org.eclipse.cdt.core.linux.%{eclipse_arch}
rm -fr org.eclipse.cdt.core.linux.x86_64
pushd org.eclipse.cdt.core.linux.%{eclipse_arch}
mv os/linux/x86_64 os/linux/%{eclipse_arch}
popd
sed -i -e 's/x86_64/%{eclipse_arch}/g' org.eclipse.cdt.core.linux/pom.xml org.eclipse.cdt.core.linux.%{eclipse_arch}/{pom.xml,META-INF/MANIFEST.MF}
popd
sed -i -e 's/"org.eclipse.cdt.core.linux.x86_64"/"org.eclipse.cdt.core.linux.%{eclipse_arch}"/g' \
       -e 's/arch="x86_64"/arch="%{eclipse_arch}"/' releng/org.eclipse.cdt.native-feature/feature.xml
sed -i -e "s|org.eclipse.cdt.core.linux.x86_64</module>|org.eclipse.cdt.core.linux.%{eclipse_arch}</module>|g" pom.xml

# Ensure serial can be built on current arch
sed -i -e 's|linux/x86_64/|linux/%{eclipse_arch}/|' \
  native/org.eclipse.cdt.native.serial/jni/Makefile
sed -i -e 's/x86_64/%{eclipse_arch}/' \
  native/org.eclipse.cdt.native.serial/pom.xml
%endif

# Ensure correct platform fragments appear in config.ini ...
sed -i -e 's/x86_64/%{eclipse_arch}/' \
  debug/org.eclipse.cdt.debug.application.product/debug.product
# ... then remove fragments on platforms they aren't shipped
%ifarch s390x aarch64 ppc64le
sed -i '/filesystem.linux.%{eclipse_arch}/d' \
  debug/org.eclipse.cdt.debug.application.product/debug.product
sed -i '/net.linux.%{eclipse_arch}/d' \
  debug/org.eclipse.cdt.debug.application.product/debug.product
%endif

# Force the arch-specific plug-ins to be dir-shaped so that binary stripping works and the native files
# aren't loaded into the user.home .eclipse configuration
echo "Eclipse-BundleShape: dir" >> core/org.eclipse.cdt.core.linux.%{eclipse_arch}/META-INF/MANIFEST.MF
echo "Eclipse-BundleShape: dir" >> native/org.eclipse.cdt.native.serial/META-INF/MANIFEST.MF
sed -i -e '/library/s/library\//library\/*.c,library\/*.h,library\/Makefile/' \
  core/org.eclipse.cdt.core.linux/build.properties

# Remove pre-built natives
rm -rf native/org.eclipse.cdt.native.serial/os/* \
       core/org.eclipse.cdt.core.linux.*/os/*
mkdir -p native/org.eclipse.cdt.native.serial/os/linux/%{eclipse_arch} \
         core/org.eclipse.cdt.core.linux.%{eclipse_arch}/os/linux/%{eclipse_arch}

# Don't use the target configuration
%pom_disable_module releng/org.eclipse.cdt.target
%pom_xpath_remove "pom:configuration/pom:target"

# Don't need to build the p2 repos
%pom_disable_module releng/org.eclipse.cdt.repo
%pom_disable_module releng/org.eclipse.cdt.testing.repo

# Disable the jgit provider and force default packaging
%pom_remove_plugin org.eclipse.tycho:tycho-packaging-plugin

# Unnecessary plugins for RPM builds
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# Disable unneeded additional parsers
sed -i -e '/<module>upc\//d' pom.xml
sed -i -e '/<module>lrparser\//d' pom.xml
sed -i -e '/<module>xlc\//d' pom.xml

# Don't build and ship test bundles
%pom_disable_module launchbar/org.eclipse.launchbar.core.tests
%pom_disable_module launchbar/org.eclipse.launchbar.ui.tests
%pom_disable_module org.eclipse.tm.terminal.test terminal/plugins
%pom_disable_module build/org.eclipse.cdt.autotools.tests
%pom_disable_module build/org.eclipse.cdt.autotools.ui.tests
%pom_disable_module build/org.eclipse.cdt.cmake.ui.tests
%pom_disable_module build/org.eclipse.cdt.make.core.tests
%pom_disable_module build/org.eclipse.cdt.make.ui.tests
%pom_disable_module build/org.eclipse.cdt.managedbuilder.core.tests
%pom_disable_module build/org.eclipse.cdt.managedbuilder.ui.tests
%pom_disable_module build/org.eclipse.cdt.meson.ui.tests
%pom_disable_module codan/org.eclipse.cdt.codan.checkers.ui.tests
%pom_disable_module codan/org.eclipse.cdt.codan.core.tests
%pom_disable_module core/org.eclipse.cdt.core.tests
%pom_disable_module core/org.eclipse.cdt.ui.tests
%pom_disable_module dsf-gdb/org.eclipse.cdt.dsf.gdb.multicorevisualizer.ui.tests
%pom_disable_module dsf-gdb/org.eclipse.cdt.dsf.gdb.tests
%pom_disable_module dsf-gdb/org.eclipse.cdt.tests.dsf.gdb
%pom_disable_module jtag/org.eclipse.cdt.debug.gdbjtag.core.tests
%pom_disable_module lsp/org.eclipse.cdt.lsp.core.tests
%pom_disable_module qt/org.eclipse.cdt.qt.ui.tests
%pom_disable_module windows/org.eclipse.cdt.msw.build.tests
%pom_disable_module testsrunner/org.eclipse.cdt.testsrunner.tests
%pom_disable_module releng/org.eclipse.cdt.testing
%pom_disable_module releng/org.eclipse.cdt.testing-feature

# Don't build and ship docker support
%pom_disable_module launch/org.eclipse.cdt.docker.launcher
%pom_disable_module launch/org.eclipse.cdt.docker.launcher-feature

# Disable autotools, and remote features if we are building a boot-strap build
%if ! %{_enable_remote_support}
%pom_disable_module org.eclipse.tm.terminal.connector.remote.feature terminal/features
%pom_disable_module org.eclipse.tm.terminal.connector.remote terminal/plugins
%pom_disable_module launchbar/org.eclipse.launchbar.remote
%pom_disable_module launchbar/org.eclipse.launchbar.remote.core
%pom_disable_module launchbar/org.eclipse.launchbar.remote.ui
%pom_disable_module build/org.eclipse.cdt.autotools.core
%pom_disable_module build/org.eclipse.cdt.autotools.docs
%pom_disable_module build/org.eclipse.cdt.autotools.ui
%pom_disable_module build/org.eclipse.cdt.autotools-feature
%pom_disable_module build/org.eclipse.cdt.cmake.core
%pom_disable_module build/org.eclipse.cdt.cmake.ui
%pom_disable_module build/org.eclipse.cdt.cmake-feature
%pom_disable_module debug/org.eclipse.cdt.debug.application
%pom_disable_module debug/org.eclipse.cdt.debug.application.product
%pom_disable_module debug/org.eclipse.cdt.debug.standalone-feature
%pom_disable_module cross/org.eclipse.cdt.launch.remote
%pom_disable_module cross/org.eclipse.cdt.launch.remote-feature
%pom_disable_module remote/org.eclipse.cdt.remote.core
%pom_disable_module qt/org.eclipse.cdt.qt.core
%pom_disable_module qt/org.eclipse.cdt.qt.ui
%pom_disable_module qt/org.eclipse.cdt.qt-feature
%pom_disable_module toolchains/arduino/org.eclipse.cdt.arduino.core
%pom_disable_module toolchains/arduino/org.eclipse.cdt.arduino.ui
%pom_disable_module toolchains/arduino/org.eclipse.cdt.arduino-feature
%pom_disable_module releng/org.eclipse.cdt.sdk
%pom_disable_module releng/org.eclipse.cdt.sdk-feature
%else
# Always disable arduino support on rhel
%if ! 0%{?fedora}
%pom_disable_module toolchains/arduino/org.eclipse.cdt.arduino.core
%pom_disable_module toolchains/arduino/org.eclipse.cdt.arduino.ui
%pom_disable_module toolchains/arduino/org.eclipse.cdt.arduino-feature
%endif
%endif

# Disable all bundles not relavent to the platform we currently building
for b in `ls core/ | grep -P -e 'org.eclipse.cdt.core\.(?!linux\.%{eclipse_arch}$|tests$|linux$|native$)'` ; do
  module=$(grep ">core/$b<" pom.xml || :)
  if [ -n "$module" ] ; then
    %pom_disable_module "core/$b"
    %pom_xpath_remove "plugin[@id='$b']" releng/org.eclipse.cdt.native-feature/feature.xml
  fi
done

# Disable meson (missing dep tm4e)
%pom_disable_module build/org.eclipse.cdt.meson.core
%pom_disable_module build/org.eclipse.cdt.meson.docs
%pom_disable_module build/org.eclipse.cdt.meson.ui
%pom_disable_module build/org.eclipse.cdt.meson.ui.editor
%pom_disable_module build/org.eclipse.cdt.meson-feature

# Disable lsp4e (missing dep)
%pom_disable_module lsp/org.eclipse.cdt.lsp.core
%pom_disable_module lsp/org.eclipse.cdt.lsp.ui
%pom_disable_module lsp/org.eclipse.cdt.lsp-feature
%pom_disable_module debug/org.eclipse.cdt.debug.dap
%pom_disable_module debug/org.eclipse.cdt.debug.dap-feature
%pom_disable_module jtag/org.eclipse.cdt.debug.dap.gdbjtag
%pom_disable_module jtag/org.eclipse.cdt.debug.dap.gdbjtag-feature

# Disable examples
%pom_disable_module visualizer/org.eclipse.cdt.visualizer.examples
%pom_disable_module dsf/org.eclipse.cdt.examples.dsf
%pom_disable_module dsf/org.eclipse.cdt.examples.dsf.pda
%pom_disable_module dsf/org.eclipse.cdt.examples.dsf.pda.ui
%pom_disable_module dsf/org.eclipse.cdt.examples.dsf-feature
%pom_disable_module dsf-gdb/org.eclipse.cdt.examples.dsf.gdb

# Fix freemarker dep
sed -i -e 's/org.freemarker/org.freemarker.freemarker/' \
  qt/org.eclipse.cdt.qt.core/META-INF/MANIFEST.MF \
  tools.templates/org.eclipse.tools.templates.freemarker/META-INF/MANIFEST.MF \
  build/org.eclipse.cdt.cmake.core/META-INF/MANIFEST.MF \
  debug/org.eclipse.cdt.debug.application.product/debug.product

# Fix deps javax -> jakarta
sed -i -e 's/>javax.annotation</>%{_jakarta_annotations}</' -e 's/"javax.annotation"/"%{_jakarta_annotations}"/' \
       -e 's/"javax.activation"/"%{_jakarta_activation}"/' -e 's/"javax.el"/"%{_jakarta_el}"/' -e 's/"javax.servlet"/"%{_jakarta_servlet}"/' \
       -e 's/"javax.servlet.jsp"/"%{_jakarta_jsp_api}"/' -e 's/"org.apache.jasper.glassfish"/"%{_jakarta_jsp}"/' \
  doc/org.eclipse.cdt.doc.isv/pom.xml \
  debug/org.eclipse.cdt.debug.application.product/debug.product

# Fix jaxb dep javax -> jakarta
sed -i -e 's/com.sun.xml.bind/com.sun.xml.bind.jaxb-impl/' \
  tools.templates/org.eclipse.tools.templates.freemarker/META-INF/MANIFEST.MF \
  debug/org.eclipse.cdt.debug.application.product/debug.product
sed -i -e 's/javax.xml.bind/%{_jakarta_jaxb}/' \
  tools.templates/org.eclipse.tools.templates.freemarker/build.properties \
  debug/org.eclipse.cdt.debug.application.product/debug.product

# Relax the version constraint of the gson dep
sed -i -e '/com.google.gson/s/;\(bundle-\)\?version=".*"//' \
  jtag/org.eclipse.cdt.debug.dap.gdbjtag/META-INF/MANIFEST.MF build/org.eclipse.cdt.managedbuilder.core/META-INF/MANIFEST.MF

%mvn_package "::pom::" __noinstall
%mvn_package "::jar:sources{,-feature}:" sdk
%mvn_package :*.sdk sdk
%mvn_package :*.doc.isv sdk
%mvn_package ":org.eclipse.cdt.core{,.native,.linux,.linux.%{eclipse_arch}}" native
%mvn_package ":org.eclipse.cdt.native{,.serial}" native
%mvn_package ":*.testsrunner*"
%mvn_package :org.eclipse.tools.templates.*
%mvn_package :org.eclipse.cdt.arduino* arduino
%mvn_package :org.eclipse.tm.terminal* terminal
%mvn_package ":org.eclipse.cdt.{managedbuilder.llvm,llvm.dsf}*" llvm
%mvn_package :org.eclipse.cdt.qt* qt
%mvn_package :org.eclipse.cdt.cmake* qt
%mvn_package :org.eclipse.cdt*
%mvn_package :org.eclipse.launchbar*

%build
export JAVA_HOME=%{_jvmdir}/java-11

export CFLAGS="${CFLAGS:-%__global_cflags}"
export LDFLAGS="${LDFLAGS:-%__global_ldflags}"

# Avoid running out of heap on s390x
export MAVEN_OPTS="-Xmx1024m"

# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +%Y%m%d%H%M)
%mvn_build -j -f -- -Dtycho.local.keepTarget -Dnative=linux.%{eclipse_arch} -DforceContextQualifier=$QUALIFIER \
  -Pbuild-standalone-debugger-rcp

%install
%mvn_install

# Avoid unnecessary dep on java-headless 11 due to Java 11 specific fragment
sed -i 's/>11</>1.8</' %{buildroot}/%{_datadir}/maven-metadata/*.xml

%if %{_enable_remote_support}
# We don't build the standalone debugger in bootstrap mode

binInstallDir=%{buildroot}/%{_bindir}
install -d -m755 $binInstallDir

libInstallDir=%{buildroot}/%{_cdtstandalonedir}
install -d -m755 $libInstallDir

#standalone debugger - copy it into right location
rsync -vrpl debug/org.eclipse.cdt.debug.application.product/target/products/org.eclipse.cdt.debug.application.product/linux/gtk/%{eclipse_arch}/cdt-stand-alone-debugger \
    %{buildroot}%{_prefix}/lib

# Symlink cdtdebug binary
pushd %{buildroot}%{_bindir}
    ln -s %{_cdtstandalonedir}/cdtdebug
popd

# Use distro-specific working dir to avoid clashing with upstream
%if 0%{?rhel}
sed -i -e '/-data/i-configuration' -e '/-data/i@user.home\/rhcdtdebugger' \
       -e 's/@noDefault/@user.home\/workspace-rhcdtdebug/' %{buildroot}%{_cdtstandalonedir}/cdtdebug.ini
%else
sed -i -e '/-data/i-configuration' -e '/-data/i@user.home\/fcdtdebugger' \
       -e 's/@noDefault/@user.home\/workspace-fcdtdebug/' %{buildroot}%{_cdtstandalonedir}/cdtdebug.ini
%endif

%endif

# Install icons for standalone debugger
install -D debug/org.eclipse.cdt.debug.application/icons/cc32.png \
    %{buildroot}/usr/share/icons/hicolor/32x32/apps/%{name}.png
install -D debug/org.eclipse.cdt.debug.application/icons/cc48.png \
    %{buildroot}/usr/share/icons/hicolor/48x48/apps/%{name}.png
install -D debug/org.eclipse.cdt.debug.application/icons/cc128.png \
    %{buildroot}/usr/share/icons/hicolor/128x128/apps/%{name}.png
install -D debug/org.eclipse.cdt.debug.application/icons/cc.png \
    %{buildroot}/usr/share/icons/hicolor/256x256/apps/%{name}.png
install -d %{buildroot}/usr/share/pixmaps
ln -s /usr/share/icons/hicolor/256x256/apps/%{name}.png \
    %{buildroot}/usr/share/pixmaps/%{name}.png

# Fix permissions on native libraries
find %{buildroot} -name *.so -exec chmod +x {} \;

# Install desktop file
sed -i -e 's|Exec=cdtdebug|Exec=%{app_exec}|g' desktop/eclipse-cdt.desktop
sed -i -e 's|Name=Eclipse.*|Name=%{app_name}|g' desktop/eclipse-cdt.desktop
sed -i -e "s|Icon=eclipse|Icon=%{name}|g" desktop/eclipse-cdt.desktop
install -D desktop/eclipse-cdt.desktop %{buildroot}/usr/share/applications/%{name}.desktop
desktop-file-validate %{buildroot}/usr/share/applications/%{name}.desktop

# Install man page
install -D -m 644 man/cdtdebug.man %{buildroot}/%{_mandir}/man1/cdtdebug.1

%files -f .mfiles
%if %{_enable_remote_support}
%{_bindir}/cdtdebug
%{_cdtstandalonedir}/*
%endif
/usr/share/applications/*
/usr/share/pixmaps/*
/usr/share/icons/*/*/apps/*
%{_mandir}/man1/cdtdebug.1*
%license releng/org.eclipse.cdt.sdk/epl-v20.html

%files native -f .mfiles-native
%license releng/org.eclipse.cdt.sdk/epl-v20.html

%files sdk -f .mfiles-sdk
%license releng/org.eclipse.cdt.sdk/epl-v20.html

%files llvm -f .mfiles-llvm
%license releng/org.eclipse.cdt.sdk/epl-v20.html

%files terminal -f .mfiles-terminal
%license releng/org.eclipse.cdt.sdk/epl-v20.html

%if %{_enable_remote_support}

%files qt -f .mfiles-qt
%license releng/org.eclipse.cdt.sdk/epl-v20.html

%if 0%{?fedora}
%files arduino -f .mfiles-arduino
%license releng/org.eclipse.cdt.sdk/epl-v20.html
%endif

%endif

%changelog
* Wed Aug 26 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-10
- Rebuild against new jakarta-jsp packages

* Mon Aug 24 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-9
- Fix build against new jakarta packages

* Sun Aug 16 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-8
- Add missing obsoletes for tm-terminal-rse

* Fri Aug 14 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-7
- Fix unnecessary Java 11 dep from this package due to Java 11 specific bundle
  fragment

* Tue Aug 11 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-6
- Fix build against updated jaxb packages
- Force build against Java 11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:9.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-4
- Non bootstrap build

* Wed Jul 22 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-3
- Fix inconsistent buildroot macro usage

* Mon Jul 20 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-2
- Enable bootstrap mode and misc other improvements

* Thu Jun 25 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.1-1
- Update to latest upstream release

* Sun May 17 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-7
- Remove explicit dep on hamcrest

* Wed May 06 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-6
- Drop docker tooling support

* Thu Mar 26 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-5
- Fix bootstrap mode

* Tue Mar 24 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-4
- Add epoch to obsoletes for launchbar package

* Tue Mar 24 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-3
- Really fix obsoletes on tm-terminal

* Tue Mar 24 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-2
- Fix obsoletes on tm-terminal

* Mon Mar 23 2020 Mat Booth <mat.booth@redhat.com> - 2:9.11.0-1
- Update to latest upstream release

* Mon Jan 06 2020 Mat Booth <mat.booth@redhat.com> - 2:9.10.0-1
- Update to latest upstream release

* Mon Sep 16 2019 Mat Booth <mat.booth@redhat.com> - 2:9.9.0-1
- Update to latest upstream release

* Wed Jun 19 2019 Mat Booth <mat.booth@redhat.com> - 2:9.8.0-1
- Update to latest upstream release

* Sun Jun 09 2019 Mat Booth <mat.booth@redhat.com> - 2:9.7.0-5
- Enable further bundles during bootstrap

* Sat Jun 08 2019 Mat Booth <mbooth@apache.org> - 2:9.7.0-4
- Allow building debug bundles in bootstrap mode

* Wed Jun 05 2019 Mat Booth <mat.booth@redhat.com> - 2:9.7.0-3
- Drop support for parsers for compilers that are not shipped by Fedora

* Fri May 10 2019 Mat Booth <mat.booth@redhat.com> - 2:9.7.0-2
- Don't build and ship test bundles
- Use proper jaxb implementation

* Thu Mar 14 2019 Mat Booth <mat.booth@redhat.com> - 2:9.7.0-1
- Update to 2019-03 release
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:9.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Mat Booth <mat.booth@redhat.com> - 2:9.6.0-4
- Patch to avoid requesting GTK2 as SWT backend
- Fix unexpected workspace directory change

* Tue Jan 08 2019 Mat Booth <mat.booth@redhat.com> - 2:9.6.0-3
- Ensure the native subpackage brings in the Eclipse Platform package

* Mon Jan 07 2019 Mat Booth <mat.booth@redhat.com> - 2:9.6.0-2
- Update to tagged sources and add patch for QT test runners problem
- Fix some build issues
- Avoid unintentional dependency on Java 11

* Tue Dec 11 2018 Mat Booth <mat.booth@redhat.com> - 2:9.6.0-1
- Update to 2018-12 release
- Switch to EPL 2.0 license

* Mon Oct 22 2018 Jeff Johnston <jjohnstn@redhat.com> - 2:9.5.3-6
- Remove generated build-ids from main package.

* Wed Oct 17 2018 Jeff Johnston <jjohnstn@redhat.com> - 2:9.5.3-5
- Remove provides/requires from CDT standalone debugger

* Tue Oct 09 2018 Jeff Johnston <jjohnstn@redhat.com> - 2:9.5.3-4
- Build the CDT standalone debugger as an RCP application and package

* Thu Oct 04 2018 Mat Booth <mat.booth@redhat.com> - 2:9.5.3-3
- Fix missing requirement on lldb and improve installtion recommendations

* Wed Sep 19 2018 Jeff Johnston <jjohnstn@redhat.com> - 2:9.5.3-2
- Fix cdtdebug.sh script to not add quotes to args and to handle blanks, etc..

* Wed Sep 12 2018 Mat Booth <mat.booth@redhat.com> - 2:9.5.3-1
- Update to latest release and correct version number

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 1:9.6.0-0.1
- Update to latest snapshot

* Tue Jul 31 2018 Mat Booth <mat.booth@redhat.com> - 1:9.5.2-1
- Update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Mat Booth <mat.booth@redhat.com> - 1:9.5.0-2
- Update due to respin of 9.5.0

* Wed Jun 13 2018 Mat Booth <mat.booth@redhat.com> - 1:9.5.0-1
- Update to Photon release

* Fri May 4 2018 Alexander Kurtakov <akurtako@redhat.com> 1:9.4.3-2
- Adjust to remove useless extra eclipse dir in droplets.

* Thu Mar 22 2018 Mat Booth <mat.booth@redhat.com> - 1:9.4.3-1
- Update to Oxygen.3 release

* Tue Mar 20 2018 Alexander Kurtakov <akurtako@redhat.com> 1:9.4.2-1
- Update to upstream 9.4.2 release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.4.1-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Mat Booth <mat.booth@redhat.com> - 1:9.4.1-0.4
- Export LDFLAGS as well as CFLAGS

* Wed Jan 31 2018 Mat Booth <mat.booth@redhat.com> - 1:9.4.1-0.3
- Fix error causing secondary arches to fail, fix bootstrap modes

* Tue Jan 30 2018 Jeff Johnston <jjohnstn@redhat.com> - 1:9.4.1-0.2
- fix building native fragments to use rpm CFLAGS
- resolves #rhbz1539083

* Fri Jan 12 2018 Mat Booth <mat.booth@redhat.com> - 1:9.4.1-0.1
- Pull in latest fixes from 9.4 branch

* Mon Jan 08 2018 Jeff Johnston <jjohnstn@redhat.com> - 1:9.3.2-4
- Fix bug 529390

* Mon Oct 02 2017 Troy Dawson <tdawson@redhat.com> - 1:9.3.2-3
- Cleanup spec file conditionals

* Wed Sep 27 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.2-2
- Update sources

* Thu Sep 21 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.2-1
- Update to Oxygen.1 release

* Thu Aug 10 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.1-1
- Update to 9.3.1 patch release

* Thu Aug 10 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.0-0.7.gitbfe45e8
- Avoid possibility of user scripts interfering with the operation of the
  cdtdebug launcher script

* Mon Aug 07 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.0-0.6.gitbfe45e8
- Don't ship example bundles

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.3.0-0.5.gitbfe45e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.3.0-0.4.gitbfe45e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.0-0.3.gitbfe45e8
- Fix build on alternative arches
- Fix standalone debugger startup

* Mon Jun 19 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.0-0.2.gitbfe45e8
- Allow boostrap modes to build against launchbar and tm-terminal when those
  packages are also bootstrapped
- Attempt to fix standalone debugger

* Sun Jun 18 2017 Mat Booth <mat.booth@redhat.com> - 1:9.3.0-0.1.gitbfe45e8
- Update to Oxygen snapshot

* Tue May 02 2017 Mat Booth <mat.booth@redhat.com> - 1:9.2.1-3
- Rebuilt for multilib change

* Thu Mar 30 2017 Mat Booth <mat.booth@redhat.com> - 1:9.2.1-2
- Increase memory to fix the build on s390

* Tue Mar 28 2017 Mat Booth <mat.booth@redhat.com> - 1:9.2.1-1
- Update to latest upstream release
- Conditionalise building of arduino support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:9.2.0-3
- Add missing build-requires on GCC

* Mon Jan 23 2017 Mat Booth <mat.booth@redhat.com> - 1:9.2.0-2
- Fix standalone debugger
- Stricter requires on launchbar
- Add fPIC to serial library build

* Mon Jan 16 2017 Jeff Johnston <jjohnstn@redhat.com> - 1:9.2.0-1
- Update to Neon.2 release
- Use org.hamcrest.library instead of org.hamcrest.core

* Tue Nov 08 2016 Mat Booth <mat.booth@redhat.com> - 1:9.1.0-2
- Full non-bootstrap build
- Ensure gtk icon cache is updated

* Mon Nov 07 2016 Mat Booth <mat.booth@redhat.com> - 1:9.1.0-1
- Update to Neon.1 release
- Fix bootstrapping modes
- Fix binary stripping and permissions on native libraries
- Fix build on ppc64le

* Mon Nov 07 2016 Jeff Johnston <jjohnstn@redhat.com> - 1:9.0.0-4
- Fix versioning typo.

* Mon Nov 07 2016 Jeff Johnston <jjohnstn@redhat.com> - 1:9.0.0-3
- Bootstrap CDT as powerpc has been added and needs to bootstrap first.
- This allows us to build eclipse-remote.

* Mon Sep 12 2016 Roland Grunberg <rgrunber@redhat.com> - 1:9.0.0-2
- Break cycle from main CDT package to the SDK.

* Wed Jun 22 2016 Mat Booth <mat.booth@redhat.com> - 1:9.0.0-1
- Update to Neon release

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:9.0.0-0.9.gitdff6b3b
- Add missing build-requires

* Mon Jun 06 2016 Jeff Johnston <jjohnstn@redhat.com> - 1:9.0.0-0.9.gitdff6b3b
- Move location code to find launchbar.core and ui.views.log into cdtdebug script
- Move setting of jar files for gson, xerces, xalan, xml.resolver, xml.serializer,
  and lucene.analysis into config.ini patch

* Thu Jun 02 2016 Jeff Johnston <jjohnstn@redhat.com> - 1:9.0.0-0.8.gitdff6b3b
- Update section of spec file that modifies standalone debugger config.ini
- Find org.eclipse.launchbar.core and org.eclipse.ui.views.log plugins
- Set jar files for com.google.gson, org.apache.xerces, org.apache.xalan,
  org.apache.xml.resolver, org.apache.xml.serializer, org.apache.lucene.analysis

* Mon May 30 2016 Jeff Johnston <jjohnstn@redhat.com> - 1:9.0.0-0.7.gitdff6b3b
- Add Requires eclipse-launchbar which is now required by standalone debugger

* Sat May 21 2016 Mat Booth <mat.booth@redhat.com> - 1:9.0.0-0.6.gitdff6b3b
- Add a patch to fix LLVM documentation, ebz#459567
- Drop unneeded BR on RSE

* Thu May 12 2016 Alexander Kurtakov <akurtako@redhat.com> 1:9.0.0-0.5.gitdff6b3b
- Fix natives compile for profiles not included upstream.

* Thu May 12 2016 Alexander Kurtakov <akurtako@redhat.com> 1:9.0.0-0.4.gitdff6b3b
- New snapshot with natives build hooked in the maven build.

* Tue May 03 2016 Mat Booth <mat.booth@redhat.com> - 1:9.0.0-0.3.git0b93e81
- Fix launching stand-alone debugger

* Mon May 02 2016 Sopot Cela <scela@redhat.com> - 1:9.0.0-0.2.git0b93e81
- Fix broken reference to license issue to fix the build

* Sun May 01 2016 Mat Booth <mat.booth@redhat.com> - 1:9.0.0-0.1.git0b93e81
- Update to latest snapshot for Neon support

* Thu Mar 10 2016 Mat Booth <mat.booth@redhat.com> - 1:8.8.1-9
- Make standalone debugger work with all versions of lucene

* Thu Mar 10 2016 Mat Booth <mat.booth@redhat.com> - 1:8.8.1-8
- Use global instead of define
- Move more bundles into SDK that should be there
- Remove forbidden SCL macros
- Minor other changes to make it easier to auto-SCLise

* Mon Feb 29 2016 Alexander Kurtakov <akurtako@redhat.com> 1:8.8.1-7
- Update to upstream 8.8.1 release.

* Tue Feb 09 2016 Roland Grunberg <rgrunber@redhat.com> - 1:8.8.0-7
- Update to use proper xmvn provided macros.
- Fix CDT GDB Standalone Debugger.

* Thu Feb 04 2016 Roland Grunberg <rgrunber@redhat.com> - 1:8.8.0-6
- Add symbolic links for google-gson and apache-commons-compress in arduino.
- Resolves: rhbz#1302131.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.8.0-4
- Drop old patches and organize them.

* Thu Oct 08 2015 Mat Booth <mat.booth@redhat.com> - 1:8.8.0-3
- Perform full build
- Exclude docker plugins on Fedora < 23

* Thu Oct 8 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.8.0-2
- Split qt feature into subpackage with proper deps to qml, qtquick, qmake so generated project works.
- Disable brp-repack script as it just slows down the build.

* Wed Oct 07 2015 Mat Booth <mat.booth@redhat.com> - 1:8.8.0-1
- Update to Mars.1 release
- Bootstrap mode for secondary arches

* Mon Sep 21 2015 Jeff Johnston <jjohnstn@redhat.com> - 1:8.7.0-10
- Fix missing test resources
- Fix missing exit code in console

* Tue Aug 04 2015 Roland Grunberg <rgrunber@redhat.com> - 1:8.7.0-9
- Add script for automatically launching CDT Test Bundles.

* Fri Jul 10 2015 Mat Booth <mat.booth@redhat.com> - 1:8.7.0-8
- No longer R/BR nekohtml

* Tue Jul 07 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-7
- Change macro controlling docker support to also control remote support
- Disable autotools and remote plug-ins/features if macro is 0
- This allows boot-strapping CDT for use by eclipse-remote and
  eclipse-linuxtools-docker packages
 
* Thu Jul 02 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-6
- Add missing src file test resources referred to by test cases.

* Mon Jun 29 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-5
- Fix for bug 1235942.
- Fix up some dependencies in the config.ini file that have changed their
  OSGI reference in rawhide.

* Fri Jun 26 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-4
- Fix for bug 1235942.
- Add back patch3 which is needed to set up the config.ini file properly.
- Also add some new dependencies to the config.ini file that were added
  as part of CDT 8.7.

* Fri Jun 26 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-3
- Fix for bug 1235945.
- Move Docker launcher plug-ins to own package: eclipse-cdt-docker.

* Thu Jun 25 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-2
- Use simpler macro to control container support and fix macro tests.

* Tue Jun 23 2015 Jeff Johnston <jjohnstn@redhat.com> 1:8.7.0-1
- Switch to use CDT_8_7 tag.
- Add with conditional to remove container support or add it in.

* Mon Jun 15 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.7.0-0.6.gitd13a53c
- Fix build with Tycho 0.23.
- Update to newer snapshot.
- Drop rse R as it's autogen.

* Thu Jun 4 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.7.0-0.5.git6c36f7f
- Disable jacoco plugin and remove useless directory from the build.

* Thu Jun 4 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.7.0-0.4.git6c36f7f
- Add arduino subpackage and enable building arduino plugins.

* Wed Jun 3 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.7.0-0.3.git6c36f7f
- Drop Linux Tools libhover compilation and Recommend eclipse-linuxtools-libhover instead. 

* Wed Jun 3 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.7.0-0.2.git6c36f7f
- Newer snapshot.
- Enable remote feature now that deps are available.
- Drop Group tags.

* Mon Jun 1 2015 Alexander Kurtakov <akurtako@redhat.com> 1:8.7.0-0.1.git136c034
- Update to 8.7.0 pre-release.
