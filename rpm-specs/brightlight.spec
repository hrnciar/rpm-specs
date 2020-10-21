Name:           brightlight
Version:        8
Release:        3%{?dist}
Summary:        CLI tool to change screen back-light brightness

License:        ISC
URL:            https://github.com/multiplexd/brightlight
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  make


%description
brightlight gets and sets the screen back-light brightness on Linux systems
using the kernel sysfs interface.


%prep
%global _hardened_build 1
%autosetup

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE.txt
%{_bindir}/%{name}
%attr(4755, root, root) %{_bindir}/%{name}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Justin W. Flory <jflory7@fedoraproject.org> - 8-1
- Upgrade to latest upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Justin W. Flory <jwf@fedoraproject.org> - 7-1
- Upgrade to upstream major release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Justin W. Flory <jwf@fedoraproject.org> - 5-2
- setuid to root to change back-light brightness as non-privileged user

* Tue Oct 31 2017 Justin W. Flory <jwf@fedoraproject.org> - 5-1
- Tweak to the Makefile, contributed by Igor Gnatenko

* Sat Oct 21 2017 Justin W. Flory <jwf@fedoraproject.org> - 4-1
- First brightlight package
