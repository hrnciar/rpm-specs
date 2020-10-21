%{?mingw_package_header}

%global pkgname python3
%global py_ver 3.9
%global py_ver_nodots 39
%global mingw32_py3_libdir       %{mingw32_libdir}/python%{py_ver}
%global mingw64_py3_libdir       %{mingw64_libdir}/python%{py_ver}
%global mingw32_py3_hostlibdir   %{_prefix}/%{mingw32_target}/lib/python%{py_ver}
%global mingw64_py3_hostlibdir   %{_prefix}/%{mingw64_target}/lib/python%{py_ver}
%global mingw32_py3_incdir       %{mingw32_includedir}/python%{py_ver}
%global mingw64_py3_incdir       %{mingw64_includedir}/python%{py_ver}
%global mingw32_python3_sitearch %{mingw32_libdir}/python%{py_ver}/site-packages
%global mingw64_python3_sitearch %{mingw64_libdir}/python%{py_ver}/site-packages

# Some of the files below /usr/lib/pythonMAJOR.MINOR/test  (e.g. bad_coding.py)
# are deliberately invalid, leading to SyntaxError exceptions if they get
# byte-compiled.
%global _python_bytecompile_errors_terminate_build 0

#global pre rc2

Name:          mingw-%{pkgname}
Version:       3.9.0
Release:       1%{?pre:.%pre}%{?dist}
Summary:       MinGW Windows %{pkgname}

BuildArch:     noarch
License:       Python
URL:           https://www.python.org/
Source0:       http://www.python.org/ftp/python/%{version}/Python-%{version}%{?pre}.tar.xz

# Add support for building with mingw
Patch1:        mingw-python3_platform-mingw.patch
# Implement setenv for PY_COERCE_C_LOCALE
Patch2:        mingw-python3_setenv.patch
# Ignore main program for frozen scripts
Patch3:        mingw-python3_frozenmain.patch
# Fix using dllhandle and winver
Patch4:        mingw-python3_dllhandle-winver.patch
# Remove gettext dependency
Patch5:        mingw-python3_gettext.patch
# Add missing include dirs and link libraries, assorted build fixes
Patch6:        mingw-python3_build.patch
# Fix misc warnings
Patch7:        mingw-python3_warnings.patch
# Link resource files and build pythonw.exe
Patch8:        mingw-python3_pythonw.patch
# Install msilib
Patch9:        mingw-python3_msilib.patch
# Use posix layout
Patch10:       mingw-python3_posix-layout.patch
# Implement PyThread_get_thread_native_id for mingw-win-pthread
Patch11:       mingw-python3_pthread_threadid.patch
# Output list of failed modules to mods_failed.txt so that we can abort the build
Patch12:       mingw-python3_mods-failed.patch
# Adapt cygwinccompiler for cross-compiling
Patch13:       mingw-python3_adapt-cygwinccompiler.patch
# Make sysconfigdata.py relocatable
Patch14:       mingw-python3_make-sysconfigdata.py-relocatable.patch
# Adapt posix build detection
Patch15:       mingw-python3_posix-build.patch
# IO_REPARSE_TAG_APPEXECLINK does not exist in mingw (yet?)
Patch16:       mingw-python3_tag_appexeclink.patch
# Enable building some modules
Patch17:       mingw-python3_enable-modules.patch
# Disable building broken / unix-only modules
Patch18:       mingw-python3_disable-modules.patch
# Fix building multiprocessing module
Patch19:       mingw-python3_module-multiprocessing.patch
# Fix building ctypes module
Patch20:       mingw-python3_module-ctypes.patch
# Fix linking against tcl/tk
Patch21 :      mingw-python3_module-tkinter.patch
# Build winreg module
Patch22:       mingw-python3_module-winreg.patch
# Configure system calls in posixmodule
Patch23:       mingw-python3_module-posix.patch
# Fix socket module build
# See also https://github.com/msys2/MINGW-packages/issues/5184
Patch24:       mingw-python3_module-socket.patch
# Fix signal module build
Patch25:       mingw-python3_module-signal.patch
# Fix select module build
Patch26:       mingw-python3_module-select.patch
# Fix ssl module build, not use enum certificates
Patch27:       mingw-python3_module-ssl.patch
# Fix building xxsubinterpreters module
Patch28:       mingw-python3_module-xxsubinterpreters.patch
# Use posix getpath
Patch29:       mingw-python3_module-getpath-posix.patch
# Add path of executable/dll to system path so that correct dependent dlls are found
Patch30:       mingw-python3_module-getpath-execprefix.patch

