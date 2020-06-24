Name:           liborigin
Version:        3.0.0
Release:        7%{?dist}
Epoch:          1
Summary:        Library for reading OriginLab OPJ project files

License:        GPLv3
URL:            https://sourceforge.net/projects/liborigin/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         liborigin-remove-exit-calls.patch
Patch1:         liborigin-use-shared-lib-to-link-opj2dat.patch

# No longer required
#BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  doxygen

Provides:       liborigin2 = 2.0.0-21
Obsoletes:      liborigin2 < 2.0.0-21

%description
A library for reading OriginLab OPJ project files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       liborigin2-devel = 2.0.0-21
Obsoletes:      liborigin2-devel < 2.0.0-21

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake .
make origin opj2dat doc

%install
%make_install

%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.3*
%{_bindir}/opj2dat
%exclude %{_docdir}/%{name}/html
# We have license in different location and FORMAT in -doc
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/FORMAT

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc FORMAT README
%license COPYING
%{_docdir}/%{name}/html/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1:3.0.0-4
- Append curdir to CMake invokation. (#1668512)

* Fri Nov 23 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-3
- Build opj2dat against shared library - patch by Miquel Garriga
- Move unversioned shared library to devel subpackage

* Wed Nov 21 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-2
- Disable static library generation
- Add patch for exit calls - bug #24, patch by Miquel Garriga

* Sun Nov 18 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-1
- First v3.0.0 release
- Remove obsolete code from spec file
- Clean up the changelog
- Use epoch to provide an upgrade path from the old version
