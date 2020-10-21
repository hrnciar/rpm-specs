Name:             gawk-pgsql
Summary:          PostgreSQL client library for gawk
Version:          1.1.1
Release:          8%{?dist}
License:          GPLv3+

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# rpmbuild finds the postgresql-libs dependency automatically
#Requires:        postgresql-libs
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    gawkextlib-devel
BuildRequires:    libpq-devel

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
The gawk-pgsql module provides a gawk extension library for accessing
PostgreSQL database servers using the libpq C library API.

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

# The */dir file is not necessary for info pages to work correctly...
rm -f %{buildroot}%{_infodir}/dir

# Install NLS language files, if translations are present:
#%find_lang %{name}

# if translations are present: %files -f %{name}.lang
%files
%license COPYING
%doc NEWS
%doc *.awk test/*.awk
%{_infodir}/*.info*
%{_libdir}/gawk/pgsql.so

# =============================================================================

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.1-5
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5 major
  api version 3

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.1.1-4
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Andrew J. Schorr <ajschorr@fedoraproject.org> - 1.1.1-1
- Upgrade to release 1.1.1 containing some packaging fixes
- Add BuildRequires: gcc
- Remove translations, since we don't have any at the moment

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 26 2017 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.0-1
- Update to new release and package for Fedora

* Thu Oct 30 2014 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.0-1
- Packaged as a separate rpm.