BuildRequires: automake autoconf libtool
BuildRequires: python3-devel

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-expat
BuildRequires: mingw32-libffi
BuildRequires: mingw32-openssl
BuildRequires: mingw32-readline
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-tcl
BuildRequires: mingw32-tk

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-expat
BuildRequires: mingw64-libffi
BuildRequires: mingw64-openssl
BuildRequires: mingw64-readline
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-tcl
BuildRequires: mingw64-tk


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Requires:      python(abi) = %{py_ver}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Requires:      python(abi) = %{py_ver}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n Python-%{version}%{?pre}
autoreconf -vfi

# Ensure that we are using the system copy of various libraries rather than copies shipped in the tarball
rm -r Modules/expat
rm -r Modules/_ctypes/{darwin,libffi}*

# Just to be sure that we are using the wanted thread model
rm -f Python/thread_nt.h


%build
export MINGW32_MAKE_ARGS="WINDRES=%{mingw32_target}-windres LD=%{mingw32_target}-ld DLLWRAP=%{mingw32_target}-dllwrap"
export MINGW64_MAKE_ARGS="WINDRES=%{mingw64_target}-windres LD=%{mingw64_target}-ld DLLWRAP=%{mingw64_target}-dllwrap"

export MINGW32_CFLAGS="%mingw32_cflags -D_GNU_SOURCE -D__USE_MINGW_ANSI_STDIO=1 -D_WIN32_WINNT=0x0601"
export MINGW64_CFLAGS="%mingw64_cflags -D_GNU_SOURCE -D__USE_MINGW_ANSI_STDIO=1 -D_WIN32_WINNT=0x0601"

# TODO Drop --with-ensurepip again (broken with python3.9-beta4?)
MSYSTEM=MINGW %mingw_configure \
--enable-shared \
--with-system-expat \
--with-system-ffi \
--with-ensurepip=no

%mingw_make_build

# Abort build if not explicitly disabled modules failed to build
if [ -e build_win32/mods_failed.txt ]; then
    echo "The following modules failed to build for win32"
    cat build_win32/mods_failed.txt
fi
if [ -e build_win64/mods_failed.txt ]; then
    echo "The following modules failed to build for win64"
    cat build_win64/mods_failed.txt
fi
if [ -e build_win32/mods_failed.txt ] || [ -e build_win64/mods_failed.txt ]; then
    exit 1;
fi


%install
%mingw_make_install

# Link import library to libdir
ln -s %{mingw32_py3_libdir}/config-%{py_ver}/libpython%{py_ver}.dll.a %{buildroot}%{mingw32_libdir}/libpython%{py_ver}.dll.a
ln -s %{mingw64_py3_libdir}/config-%{py_ver}/libpython%{py_ver}.dll.a %{buildroot}%{mingw64_libdir}/libpython%{py_ver}.dll.a

# Copy some useful "stuff"
install -dm755 %{buildroot}%{mingw32_py3_libdir}/Tools/{i18n,scripts}
install -dm755 %{buildroot}%{mingw64_py3_libdir}/Tools/{i18n,scripts}
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw32_py3_libdir}/Tools/i18n/
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw64_py3_libdir}/Tools/i18n/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw32_py3_libdir}/Tools/scripts/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw64_py3_libdir}/Tools/scripts/

# Cleanup shebangs
find %{buildroot}%{mingw32_py3_libdir}/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/python3|"
find %{buildroot}%{mingw64_py3_libdir}/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/python3|"

# Remove references to build directory
for file in config-%{py_ver}/Makefile _sysconfigdata__win_.py; do
    sed -i "s|%{_builddir}|/build|g" %{buildroot}%{mingw32_py3_libdir}/$file
    sed -i "s|%{_builddir}|/build|g" %{buildroot}%{mingw64_py3_libdir}/$file
done

# Fix permissons
find %{buildroot} -type f | xargs chmod 0644
find %{buildroot} -type f \( -name "*.dll" -o -name "*.exe" \) | xargs chmod 0755

# Don't ship manpages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Mingw python host wrappers
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/bin/
mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/bin/

cat > %{buildroot}%{_prefix}/%{mingw32_target}/bin/python3 <<EOF
#!/bin/sh
pylibdynload=\$(/usr/bin/python%{py_ver} -c 'import sysconfig; import os; print(os.path.join(sysconfig.get_path("platstdlib"), "lib-dynload"))')
CC=%{mingw32_cc} LD=%{mingw32_target}-ld DLLWRAP=%{mingw32_target}-dllwrap _PYTHON_HOST_PLATFORM=mingw _PYTHON_SYSCONFIGDATA_NAME="_sysconfigdata__win_" PYTHONHOME=%{mingw32_prefix} PYTHONPATH=\$PYTHONPATH:%{mingw32_py3_hostlibdir}:%{mingw32_py3_hostlibdir}/site-packages:\$pylibdynload:%{mingw32_py3_libdir}:%{mingw32_python3_sitearch} PYTHONPLATLIBDIR=lib /usr/bin/python3 "\$@"
EOF

