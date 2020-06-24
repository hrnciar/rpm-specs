%bcond_with debug

# This flag produces undefined references to the EGL libraries
%undefine _ld_as_needed

Name: gtengine
Summary: Library for computations in mathematics, graphics, image analysis, and physics
Version: 4.6
Release: 1%{?dist}
Epoch: 1
License: Boost
URL: http://www.geometrictools.com
Source0: http://www.geometrictools.com/Downloads/GeometricToolsEngine4p6.zip
Source1: http://www.geometrictools.com/License/Boost/LICENSE_1_0.txt#/%{name}-LICENSE_1_0.txt

BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(egl)
BuildRequires: glibc-devel
BuildRequires: gcc-c++, dos2unix
BuildRequires: libstdc++-devel

%description
A library of source code for computing in the fields of mathematics,
graphics, image analysis, and physics.
The engine is written in C++ 11 and, as such, has portable access
to standard constructs for multithreading programming on cores.
The engine also supports high-performance computing using general
purpose GPU programming (GPGPU).
SIMD code is also available using Intel Streaming SIMD Extensions (SSE).

GTEngine requires OpenGL 4.5.0 (or later).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
Requires: pkgconf-pkg-config%{?_isa}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package samples
Summary: Samples files of %{name}
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
%description samples
This package contains samples files for
testing that use %{name}.

%prep
%autosetup -n GeometricTools
cp -p %{SOURCE1} License

%build
%if %{with debug}
export LDFLAGS="%{__global_ldflags} -lpthread -lGL -lEGL -lX11 -lpng -lm -Wl,--no-undefined -Wl,--no-allow-shlib-undefined"
export CFLAGS="-g -O0 -D_DEBUG -pthread"
mkdir -p GTE/obj/DebugDynamic
make V=1 CFG=DebugDynamic -f makegraphics.gte -C GTE 
make V=1 CFG=DebugDynamic -f makemathematicsgpu.gte -C GTE
make V=1 CFG=DebugDynamic -f makeapplications.gte -C GTE
%else
export LDFLAGS="%{__global_ldflags} -lpthread -lGL -lEGL -lX11 -lpng -lm -Wl,--no-undefined -Wl,--no-allow-shlib-undefined"
export CFLAGS="%{optflags} -pthread -DNDEBUG"
mkdir -p GTE/obj/ReleaseDynamic
make V=1 CFG=ReleaseDynamic -f makegraphics.gte -C GTE -j1
make V=1 CFG=ReleaseDynamic -f makemathematicsgpu.gte -C GTE -j1
make V=1 CFG=ReleaseDynamic -f makeapplications.gte -C GTE -j1
%endif

%if %{with debug}
make V=1 CFG=DebugDynamic -f makeallsamples.gte -C GTE/Samples -j1 \
 CFLAGS="-g -O0 -D_DEBUG -pthread -c -DGTE_USE_LINUX -DGTE_USE_OPENGL -std=c++14" LDFLAGS="%{__global_ldflags}" \
 INCPATH="-I$PWD/GTE" LIBS:="%{__global_ldflags} -L$PWD/GTE/lib/DebugDynamic -lgtgraphics -lgtmathematicsgpu -lgtapplications -L%{_libdir} -lX11 -lXext -lGL -lEGL -lpng -lpthread -lm"
%else
make V=1 CFG=ReleaseDynamic -f makeallsamples.gte -C GTE/Samples -j1 \
 CFLAGS="%{optflags} -DNDEBUG -pthread -c -DGTE_USE_LINUX -DGTE_USE_OPENGL -std=c++14" LDFLAGS="%{__global_ldflags}" \
 INCPATH="-I$PWD/GTE" LIBS:="%{__global_ldflags} -L$PWD/GTE/lib/ReleaseDynamic -lgtgraphics -lgtmathematicsgpu -lgtapplications -L%{_libdir} -lX11 -lXext -lGL -lEGL -lpng -lpthread -lm"
%endif

