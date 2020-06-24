%bcond_without check
%bcond_without bundle_libodb
%bcond_with bootstrap
%bcond_with network_checks
%bcond_with static

Name:           build2
Version:        0.12.0
Release:        2%{?dist}
Summary:        Cross-platform build toolchain for developing and packaging C++ code

License:        MIT
URL:            https://build2.org/
Source0:        https://pkg.cppget.org/1/alpha/%{name}/%{name}-%{version}.tar.gz
Source1:        https://pkg.cppget.org/1/alpha/%{name}/libbutl-%{version}.tar.gz
Source2:        https://pkg.cppget.org/1/alpha/%{name}/libbpkg-%{version}.tar.gz
Source3:        https://pkg.cppget.org/1/alpha/%{name}/bpkg-%{version}.tar.gz
Source4:        https://pkg.cppget.org/1/alpha/%{name}/bdep-%{version}.tar.gz
Source5:        macros.%{name}

# The latest official release of libodb is not compatible with build2
%if %{with bundle_libodb}
%global         libodb_bundle_version 2.5.0-b.17
Source100:      https://pkg.cppget.org/1/beta/odb/libodb-%{libodb_bundle_version}.tar.gz
Source101:      https://pkg.cppget.org/1/beta/odb/libodb-sqlite-%{libodb_bundle_version}.tar.gz
%endif

# Upstream https://git.build2.org/cgit/build2/commit/?id=0e9bf64dadc029bdf3e97ffb982d297eee0499e4
Patch0000:      build2-libbuild2-buildfile-host_config-config.install.chroot-remove.patch

BuildRequires:  gcc-c++
BuildRequires:  libpkgconf-devel
%if %{with bootstrap}
BuildRequires:  make
BuildRequires:  pkgconf
%else
BuildRequires:  %{name}
BuildRequires:  %{name}-rpm-macros
%endif
%if %{with check}
# libbuild2, bpkg
BuildRequires:  bzip2
# install: libbuild2; readlink: libbuild2; sha256sum: bpkg, bdep
BuildRequires:  coreutils
# libbuild2, libbutl
BuildRequires:  diffutils
%if %{with network_checks}
# libbutl, bpkg, bdep
BuildRequires:  curl
%endif
# libbuild2, bpkg, bdep
BuildRequires:  git
# libbuild2, bpkg
BuildRequires:  gzip
# libbutl, bpkg
BuildRequires:  openssl
# libbuild2, bpkg
BuildRequires:  tar
# libbuild2, bpkg
BuildRequires:  xz
%endif
Recommends:     %{name}-rpm-macros

%description
%{name} is an open source (MIT), cross-platform build toolchain for developing
and packaging C++ code. It is a hierarchy of tools that includes the build
system, package dependency manager (for package consumption), and project
dependency manager (for project development). Key features:

 * Next-generation, Cargo-like integrated build toolchain for C++.
 * Covers entire project life cycle: creation, development, testing, and
   delivery.
 * Uniform and consistent interface across all platforms and compilers.
 * Fast, multi-threaded build system with parallel building and testing.
 * Archive and version control-based package repositories.
 * Dependency-free, all you need is a C++ compiler.

%package -n     %{name}-doc
Summary:        %{name} documentation
BuildArch:      noarch

%description -n %{name}-doc
This package contains the %{name} documentation.

%package -n     lib%{name}
Summary:        %{name} library
# libbuild2-dist
Requires:       bzip2
# install: libbuild2-install; readlink: libbuild2-bash
Requires:       coreutils
# libbuild2-test
Requires:       diffutils
# libbuild2-version
Requires:       git
# libbuild2-dist
Requires:       gzip
# libbuild2-dist
Requires:       tar
# libbuild2-dist
Requires:       xz

%description -n lib%{name}
This package contains the %{name} library.