cat > %{buildroot}%{_prefix}/%{mingw64_target}/bin/python3 <<EOF
#!/bin/sh
pylibdynload=\$(/usr/bin/python%{py_ver} -c 'import sysconfig; import os; print(os.path.join(sysconfig.get_path("platstdlib"), "lib-dynload"))')
CC=%{mingw64_cc} LD=%{mingw64_target}-ld DLLWRAP=%{mingw64_target}-dllwrap _PYTHON_HOST_PLATFORM=mingw _PYTHON_SYSCONFIGDATA_NAME="_sysconfigdata__win_" PYTHONHOME=%{mingw64_prefix} PYTHONPATH=\$PYTHONPATH:%{mingw64_py3_hostlibdir}:%{mingw64_py3_hostlibdir}/site-packages:\$pylibdynload:%{mingw64_py3_libdir}:%{mingw64_python3_sitearch} PYTHONPLATLIBDIR=lib /usr/bin/python3 "\$@"
EOF

chmod +x %{buildroot}%{_prefix}/%{mingw32_target}/bin/python3
chmod +x %{buildroot}%{_prefix}/%{mingw64_target}/bin/python3

ln -s %{_prefix}/%{mingw32_target}/bin/python3 %{buildroot}%{_bindir}/mingw32-python3
ln -s %{_prefix}/%{mingw64_target}/bin/python3 %{buildroot}%{_bindir}/mingw64-python3

# Host site-packages skeleton
mkdir -p %{buildroot}%{mingw32_py3_hostlibdir}/site-packages
mkdir -p %{buildroot}%{mingw64_py3_hostlibdir}/site-packages

# Hackishly faked distutils/sysconfig.py
mkdir -p %{buildroot}%{mingw32_py3_hostlibdir}/distutils
mkdir -p %{buildroot}%{mingw64_py3_hostlibdir}/distutils
pushd %{buildroot}%{mingw32_libdir}/python%{py_ver}/distutils/
for file in *.py; do
    ln -s %{mingw32_libdir}/python%{py_ver}/distutils/$file %{buildroot}%{mingw32_py3_hostlibdir}/distutils/$file
done
popd
pushd %{buildroot}%{mingw64_libdir}/python%{py_ver}/distutils/
for file in *.py; do
    ln -s %{mingw64_libdir}/python%{py_ver}/distutils/$file %{buildroot}%{mingw64_py3_hostlibdir}/distutils/$file
done
popd
ln -s %{mingw32_py3_libdir}/distutils/command %{buildroot}%{mingw32_py3_hostlibdir}/distutils/command
ln -s %{mingw64_py3_libdir}/distutils/command %{buildroot}%{mingw64_py3_hostlibdir}/distutils/command
rm %{buildroot}%{mingw32_py3_hostlibdir}/distutils/sysconfig.py
rm %{buildroot}%{mingw64_py3_hostlibdir}/distutils/sysconfig.py
cat > %{buildroot}%{mingw32_py3_hostlibdir}/distutils/sysconfig.py <<EOF
import imp
_sysconfig = imp.load_source('distutils.sysconfig', '%{mingw32_py3_libdir}/distutils/sysconfig.py')
from distutils.sysconfig import *
# Overwrite methods from sysconfig
get_python_inc = lambda plat_specific=0, prefix=None: "%{mingw32_py3_incdir}"
get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{mingw32_python3_sitearch}"
EOF
cat > %{buildroot}%{mingw64_py3_hostlibdir}/distutils/sysconfig.py <<EOF
import imp
_sysconfig = imp.load_source('distutils.sysconfig', '%{mingw64_py3_libdir}/distutils/sysconfig.py')
from distutils.sysconfig import *
# Overwrite methods from sysconfig
get_python_inc = lambda plat_specific=0, prefix=None: "%{mingw64_py3_incdir}"
get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{mingw64_python3_sitearch}"
EOF

# mingw-python rpm macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw32-python3 <<EOF
%%mingw32_python3 %{_prefix}/%{mingw32_target}/bin/python3
%%mingw32_python3_sitearch %{mingw32_python3_sitearch}
%%mingw32_python3_version %{py_ver}
%%mingw32_python3_version_nodots %{py_ver_nodots}
EOF
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw64-python3 <<EOF
%%mingw64_python3 %{_prefix}/%{mingw64_target}/bin/python3
%%mingw64_python3_sitearch %{mingw64_python3_sitearch}
%%mingw64_python3_version %{py_ver}
%%mingw64_python3_version_nodots %{py_ver_nodots}
EOF

