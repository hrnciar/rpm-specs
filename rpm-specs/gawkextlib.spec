Name:             gawkextlib
Summary:          Library providing common infrastructure for gawk extension libraries
Version:          1.0.4
Release:          9%{?dist}
License:          GPLv3+

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
BuildRequires:    gawk-devel
BuildRequires:    gcc

# Make sure the API version is compatible with our source code:
BuildRequires:    gawk(abi) >= 1.1
BuildRequires:    gawk(abi) < 4.0

# At runtime, the ABI must be compatible with the compile-time version
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')

# This is the default as of Fedora 23:
%global _hardened_build 1

%description
%{name} is a library providing common support infrastructure for gawk
extensions. This package provides 'libgawkextlib', which is used by various
gawk extension modules -- for example gawk-xml, gawk-pgsql, and more.

%package devel
Summary:          Header files and libraries for gawkextlib development
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         gawk-devel

%description devel
The %{name}-devel package contains the header files and libraries
needed to develop gawk extension modules that use %{name} facilities.

# =============================================================================

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

# =============================================================================

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.4-6
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5 major
  api version 3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Andrew J. Schorr <ajschorr@fedoraproject.org> - 1.0.4-3
- Add BuildRequires: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.4-1
- Update to new upstream release

* Mon Nov 13 2017 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.3-2
- Rebuilt against new version of gawk

* Sat Jul 23 2016 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.3-1
- Rebuilt for new release

* Thu Oct 30 2014 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.0-1
* Restructure so each extension package will be distributed separately.

* Fri Aug 31 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.3.9-1
- Update a few obsolete references to xmlgawk to say gawkextlib.

* Sun Jul 22 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.3.0-1
- Rename from gawklib to gawkextlib.

* Sat Jul 21 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.2.0-1
- This version has been tested and should work.

* Thu Jul 19 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.1.9-1
- Initial packaging.  This has not been tested and almost certainly contains
  errors.