%package -n     lib%{name}-devel
Summary:        Development files for %{name} library
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n lib%{name}-devel
The lib%{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%if %{with static}
%package -n     lib%{name}-static
Summary:        Static libraries for %{name} library
Requires:       lib%{name}-devel%{?_isa} = %{version}-%{release}

%description -n lib%{name}-static
The lib%{name}-static package contains static libraries for developing
applications that use lib%{name}.
%endif

%package -n     libbutl
Summary:        %{name} utility library
# BSD-2 clause:
#   libbutl/sha256c.c
#   libbutl/strptime.c
#   libbutl/timelocal.c
#   libbutl/timelocal.h
# BSD-3 clause:
#   libbutl/sha1.c
License:        MIT and BSD
Requires:       curl
Requires:       openssl

%description -n libbutl
This package contains the %{name} utility library.

%package -n     libbutl-devel
Summary:        Development files for %{name} utility library
License:        MIT and BSD
Requires:       libbutl%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libbutl-devel
The libbutl-devel package contains libraries and header files for
developing applications that use libbutl.

%if %{with static}
%package -n     libbutl-static
Summary:        Static libraries for %{name} utility library
License:        MIT and BSD
Requires:       libbutl-devel%{?_isa} = %{version}-%{release}

%description -n libbutl-static
The libbutl-static package contains static libraries for developing
applications that use libbutl.
%endif

%package -n     libbpkg
Summary:        %{name} package dependency manager library

%description -n libbpkg
This package contains the %{name} package dependency manager library.

%package -n     libbpkg-devel
Summary:        Development files for %{name} package dependency manager library
Requires:       libbpkg%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libbpkg-devel
The libbpkg-devel package contains libraries and header files for
developing applications that use libbpkg.

%if %{with static}
%package -n     libbpkg-static
Summary:        Static libraries for %{name} package dependency manager library
Requires:       libbpkg-devel%{?_isa} = %{version}-%{release}

%description -n libbpkg-static
The libbpkg-static package contains static libraries for developing
applications that use libbpkg.
%endif

%package -n     bpkg
Summary:        %{name} package dependency manager
%if %{with bundle_libodb}
Provides:       bundled(libodb) = %{libodb_bundle_version}
Provides:       bundled(libodb-sqlite) = %{libodb_bundle_version}
%else
BuildRequires:  pkgconfig(libodb)
BuildRequires:  pkgconfig(libodb-sqlite)
%endif
BuildRequires:  pkgconfig(sqlite3)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bzip2
Requires:       coreutils
Requires:       curl
Requires:       git
Requires:       gzip
Requires:       openssl
Requires:       tar
Requires:       xz

%description -n bpkg
The %{name} package dependency manager is used to manipulate build
configurations, packages, and repositories.

%package -n     bpkg-doc
Summary:        bpkg documentation
BuildArch:      noarch

%description -n bpkg-doc
This package contains the bpkg documentation.

%package -n     bdep
Summary:        %{name} project dependency manager
%if %{with bundle_libodb}
Provides:       bundled(libodb) = %{libodb_bundle_version}
Provides:       bundled(libodb-sqlite) = %{libodb_bundle_version}
%else
BuildRequires:  pkgconfig(libodb)
BuildRequires:  pkgconfig(libodb-sqlite)
%endif
BuildRequires:  pkgconfig(sqlite3)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bpkg%{?_isa} = %{version}-%{release}
Requires:       coreutils
Requires:       curl
Requires:       git

%description -n bdep
The %{name} project dependency manager is used to manage the dependencies of a
project during development.

%package -n     bdep-doc
Summary:        bdep documentation
BuildArch:      noarch

%description -n bdep-doc
This package contains the bdep documentation.

%package -n     %{name}-rpm-macros
Summary:        %{name} RPM macros
BuildArch:      noarch
Requires:       %{name}

%description -n %{name}-rpm-macros
This package contains the %{name} RPM macros.

%prep
%if ! %{with bundle_libodb}
%setup -q -c -n %{name}-toolchain-%{version} -a 1 -a 2 -a 3 -a 4
%else
%setup -q -c -n %{name}-toolchain-%{version} -a 1 -a 2 -a 3 -a 4 -a 100 -a 101
%endif
pushd build2-%{version}
%patch -p 1 -P 0000
popd
mv libbutl-%{version} %{name}-%{version}

%build
# Define basic installation configuration. Note that this does not include:
#  %%{_sysconfdir}           /etc
#  %%{_libexecdir}           %%{_exec_prefix}/libexec
#  %%{_sharedstatedir}       /var/lib
#  %%{_datadir}              %%{_prefix}/share
#  %%{_infodir}              /usr/share/info
#  %%{_localstatedir}        /var
# config.install.data and config.install.libexec seems to default to a value
# like %%{_datadir}/${project} and %%{_libexecdir}/${project} so that data files
# are not installed directly in %%{_datadir} or %%{_libexecdir}
# By specifying the installation location, the default file install mode will be
# 644, so we should set mode 755 for executable target install directories
# explicitly
%global config_install                                                          \\\
  config.install.root=%{_prefix}                                                \\\
  config.install.exec_root=%{_exec_prefix}                                      \\\
  config.install.bin=%{_bindir}                                                 \\\
  config.install.sbin=%{_sbindir}                                               \\\
  config.install.include=%{_includedir}                                         \\\
  config.install.lib=%{_libdir}                                                 \\\
  config.install.man=%{_mandir}                                                 \\\
  config.install.pkgconfig=%{_libdir}/pkgconfig                                 \\\
  config.install.bin.mode=755                                                   \\\
  config.install.sbin.mode=755                                                  \\\
  config.install.lib.mode=755                                                   \\\
  config.install.chroot=%{?buildroot}
%if %{with bootstrap}
CXX=g++
CXXFLAGS="${CXXFLAGS:-%{build_cxxflags}}"
LDFLAGS="${LDFLAGS:-%{build_ldflags}}"
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bash:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bin:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/c:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cc:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cxx:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/in:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/version:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl:${LD_LIBRARY_PATH}
pushd %{name}-%{version}
# bootstrap, phase 1: minimal build system
export CXX
export CXXFLAGS
export LDFLAGS
%make_build -f bootstrap.gmake
# bootstrap, phase 2: statically linked build system
build2/b-boot                                                                   \
  config.bin.lib=static                                                         \
  config.cxx=${CXX}                                                             \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.poptions+="$(pkgconf --cflags-only-I libpkgconf)"                  \
  config.cxx.loptions+="$(pkgconf --libs-only-L libpkgconf) ${LDFLAGS}"         \
  build2/exe{b}
mv build2/b build2/b-boot
# configure and build final, shared library build system
build2/b-boot configure                                                         \
%if ! %{with static}
  config.bin.lib=shared                                                         \
%endif
  config.bin.rpath.auto=false                                                   \
  config.bin.rpath_link.auto=false                                              \
  config.cxx=${CXX}                                                             \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.loptions="${LDFLAGS}"                                              \
%{config_install}
build2/b-boot
popd
%if %{with bundle_libodb}
# configure libodb to build static and not install
%{name}-%{version}/build2/b configure:                                          \
  libodb-%{libodb_bundle_version}/                                              \
  libodb-sqlite-%{libodb_bundle_version}/                                       \
  config.bin.lib=static                                                         \
  config.cxx=${CXX}                                                             \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.loptions="${LDFLAGS}"                                              \
  config.import.libodb="libodb-%{libodb_bundle_version}/"                       \
  config.install=false
%endif
# configure bpkg and bdep and their dependencies
%{name}-%{version}/build2/b configure:                                          \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
%if ! %{with static}
  config.bin.lib=shared                                                         \
%endif
  config.bin.rpath.auto=false                                                   \
  config.bin.rpath_link.auto=false                                              \
  config.cxx=${CXX}                                                             \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.loptions="${LDFLAGS}"                                              \
%if %{with bundle_libodb}
  config.import.libodb="libodb-%{libodb_bundle_version}/"                       \
  config.import.libodb_sqlite="libodb-sqlite-%{libodb_bundle_version}/"         \
%endif
  config.import.libbutl="%{name}-%{version}/libbutl-%{version}/"                \
  config.import.libbpkg="libbpkg-%{version}/"                                   \
%{config_install}
# build bpkg and bdep and their dependencies
%{name}-%{version}/build2/b                                                     \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/
%else
# ! %%{with bootstrap}
%if %{with bundle_libodb}
# configure libodb to build static and not install
%build2 configure:                                                              \
  libodb-%{libodb_bundle_version}/                                              \
  libodb-sqlite-%{libodb_bundle_version}/                                       \
  config.bin.lib=static                                                         \
  config.import.libodb="libodb-%{libodb_bundle_version}/"                       \
  config.install=false
%endif
# configure build2, bpkg, and bdep and their dependencies
%build2_configure                                                               \
  %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
%if %{with static}
  config.bin.lib=both                                                           \
%endif
%if %{with bundle_libodb}
  config.import.libodb="libodb-%{libodb_bundle_version}/"                       \
  config.import.libodb_sqlite="libodb-sqlite-%{libodb_bundle_version}/"         \
%endif
  config.import.libbutl="%{name}-%{version}/libbutl-%{version}/"                \
  config.import.libbpkg="libbpkg-%{version}/"
# build build2, bpkg, and bdep and their dependencies
b %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/
%endif

%install
%if %{with bootstrap}
%{name}-%{version}/build2/b-boot install:                                       \
%else
b install:                                                                      \
%endif
  %{name}-%{version}/libbutl-%{version}/                                        \
  %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/
# move licenses from %%{_docdir} to %%{_defaultlicensedir}
for p in %{name} libbutl libbpkg bpkg bdep; do
  mkdir -p %{buildroot}%{_defaultlicensedir}/${p}
  mv %{buildroot}%{_docdir}/${p}/LICENSE %{buildroot}%{_defaultlicensedir}/${p}
done
mkdir -p %{buildroot}%{_defaultlicensedir}/lib%{name}
cp %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE %{buildroot}%{_defaultlicensedir}/lib%{name}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_rpmmacrodir}/macros.%{name}

