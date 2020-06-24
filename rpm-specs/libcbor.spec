Name:		libcbor
Version:	0.5.0
Release:	7%{?dist}
Summary:	A CBOR parsing library

License:	MIT
URL:		http://libcbor.org
Source0:	libcbor-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme

%description
libcbor is a C library for parsing and generating CBOR.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel contains libraries and header files for %{name}.

%prep
%setup -q


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFFIX="/usr" ./
%make_build cbor_shared
cd doc
make man


%install
%make_install 
mkdir -p %{buildroot}%{_mandir}/man1
cp doc/build/man/* %{buildroot}%{_mandir}/man1

%ldconfig_scriptlets


%files
%license LICENSE.md
%doc README.md
%{_libdir}/libcbor.so.0*
%{_mandir}/man1/libcbor.1.gz

%files devel
%{_includedir}/cbor.h
%{_includedir}/cbor/*.h
%{_includedir}/cbor/internal/*.h
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc

%changelog
* Sat Feb 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-7
- Fix FTBFS, add version for soname, minor cleanups

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 19 2017 Marek Tamaskovic <mtamasko@redhat.com> 0.5.0-1
- Init package.

