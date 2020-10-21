# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

# Repo tag for the release
%global git_tag pydev_7_7_0

Epoch: 1
Summary: Eclipse Python development plug-in
Name:    eclipse-pydev
Version:          7.7.0
Release:          2%{?dist}
License:          EPL-1.0
URL:              http://pydev.org

Source0:          https://github.com/fabioz/Pydev/archive/%{git_tag}.tar.gz
Source1:          eclipse-pydev.metainfo.xml

# Remove windows specific code that manipulates the windows registry
Patch0:           remove-winregistry.patch

# Fix native name
Patch1:           native-name.patch

# Allow system jython interpreter to be configured in preferences
Patch2:           system-jython-interpreter.patch

# Fix for failing to kill django processes
Patch3:           fix-process-killing.patch

# Don't package source for natives in binary plugins
Patch4:           exclude-project-files.patch

# Snakeyaml 2 not available in Fedora yet
Patch5:           snakeyaml.patch

# Port to latest lucene
Patch6:           lucene-8.patch

# Improvements for pip integration
Patch7: better-pip-integration.patch

# Don't attempt update of outline if already disposed
Patch8: prevent_update_outline_when_disposed.patch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

Requires: eclipse-platform
Requires: python3
Requires: apache-commons-logging
Requires: snakeyaml
Requires: ws-commons-util
Requires: xmlrpc-common
Requires: xmlrpc-client
Requires: xmlrpc-server
Requires: jython
Requires: antlr32-java
Recommends: python3-pylint
Recommends: python3-django
Recommends: python3-ipython-console
BuildRequires:  gcc-c++
BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  eclipse-jdt
BuildRequires:  apache-commons-logging
BuildRequires:  snakeyaml
BuildRequires:  ws-commons-util
BuildRequires:  xmlrpc-common
BuildRequires:  xmlrpc-client
BuildRequires:  xmlrpc-server
BuildRequires:  jython
BuildRequires:  lucene >= 8.0.0
BuildRequires:  lucene-analysis >= 8.0.0

# Required for symlinking into the plugin
%if 0%{?fedora}
BuildRequires:    python3-autopep8
BuildRequires:    python3-isort
BuildRequires:    python3-pycodestyle
Requires: python3-autopep8
Requires: python3-isort
Requires: python3-pycodestyle
%endif

# For building native debugging extensions
%if 0%{?fedora}
BuildRequires:    python3-devel
BuildRequires:    python3-Cython
%endif

# Obsoletes added in F32
Obsoletes: %{name}-mylyn <= 1:7.5.0-1

%description
The eclipse-pydev package contains Eclipse plugins for
Python development.

%prep
%setup -q -n Pydev-%{git_tag}
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4
%patch5 -p1 -R
%patch6 -p1
%patch7
%patch8

%mvn_package "::pom:" __noinstall
%mvn_package ":::sources{,-feature}:" __noinstall
%mvn_package ":"

# Fix line endings
sed -i -e 's/\r$//' $(find plugins/org.python.pydev.core/pysrc -name "*.py")

# Remove bundled ctypes (used only under cygwin)
rm -r plugins/org.python.pydev.core/pysrc/third_party/wrapped_for_pydev
# Remove lib2to3 (provided by jython)
rm -r plugins/org.python.pydev.core/pysrc/third_party/pep8/lib2to3

%if 0%{?fedora}
# Symlink to system version of isort
rm -r plugins/org.python.pydev.core/pysrc/third_party/isort_container/isort
(cd plugins/org.python.pydev.core/pysrc/third_party/isort_container && ln -s %{python3_sitelib}/isort)
# Symlink to system versions of autopep8 and pycodestyle
rm plugins/org.python.pydev.core/pysrc/third_party/pep8/{autopep8,pycodestyle}*
(cd plugins/org.python.pydev.core/pysrc/third_party/pep8/ && ln -s %{python3_sitelib}/autopep8.py)
(cd plugins/org.python.pydev.core/pysrc/third_party/pep8/ && ln -s %{python3_sitelib}/pycodestyle.py)
%endif