%check
%if %{with check}
export PATH=$PWD/bpkg-%{version}/bpkg:$PATH
export PATH=$PWD/%{name}-%{version}/build2:$PATH
export LD_LIBRARY_PATH=$PWD/libbpkg-%{version}/libbpkg:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bash:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bin:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/c:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cc:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cxx:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/in:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/version:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl:${LD_LIBRARY_PATH}
b test:                                                                         \
  %{name}-%{version}/libbutl-%{version}/                                        \
  %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
%if ! %{with network_checks}
  config.bdep.test.repository=''
%endif
%endif

%files
%dir %{_defaultlicensedir}/%{name}
%dir %{_docdir}/%{name}
%license %{_defaultlicensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/CONTRIBUTING.md
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%{_bindir}/b
%{_mandir}/man1/b.1*

%files -n       %{name}-doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/%{name}-build-system-manual*
%doc %{_docdir}/%{name}/b.xhtml
%doc %{_docdir}/%{name}/manifest

%files -n       lib%{name}
%dir %{_defaultlicensedir}/lib%{name}
%license %{_defaultlicensedir}/lib%{name}/LICENSE
%{_libdir}/lib%{name}-0.12.so
%{_libdir}/lib%{name}-bash-0.12-0.12.so
%{_libdir}/lib%{name}-bin-0.12-0.12.so
%{_libdir}/lib%{name}-c-0.12-0.12.so
%{_libdir}/lib%{name}-cc-0.12-0.12.so
%{_libdir}/lib%{name}-cxx-0.12-0.12.so
%{_libdir}/lib%{name}-in-0.12-0.12.so
%{_libdir}/lib%{name}-version-0.12-0.12.so

%files -n       lib%{name}-devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-bash{,-0.12}.so
%{_libdir}/lib%{name}-bin{,-0.12}.so
%{_libdir}/lib%{name}-c{,-0.12}.so
%{_libdir}/lib%{name}-cc{,-0.12}.so
%{_libdir}/lib%{name}-cxx{,-0.12}.so
%{_libdir}/lib%{name}-in{,-0.12}.so
%{_libdir}/lib%{name}-version{,-0.12}.so
%{_libdir}/pkgconfig/lib%{name}.shared.pc
%{_libdir}/pkgconfig/lib%{name}-bash.shared.pc
%{_libdir}/pkgconfig/lib%{name}-bin.shared.pc
%{_libdir}/pkgconfig/lib%{name}-c.shared.pc
%{_libdir}/pkgconfig/lib%{name}-cc.shared.pc
%{_libdir}/pkgconfig/lib%{name}-cxx.shared.pc
%{_libdir}/pkgconfig/lib%{name}-in.shared.pc
%{_libdir}/pkgconfig/lib%{name}-version.shared.pc

%if %{with static}
%files -n       lib%{name}-static
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}-bash.a
%{_libdir}/lib%{name}-bin.a
%{_libdir}/lib%{name}-c.a
%{_libdir}/lib%{name}-cc.a
%{_libdir}/lib%{name}-cxx.a
%{_libdir}/lib%{name}-in.a
%{_libdir}/lib%{name}-version.a
%{_libdir}/pkgconfig/lib%{name}.static.pc
%{_libdir}/pkgconfig/lib%{name}-bash.static.pc
%{_libdir}/pkgconfig/lib%{name}-bin.static.pc
%{_libdir}/pkgconfig/lib%{name}-c.static.pc
%{_libdir}/pkgconfig/lib%{name}-cc.static.pc
%{_libdir}/pkgconfig/lib%{name}-cxx.static.pc
%{_libdir}/pkgconfig/lib%{name}-in.static.pc
%{_libdir}/pkgconfig/lib%{name}-version.static.pc
%endif