%install
# Manual installation

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -pm 755 GTE/lib/ReleaseDynamic/* $RPM_BUILD_ROOT%{_libdir}/

ln -sf libgtapplications.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtapplications.so
ln -sf libgtapplications.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtapplications.so.4
ln -sf libgtgraphics.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtgraphics.so
ln -sf libgtgraphics.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtgraphics.so.4
ln -sf libgtmathematicsgpu.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtmathematicsgpu.so
ln -sf libgtmathematicsgpu.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtmathematicsgpu.so.4

mkdir -p $RPM_BUILD_ROOT%{_includedir}/GTE
cp -a GTE/Applications $RPM_BUILD_ROOT%{_includedir}/GTE/
cp -a GTE/Graphics $RPM_BUILD_ROOT%{_includedir}/GTE/
cp -a GTE/Mathematics $RPM_BUILD_ROOT%{_includedir}/GTE/
find $RPM_BUILD_ROOT%{_includedir}/GTE -type f -maxdepth 4 -name "*.cpp" -exec rm -f '{}' \;

## Install samples files
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a GTE/Samples $RPM_BUILD_ROOT%{_libexecdir}/%{name}/

# Remove unused files
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.h" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.cpp" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.filters" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.vcxproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.sln" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.gte" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.o" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type d -maxdepth 3 -name "ReleaseDynamic" -exec rmdir -v '{}' \;

# Fix executable permissions
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -maxdepth 3 -name "*.ReleaseDynamic" -exec chmod +x '{}' \;
##

# Edit a pkg-config file
cat > $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gtengine.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

xthreadlib=-lpthread

Name: GTEngine
Description: Library for computations in mathematics, graphics, image analysis, and physics
Version: %{version}
Cflags: -I%{_includedir}/GTE
Libs: -lgtgraphics -lgtmathematicsgpu -lgtapplications
Libs.private: -lpthread
EOF

%ldconfig_scriptlets

%files
%license License
%{_libdir}/libgt*.so.*

%files devel
%{_includedir}/GTE/
%{_libdir}/libgt*.so
%{_libdir}/pkgconfig/gtengine.pc

%files samples
%doc GTE/Gte4p6InstallationRelease.pdf
%{_libexecdir}/%{name}/

%changelog
* Fri Jun 12 2020 Antonio Trande <sagitter@fedoraproject.org> 1:4.6-1
- Release 4.6

* Sat Feb 01 2020 Antonio Trande <sagitter@fedoraproject.org> 1:4.5-1
- Release 4.5
- Epoch 1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> 3.28-3
- Add missing #include for gcc-10

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.28-2
- Rebuilt for new freeglut

* Thu Sep 05 2019 Antonio Trande <sagitter@fedoraproject.org> 3.28-1
- Release 3.28

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Antonio Trande <sagitter@fedoraproject.org> 3.21-1
- Release 3.21

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Antonio Trande <sagitter@fedoraproject.org> 3.19-1
- Release 3.19

* Thu Oct 18 2018 Antonio Trande <sagitter@fedoraproject.org> 3.16-1
- Update to 3.16

* Thu Sep 13 2018 Antonio Trande <sagitter@fedoraproject.org> 3.15-1
- Update to 3.15

* Sun Jul 22 2018 Antonio Trande <sagitter@fedoraproject.org> 3.14-1
- Update to 3.14
- Include EGL support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Antonio Trande <sagitter@fedoraproject.org> 3.12-1
- Update to 3.12

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> 3.11-1
- Update to 3.11

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10-3
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Antonio Trande <sagitter@fedoraproject.org> 3.10-1
- Update to 3.10

* Sun Aug 06 2017 Antonio Trande <sagitter@fedoraproject.org> 3.9-1
- Update to 3.9

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Antonio Trande <sagitter@fedoraproject.org> 3.8-1
- Update to 3.8

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 07 2017 Antonio Trande <sagitter@fedoraproject.org> 3.7-1
- Update to 3.7

* Sun Feb 05 2017 Antonio Trande <sagitter@fedoraproject.org> 3.6-1
- Update to 3.6

* Sun Dec 25 2016 Antonio Trande <sagitter@fedoraproject.org> 3.5-1
- Update to 3.5

* Tue Nov 15 2016 Antonio Trande <sagitter@fedoraproject.org> 3.4-1
- Update to 3.4

* Sat Oct 01 2016 Antonio Trande <sagitter@fedoraproject.org> 3.3-1
- Update to 3.3

* Thu Jul 07 2016 Antonio Trande <sagitter@fedoraproject.org> 3.2-2
- Make obj directories (strange assembler error)

* Thu Jul 07 2016 Antonio Trande <sagitter@fedoraproject.org> 3.2-1
- Update to 3.2

* Sun Jun 26 2016 Antonio Trande <sagitter@fedoraproject.org> 3.1-1
- Update to 3.1

* Sun May 29 2016 Antonio Trande <sagitter@fedoraproject.org> 2.5-1
- Update to 2.5

* Sat Apr 09 2016 Antonio Trande <sagitter@fedoraproject.org> 2.4-1
- Update to 2.4

* Sat Apr 02 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-4
- Parallel Make disabled

* Fri Apr 01 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-3
- Install commands modified

* Fri Apr 01 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-2
- Renamed as gtengine

* Wed Mar 16 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-1
- Update to 2.3

* Mon Feb 22 2016 Antonio Trande <sagitter@fedoraproject.org> 2.2-1
- Update to 2.2

* Wed Jan 27 2016 Antonio Trande <sagitter@fedoraproject.org> 2.1-1
- Update to 2.1

* Tue Sep 29 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0-1
- Update to 2.0

* Mon Jun 29 2015 Antonio Trande <sagitter@fedoraproject.org> 1.14-1
- First package