# Remove pre-built artifacts
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.dll' -delete
find -name '*.dylib' -delete
find -name '*.so' -delete
rm -rf plugins/org.python.pydev.jython/Lib

# Symlink to system jython and standard library
pushd plugins/org.python.pydev.jython
ln -sf %{_datadir}/jython/jython.jar
ln -sf %{_datadir}/jython/javalib
ln -sf %{_datadir}/jython/Lib
popd

# Link to system jython
# we must include all of jython's runtime dependencies on the classpath
pushd plugins/org.python.pydev.jython
for j in $(ls javalib/*.jar) ; do
  sed -i -e 's/\r//' -e "/^ jython\.jar/i\ $j," META-INF/MANIFEST.MF
done
sed -i -e "s/ jython\.jar/ jython.jar,javalib\//" build.properties
popd

# Symlinks to other system jars
ln -sf $(build-classpath commons-logging) \
       plugins/org.python.pydev.shared_interactive_console/commons-logging-1.1.1.jar
ln -sf $(build-classpath ws-commons-util) \
       plugins/org.python.pydev.shared_interactive_console/ws-commons-util-1.0.2.jar
ln -sf $(build-classpath xmlrpc-client) \
       plugins/org.python.pydev.shared_interactive_console/xmlrpc-client-3.1.3.jar
ln -sf $(build-classpath xmlrpc-common) \
       plugins/org.python.pydev.shared_interactive_console/xmlrpc-common-3.1.3.jar
ln -sf $(build-classpath xmlrpc-server) \
       plugins/org.python.pydev.shared_interactive_console/xmlrpc-server-3.1.3.jar
ln -sf $(build-classpath snakeyaml) \
       plugins/org.python.pydev.shared_core/libs/snakeyaml-1.11.jar
ln -sf $(build-classpath lucene/lucene-core) \
       plugins/org.python.pydev.shared_core/libs/lucene-core-8.1.1.jar
ln -sf $(build-classpath lucene/lucene-analyzers-common) \
       plugins/org.python.pydev.shared_core/libs/lucene-analyzers-common-8.1.1.jar

# Some bundles that don't need to be dir-shaped
sed -i -e '/Eclipse-BundleShape/d' \
  plugins/org.python.pydev.help/META-INF/MANIFEST.MF

# Fix encodings
iconv -f CP1252 -t UTF-8 LICENSE.txt > LICENSE.txt.utf
mv LICENSE.txt.utf LICENSE.txt

# Update site is not relevant for RPM builds
%pom_disable_module org.python.pydev.p2-repo features

# Don't ship mylyn extension
%pom_disable_module org.python.pydev.mylyn plugins
%pom_disable_module org.python.pydev.mylyn.feature features

%build
# Build native part first
pushd plugins/org.python.pydev.core/pysrc &>/dev/null
(cd pydevd_attach_to_process && \
  g++ %{optflags} -shared -o attach_linux.so -fPIC -nostartfiles linux_and_mac/attach.cpp)
%if 0%{?fedora}
%if 0%{?fedora} < 33
PYTHONPATH=. %{__python3} build_tools/build.py --no-remove-binaries
%endif
%endif
popd &>/dev/null

# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +v%Y%m%d-%H%M)

# Build everything else
%mvn_build -j -f -- -DforceContextQualifier=$QUALIFIER

%install
%mvn_install

# fix perms on native lib
find ${RPM_BUILD_ROOT} -name attach_linux.so -exec chmod +x {} \;

# Install appdata
install -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/appdata/eclipse-pydev.metainfo.xml

# Have to re-symlink embedded system jars
installDir=${RPM_BUILD_ROOT}/%{_prefix}/lib/eclipse/droplets/pydev
pushd $installDir/plugins
for f in commons-logging \
         ws-commons-util \
         xmlrpc-client \
         xmlrpc-common \
         xmlrpc-server \
         snakeyaml \
         lucene/lucene-core \
         lucene/lucene-analyzers-common ; do
  file=$(find . -name $(basename $f)*.jar)
  rm $file
  ln -sf $(build-classpath $f) $file
done
popd

# Symlink to system jython and standard library
pushd $installDir/plugins/org.python.pydev.jython_*
rm -rf jython.jar javalib Lib
ln -sf %{_datadir}/jython/jython.jar
ln -sf %{_datadir}/jython/javalib
ln -sf %{_datadir}/jython/Lib
popd

%if 0%{?fedora}
pushd $installDir/plugins/org.python.pydev.core_*
# Symlink to system versions of autopep8 and pycodestyle
rm pysrc/third_party/pep8/*.py
(cd pysrc/third_party/pep8/ && ln -s %{python3_sitelib}/autopep8.py)
(cd pysrc/third_party/pep8/ && ln -s %{python3_sitelib}/pycodestyle.py)
# Symlink to system version of isort
rm pysrc/third_party/isort_container/isort
(cd pysrc/third_party/isort_container && ln -s %{python3_sitelib}/isort)
popd
%endif

# convert .py$ files from mode 0644 to mode 0755
sed -i -e '/.*\.py$/s/0644/0755/' .mfiles*

%files -f .mfiles
%license LICENSE.txt
%doc README.txt
%{_datadir}/appdata/eclipse-pydev.metainfo.xml

%changelog
* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 1:7.7.0-2
- Do not force C++11 mode

* Fri Aug 14 2020 Mat Booth <mat.booth@redhat.com> - 1:7.7.0-1
- Update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Mat Booth <mat.booth@redhat.com> - 1:7.6.0-2
- Temporarily disable cython debugging extension on F33+ due to a problem
  building against python 3.9

* Thu Jun 25 2020 Mat Booth <mat.booth@redhat.com> - 1:7.6.0-1
- Update to latest upstream release

* Tue Mar 24 2020 Mat Booth <mat.booth@redhat.com> - 1:7.5.0-1
- Update to latest upstream release
- Drop mylyn extension
- Drop python 2 cython extension support

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Mat Booth <mat.booth@redhat.com> - 1:7.4.0-2
- Don't build python 2 extensions for Fedora >= 32

* Wed Nov 20 2019 Mat Booth <mat.booth@redhat.com> - 1:7.4.0-1
- Update to latest upstream release

* Mon Sep 23 2019 Mat Booth <mat.booth@redhat.com> - 1:7.3.0-2
- Ensure c++11 is used when building native part

* Mon Sep 09 2019 Mat Booth <mat.booth@redhat.com> - 1:7.3.0-1
- Update to latest upstream release

* Sun Sep 01 2019 Mat Booth <mat.booth@redhat.com> - 1:7.2.1-4
- Temporarily disable cython debugging extension on F32 due to a problem
  building against python 3.8

* Fri Jun 21 2019 Mat Booth <mat.booth@redhat.com> - 1:7.2.1-3
- Fix failure to build against Eclipse 2019-06

* Mon Jun 17 2019 Mat Booth <mat.booth@redhat.com> - 1:7.2.1-2
- Rebuild against Lucene 8

* Sat Jun 01 2019 Mat Booth <mat.booth@redhat.com> - 1:7.2.1-1
- Update to latest upstream release
- Fix missing cython extension for python 2 users

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 1:7.1.0-2
- Restrict to same architectures as Eclipse itself

* Wed Feb 20 2019 Mat Booth <mat.booth@redhat.com> - 1:7.1.0-1
- Update to latest upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Mat Booth <mat.booth@redhat.com> - 1:7.0.3-1
- Update to upstream release 7.0.3

* Thu Sep 13 2018 Mat Booth <mat.booth@redhat.com> - 1:6.5.0-2
- Patch for NPE/dispose errors

* Thu Sep 13 2018 Mat Booth <mat.booth@redhat.com> - 1:6.5.0-1
- Update to latest upstream release
- Amend license tag
- Fix some issues with pip integration (avoid misleading messages about
  the upgradability of the system pip, install into user area by default
  because the system area is read only)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:6.3.3-3
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Mat Booth <mat.booth@redhat.com> - 1:6.3.3-2
- Conditionally build stuff that is only available on Fedora

* Tue May 15 2018 Mat Booth <mat.booth@redhat.com> - 1:6.3.3-1
- Update to latest version

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 1:6.3.2-2
- Install appdata

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 1:6.3.2-1
- Update to latest upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Mat Booth <mat.booth@redhat.com> - 1:6.1.0-1
- Update to latest upstream release, rhbz#1514252
- Avoid installing source with binary bundles, rhbz#1474069
- Fix cython debugging extensions, rhbz#1404801
- Unbundle isort utility

* Thu Sep 28 2017 Mat Booth <mat.booth@redhat.com> - 1:5.9.2-2
- Fix broken internal Jython console
- Fix pycodestyle usage, rhbz#1496452

* Sat Sep 16 2017 Mat Booth <mat.booth@redhat.com> - 1:5.9.2-1
- Update to latest upstream release

* Fri Aug 11 2017 Mat Booth <mat.booth@redhat.com> - 1:5.9.0-1
- Update to latest upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Mat Booth <mat.booth@redhat.com> - 1:5.8.0-1
- Update to latest upstream release
- Drop upstreamed patch

* Tue May 02 2017 Mat Booth <mat.booth@redhat.com> - 1:5.6.0-2
- Rebuilt for multilib change

* Tue Apr 04 2017 nboldt <nickboldt+redhat@gmail.com> - 1:5.6.0-1
- Update to latest upstream releases - PyDev 5.6.0 and Lucene 6.1.0 (FC27+ only)

* Tue Feb 28 2017 Roland Grunberg <rgrunber@redhat.com> - 1:5.5.0-3
- Add jffi-native onto the classpath of org.python.pydev.jython.
- Resolves: rhbz#1399793

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Mat Booth <mat.booth@redhat.com> - 1:5.5.0-1
- Update to latest release

* Tue Jan 17 2017 Mat Booth <mat.booth@redhat.com> - 1:5.4.0-3
- Fix some minor packaging issues (perms, line endings, etc)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:5.4.0-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 1:5.4.0-1
- Update to upstream 5.4.0.

* Thu Sep 29 2016 Alexander Kurtakov <akurtako@redhat.com> 1:5.2.0-1
- Update to upstream 5.2.0.

* Fri Jun 24 2016 Mat Booth <mat.booth@redhat.com> - 1:5.1.2-1
- Update to release 5.1.2
- Remove bundled third-party libs rhbz#1339362
- Fix valid encoding detection failure rhbz#1327642
- Improve system jython integration
- Make symlinking jars more portable

* Fri Jun 17 2016 Alexander Kurtakov <akurtako@redhat.com> 1:5.1.1-1
- Update to upstream 5.1.1.

* Wed May 18 2016 Sopot Cela <scela@redhat.com> 1:5.0.0-1
- Update to upstream 5.0.0

* Wed May 04 2016 Sopot Cela <scela@redhat.com> 1:4.6.0-1
- Update to upstream 4.6.0

* Mon Apr 25 2016 Sopot Cela <scela@redhat.com> 1:4.5.5-3
- Patch so it builds with Neon

* Wed Apr 6 2016 Alexander Kurtakov <akurtako@redhat.com> 1:4.5.5-2
- Switch python* requires to python3.

* Fri Mar 25 2016 Alexander Kurtakov <akurtako@redhat.com> 1:4.5.5-1
- Update to upstream 4.5.5.

* Thu Feb 04 2016 Sopot Cela <scela@redhat.com> 1:4.5.4-0.2.git3694021
- Minor changelog correction

* Thu Feb 04 2016 Sopot Cela <scela@redhat.com> 1:4.5.4-0.1
- Upgrade to upstream 4.5.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Alexander Kurtakov <akurtako@redhat.com> 1:4.5.3-1
- Update to upstream 4.5.3.

* Tue Jan 19 2016 Alexander Kurtakov <akurtako@redhat.com> 1:4.5.1-1
- Update to upstream 4.5.1.

* Sun Nov 29 2015 Mat Booth <mat.booth@redhat.com> - 1:4.4.0-3
- Rebuild to fix broken antlr symlink

* Wed Oct 21 2015 Mat Booth <mat.booth@redhat.com> - 1:4.4.0-2
- Fix for failing to kill django processes
- rhbz#1264446

* Thu Oct 8 2015 Alexander Kurtakov <akurtako@redhat.com> 1:4.4.0-1
- Update to upstream 4.4.0.
- Disable brp-repack.

* Mon Sep 14 2015 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.0-3
- Rebuild as an Eclipse p2 Droplet.

* Mon Aug 31 2015 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.0-2
- Minor change to build as a droplet.

* Fri Aug 21 2015 akurtakov <akurtakov@localhost.localdomain> 1:4.3.0-1
- Update to upstream 4.3.0.
- Simplify BR/R to adapt new names and remove autogenerated ones now.

* Wed Aug 12 2015 Mat Booth <mat.booth@redhat.com> - 1:4.2.0-3
- Add all necessary symlinks for jython

* Mon Jul 20 2015 Mat Booth <mat.booth@redhat.com> - 1:4.2.0-2
- Fix perms on native lib to fix binary stripping
- Generate debuginfo

* Thu Jul 16 2015 Sopot Cela <scela@redhat.com> - 1:4.2.0-1
- Update to 4.2.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Alexander Kurtakov <akurtako@redhat.com> 1:4.1.0-1
- Update to upstream 4.1.0 release.

* Wed May 13 2015 Alexander Kurtakov <akurtako@redhat.com> 1:4.0.0-2
- Make mylyn subpackage archful as timestamps make diff and fail builds.

* Wed Apr 15 2015 Mat Booth <mat.booth@redhat.com> - 1:4.0.0-1
- Update to latest upstream release
- No longer necessary to symlink optparse
- Now archful package due to having a native component

* Mon Dec 8 2014 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.1-2
- Build with xmvn.

* Thu Sep 18 2014 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.1-1
- Update to upstream 3.7.1.

* Thu Jul 31 2014 Mat Booth <mat.booth@redhat.com> - 1:3.6.0-1
- Update to latest upstream release
- Require jython 2.7
- Remove no longer needed patches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Mat Booth <mat.booth@redhat.com> - 1:3.5.0-3
- Patch to allow system jython interpreter to be configured in preferences

* Mon Jun 02 2014 Mat Booth <mat.booth@redhat.com> - 1:3.5.0-2
- Patch to build with latest version of jython
- Install license files
- No longer need to package a portion of jython's lib dir

* Thu May 29 2014 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-1
- Update to 3.5.0.

* Thu Mar 20 2014 Alexander Kurtakov <akurtako@redhat.com> 1:3.4.1-1
- Update to 3.4.1.

* Wed Feb 12 2014 Alexander Kurtakov <akurtako@redhat.com> 1:3.3.3-1
- Update to 3.3.3.

* Mon Dec 30 2013 Alexander Kurtakov <akurtako@redhat.com> 1:3.2.0-1
- Update to 3.2.0.

* Fri Dec 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1:3.1.0-1
- Update to 3.1.0.

* Mon Nov 11 2013 Alexander Kurtakov <akurtako@redhat.com> 1:3.0-1
- Update to 3.0.
- Drop old changelog now that we move to tycho builds.
