Name:             gawk-json
Summary:          JSON encoder/decoder for gawk
Version:          1.0.2
Release:          6%{?dist}
License:          GPLv3+

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
BuildRequires:    gawk-devel >= 4.2.1
BuildRequires:    gcc-c++
BuildRequires:    rapidjson-devel

# Make sure the API version is compatible with our source code:
BuildRequires:    gawk(abi) >= 2.0
BuildRequires:    gawk(abi) < 4.0

# At runtime, the ABI must be compatible with the compile-time version
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')

# This is the default as of Fedora 23:
%global _hardened_build 1

%description
The %{name} module provides a gawk extension library that uses RapidJSON to
implement functions mapping between gawk associative arrays and JSON.

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

# Install NLS language files, if and when translations are added:
#%find_lang %{name}

#%files -f %{name}.lang
%files
%license COPYING
%doc NEWS
%doc test/*.awk
%{_libdir}/gawk/json.so
%{_mandir}/man3/*

# =============================================================================

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.2-4
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5 major
  api version 3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.2-1
- Update to new upstream release that works with new gawk version 4.2.1
- Update BuildRequires: gawk-devel from = 4.2.0 to >= 4.2.1
- Add BuildRequires: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.1-1
- First version.