%files -n       libbutl
%dir %{_defaultlicensedir}/libbutl
%license %{_defaultlicensedir}/libbutl/LICENSE
%{_libdir}/libbutl-0.12.so

%files -n       libbutl-devel
%dir %{_docdir}/libbutl
%doc %{_docdir}/libbutl/manifest
%doc %{_docdir}/libbutl/CONTRIBUTING.md
%doc %{_docdir}/libbutl/NEWS
%doc %{_docdir}/libbutl/README
%{_includedir}/libbutl
%{_libdir}/libbutl.so
%{_libdir}/pkgconfig/libbutl.shared.pc

%if %{with static}
%files -n       libbutl-static
%{_libdir}/libbutl.a
%{_libdir}/pkgconfig/libbutl.static.pc
%endif

%files -n       libbpkg
%dir %{_defaultlicensedir}/libbpkg
%license %{_defaultlicensedir}/libbpkg/LICENSE
%{_libdir}/libbpkg-0.12.so

%files -n       libbpkg-devel
%dir %{_docdir}/libbpkg
%doc %{_docdir}/libbpkg/manifest
%doc %{_docdir}/libbpkg/CONTRIBUTING.md
%doc %{_docdir}/libbpkg/NEWS
%doc %{_docdir}/libbpkg/README
%{_includedir}/libbpkg
%{_libdir}/libbpkg.so
%{_libdir}/pkgconfig/libbpkg.shared.pc