# TODO: These cause unsatisfyable requires on msvcr71.dll
rm -f %{buildroot}%{mingw32_py3_libdir}/distutils/command/wininst-7.1.exe
rm -f %{buildroot}%{mingw64_py3_libdir}/distutils/command/wininst-7.1.exe

# Drop unversioned 2to3
rm %{buildroot}%{mingw32_bindir}/2to3
rm %{buildroot}%{mingw64_bindir}/2to3

# Drop pip stuff installed to native dirs
rm -f %{buildroot}%{_bindir}/pip*
rm -rf %{buildroot}%{_prefix}/lib/python%{py_ver}/site-packages/pip*

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license LICENSE
%{_bindir}/mingw32-python3
%{_rpmconfigdir}/macros.d/macros.mingw32-python3
%{_prefix}/%{mingw32_target}/bin/python3
%{mingw32_py3_hostlibdir}/
%{mingw32_bindir}/2to3-%{py_ver}
%{mingw32_bindir}/idle3*
%{mingw32_bindir}/pydoc3*
%{mingw32_bindir}/python3.exe
%{mingw32_bindir}/python3-config
%{mingw32_bindir}/python%{py_ver}.exe
%{mingw32_bindir}/python%{py_ver}-config
%{mingw32_bindir}/python%{py_ver}.exe
%{mingw32_bindir}/python%{py_ver}-config
%{mingw32_bindir}/python3w.exe
%{mingw32_bindir}/libpython%{py_ver}.dll
%{mingw32_py3_incdir}/
%{mingw32_libdir}/libpython%{py_ver}.dll.a
%{mingw32_py3_libdir}/
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license LICENSE
%{_bindir}/mingw64-python3
%{_rpmconfigdir}/macros.d/macros.mingw64-python3
%{_prefix}/%{mingw64_target}/bin/python3
%{mingw64_py3_hostlibdir}/
%{mingw64_bindir}/2to3-%{py_ver}
%{mingw64_bindir}/idle3*
%{mingw64_bindir}/pydoc3*
%{mingw64_bindir}/python3.exe
%{mingw64_bindir}/python3-config
%{mingw64_bindir}/python%{py_ver}.exe
%{mingw64_bindir}/python%{py_ver}-config
%{mingw64_bindir}/python%{py_ver}.exe
%{mingw64_bindir}/python%{py_ver}-config
%{mingw64_bindir}/python3w.exe
%{mingw64_bindir}/libpython%{py_ver}.dll
%{mingw64_py3_incdir}/
%{mingw64_libdir}/libpython%{py_ver}.dll.a
%{mingw64_py3_libdir}/
%{mingw64_libdir}/pkgconfig/*.pc


%changelog
* Tue Oct 06 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Fri Sep 18 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.12-rc2
- Update to 3.9.0-rc2

* Wed Aug 12 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.11.rc1
- Update to 3.9.0-rc1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-0.10.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.9.b5
- Update to 3.9.0-beta5

* Tue Jul 14 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.8.b4
- Backport patch for CVE-2019-20907

* Sun Jul 12 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.7.b4
- Update to 3.9.0-beta4

* Wed Jun 24 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.9.0-0.6.b3
- Add mingw32/64_python3_version_nodots

* Thu Jun 11 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.5.b3
- Update to 3.9.0-beta3
- Set PYTHONPLATLIBDIR=lib

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.2.b1
- Add mingw-python3_platlibdir.patch

* Thu May 28 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.1.b1
- Update to 3.9.0-beta1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.8.3-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Sandro Mani <manisandro@gmail.com> - 3.8.3-1
- Update to 3.8.3

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 3.8.2-1
- Update to 3.8.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Sandro Mani <manisandro@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Dec 04 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-2
- Exclude debug files

* Thu Oct 17 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.5.rc1
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Oct 04 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.4.rc1
- Update to 3.8.0-rc1

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.3.b4
- Remove gettext dependency
- Remove dlfcn dependency
- Update mingw-python3_adapt-cygwinccompiler.patch to ensure native gcc is not invoked

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.2.b4
- Adapt host wrappers
- Don't strip extensions

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.1.b4
- Update to 3.8.0b4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Sandro Mani <manisandro@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 3.7.3-3
- %%define -> %%global

* Wed Apr 24 2019 Sandro Mani <manisandro@gmail.com> - 3.7.3-2
- Set _PYTHON_SYSCONFIGDATA_NAME in host wrapper

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 3.7.3-1
- Initial package
