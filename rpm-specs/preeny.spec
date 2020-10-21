Name:             preeny
URL:              https://github.com/zardus/preeny
Version:          0.1
Release:          9%{?dist}
License:          BSD
BuildRequires:    coreutils, make, gcc, libini_config-devel
Summary:          Some helpful preload libraries for pwning stuff
Source0:          https://github.com/zardus/preeny/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Preeny helps you pwn noobs by making it easier to interact with services
locally. It disables fork(), rand(), and alarm() and, if you want, can convert
a server application to a console one using clever/hackish tricks, and can
even patch binaries.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}

%install
cd src
# workaround for RHEL-7, "install -pDt" doesn't seem to work
mkdir -p %{buildroot}%{_libdir}/%{name}
install -pt %{buildroot}%{_libdir}/%{name} *.so

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-3
- Added workaround for RHEL-7

* Tue Aug  8 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-2
- Various fixes according to review

* Mon Aug  7 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-1
- Initial version
