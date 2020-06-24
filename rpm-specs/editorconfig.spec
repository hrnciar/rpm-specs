%global srcname editorconfig-core-c

%global common_description %{expand:
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.
}

Name:           editorconfig
Summary:        Parser for EditorConfig files written in C
Version:        0.12.3
Release:        4%{?dist}
License:        BSD

URL:            https://github.com/%{name}/%{srcname}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  pcre2-devel


%description
%common_description


%package        libs
Summary:        Parser library for EditorConfig files (shared library)
%description    libs
%common_description

This package contains the shared library.


%package        devel
Summary:        Parser library for EditorConfig files (development files)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake

%description    devel
%common_description

This package contains the files needed for development.


%prep
%autosetup -n %{srcname}-%{version}


%build
mkdir build && pushd build
%cmake ..
make
popd


%install
pushd build
%make_install
popd

# Remove static library
rm %{buildroot}/%{_libdir}/libeditorconfig_static.a


%files
%{_bindir}/editorconfig
%{_bindir}/editorconfig-%{version}

%{_mandir}/man1/editorconfig.1.*

%files libs
%doc README.md
%license LICENSE

%{_libdir}/libeditorconfig.so.0*

%{_mandir}/man3/editorconfig*
%{_mandir}/man5/editorconfig*

%files devel
%{_includedir}/editorconfig/

%{_libdir}/libeditorconfig.so
%{_libdir}/cmake/EditorConfig/
%{_libdir}/pkgconfig/editorconfig.pc


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.3-1
- Update to version 0.12.3.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-3
- Fix broken ldconfig_scriptlets use.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-2
- Use single-job make for building.
- Added missing ldconfig scriptlets.
- Rewritten summaries.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-1
- Initial package.

