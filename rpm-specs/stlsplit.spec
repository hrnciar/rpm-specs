Name:           stlsplit
Version:        1.2
Release:        10%{?dist}
Summary:        Split STL file to more files - one shell each
License:        AGPLv3+
URL:            http://github.com/admesh/stlsplit/
Source0:        https://github.com/admesh/stlsplit/archive/v%{version}.tar.gz
BuildRequires:  admesh-devel >= 0.98
BuildRequires:  gcc-c++
BuildRequires:  premake

%description
stlsplit receives one STL file and splits it to several files -
one shell a file.

%package devel
Summary:        Development files for the %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This tool receives one STL file and splits it to several files -
one shell a file.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%prep
%setup -q

%build
premake4 gmake
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' lib.make
CFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}

%install
install -Dpm 755 build/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 755 build/lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so
install -Dpm 644 %{name}.h %{buildroot}%{_includedir}/%{name}.h

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.1

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 08 2015 Miro Hrončok <mhroncok@redhat.com> - 1.2-1
- New version

* Fri Apr 24 2015 Miro Hrončok <mhroncok@redhat.com> - 1.1-1
- Initial package
