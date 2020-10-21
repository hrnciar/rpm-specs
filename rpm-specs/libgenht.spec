%global srcname genht

Name:           lib%{srcname}
Version:        1.0.1
Release:        7%{?dist}
Summary:        Simple generic hash table implementation in C

License:        Public Domain
URL:            http://repo.hu/projects/genht
Source0:        http://repo.hu/projects/genht/releases/%{srcname}-%{version}.tar.gz

# patch Makefile to accept CFLAGS and LDFLAGS from environment and set SONAME
Patch0:         00-fix-makefile.patch

BuildRequires:  gcc
BuildRequires:  make

%description
genht is a simple generic hash table implementation in C.
Uses open addressing scheme with space doubling.
Type generics is achieved by ugly name prefixing macros.

%package devel
Summary:        Libraries, includes, etc. to develop applications using genht
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries, includes, etc. to develop applications using genht.


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%set_build_flags
%make_build

%install
# Depending on arch, install in /usr/lib or /usr/lib64.
%make_install LIBDIR=%{buildroot}/%{_libdir}


%files
%license src/LICENSE
%doc src/AUTHORS
%{_libdir}/libgenht.so.1*


%files devel
%{_includedir}/%{srcname}/

%{_libdir}/libgenht.so



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 01 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.0.1-3
- Remove static subpackage
- Patch the Makefile to install the .so file link.

* Sat Nov 24 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.0.1-2
- Implement suggestions from review

* Sat Nov 17 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> 1.0.1-1
- Initial proposal