%if %{with static}
%files -n       libbpkg-static
%{_libdir}/libbpkg.a
%{_libdir}/pkgconfig/libbpkg.static.pc
%endif

%files -n       bpkg
%dir %{_defaultlicensedir}/bpkg
%dir %{_docdir}/bpkg
%license %{_defaultlicensedir}/bpkg/LICENSE
%doc %{_docdir}/bpkg/CONTRIBUTING.md
%doc %{_docdir}/bpkg/NEWS
%doc %{_docdir}/bpkg/README
%{_bindir}/bpkg
%{_mandir}/man1/bpkg.1*
%{_mandir}/man1/bpkg-*1.*

%files -n       bpkg-doc
%dir %{_docdir}/bpkg
%doc %{_docdir}/bpkg/%{name}-package-manager-manual*
%doc %{_docdir}/bpkg/bpkg*.xhtml
%doc %{_docdir}/bpkg/manifest

%files -n       bdep
%dir %{_defaultlicensedir}/bdep
%dir %{_docdir}/bdep
%license %{_defaultlicensedir}/bdep/LICENSE
%doc %{_docdir}/bdep/CONTRIBUTING.md
%doc %{_docdir}/bdep/NEWS
%doc %{_docdir}/bdep/README
%{_bindir}/bdep
%{_mandir}/man1/bdep.1*
%{_mandir}/man1/bdep-*1.*

%files -n       bdep-doc
%dir %{_docdir}/bdep
%doc %{_docdir}/bdep/bdep*.xhtml
%doc %{_docdir}/bdep/manifest

%files -n       %{name}-rpm-macros
%{_rpmmacrodir}/macros.%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.12.0-1
- Update to v0.12.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.11.0-1
- Initial package
