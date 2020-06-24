%global POSTYEAR 2018
%global POSTMONTH 12
%global POSTNUM 1

Name:           libbtbb
Version:        %{POSTYEAR}.%{POSTMONTH}.R%{POSTNUM}
Release:        5%{?dist}
Summary:        A Bluetooth baseband decoding library
License:        GPLv2
URL:            https://github.com/greatscottgadgets/libbtbb
Source0:        https://github.com/greatscottgadgets/libbtbb/archive/%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}.tar.gz

BuildRequires:  cmake gcc-c++

%description
This is the Bluetooth baseband decoding library, forked from the GR-Bluetooth
project. It can be used to extract Bluetooth packet and piconet information
from Ubertooth devices as well as GR-Bluetooth/USRP.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}


%build
%cmake .
%make_build


%install
%make_install


%ldconfig_scriptlets


%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2018.12.R1-2
- Add explicit curdir on CMake invocation

* Thu Dec 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.12.R1-1
- Update to 2018-12-R1

* Fri Aug 10 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.08.R1-1
- Update to 2018-08-R1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.06.R1-2
- Fix changelog in spec

* Wed Jun 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.06.R1-1
- Update to 2018-06-R1

* Tue Apr 17 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2017.03.R2-1
- Initial import
